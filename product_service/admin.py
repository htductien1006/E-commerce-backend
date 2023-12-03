from django.contrib import admin
from . import models

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        "id",
        "name",
        "uom_name",
        "uom_quantitive",
        "image_url",
    )


class CategoryAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        "id",
        "name",
    )


class InventoryAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        "id",
        "quantity",
    )


class PromotionAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        "id",
        "name",
        'type_of_promotion',
        'discount_percent',
        'active',
        'start_date',
        'end_date'
    )


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Promotion, PromotionAdmin)
admin.site.register(models.Inventory, InventoryAdmin)
admin.site.register(models.Category, CategoryAdmin)

# ------------------Order Item--------------------------


class PaymentDetailAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        "id",
        "payment_type",
        "amount",
        'status',
    )


class OrderDetailsAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        "id",
        "payment_id",
        'user_id',
    )


class CartItemAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        "id",
        "product_id",
        'quantity',
    )


class OrderItemAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        "id",
        "product_id",
        'quantity',
    )


admin.site.register(models.PaymentDetail, PaymentDetailAdmin)
admin.site.register(models.OrderDetails, OrderDetailsAdmin)
admin.site.register(models.OrderItems, OrderItemAdmin)
