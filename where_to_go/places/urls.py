"""URL routing of the Places app."""

from django.urls import path

from where_to_go.places.views import MainPageView, get_place_details

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('places/<int:pk>/', get_place_details, name='place_details'),
]
