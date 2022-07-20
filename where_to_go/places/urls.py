"""URL routing of the places app."""

from django.urls import path

from where_to_go.places.views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
]