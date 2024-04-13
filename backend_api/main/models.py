from django.db import models
from django.contrib.auth.models import User

# Seller Models

class Vendor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField(null=True)
    
    def __str__(self):
      return self.user.username
 

# Product Category 

class ProductCategory(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(null= True)
    
    def __str__(self):
      return self.title

# Product       
    
class Product(models.Model):
    category = models.ForeignKey(ProductCategory , on_delete=models.SET_NULL,null=True, related_name='category_product')
    vendor = models.ForeignKey(Vendor , on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=100)
    detail = models.TextField(null= True)
    price = models.FloatField()
    tags = models.TextField(null=True,blank=True)
    demo= models.URLField(null=True,blank=True)
    def __str__(self):
      return self.title
    
    def tag_list(self):
        if self.tags:
            return self.tags.split(',')
        else:
            return []

    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE , null=True,related_name="product_images")
    image= models.ImageField(upload_to='prod_images/', null=True)
    def __str__(self):
       return self.image.name if self.image else 'No Image'
        
  
  
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phonenumber = models.PositiveBigIntegerField()
    # address = models.TextField(null=True)
    
    def __str__(self):
      return self.user.username  
    


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add= True)
    
    
    
class OrderItems(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE , related_name='order_items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
      return self.product.title
      
class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE , related_name='customer_address')
    address = models.TextField()
    default_address = models.BooleanField(default = False)
    def __str__(self):
      return self.address
    
class ProductRating(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE , related_name='rating_customers')
    product = models.ForeignKey(Product , on_delete=models.CASCADE,related_name='product_ratings')
    rating = models.IntegerField()
    reviews = models.TextField()
    add_time = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
      return f'{self.rating} - {self.reviews}'
   
