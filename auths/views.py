from turtle import home
from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from auths.productform import productform
from .forms import RegisterForm
from .models import Order, Product
from .forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def usercreation_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
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
          product=form.save()
          product.user=request.user
          product.ordered=False
          product.save()          
            
        return redirect('products')
    else:
        form =productform()
    products =Product.objects.all()
    orders=Order.objects.all()
    return render(request, 'products.html',{'form':form,'products':products,'orders':orders})  
  
def search_view(request):
    query=request.GET.get('q')
    if(query):
        results=Product.objects.filter(name__icontains=query)
    else:
        results=Product.objects.none()       
    return render(request, 'search_results.html',{'results' : results})            
      
  
@login_required
def edit_product(request,id):
    product =get_object_or_404(Product,id=id)
    if request.method == "POST":
        form = productform(request.POST ,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form =productform(instance=product)
    return render(request, 'edit_product.html',{'form':form,'product':product})    
                
def delete_product(request,id):
    product =get_object_or_404(Product,id=id)
    if request.method=='POST':
        product.delete()
        return redirect('products')
    
def delete_order(request,id):
    order=get_object_or_404(Order,id=id)
    product =get_object_or_404(Product,id=order.product.id)
    if request.method=='POST':
        order.delete()
        product.ordered=False
        product.save()
        return redirect('home')
          
@login_required
def home_view(request):
    products =Product.objects.all()
    return render(request, 'home.html',{'products':products})
def orders_view(request):
    orders=Order.objects.filter(user=request.user).select_related('product')
    return render(request, 'orders.html',{'orders':orders})

def book_product(request,id):
    product =get_object_or_404(Product,id=id)
    if request.method == "POST":
        order= Order.objects.create(
            product=product,
            user=request.user,
            ordered_at=now()
        )
        product.ordered=True
        product.save()
        order.save()
        return redirect('orders')

    

    

        
def contact_view(request):
    return render(request, 'contact.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def ok (request):
     return render(request, home.html)

