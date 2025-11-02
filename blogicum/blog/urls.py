from django.urls import path, include
from . import views

app_name = 'blog'

post_urls = [
    path('create/',
         views.PostCreateView.as_view(), name='create_post'),
    path('<int:pk>/',
         views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit/',
         views.PostUpdateView.as_view(), name='edit_post'),
    path('<int:pk>/delete/',
         views.PostDeleteView.as_view(), name='delete_post'),
    path('<int:pk>/comment/',
         views.CommentCreateView.as_view(), name='add_comment'),
    path('<int:pk>/edit_comment/<int:comment_id>/',
         views.CommentUpdateView.as_view(), name='edit_comment'),
    path('<int:pk>/delete_comment/<int:comment_id>/',
         views.CommentDeleteView.as_view(), name='delete_comment'),
]

profile_urls = [
    path('edit/',
         views.ProfileUpdateView.as_view(), name='edit_profile'),
    path('<slug:username>/',
         views.ProfileDetailView.as_view(), name='profile'),
]

urlpatterns = [
    path('',
         views.PostListView.as_view(), name='index'),
    path('category/<slug:category_slug>/',
         views.CategoryPostsView.as_view(), name='category_posts'),
    path('posts/', include(post_urls)),
    path('profile/', include(profile_urls)),
]
