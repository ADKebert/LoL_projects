__author__ = 'Alan'

import requests
import API_KEY

#test_item = (requests.get('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/RiotSchmick?api_key={}'.format(API_KEY.API_KEY)))

#print(test_item.json())

#schmick = test_item.json()

#print(schmick['riotschmick']['name'])

REGIONAL_ENDPOINT = 'na.api.pvp.net'

champ_test = requests.get('https://{0}/api/lol/na/v1.2/champion?freeToPlay=true&api_key={1}'.format(REGIONAL_ENDPOINT, API_KEY.API_KEY))

print(champ_test.json())

champs = champ_test.json()

for champ in champs['champions']:
    champ_info = requests.get('https://{0}//api/lol/static-data/na/v1.2/champion/{1}?api_key={2}'.format(REGIONAL_ENDPOINT, champ['id'], API_KEY.API_KEY)).json()
    print(champ_info['name'])


