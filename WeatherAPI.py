import requests as r
import pandas as pd

#end point
url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 28.61,   # Delhi
    "longitude": 77.23,  # Delhi
    "current_weather": True
}

response = r.get(url, params=params)

data = response.json()

# Safely extract weather data
current = data.get("current_weather", {})

print("Full data:", current)
print("Wind speed:", current.get("windspeed"))

# Convert to DataFrame properly
df = pd.DataFrame([current])

# Save to CSV
df.to_csv("./data/weather_output.csv", index=False)

print("✅ Weather data saved to ./data/weather_output.csv")