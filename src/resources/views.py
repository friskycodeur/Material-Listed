from django.shortcuts import get_object_or_404, render
from django.contrib import settings
from django.db.models import F

from resources.models import Material, TechCategory, Technology

# Create your views here.


def render_home_page(request, **kwargs):
    """
    Renders the home page.
    """
    category = kwargs.get("category", default="home")
    context = {}
    template_name = "resources/home_page.html"
    all_technology = Technology.objects.filter(category=category)
    context["tech_cards"] = all_technology.for_home_page()[
        : settings.DISPLAY_CARD_VALUE
    ]
    context["show_view_all_for_tech"] = (
        True if all_technology.count() > settings.DISPLAY_CARD_VALUE else False
    )
    return render(request, template_name, context)


def render_material_page(request, id=None, **kwargs):
    """
    Renders the material list page
    """
    tech = get_object_or_404(Technology, id=id)
    Technology.objects.filter(id=id).update(views=F("views")+1)
    context = {}
    template_name = "resources/material_list.html"
    context["material_list"] = Material.objects.filter(technology=tech)

    return render(request, template_name, context)
