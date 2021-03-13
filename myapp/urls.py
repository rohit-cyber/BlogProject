from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register('', views.BlogView)

urlpatterns = [
    path('', views.index),
    path('addblog/', views.addblog),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('setcookie/',views.setcookie),  
    path('getcookie/',views.getcookie),
    path('blogs/<str:blog_title>', views.blog_details),
    path('api/', include(router.urls)),
]

# 127.0.0.1:8000/