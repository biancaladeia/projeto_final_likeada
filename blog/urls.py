# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/<int:id>/edit/', views.edit_post, name='edit_post'),  
    path('post/<int:id>/delete/', views.delete_post, name='delete_post'),
    path('search/', views.search, name='search_results'),
    path('post/<int:post_id>/add_comment/', views.add_comment_to_post, name='add_comment_to_post'),
]