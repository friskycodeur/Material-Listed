from django.contrib import admin
from .models import TechCategory, Technology, Material

# Register your models here.

admin.site.register(TechCategory)
admin.site.register(Technology)
admin.site.register(Material)
