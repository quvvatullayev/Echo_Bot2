import json, requests

TOKIN = '5505244566:AAFRwoxaYH-ahK27OKN0_6MPKStev9LJ1R4'

def getUpdates():
    url = f'https://api.telegram.org/bot{TOKIN}/getUpdates'
    data = requests.get(url)
    return data.json()

def sendMessage(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKIN}/sendMessage'
    data = requests.get(url, params={'chat_id':chat_id, 'text':text})
    return data.json()

def sendDocument(chat_id, document):
    url = f'https://api.telegram.org/bot{TOKIN}/sendDocument'
    data = requests.get(url, params={'chat_id':chat_id, 'document':document})
    return data.json()

def sendPhoto(chat_id, photo):
    url = f'https://api.telegram.org/bot{TOKIN}/sendPhoto'
    data = requests.get(url, params={'chat_id':chat_id, 'photo':photo})
    return data.json()

def sendDice(chat_id, emoji):
    url = f'https://api.telegram.org/bot{TOKIN}/sendDice'
    data = requests.get(url, params={'chat_id':chat_id, 'emoji':emoji})
    return data.json()

def sendSticker(chat_id, sticker):
    url = f'https://api.telegram.org/bot{TOKIN}/sendSticker'
    data = requests.get(url, params={'chat_id':chat_id, 'sticker':sticker})
    return data.json()

def sendVideo(chat_id, video):
    url = f'https://api.telegram.org/bot{TOKIN}/sendVideo'
    data = requests.get(url, params={'chat_id':chat_id, 'video':video})
    return data.json()

def sendAudio(chat_id, audio):
    url = f'https://api.telegram.org/bot{TOKIN}/sendAudio'
    data = requests.get(url, params={'chat_id':chat_id, 'audio':audio})
    return data.json()

def sendVoice(chat_id, voice):
    url = f'https://api.telegram.org/bot{TOKIN}/sendVoice'
    data = requests.get(url, params={'chat_id':chat_id, 'voice':voice})
    return data.json()

def sendVideoNote(chat_id, video_note):
    url = f'https://api.telegram.org/bot{TOKIN}/sendVideoNote'
    data = requests.get(url, params={'chat_id':chat_id, 'video_note':video_note})
    return data.json()

def sendAll(chat_id, document, text, photo, emoji, sticker, video, audio, voice, video_note):
    if document:
        sendDocument(chat_id, document)
    elif text:
        sendMessage(chat_id, text)
    elif photo:
        sendPhoto(chat_id, photo)
    elif emoji:
        sendDice(chat_id, emoji)
    elif sticker:
        sendSticker(chat_id, sticker)
    elif video:
        sendVideo(video)
    elif audio:
        sendAudio(chat_id, video)
    elif voice:
        sendVoice(chat_id, voice)
    elif video_note:
        sendVideoNote(chat_id, video_note)

def getData(data):
    data = data['result'][-1]
    update_id = data['update_id']
    chat_id = data['message']['from']['id']

    text = data['message'].get('text')
    document = data['message'].get('document')
    photo = data['message'].get('photo')
    emoji = data['message'].get('dice')
    sticker = data['message'].get('sticker')
    video = data['message'].get('video')
    audio = data['message'].get('audio')
    voice = data['message'].get('voice')
    video_note = data['message'].get('video_note')

    if video_note:
        video_note = video_note['file_id']
    if voice:
        voice = voice['file_id']
    if video:
        video = video['file_id']
    if audio:
        audio = audio['file_id']
    if sticker:
        sticker = sticker['file_id']
    if emoji:
        emoji = emoji['emoji']
    if document:
        document = document['file_id']
    if photo:
        photo = photo[0]['file_id']
    return update_id, chat_id, document,text,photo, emoji, sticker, video, audio, voice, video_note

s = ''
while True:
    data = getData(getUpdates())
    update_id, chat_id, document, text, photo, emoji, sticker, video, audio, voice, video_note = data
    if s != update_id:
        sendAll(chat_id, document, text, photo, emoji, sticker, video, audio, voice, video_note)
        s = update_id