from django.contrib import admin
from . import models


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
