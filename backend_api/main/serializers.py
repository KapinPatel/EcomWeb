from rest_framework import serializers
from . import models

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id','user','address']
    def __init__(self,*args,**kwargs):
        super(VendorSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth=1

class VendorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id','user','address']
    
    def __init__(self,*args,**kwargs):
        super(VendorDetailsSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth=1

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id','category','vendor','title','details','price']
    
    def __init__(self,*args,**kwargs):
        super(ProductListSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth=1

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id','category','vendor','title','details','price']
    
    def __init__(self,*args,**kwargs):
        super(ProductDetailSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth=1