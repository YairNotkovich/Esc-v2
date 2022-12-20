from django.apps import AppConfig


class EscConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "esc"

    def ready(self) -> None:
        import esc.signals
