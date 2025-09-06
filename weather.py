"""
weather.py
Generates fake weather reports for demonstration purposes.
"""

import random

def get_weather_report(city: str) -> str:
    """Return a fake weather report for the given city."""
    conditions = ["sunny ☀️", "rainy 🌧️", "cloudy ☁️", "stormy ⛈️", "snowy ❄️"]
    temperature = random.randint(-10, 35)
    condition = random.choice(conditions)
    return f"The weather in {city.title()} today is {condition} with {temperature}°C."
