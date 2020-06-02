import urllib.request
import urllib.parse
import json

#api_key=False
#if api_key is False:
    #api_key=42
serviceurl='http://py4e-data.dr-chuck.net/json?'
#else:
    #serviceurl='https://maps.googleapis.com/maps/api/geocode/json?'








while True:
    address=input('Enter Location:')
    if len(address)<1:
        break
    url=serviceurl+urllib.parse.urlencode({'sensor':'false','address':address})
    print('Retrieving',url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    print('Retreived',len(data),'characters')

    try:
        js=json.loads(str(data))
    except:
        js=None
    print('Place ID:', js['results'][0]['place_id'])


#Place ID - ChIJYzrIIDEJZ0gRz78kFPMqdjY
