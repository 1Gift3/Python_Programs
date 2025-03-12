import json
import urllib.request

url = input ('Enter url:')
print('Retrieving', url)

data = urllib.request.urlopen(url).read()
extra_data = len(data)


info = json.loads(data)
#print('User count:', len(info))
total = 0
counts = 0


for item in info['comments']:
    total += int(item['count'])
    counts +=1

print('Count:', counts)
print('Sum:', total)    
    
    