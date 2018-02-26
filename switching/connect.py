from urllib.request import urlopen, Request
import requests
import urllib.parse
import json
import re
HOST_CID = 'https://api.neople.co.kr/df/servers/<serverId>/characters/<characterId>/skill/buff/equip/<url>?apikey='
HOST_CNAME ='https://api.neople.co.kr/df/servers/<serverId>/characters?characterName=<characterName>&limit=<limit>&wordType=<wordType>&apikey='
BUFF = 'skill/buff/equip/'
APIKEY = 'USctY4GfphJHwslYdETJ1ILvdkIE9IB9'


def get_characterId(serverName,characterName):
    encodeCharacterName = urllib.parse.quote(characterName, safe='')
    tmpHost = HOST_CNAME
    tmpHost = re.sub('<serverId>', serverName, tmpHost)
    tmpHost = re.sub('<characterName>', encodeCharacterName, tmpHost)
    api_url = tmpHost + APIKEY
    req = requests.get(api_url)
    data = json.loads(req.text)
    return(data['rows'][0]['characterId'])

def get_response(url, serverName, characterId):
    tmpHost = HOST_CID
    tmpHost = re.sub('<serverId>', serverName, tmpHost)
    tmpHost = re.sub('<characterId>', characterId, tmpHost)
    tmpHost = re.sub('<url>', url, tmpHost)
    api_url = tmpHost + APIKEY
    print(api_url)
    req = requests.get(api_url)
    return json.loads(req.text)
