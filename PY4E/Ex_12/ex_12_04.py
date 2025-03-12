# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
list = []
count = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    count += 1
    for num in tag.contents:
        list.append(int(num))
        new = sum(list)

print("Count", count)
print("Sum", new)
