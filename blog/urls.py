# blog/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/<int:id>/edit/', views.edit_post, name='edit_post'),  
    path('post/<int:id>/delete/', views.delete_post, name='delete_post'),
    path('search/', views.search, name='search_results'),
    path('post/<int:post_id>/add_comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    #path('change_password/', views.change_password, name='change_password'),
    # path('new/', views.post_new, name='post_new'),
    # path('profile/', views.profile, name='profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)