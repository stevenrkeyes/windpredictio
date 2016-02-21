# print_if_good.py
# Author: Steven Keyes
# This script prints if the weather looks good for fire eating in two days

import datetime
import pytz

# definition of good conditions
maxWindSpeed = 2 #mph
minTemperature = 30 #degF
# maybe something about rain intensity or probability
# (i.e., something that's just mist or that has low probability is ok)

# get the hourly weather report for two days from now
from get_ec_weather import *
hours = get_ec_weather()

# check if any hour in the evening the day after tomorrow is good in terms of wind speed, precipitation, and temperature

# evening hours of the day after tomorrow
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
dayAfterTomorrow = tomorrow + datetime.timedelta(days=1)
eveningStartTime = datetime.time(17, tzinfo = pytz.timezone('US/Eastern'))
eveningStart = datetime.datetime.combine(dayAfterTomorrow, eveningStartTime)
eveningEnd = eveningStart + datetime.timedelta(hours=9)
dayAfterTomorrowEveningHours = [hour for hour in hours if eveningStart <= hour.time <= eveningEnd]

#for hour in dayAfterTomorrowEveningHours:
#    print hour

acceptableHours = []
# if so, print out the weather report for that evening
for hour in dayAfterTomorrowEveningHours:
    if hour.windSpeed <= maxWindSpeed:
        if hour.temperature >= minTemperature:
            acceptableHours.append(hour)

def bearingToCompassDirection(bearing):
    directions = ['south',
                  'southwest',
                  'west',
                  'northwest',
                  'north',
                  'northeast',
                  'east',
                  'southeast']
    rounded = int(((bearing+22.5)%360)/45)
    return directions[rounded]

degree_sign= u'\N{DEGREE SIGN}'

if acceptableHours:
    print "Acceptable conditions for fire-eating have been found two days from now"
    print "on " + str(dayAfterTomorrow) + ". Here is the hourly weather report for that evening:"
    print 
    for hour in dayAfterTomorrowEveningHours:
        print str(hour.time.hour) + ":00: " + hour.summary + ", " + \
              str(int(hour.temperature)) + degree_sign + "F, wind " + str(hour.windSpeed) + \
              " mph to the " + bearingToCompassDirection(hour.windBearing) + \
              ", " + str(100*hour.precipProbability) + "% precip."
