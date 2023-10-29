# blog/forms.py
from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'content']
        

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Seu nome de usuário'
        self.fields['email'].widget.attrs['placeholder'] = 'Seu endereço de e-mail'
        self.fields['password1'].widget.attrs['placeholder'] = 'Sua senha'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme sua senha'

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este endereço de e-mail já está em uso.')

        return email

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Seu nome de usuário'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Sua senha'}))

