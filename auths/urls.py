# myapp/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('profile/', views.usercreation_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('', views.home_view, name='home'),
    path('products/', views.product_view, name='products'),
    path('contact/', views.contact_view, name='contact'),
    path('logout/', views.logout_view, name='logout'),
    path('orders/', views.orders_view, name='orders'),
    path('products/delete/<int:id>/', views.delete_product, name='delete_product'),
    path('order/delete/<int:id>/', views.delete_order, name='delete_order'),
    path('products/book/<int:id>/', views.book_product, name='book_product'),
    path('products/edit/<int:id>/', views.edit_product, name='edit_product'),
    path('search/', views.search_view, name='search'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

