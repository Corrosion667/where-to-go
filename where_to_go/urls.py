"""URL routing of the project."""

from django.contrib import admin
from django.urls import path
from where_to_go.views import MainPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='main'),
]
