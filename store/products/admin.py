from django.contrib import admin

from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', 'category', ('price', 'quantity'), 'stripe_product_price_id', 'image')
    search_fields = ('name',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
    verbose_name = 'заказ клиента'
    verbose_name_plural = 'заказы клиента:'















# from django.contrib import admin
#
# from products.models import Brand, Parts, PartsCategories, PartsSubCategories
#
# admin.site.register(Parts)
# admin.site.register(Brand)
# admin.site.register(PartsCategories)
# admin.site.register(PartsSubCategories)
