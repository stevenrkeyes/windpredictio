# get_forecast.py
# Author: Steven Keyes
# This script gets the forecast using forecast.io, but it also caches the results, so the forecast can be requested several times in an hour without using up API key calls. This is good if you have several scripts that all require forecasts but that run at the same time.

import pickle
import forecastio
import time
import os
import warnings
import sys

# import an api key as the variable api_key
from api_key import *

def num2str(num):
    num_str = str(abs(num))
    prefix = num_str.split(".")[0].zfill(3)
    if num >= 0:
        prefix = "p" + prefix
    else:
        prefix = "n" + prefix
    if "." in num_str:
        suffix = num_str.split(".")[1].ljust(10,"0")
    else:
        suffix = 10*"0"
    return prefix + suffix
    

def latlng2str(lat, lng):
    return num2str(lat) + num2str(lng)

def get_forecast(lat, lng, force_renew = False):
    
    # These are the things we will check to determine if we should refresh the cache
    no_cache_exists = False
    cache_stale = False
    # also force_renew
    
    # the filename also encodes the coordinates, so there is one cache per location
    filename = ".forecast_cache_" + latlng2str(lat, lng) + ".pkl"
    fullname = os.path.join(sys.path[0], filename)
    
    stale_time = 3600 # seconds
    
    try:
        # check the timestamp of the cache file (in seconds)
        last_modified = os.path.getmtime(fullname)
        age = time.time() - last_modified
        # check if it's more than 1 hour old
        if age > stale_time:
            cache_stale = True
    except OSError as e:
        # we can handle "no such file" errors
        if e.errno == 2:
            print "No cache exists. A cache will be created."
            no_cache_exists = True
        else:
            raise
    
    # if necessary, refresh the cache with a new forecast from forecastio
    if no_cache_exists or cache_stale or force_renew:
        with warnings.catch_warnings():
            # forecastio is giving me TLS certificate warnings
            # which I'll have to debug later
            warnings.simplefilter("ignore")
            forecast = forecastio.load_forecast(api_key, lat, lng)
        f = open(fullname, "wb")
        pickle.dump(forecast, f, -1)
        f.close()
    else:
        # otherwise, get the forecast from the cache
        f = open(fullname, "rb")
        forecast = pickle.load(f)
        f.close()
    # and return the forecast
    return forecast

if __name__ == "__main__":
    # East Campus Courtyard
    lat = 42.359951
    lng = -71.088215
    forecast = get_forecast(lat,lng)
    print "The following forecast was retreived from forecastio or from the cache:"
    print forecast.hourly()
