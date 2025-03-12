import urllib.request
import xml.etree.ElementTree as ET 

url = input('Enter location: ')
print('Retrieving', url)

uh = urllib.request.urlopen(url).read()
data = len(uh)
print('Retrieved', data, 'characters')

tree = ET.fromstring(uh)
trees = tree.findall('.//count')
nums = []
counts = 0

for result in trees:
    nums.append(int(result.text))
    rnum = sum(nums)
    counts += 1
    # Debug print the data :)
    #print(result.text)

print('Count:', counts)
print('Sum:', rnum)

