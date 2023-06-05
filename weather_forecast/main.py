import argparse
import base64
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather(city_name, encoded_api_key, date):
    api_key = base64.b64decode(encoded_api_key).decode()
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    request_url = f"{base_url}/{city_name}/{date}?key={api_key}&unitGroup=metric"

    response = requests.get(request_url)
    weather_data = response.json()

    if response.status_code == 200:
        date = weather_data["days"][0]["datetime"]
        temp = weather_data["days"][0]["temp"]
        humidity = weather_data["days"][0]["humidity"]

        print(f"Погода в {city_name} на {date}:")
        print(f"Температура: {temp}°C")
        print(f"Вологість повітря: {humidity}%")
    else:
        print(
            f"Помилка отримання даних про погоду для міста {city_name}. Код статусу HTTP: {response.status_code}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Отримати дані про погоду для конкретного міста та дати."
    )
    parser.add_argument(
        "city", type=str, help="Місто, для якого потрібно дізнатися погоду."
    )
    parser.add_argument(
        "date",
        type=str,
        nargs="?",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Дата для отримання прогнозу погоди у форматі РРРР-ММ-ДД. За замовчуванням сьогодні.",
    )

    args = parser.parse_args()

    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        raise ValueError("Установіть змінну середовища WEATHER_API_KEY у файлі .env.")
    get_weather(args.city, api_key, args.date)
