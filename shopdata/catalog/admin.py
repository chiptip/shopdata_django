from django.contrib import admin
from shopdata.catalog.models import Catalog, Product
# Register your models here.


class CatalogAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Product, ProductAdmin)
