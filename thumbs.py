import json
from fan import Fan


with open('raw.json', 'r') as openfile:
    json_object = json.load(openfile)

supporters =[]

for thumb in json_object['thumbs']:
    supporters.append(Fan(username=thumb['username'], token=thumb['token']))

print(supporters[-1].username)