"""Admin module of Palces app."""

from django.contrib import admin

from where_to_go.places.models import Image, Place

admin.site.register(Place)
admin.site.register(Image)
