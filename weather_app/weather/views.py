from django.shortcuts import render
import requests
from .forms import CityForm
from .models import City
from .get_weather_table import get_weather_dataframe
from .visualize_weather import visualize_weather_df_html

def index(request):
    weather_plots = None
    error = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        # cities = City.objects.values_list('name', flat=True).distinct()

        if form.is_valid():
            city_name = form.cleaned_data['city']
            try:
                city = City.objects.filter(name__iregex=city_name)[0]
                # TODO: обработка исключений
                data = get_weather_dataframe(city.latitude, city.longitude)
                weather_plots = visualize_weather_df_html(data)
            except IndexError:
                error = f"Город '{city_name}' не найден в базе данных."
    else:
        form = CityForm()

    return render(request, 'weather/index.html', {
        'form': form,
        'weather_plots': weather_plots,
        'error': error
        # 'cities': cities,
    })
