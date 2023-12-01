from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        "id",
        "first_name",
        "last_name",
        "username",
        "email"
    )


admin.site.register(models.User, UserAdmin)
