This script checks if the weather will be good for fire eating in the
next two days and prints out a weather report if so.

I set up cron to run this script daily (see below). On my cron setup, cron sends me an
email if anything is printed.

`0 9 * * * python /path/to/windpredictio/print_if_good.py`

This script requires forecastio be installed with ZeeG's python wrappers.

In order to use this script, you must get an API key for forecastio
(see forecast.io). Then, place the api key in a file called
"api_key.py", and put that file in this directory. The contents of the
file should be the following line:

`api_key = 'YOUR API KEY GOES HERE'`
