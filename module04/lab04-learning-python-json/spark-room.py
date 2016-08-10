import json
import requests

accessToken = "ZjU1ZWEyNWMtYjI0MC00NGI5LTgyM2UtN2FlNmQzOWU5NjlhMzRiZmJlMDYtYzcx" #put your access token here between the quotes.


def setHeaders():         
	accessToken_hdr = 'Bearer ' + accessToken
	spark_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
	return spark_header


def getRooms(theHeader):    
	uri = 'https://api.ciscospark.com/v1/rooms'
	resp = requests.get(uri, headers=theHeader)
	print("SparkAPI: ")	
	return resp.json()
    

header=setHeaders()
value=getRooms(header)
print (json.dumps(value, indent=4, separators=(',', ': ')))
print(value)
