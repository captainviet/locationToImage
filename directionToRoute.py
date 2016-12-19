import ssl
import urllib.request
import json
import re

context = ssl._create_unverified_context()
host = "https://maps.googleapis.com/maps/api/directions/"
outputFormat = "json"
origin = "?origin=place_id:ChIJCflhUV2rNTER4yviDFCvr00"
destination = "&destination=place_id:ChIJLcFRgHisNTERWJwBwSBcev8"
key = "&key=AIzaSyB7oMQlJ4r30K8Gl4gQuPD0H7G1rkclVWY"
requestUrl = host + outputFormat + origin + destination + key
byteResponse = urllib.request.urlopen(requestUrl, context=context).read()
stringResponse = byteResponse.decode('utf-8')
jsonResponse = json.loads(stringResponse)
steps = jsonResponse["routes"][0]["legs"][0]["steps"]
for step in steps:
    print(re.findall("\u003cb\u003e.*\u003c/b\u003e",
                     step["html_instructions"]))
