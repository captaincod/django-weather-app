import pandas as pd
from datetime import datetime, timezone


def get_current_weather(df: pd.DataFrame):
    now = datetime.now(timezone.utc)
    current_hour = now.replace(minute=0, second=0, microsecond=0)
    df['date'] = pd.to_datetime(df['date'])
    try:
        matched = df[df['date'] == current_hour]
    except KeyError:
        current_date = current_hour.replace(hour=0)
        matched = df[df['date'] == current_date]
    return {'temperature': matched['temperature_2m'].iloc[0], 'humidity': matched['relative_humidity_2m'].iloc[0]}