from typing import Any
from blogapp.forms import CommentForm
from .models import Category, Tag, Comment, SavePost, Subscription, Post
from django.shortcuts import render,  get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.core.cache import cache
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class PostListView(ListView):
    model = Post
    template_name = 'home.html'  # Tên template sử dụng cho danh sách bài viết
    context_object_name = 'posts'  # Tên biến trong template để truy cập danh sách các bài viết
    paginate_by = 10  # Số lượng bài viết trên mỗi trang

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Truyền danh sách các danh mục vào context
        return context


class PostSearchListView(ListView):
    model = Post
    template_name = 'search_results.html'
    context_object_name = 'posts'
    paginate_by = 5  # Tùy chọn số lượng bài viết mỗi trang

    def get_queryset(self):
        query = self.request.GET.get('q')
        cache_key = f"search_{query}"
        posts = cache.get(cache_key)
        if not posts:
            if query:
                # posts = Post.objects.annotate(
                #     rank=SearchRank('search_vector', query)
                # ).filter(search_vector=query).order_by('-rank')
                posts = Post.objects.filter(
                    Q(title__icontains=query) | Q(content__icontains=query)
                ).distinct().order_by('-created_at').select_related('author').prefetch_related('comments')
                cache.set(cache_key, posts, timeout=300)  # Cache for 5 minutes
                return posts
            else:
                posts = Post.objects.none()
        return posts

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryPostListView(ListView):
    model = Post
    template_name = 'category.html'
    context_object_name = 'posts'
    paginate_by = 5  # Số bài viết mỗi trang, tùy chọn

    def get_queryset(self):
        # Lấy slug từ URL
        slug = self.kwargs.get('slug')
        # Tìm category dựa trên slug, nếu không tồn tại thì trả về 404
        category = get_object_or_404(Category, slug=slug)
        # Trả về danh sách các bài viết liên quan đến category
        return Post.objects.filter(category=category).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Lấy slug từ URL
        slug = self.kwargs.get('slug')
        # Thêm category vào context để sử dụng trong template
        context['category'] = get_object_or_404(Category, slug=slug)
        context['categories'] = Category.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  # Tên template sẽ được sử dụng để render chi tiết bài viết
    context_object_name = 'post'         # Tên biến trong template để truy cập bài viết cụ thể

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context['comment_form'] = CommentForm() 
        context['categories'] = Category.objects.all()
        return context
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        data = {'user': request.user, 'content': request.POST.get('content')}
        form = CommentForm(data)
        print("form valid >>>>>>>>>", form.is_valid())
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            return redirect('post_detail', slug=self.object.slug)
        return self.render_to_response(self.get_context_data(comment_form=form))
    
