from django.shortcuts import render
from django.contrib import settings

from resources.models import Technology

# Create your views here.


def render_home_page(request, **kwargs):
    """
    Renders the home page.
    """

    context = {}
    template_name = "resources/home_page.html"
    all_technology = Technology.objects.all()
    context["tech"] = all_technology.for_home_page()[
        : settings.DISPLAY_CARD_VALUE
    ]
    context["show_view_all_for_tech"] = (
        True if all_technology.count() > settings.DISPLAY_CARD_VALUE else False
    )
    return render(request, template_name, context)


def render_material_page(request, **kwargs):
    """
    Renders the material list page
    """
    context = {}
    template_name = "resources/material_list.html"
