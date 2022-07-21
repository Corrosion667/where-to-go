"""Places app config file."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PlacesConfig(AppConfig):
    """Application config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'where_to_go.places'
    verbose_name = _('Interesting places to visit')
