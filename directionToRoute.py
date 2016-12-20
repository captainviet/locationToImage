import ssl
import urllib.request
import json
import re

fi = open("files/gm.inp", "r")
# open file to read
content = fi.readlines()
# read content by lines
originId = content[0].strip("\n")
# get origin placeId
destinationId = content[1].strip("\n")
# get destination placeId
fi.close()
# close file


def wrapInstruction(string):
    return "<b>" + string + "</b>"


instructions = ["left", "right", "U-turn", "north", "south", "east", "west"]
# instructions to be excluded from the results
wrappped = list(map(wrapInstruction, instructions))
# wrap the instructions in the HTML bold tag

context = ssl._create_unverified_context()
# create context to bypass Python certificate error
host = "https://maps.googleapis.com/maps/api/directions/"
# gmaps api host address
outputFormat = "json"
# response format
origin = "?origin=place_id:" + originId
# origin parameter
destination = "&destination=place_id:" + destinationId
# destination parameter
key = "&key=AIzaSyB7oMQlJ4r30K8Gl4gQuPD0H7G1rkclVWY"
# api key
requestUrl = host + outputFormat + origin + destination + key
# construct api request URL from the parameters above
byteResponse = urllib.request.urlopen(requestUrl, context=context).read()
# receive the response in bytes
stringResponse = byteResponse.decode('utf-8')
# convert response to string
jsonResponse = json.loads(stringResponse)
# parse the response to JSON
distance = jsonResponse["routes"][0]["legs"][0]["distance"]["text"]
# get the distance between the two locations
steps = jsonResponse["routes"][0]["legs"][0]["steps"]
# get the list of navigation steps
routes = distance + "\n"
# routes = output string
for step in steps:
    # for each element of steps array
    route = re.findall("\u003cb\u003e[^(\u003cb\u003e)]*\u003c/b\u003e",
                       step["html_instructions"])
    # filter only bold text (marked by HTML bold tag)
    for i in range(len(route) - 1, -1, -1):
        string = route[i]
        if string in wrappped:
            route.remove(route[i])
        # remove all instruction-like elements
    if route:
        # if there is element left after filter --> road address
        routes += (route[0][3:-4] + ", ")
        # append road address to output string
stringtoWrite = routes[:-2]
# cut the redundant characters ", " out

fo = open("files/gm.out", "w")
# open file to write
fo.writelines(stringtoWrite)
# write the output string to file
fo.close()
# close file
