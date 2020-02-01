#Write a program that will prompt for a URL, read the XML data from that URL using urllib, and then parse 
#and extract the comment counts from the XML data, compute the sum of the numbers in the file.
#You are to look through all the <comment> tags and find the <count> values sum the numbers.

from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if url == '':
    url = 'http://py4e-data.dr-chuck.net/comments_262084.xml'

#Test url
#http://py4e-data.dr-chuck.net/comments_42.xml

print('Retrieving', url)
xml = urlopen(url, context=ctx).read()
chars = len(xml)
print('Retrieved', chars, 'characters')

tree = ET.fromstring(xml)
lst = tree.findall('comments/comment')

count = 0
sum = 0

for item in lst:
    count += 1
    num = int(item.find('count').text)
    sum += num

print('Count:', count)
print('Sum:', sum)