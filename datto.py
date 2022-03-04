import json
import requests


tok='XJqlvIKT5IFHIE8RzuZO05GQ'
contentId='a0m3j00000i4B3o'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'KeepAlive': 'True',
    'Authorization': 'Bearer %s' % tok
}

params = {
    ('target', 'SiteAddPageDataServer'),
    ('action', 'get'),
    ('contentId', contentId),
}

try:
    response = requests.get('https://demoURLsimpplr.visualforce.com/apex/DataServerRW', headers=headers, params=params)
    print(response)
    print(response.content)
    try:
            statJson = json.loads(response.content)
            print(statsJson)
    except Exception as e:
            print(e)
except Exception as e:
    print(e)


print("completion")
