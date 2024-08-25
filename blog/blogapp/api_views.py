from rest_framework import viewsets
from .models import Category, Tag, Comment, SavePost, Subscription, Post
from .serializers import (CategorySerializer, TagSerializer,
                           CommentSerializer, PostSerializer,
                           SavedPostSerializer, SubcriptionSerializer )
from rest_framework.pagination import PageNumberPagination


class PostPagination(PageNumberPagination):
    page_size = 5  # Số lượng items mỗi trang
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination


class SavedPostViewSet(viewsets.ModelViewSet):
    queryset = SavePost.objects.all()
    serializer_class = SavedPostSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubcriptionSerializer


# define the pagination class
