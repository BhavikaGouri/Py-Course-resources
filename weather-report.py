import requests

key = "<YOUR KEY>"

# example of latitude and longitude has been taken
parameters = {
    "lat": 28.704060,
    "lon": 77.102493,
    "appid": key,
    "cnt": 4
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
print(response.status_code)
data = response.json()

for i in range(4):
    if 700 > int(data['list'][i]['weather'][0]['id']):
        print("will rain")
    else:
        print("will not rain")
