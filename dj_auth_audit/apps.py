# -*- coding: utf-8
from django.apps import AppConfig


class DjAuthAuditConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dj_auth_audit'
    def ready(self) -> None:
        from .signals import AUTH_SIGNALS_CLASSES
        from .handlers import create_auth_log
        for siganl in AUTH_SIGNALS_CLASSES:
            siganl.connect(create_auth_log)
