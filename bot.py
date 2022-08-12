import requests, json, pprint

def Bot_info(data:json) -> json:
    data = data['result']
    for i in data:
        userid = i['message']['from']['id']
        usertext = i['message']['text']
    url = 'https://api.telegram.org/bot5567524975:AAHH4ioN3ZGUXbzPPPrXNk2tdWJU3O_fFyk/sendMessage'
    r = requests.get(url, params={'chat_id':userid, 'text':usertext})

"""send a request to the function"""
            #URL request
url = 'https://api.telegram.org/bot5567524975:AAHH4ioN3ZGUXbzPPPrXNk2tdWJU3O_fFyk/getUpdates'
r = requests.get(url)
h = r.json()
x = Bot_info(h)
print(x)