from turtle import home
from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from auths.productform import productform
from .forms import RegisterForm
from .models import Product
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def product_view(request):
    if request.method == "POST":
        form = productform(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form =productform()
    products =Product.objects.all()
    return render(request, 'products.html',{'form':form,'products':products})    
        


@login_required
def home_view(request):
    products =Product.objects.all()
    return render(request, 'home.html',{'products':products})


def orders_view(request):
    return render(request, 'orders.html')
def contact_view(request):
    return render(request, 'contact.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def ok (request):
     return render(request, home.html)

