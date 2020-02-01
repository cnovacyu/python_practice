# Write a program that will prompt for a URL, read the 
# JSON data from that URL using urllib and then parse 
# and extract the comment counts from the JSON data, 
# compute the sum of the numbers in the file and enter 
# the sum

from urllib.request import urlopen
import ssl
import json

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if url == '':
    url = 'http://py4e-data.dr-chuck.net/comments_262085.json'

#Test url
#http://py4e-data.dr-chuck.net/comments_42.json

print('Retrieving', url)
#open up the actual url
data = urlopen(url, context=ctx).read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
# Look at json data
#print(json.dumps(js, indent=4))

#count of records in json data
count = len(js['comments'])
print('Count:', count)

sum = 0
for x in range(count):
    #get the num from the count attr and sum
    sum += (js['comments'][x]['count'])

print('Sum:', sum)