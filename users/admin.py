from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Admin for the custom User model (email as username).
    """
    ordering = ("email",)
    list_display = ("id", "email", "username", "display_name",
                    "is_staff", "is_active", "date_joined")
    list_filter = ("is_staff", "is_active", "is_superuser", "groups")
    search_fields = ("email", "username", "display_name",
                     "first_name", "last_name")

    readonly_fields = ("date_joined", "last_login")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("username",
                                         "display_name", "first_name", "last_name")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff",
                                       "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2"),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        """
        Ensure email is required in the admin create/edit form.
        """
        form = super().get_form(request, obj, **kwargs)
        if "email" in form.base_fields:
            form.base_fields["email"].required = True
        return form
