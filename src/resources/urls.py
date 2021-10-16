from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.render_home_page,
        {"category": "programming"},
        name="programming-page",
    ),
    path(
        "devops",
        views.render_home_page,
        {"category": "devops"},
        name="devops-page",
    ),
    path(
        "machinelearning",
        views.render_home_page,
        {"category": "machinelearning"},
        name="ml-page",
    ),
    path(
        "design",
        views.render_home_page,
        {"category": "design"},
        name="design-page",
    ),
    path(
        "webdev",
        views.render_home_page,
        {"category": "webdev"},
        name="webdev-page",
    ),
    path(
        "materials/<int:id>",
        views.render_material_page,
        name="material-page",
    ),
]
