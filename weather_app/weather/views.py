from django.shortcuts import render
from .forms import CityForm
from .models import City
from .get_weather_table import get_weather_dataframe
from .visualize_weather import visualize_weather_df_html
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
    weather_plots = None
    error = ""
    city = ""

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city']
            try:
                city = City.objects.filter(name__iregex=city_name)[0]
                print(list(City.objects.filter(name__iregex=city_name)))
                # TODO: обработка исключений
                data = get_weather_dataframe(city.latitude, city.longitude)
                weather_plots = visualize_weather_df_html(data)
            except IndexError:
                error = f"Город '{city_name}' не найден в базе данных."
    else:
        form = CityForm()

    return render(request, 'weather/index.html', {
        'city': city,
        'form': form,
        'weather_plots': weather_plots,
        'error': error
    })
