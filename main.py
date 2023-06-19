import requests
from bs4 import BeautifulSoup
import json
from fan import Fan


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

PROXIES = { 
              "http" : 'http://209.145.60.213:80', 
            }

def get_more_collectors(last_collector_token):
  req_data = {
      "tralbum_type": "a",
      "tralbum_id": 185217827,
      "token": last_collector_token,
      "count": 100
  }  
  response = requests.post('https://henrythreadgill.bandcamp.com/api/tralbumcollectors/2/thumbs', data=req_data, proxies=PROXIES, headers=HEADERS )


    

s = requests.Session()
s.headers.update(HEADERS)

response = s.get('https://henrythreadgill.bandcamp.com/album/poof', proxies=PROXIES, headers=HEADERS)

soup = BeautifulSoup(response.text, 'html.parser')

collectors_data = soup.find(id='collectors-data')
output = collectors_data['data-blob']

with open("raw-data-blob.json", "w") as outfile:
    outfile.write(output)

supporters = []

for thumb in output['thumbs']:
    supporters.append(Fan(username=thumb['username'], token=thumb['token']))

for review in output['reviews']:
    supporters.append(Fan(username=review['username'], token=review['token']))

#print('json_output last username', json_output[-1]['username'])

more_thumbs_available = output["more_thumbs_available"]


