from django.shortcuts import render
from .serializers import VendorSerializer,ProductSerializer,CustomerSerializer,OrderSerializer,OrderDetailsSerializer,CustomerAddressSerializer,ProductRatingSerializer,CategorySerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from .models import Vendor,Product,Customer,Order,OrderItems,CustomerAddress,ProductRating,ProductCategory
from rest_framework.permissions import IsAuthenticated
from rest_framework import pagination,viewsets

# Create your views here.

class VendorList(ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes=[IsAuthenticated]
    
class VendorDetails(RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes=[IsAuthenticated]

class CustomerList(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes=[IsAuthenticated]
    
class CustomerDetails(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes=[IsAuthenticated]

class ProductsList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = pagination.PageNumberPagination
    # pagination_class = pagination.LimitOffsetPagination
    
class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderList(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderDetails(ListAPIView):
    def get_queryset(self):
        order_id= self.kwargs['pk']
        order = Order.objects.get(id = order_id)
        order_items = OrderItems.objects.filter(order=order)
        return order_items
        
    serializer_class = OrderDetailsSerializer
    
class CustomerAddressViewSet(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer
    
class ProductRatingViewSet(viewsets.ModelViewSet):
    queryset = ProductRating.objects.all()
    serializer_class = ProductRatingSerializer
        
class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
