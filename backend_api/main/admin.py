from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Vendor)
admin.site.register(models.Product_category)
admin.site.register(models.Product)