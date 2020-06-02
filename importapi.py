#Calling a JSON API
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py.
#The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON.
#A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"
sample_address = "South Federal University"
data_address="University College Dublin"
address_wanted=data_address

parameters={'sensor':'false','address':address_wanted}
paramsurl=urllib.parse.urlencode(parameters)

queryurl=serviceurl+paramsurl
print('Data URL:',queryurl)

data=urllib.request.urlopen(queryurl).read()

jsondata=json.loads(str(data))
place_id=jsondata['results'][0]['place_id']
print('Place ID:',place_id)
