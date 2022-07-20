"""URL routing of the project."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('where_to_go.places.urls')),
]
