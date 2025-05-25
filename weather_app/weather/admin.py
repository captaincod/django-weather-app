from django.contrib import admin

from .models import City

class CityAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Город", {"fields": ["name"]}),
        ("Координаты", {"fields": ["latitude", "longitude"]}),
    ]
    list_display = ["name", "latitude", "longitude"]
    search_fields = ["name"]
    search_help_text = "Введите город"

admin.site.register(City, CityAdmin)