__author__ = 'Alan'

import requests
import shutil
import API_KEY

PATCH_VERSION = '4.21.5'
REGIONAL_ENDPOINT = 'na.api.pvp.net'

def getIcon(patchVersion, champName):
    url = 'http://ddragon.leagueoflegends.com/cdn/{0}/img/champion/{1}.png'.format(patchVersion, champName)
    response = requests.get(url, stream=True)
    with open('C:\\Users\Alan\Documents\GitHub\LoL_projects\ChampIcons\{}.png'.format(champName), 'wb') as outFile:
        shutil.copyfileobj(response.raw, outFile)
    del response

#getIcon(PATCH_VERSION, '512')

ChampList = requests.get('https://{0}/api/lol/na/v1.2/champion?api_key={1}'.format(REGIONAL_ENDPOINT, API_KEY.API_KEY)).json()
for champ in ChampList['champions']:
    champ_info = requests.get('https://{0}//api/lol/static-data/na/v1.2/champion/{1}?api_key={2}'.format(REGIONAL_ENDPOINT, champ['id'], API_KEY.API_KEY)).json()
    getIcon(PATCH_VERSION, champ_info['name'])