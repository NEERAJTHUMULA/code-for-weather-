import requests
from datetime import datetime
api_key='3d2b0607dfa7de038532106616405471'
location=input("enter the city name:")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid"+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %f | %I:%M:%S %p")

print("-------------------------------------------------------------")
print("weather stats for - {} || {} ".format(location.upper(), data_time))
print("-------------------------------------------------------------")

print("current temperature is:{:.2f} deg C".format(temp_city))
print("current weather desc:",weather_desc)
print("current humudity:",hmdt, '%')
print("current wind speed:", wind_spd,'kmph')