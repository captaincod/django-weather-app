import csv
import requests
from io import StringIO
from django.core.management.base import BaseCommand
from weather.models import City

class Command(BaseCommand):
    help = 'Импортирует города из CSV-файла по ссылке'

    def handle(self, *args, **kwargs):
        csv_url = "https://raw.githubusercontent.com/hflabs/city/master/city.csv"
        try:
            response = requests.get(csv_url)
            response.raise_for_status()
        except requests.RequestException as e:
            self.stderr.write(self.style.ERROR(f'Ошибка при загрузке файла: {e}'))
            return

        file_content = response.content.decode('utf-8')
        csv_file = StringIO(file_content)
        reader = csv.DictReader(csv_file)
        count = 0

        for row in reader:
            name = row.get('address').strip()
            try:
                latitude = float(row['geo_lat'])
                longitude = float(row['geo_lon'])
            except (ValueError, KeyError):
                continue

            if name and not City.objects.filter(name=name).exists():
                City.objects.create(name=name, latitude=latitude, longitude=longitude)
                count += 1

        self.stdout.write(self.style.SUCCESS(f'Импортировано {count} городов'))