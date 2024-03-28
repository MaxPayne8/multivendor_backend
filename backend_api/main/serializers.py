from rest_framework import serializers
from .models import Vendor,Product,Customer,Order,OrderItems,CustomerAddress,ProductRating,ProductCategory

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Vendor
        fields = ['id','user' , 'address']
        
    def __init__(self, *args, **kwargs):
        super(VendorSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1
        
    
# class VendorDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Vendor
#         fields = ['id','user' , 'address']
        
#     def __init__(self, *args, **kwargs):
#         super(VendorDetailSerializer,self).__init__(*args, **kwargs)
#         self.Meta.depth = 1


class ProductSerializer(serializers.ModelSerializer):
    product_ratings = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model= Product 
        fields = ['id','category','vendor','title','detail','price','product_ratings']
        
    def __init__(self, *args, **kwargs):        
        super(ProductSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1
        
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model= ProductCategory
        fields = ['id','title','details']
        
    def __init__(self, *args, **kwargs):        
        super(CategorySerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1
        
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields = ['id','user' ,'phonenumber']
        
    def __init__(self, *args, **kwargs):
        super(CustomerSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1       

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields = ['id','customer' ,'order_time']
        
    def __init__(self, *args, **kwargs):
        super(OrderSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1       

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= OrderItems
        fields = ['id' ,'order','product']
        
    def __init__(self, *args, **kwargs):
        super(OrderDetailsSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1       

class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomerAddress
        fields = ['id' ,'customer','address','default_address']
        
    def __init__(self, *args, **kwargs):
        super(CustomerAddressSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1       

class ProductRatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= ProductRating
        fields = ['id' ,'customer','product','reviews','rating','add_time']
        
    def __init__(self, *args, **kwargs):
        super(ProductRatingSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth = 1       