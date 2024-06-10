from django.contrib import admin
from .models import Products, Order
# Register your models here.

admin.site.site_header = "E-Commerce Site"
admin.site.site_title = "ABC shopping"
admin.site.index_title = "Manage ABC shopping"




class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, querset):
        querset.update(category = "default")

    change_category_to_default.short_description = 'Default category'
    list_display = ('title','price','discount_price','category','description',)
    search_fields = ('title','category','description',)
    actions = ('change_category_to_default',)
    # fields = ('title','category','price',)
    list_editable = ('price','category',)





admin.site.register(Products, ProductAdmin)
admin.site.register(Order)
