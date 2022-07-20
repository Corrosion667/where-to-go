"""Places app config file."""

from django.apps import AppConfig


class PlacesConfig(AppConfig):
    """Application config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'where_to_go.places'
    label = 'places'
