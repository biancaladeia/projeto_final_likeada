# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, User, Permission


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.title   

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'

class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='blog_users')  # Adicione related_name aqui
    user_permissions = models.ManyToManyField(Permission, related_name='blog_users')  # Adicione related_name aqui
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.username
