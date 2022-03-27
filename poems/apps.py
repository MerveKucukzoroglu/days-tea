"""Apps"""
from django.apps import AppConfig


class PoemsConfig(AppConfig):
    """Configuring the Poems App"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'poems'
