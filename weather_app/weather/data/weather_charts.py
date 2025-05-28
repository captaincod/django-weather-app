import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def weather_to_charts(df: pd.DataFrame) -> list[str]:
    matplotlib.use('agg')
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'])
    
    html_images = []

    def fig_to_base64_img(fig) -> str:
        buf = BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight')
        plt.close(fig)
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        return f'<img src="data:image/png;base64,{img_base64}" style="max-width:100%;">'

    # Температура по времени
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df['date'], df['temperature_2m'], color='tomato')
    ax.set_title('Температура по времени')
    ax.set_xlabel('Дата')
    ax.set_ylabel('Температура (°C)')
    ax.grid(True)
    html_images.append(fig_to_base64_img(fig))

    # Влажность по времени
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df['date'], df['relative_humidity_2m'], color='skyblue')
    ax.set_title('Влажность по времени')
    ax.set_xlabel('Дата')
    ax.set_ylabel('Влажность (%)')
    ax.grid(True)
    html_images.append(fig_to_base64_img(fig))

    return "".join(html_images)