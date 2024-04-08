import requests

# https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=precipitation_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}`

url = "https://api.open-meteo.com/v1/forecast?latitude=53.3465&longitude=-6.2663&daily=precipitation_sum&timezone=Europe%2FLondon&start_date=2024-04-05&end_date=2024-04-05"

response = requests.get(url)

print(response.json())