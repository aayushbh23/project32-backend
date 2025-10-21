from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "authentication"
    verbose_name = "Authentication"

    def ready(self):
        # Place for auth-related signals (e.g., post-save hooks).
        # from . import signals  # noqa: F401
        pass
