import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')
repeat = int(input('Enter count: '))
position = int(input('Enter position: '))

#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
while repeat != 0:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = tags[position-1]
    url = tag.get('href', None)
    repeat -= 1

print(tag.contents[0])