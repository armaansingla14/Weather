"""
app.py
Entry point for the project. This is a simple text-based weather simulator.
"""

from weather import get_weather_report

def main():
    print("=== Welcome to the Weather Simulator 🌦️ ===")
    city = input("Enter a city name: ")
    report = get_weather_report(city)
    print(report)

if __name__ == "__main__":
    main()
