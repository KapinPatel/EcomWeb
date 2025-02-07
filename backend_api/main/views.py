from django.shortcuts import render
from rest_framework import generics,permissions
from . import models
from . import serializers

class VendorList(generics.ListCreateAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorSerializer
    # permission_classes=[permissions.IsAuthenticated]

class VendorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorDetailsSerializer

class ProductList(generics.ListCreateAPIView):
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductListSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductDetailSerializer