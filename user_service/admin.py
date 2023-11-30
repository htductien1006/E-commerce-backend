from django.contrib import admin
from . import models
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "username",
        "email"
    )

    def has_delete_permission(self, *args, **kwargs):
        return True


admin.site.register(models.User, UserAdmin)


# class NewOutstandingTokenAdmin(admin.ModelAdmin):

#     def has_delete_permission(self, *args, **kwargs):
#         return True


# admin.site.unregister(admin.ModelAdmin)
# admin.site.register(admin.ModelAdmin, NewOutstandingTokenAdmin)
