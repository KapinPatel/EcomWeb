from django.urls import path
from . import views

urlpatterns = [
    path('vendors',views.VendorList.as_view()),
    path('vendor/<int:pk>/',views.VendorDetails.as_view()),
    path('products/',views.ProductList.as_view()),
    path('product/<int:pk>/',views.ProductDetail.as_view()),
]