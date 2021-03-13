from django import forms
from .models import Blog
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ('banner', 'title', 'author', 'dop', 'content')
		# fields = '__all__'

class UserRegistrationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password', 'first_name', 'last_name', 'email')
		widgets = {'password': forms.PasswordInput()}

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')