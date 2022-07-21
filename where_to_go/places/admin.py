"""Admin module of Palces app."""

from django.contrib import admin

from where_to_go.places.models import Place

admin.site.register(Place)
