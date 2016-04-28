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
