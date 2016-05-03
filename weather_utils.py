# weather_utils.py
# Author: Steven Keyes

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

# make a pretty, concise printout of an hour of an hourly forecast
def nice_hourly_print(hour_forecast):
    # check if this is an hour or a list of hours
    if type(hour_forecast) == type(list()):
        for hour in hour_forecast:
            nice_hourly_print(hour)
    else:
        hour = hour_forecast
        print str(hour.time.month) + "/" + str(hour.time.day) + " " + str(hour.time.hour) + "hr: " + hour.summary + ", " + \
              str(int(hour.temperature)) + degree_sign + "F, wind " + str(hour.windSpeed) + \
              " mph to the " + bearingToCompassDirection(hour.windBearing) + \
              ", " + str(100*hour.precipProbability) + "% precip."

