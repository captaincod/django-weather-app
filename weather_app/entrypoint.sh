#!/bin/sh

set -e

if [ ! -f "/init/.initialized" ]; then
  echo "🔧 Работа с базой данных..."
  python manage.py migrate

  echo "🌍 Импортируются города..."
  python manage.py import_cities 

  touch /init/.initialized
else
  echo "✅ Уже инициализировано, пропускаем работу с данными."
fi

echo "📦 Собирается static..."
python manage.py collectstatic --noinput

echo "🚀 Запуск Gunicorn..."
gunicorn weather_app.wsgi:application --bind 0.0.0.0:8000 --workers 3
