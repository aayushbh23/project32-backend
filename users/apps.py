from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
    verbose_name = "Users"

    def ready(self):
        # Place for signals import if/when needed.
        # from . import signals  # noqa: F401
        pass
