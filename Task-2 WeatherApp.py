import requests

def get_weather(city):
    API_KEY = "d52061c17b0c99dcd82f7934c32bbc38"  
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") == 200:
            main = data["main"]
            weather = data["weather"][0]

            print(f"\n✅ Weather in {city.capitalize()}:")
            print(f"🌡️ Temperature: {main['temp']}°C")
            print(f"💧 Humidity: {main['humidity']}%")
            print(f"🌥️ Condition: {weather['description'].capitalize()}\n")
        else:
            print("⚠️ City not found.\n")

    except requests.exceptions.RequestException as err:
        print(f"❌ Error: {err}\n")

# 🔁 Loop
while True:
    city = input("Enter city name (or type 'exit' to quit): ")
    if city.lower() == "exit":
        print("👋 Exiting the weather app. Stay safe!")
        break
    get_weather(city)


