import json
from fan import Fan


with open('raw-data-blob.json', 'r') as openfile:
    json_object = json.load(openfile)

more_thumbs_available = json_object["more_thumbs_available"]

supporters = []

for thumb in json_object['thumbs']:
    supporters.append(Fan(username=thumb['username'], token=thumb['token']))

for review in json_object['reviews']:
    supporters.append(Fan(username=review['username'], token=review['token']))

for supporter in supporters:
    supporter.print()
print('length:', len(supporters))