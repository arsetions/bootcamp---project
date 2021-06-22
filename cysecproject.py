import requests
#import os
from datetime import datetime

api_key = '44e4c397b80579e67a196fda762c8998'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

def weatherloc1():
    return ("-------------------------------------------------------------")
def weatherloc2():
    return ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
def weatherloc3():
    return ("-------------------------------------------------------------")

def weatherloc4():
    return ("Current temperature is: {:.2f} deg C".format(temp_city))
def weatherloc5():
    return ("Current weather:{}".format(weather_desc))
def weatherloc6():
    return ('Current Humidity:{} %'.format(hmdt))
def weatherloc7():
    return ("Current wind speed:{} kmph".format(wind_spd))

result1 = weatherloc1()
result2 = weatherloc2()
result3 = weatherloc3()
result4 = weatherloc4()
result5 = weatherloc5()
result6 = weatherloc6()
result7 = weatherloc7()
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)

with open('cysec_project.txt','wt') as f:
    f.write(result1)
    f.write('\n')
    f.write(result2)
    f.write('\n')
    f.write(result3)
    f.write('\n')
    f.write(result4)
    f.write('\n')
    f.write(result5)
    f.write('\n')
    f.write(result6)
    f.write('\n')
    f.write(result7)
    f.write('\n')

