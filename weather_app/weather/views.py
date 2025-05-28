from django.shortcuts import render
from .forms import CityForm
from .models import City
from .data.get_weather import get_weather_dataframe
from .data.current_weather import get_current_weather
from .data.weather_charts import weather_to_charts
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from weather.models import City

@require_GET
def autocomplete_city(request):
    query = request.GET.get('q', '')
    if query:
        cities = City.objects.filter(name__iregex=query).values_list('name', flat=True).distinct()[:10]
        return JsonResponse({'results': list(cities)})
    return JsonResponse({'results': []})

def index(request):
    city = ""
    cur_temp = None
    cur_humid = None
    weather_charts = None
    error = ""

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city']
            try:
                city = City.objects.filter(name__iregex=city_name)[0]
                print(list(City.objects.filter(name__iregex=city_name)))
                # TODO: обработка исключений
                data = get_weather_dataframe(city.latitude, city.longitude)
                cur_weather = get_current_weather(data)
                cur_temp = int(cur_weather['temperature'])
                cur_humid = int(cur_weather['humidity'])
                weather_charts = weather_to_charts(data)
            except IndexError:
                error = f"Город '{city_name}' не найден в базе данных."
    else:
        form = CityForm()

    return render(request, 'weather/index.html', {
        'form': form,
        'city': city,
        'temperature': cur_temp,
        'humidity': cur_humid,
        'weather_charts': weather_charts,
        'error': error
    })
