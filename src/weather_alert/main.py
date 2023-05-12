import requests
from texter import text_me
from env import WEATHER_KEY

'''
openweathermap Documentation:
https://openweathermap.org/api
Example:
 https://api.openweathermap.org/data/2.5/weather?q=Toronto&appid=
 https://api.openweathermap.org/data/2.8/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=


To find a place that is currently raining:
https://weather-radar-live.com/rain-radar/

To find lat and lon:
https://www.latlong.net/
'''



url = "https://api.openweathermap.org/data/2.5/weather"
url_one_call ="https://api.openweathermap.org/data/2.8/onecall"

params = {
  # 'q' : 'Toronto',
  # "lat": 44.28,
  # "lon":-78.13,
  "lat": 42.04,
  "lon":-101.04,
  'exclude':'minutely,daily,current',
  'APPID': WEATHER_KEY
}

response = requests.get(url_one_call, params=params)
response.raise_for_status()

twelve_hours = response.json()["hourly"][0:12]

for hour_data in twelve_hours:
  condition_code = hour_data["weather"][0]["id"]
  if condition_code <600:
    print("Rain")
    text_me("It wil be wet today! ☂️")
    break
  else:
    print("not yet")
    
# print(twelve_hours)
# print(response.json()["hourly"])