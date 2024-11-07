# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
]

