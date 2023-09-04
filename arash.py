import json
from telethon import TelegramClient

api_id = 20943743
api_hash = "6b97d1f4da545ab543b0a8c8831c1aee"
client = TelegramClient('alireza', api_id, api_hash)

async def main():
    all_messages = {}
    all_images_list = []

    chats = ['Tasnimnews','mehrnews','irna_1313','farsna','ManotoTV','IranintlTV']
    for chat in chats:
        messages = await client.get_messages(chat,limit=1)
        for message in messages:
            print(message)
            message_type = ''
            media_id = ''
            try:
                if message.media.document.mime_type:
                    temp = str(message.document.id)
                    media_id = temp[::-1]
                    message_type = 'video'
                    path = await message.download_media(media_id,thumb=-1)
                    print('File saved to', path)
                    all_images_list.append(media_id)
            except AttributeError:
                print('error',message)

            try:
                if(message.photo.id):
                    temp = str(message.photo.id)
                    media_id = temp[::-1]
                    message_type = 'image'
                    path = await message.download_media(media_id)
                    print('File saved to', path)
                    all_images_list.append(media_id)
            except AttributeError:
                print('error',message)

            message_dict = {
                'channel':chat,
                'message':getattr(message,'message',''),
                'views':message.views,
                'message_type' : message_type,
                'media_id': media_id
            }
            all_messages[message.id] = message_dict

    with open('msg.json','w',encoding='utf-8') as file:
        file.write(json.dumps(all_messages) + '\n')

with client:
    client.loop.run_until_complete(main())
    