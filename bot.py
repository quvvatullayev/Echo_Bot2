import json, requests

TOKIN = '5567524975:AAHH4ioN3ZGUXbzPPPrXNk2tdWJU3O_fFyk'

def getUpdet():
    url = f'https://api.telegram.org/bot{TOKIN}/getUpdates'
    data = requests.get(url)
    return data.json()

def sendMessage(userId, userText):
    url = f'https://api.telegram.org/bot{TOKIN}/sendMessage'
    data = requests.get(url, params={'chat_id':userId, 'text':userText})
    return data.json()

def dataBeth(data):
    update_id = data[-1]['update_id']
    userText = data[-1]['message'].get('text')
    userId = data[-1]['message']['chat']['id']
    return update_id, userId, userText

s =  ''
while True:
    result = getUpdet()
    dB = dataBeth(result['result'])
    update_id,userId,userText = dB

    if s != update_id:
        sendMessage(userId, userText)
        s = update_id