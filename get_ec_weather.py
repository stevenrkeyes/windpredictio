# get_ec_weather.py
# Author: Steven Keyes
# gets the hourly weather forcast for EC courtyard

import forecastio
import pytz

# import an api key as the variable api_key
from api_key import *

# East Campus Courtyard
lat = 42.359951
lng = -71.088215

# get the hourly weather forecast for EC courtyard for the next 49 hours
def get_ec_weather():
    forecast = forecastio.load_forecast(api_key, lat, lng)
    
    byHour = forecast.hourly()
    
    # fix the timestamps, which are UTC but have no indication of this
    easternZone = pytz.timezone('US/Eastern')
    for hourlyData in byHour.data:
        hourlyData.time = hourlyData.time.replace(tzinfo=pytz.utc)
        hourlyData.time = hourlyData.time.astimezone(easternZone)

    #for hourlyData in byHour.data:
    #        print hourlyData.time, hourlyData.temperature, hourlyData.apparentTemperature, hourlyData.windSpeed, hourlyData.precipIntensity, hourlyData.precipProbability

    return byHour.data
