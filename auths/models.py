from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='product_images/',blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    ordered=models.BooleanField(default=False,null=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        product=models.ForeignKey(Product,on_delete=models.CASCADE)
        ordered_at=models.DateTimeField(auto_now_add=True)
        
def __str__(self):
        return f"{self.user.username} -{self.product.name}"


