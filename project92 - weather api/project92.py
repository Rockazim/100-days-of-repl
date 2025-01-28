import requests, json
timezone = "PST"
latitude = 33.7844
longitude = -118.0844

weather_features = [
    "Clear sky",
    'Mainly clear, partly cloudy, and overcast',
    'Fog and depositing rime fog',
    'Drizzle: Light, moderate, and dense intensity',
    'Freezing Drizzle: Light and dense intensity',
    "Rain: Slight, moderate and heavy intensity",
    "Freezing Rain: Light and heavy intensity",
    "Snow fall: Slight, moderate, and heavy intensity",
    "Snow grains",
    "Rain showers: Slight, moderate, and violent",
    "Snow showers: Slight and heavy",
    "Thunderstorm: Slight or moderate",
    "Thunderstorm with slight and heavy hail"
]

weather_interpretation = {
    "0": weather_features[0],
    "1": weather_features[1], "2": weather_features[1], "3": weather_features[1],
    "45": weather_features[2], "48": weather_features[2],
    "51": weather_features[3], "53": weather_features[3], "55": weather_features[3],
    "56": weather_features[4], "57": weather_features[4],
    "61": weather_features[5], "63": weather_features[5], "65": weather_features[5],
    "66": weather_features[6], "67": weather_features[6],
    "71": weather_features[7], "73": weather_features[7], "75": weather_features[7],
    "77": weather_features[8],
    "80": weather_features[9], "81": weather_features[9], "82": weather_features[9],
    "85": weather_features[10], "86": weather_features[10],
    "95": weather_features[11],
    "96": weather_features[12], "99": weather_features[12]
}

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")
user = result.json()

for x in weather_interpretation.keys():
    if x == str(user['daily']['weathercode'][0]):
        weather_description = weather_interpretation[x]


def convert_to_farenheit(celsius):
    return 1.8 * celsius + 32


print(weather_description)
print(f"High: {convert_to_farenheit(user['daily']['temperature_2m_max'][0])} Low: {convert_to_farenheit(user['daily']['temperature_2m_min'][0])}")