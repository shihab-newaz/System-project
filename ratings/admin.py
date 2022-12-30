from django.contrib import admin
from ratings.models import Review,Customer,Product,Record

@admin.register(Review)
class ReviewDisplay(admin.ModelAdmin):
    list_display=('product','review',)
    ordering=('product',)
    search_fields=('product',)
    
@admin.register(Record)
class RecordDisplay(admin.ModelAdmin):
    list_display=('customer','bought_at',)
    ordering=('customer',)
    search_fields=('customer',)


@admin.register(Product)
class ProductDisplay(admin.ModelAdmin):
    list_display=('title','price',)
    ordering=('title',)
    search_fields=('title',)
    
@admin.register(Customer)
class CustomerDisplay(admin.ModelAdmin):
    list_display=('first_name','last_name','email',)
    ordering=('first_name',)
    search_fields=('phone','first_name',)