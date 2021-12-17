from django.urls import path
from .views import HomeView, BlogDetailsView, CreateBlogView, UpdateBlogView, DeleteBlogView, CreateCategories, CategoryBlogView, LikePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', BlogDetailsView.as_view(), name="blog_details"),
    path('create_blog', CreateBlogView.as_view(), name="create_blog"),
    path('create_category', CreateCategories.as_view(), name="create_category"),
    path('update_blog/<int:pk>', UpdateBlogView.as_view(), name="update_blog"),
    path('delete_blog/<int:pk>/delete', DeleteBlogView.as_view(), name="delete_blog"),
    path('category_blogs/<str:cats>', CategoryBlogView, name="category_blog_view"),
    path('like/<int:pk>', LikePostView, name="like_post"),
]
