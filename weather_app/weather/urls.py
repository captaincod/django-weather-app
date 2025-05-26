from django.urls import path

from . import views

app_name = "weather"
urlpatterns = [
    path("", views.index, name="index"),
    path('autocomplete/', views.autocomplete_city, name='autocomplete_city'),
]