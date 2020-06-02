#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse
#and extract the comment counts from the JSON data,
#compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter Location:')
address=urllib.request.urlopen(url)
data=address.read()

total=0
while True:
    if len(url)<1:break

    print('Retrieving:',address)
    print('Retrived',len(data),'characters')

    info=json.loads(data)
    info=info['comments']

    for item in info:
        print('Count:',item['count'])
        total+=int(item['count'])
        print('Sum:',total)
    print('Final sum:',total)
    break
