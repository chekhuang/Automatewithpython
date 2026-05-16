import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 28.61,# Delhi
    "longitude": 77.23,#Delhi
    "current_weather": True
}

response = requests.get(url, params=params)

data = response.json()

#print only wind speed
print(data)
print("windspeed:", data["current_weather"]["windspeed"])

# Save to CSV
df = pd.DataFrame(["current"])
df.to_csv("weather_output.csv", index=False)

print("Weather data saved to weather_output.csv")