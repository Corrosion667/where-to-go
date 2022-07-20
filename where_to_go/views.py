"""Module with views for project."""

from django.views.generic import TemplateView


class MainPageView(TemplateView):
    """View for main (home) site page."""

    template_name = 'main_page.html'
