from django.shortcuts import render
import requests
from .forms import CityForm
from .models import City

def index(request):
    weather_data = None
    error = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        # cities = City.objects.values_list('name', flat=True).distinct()

        if form.is_valid():
            city_name = form.cleaned_data['city']
            try:
                city = City.objects.filter(name__regex=city_name)[0]
                url = f"https://api.open-meteo.com/v1/forecast?latitude={city.latitude}&longitude={city.longitude}&daily=uv_index_max&hourly=rain,snowfall,temperature_2m,relative_humidity_2m&timezone=auto"
                response = requests.get(url)
                if response.status_code == 200:
                    weather_data = response.json()
                else:
                    error = "Город не найден."
            except IndexError:
                error = f"Город '{city_name}' не найден в базе данных."
    else:
        form = CityForm()

    return render(request, 'weather/index.html', {
        'form': form,
        'weather': weather_data,
        'error': error
        # 'cities': cities,
    })
