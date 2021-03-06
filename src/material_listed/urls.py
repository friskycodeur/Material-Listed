from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path(
        "",
        TemplateView.as_view(template_name="resources/home.html"),
        name="home",
    ),
]
