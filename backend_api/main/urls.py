from rest_framework import routers
from django.urls import path 
from .views import VendorList,VendorDetails,ProductsList,ProductDetails,CustomerList,CustomerDetails,OrderDetails,OrderList,CustomerAddressViewSet,ProductRatingViewSet,ProductCategoryViewSet,TagProducts,CategoryRelatedProducts

router = routers.DefaultRouter()
router.register('address',CustomerAddressViewSet)
router.register('ratings',ProductRatingViewSet)
router.register('categories',ProductCategoryViewSet)



urlpatterns = [
    path('vendors/',  VendorList.as_view()),
    path('vendor/<int:pk>/',  VendorDetails.as_view()),
    path('customers/',  CustomerList.as_view()),
    path('customer/<int:pk>/',  CustomerDetails.as_view()),
    path('products/',  ProductsList.as_view()),    
    path('product/<int:pk>/',  ProductDetails.as_view())   , 
    path('related-products/<int:pk>/',  CategoryRelatedProducts.as_view())   , 
    path('product/<str:tag>/',  TagProducts.as_view())   , 
    path('orders/',  OrderList.as_view()),    
    path('order/<int:pk>/',  OrderDetails.as_view())    
]

urlpatterns+= router.urls


