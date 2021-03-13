from django.shortcuts import render, redirect
from .models import Blog
from .serializers import BlogSerializer
from .forms import BlogForm, UserRegistrationForm, UserForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets


@login_required
def index(request):
	q = Blog.objects.all()
	p = Paginator(q, 5) # 10 record per page
	try:
		page_number = request.GET.get('page')
		page_object = p.page(page_number)
	except:
		page_object = p.page(1)
	return render(request, 'index.html', {'page_object':page_object}) # context

def addblog(request):
	form = BlogForm(request.POST, request.FILES)
	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request, 'addblog.html', {'form':form})

def signup(request):
	if request.method=="POST":
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']
		newuser = User.objects.create_user(
			first_name=first_name,
			last_name=last_name,
			username=username,
			password=password,
			email=email
			)
		try:
			newuser.save()
		except:
			return HttpResponse("Something went wrong.")
	else:
		form = UserRegistrationForm()		
	return render(request, 'signup.html', {'form':form})

def signin(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is None:
			return HttpResponse("User not found.")
		login(request, user)
		return redirect('/')
	else:
		form = UserForm()
	return render(request, 'signin.html', {'form':form})

def signout(request):
	logout(request)
	return redirect('/')

def setcookie(request):  
    response = HttpResponse("Welcome Guest.")  
    response.set_cookie('programink', 'We love Django')  
    return response  

def getcookie(request):  
    info = request.COOKIES.get('programink')
    return HttpResponse("Welcome Back. %s" %info)


def blog_details(request, blog_title=""):
	try:
		blog = Blog.objects.filter(title=blog_title)
	except:
		return HttpResponse("Blog details loading error")
	return render(request, 'blog_details.html', {'blog':blog})

class BlogView(viewsets.ModelViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer

