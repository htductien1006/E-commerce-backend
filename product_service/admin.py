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
admin.site.register(models.Invetory, InventoryAdmin)
admin.site.register(models.Category, CategoryAdmin)
