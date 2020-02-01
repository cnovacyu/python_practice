# Write a program that will prompt for a location, 
# contact a web service and retrieve JSON for the 
# web service and parse that data, and retrieve the 
# first place_id from the JSON. A place ID is a 
# textual identifier that uniquely identifies a 
# place as within Google Maps.

import urllib.request, urllib.parse, urllib.error
import ssl
import json

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if address == '':
    address = 'South Federal University'

parms = dict()
parms['address'] = address
parms['key'] = 42

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
# view json data
#print(json.dumps(js, indent=4))

print('Place id', js['results'][0]['place_id'])