# from rest_framework.routers import DefaultRouter
# from .views import (
#     CategoryViewSet, TagViewSet, PostViewSet, CommentViewSet,
#     SubscriptionViewSet, SavedPostViewSet
# )

# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet)
# router.register(r'tags', TagViewSet)
# router.register(r'posts', PostViewSet)
# router.register(r'comments', CommentViewSet)
# router.register(r'subscriptions', SubscriptionViewSet)
# router.register(r'savedposts', SavedPostViewSet)

# urlpatterns = router.urls

# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('category/<slug:slug>/', CategoryPostListView.as_view(), name='category_posts'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='add_comment'),
    path('search/', PostSearchListView.as_view(), name='search'),
]

