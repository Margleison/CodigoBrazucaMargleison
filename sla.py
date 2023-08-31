import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term="+sys.argv[1])

v = response.json()

for c in v ["results"]:
    print(c["trackName"]) 
    print(c["artistName"])
    print(c["collectionName"])