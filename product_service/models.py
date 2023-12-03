from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# Create your models here.

# ------------------------Product Model-------------------------------


class Category(models.Model):
    name = models.CharField(
        _('Category Name'), max_length=255)


class Inventory(models.Model):
    quantity = models.IntegerField(_("Quantity"))


class Promotion(models.Model):
    name = models.CharField(_("Promotion Name"), max_length=255)
    description = models.TextField(_("Description"))
    type_of_promotion = models.CharField(_("Type of Promotion"))
    discount_percent = models.CharField(_("Discount"))
    active = models.BooleanField(_("Active"))
    start_date = models.DateTimeField(_("Start Date"), help_text=_(
        "Enter the date that you want to start"), null=False, blank=False)
    end_date = models.DateTimeField(_("End Date"), help_text=_(
        "Enter the date that you want to end"), null=False, blank=False)


class Product(models.Model):
    name = models.CharField(_('Product Name'), max_length=255)
    description = models.TextField(_('Description'))
    price = models.IntegerField(_('Price'), default=0)
    uom_name = models.CharField(_('UOM Name'), max_length=255)
    uom_quantitive = models.IntegerField(_('UOM Quantity'))
    image_url = models.CharField(_('Image Url'))
    # ForeginKey for Product
    category_id = models.ForeignKey(
        "Category", on_delete=models.CASCADE, to_field='id', default=0)
    inventory_id = models.ForeignKey(
        "Inventory", on_delete=models.CASCADE, to_field='id', default=0)
    promotion_id = models.ForeignKey(
        "Promotion", on_delete=models.CASCADE, to_field='id', default=0)

    # @property
    # def price(self):
    #     if self.promotion_id:
    #         new_price = self.old_price - ((30/100)*self.old_price)
    #     else:
    #         new_price = self.old_price
    #     return new_price


# ----------------------------Order Payment---------------------------------
class PaymentDetail(models.Model):
    payment_type = models.CharField(
        _('Payment Type'), max_length=255, default="VNPay")
    amount = models.IntegerField(_("Amount"), default=0)
    status = models.CharField(
        _('Status'), max_length=255, default="Not Completed")
    create_time = models.DateTimeField(default=timezone.now)


class OrderDetails(models.Model):
    total = models.IntegerField(_("Total"), null=False, default=0)
    payment_id = models.ForeignKey(
        "PaymentDetail", on_delete=models.CASCADE, to_field="id", default=0)
    user_id = models.ForeignKey(
        "user_service.User", on_delete=models.CASCADE, to_field="id", default=0)


class OrderItems(models.Model):
    quantity = models.CharField(null=False, default="")
    product_id = models.ForeignKey(
        "Product", on_delete=models.CASCADE, to_field="id", default=0)
    order_id = models.ForeignKey(
        "OrderDetails", on_delete=models.CASCADE, to_field="id", default=0)


class CartItems(models.Model):
    quantity = models.IntegerField(null=False, default=0)
    product_id = models.ForeignKey(
        "Product", on_delete=models.CASCADE, to_field="id", default=0)
    session_id = models.ForeignKey(
        "user_service.ShoppingSession", on_delete=models.CASCADE, to_field="id", default=0)
