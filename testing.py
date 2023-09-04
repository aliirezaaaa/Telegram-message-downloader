import json
from telethon import TelegramClient

# Remember to use your own values from my.telegram.org!
api_id = 20943743
api_hash = "6b97d1f4da545ab543b0a8c8831c1aee"
client = TelegramClient('alireza', api_id, api_hash)

async def main():
    # Getting information about yourself
    #me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    #print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    # username = me.username
    # print(username)
    # print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    # async for dialog in client.iter_dialogs():
    #     print(dialog.name, 'has ID', dialog.id)

    # You can print the message history of any chat:
    # async for message in client.iter_messages('me'):
    #     print(message.id, message.text)

        # You can download media from messages, too!
        # The method will return the path where the file was saved.
        # if message.photo:
        #     path = await message.download_media()
        #     print('File saved to', path)  # printed after download is done


    #   MY CODE IS THIS:    
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
                    # print('1',message.document.id)
                    temp = str(message.document.id)
                    media_id = temp[::-1]
                    message_type = 'video'
                    path = await message.download_media(media_id,thumb=-1)
                    print('File saved to', path)
                    all_images_list.append(media_id)
            except AttributeError:
                # media_id = None
                # message_type = 'text'
                print('error',message)

            try:
                if(message.photo.id):
                    # print('2',message.photo.id)
                    temp = str(message.photo.id)
                    media_id = temp[::-1]
                    message_type = 'image'
                    path = await message.download_media(media_id)
                    print('File saved to', path)
                    all_images_list.append(media_id)
            except AttributeError:
                # media_id = None
                # message_type = 'text'
                print('error',message)

            # temp = message.to_dict()
            # # temp.pop('date')
            # all_messages[chat] = temp
            message_dict = {
                'channel':chat,
                'message':getattr(message,'message',''),
                'views':message.views,
                'message_type' : message_type,
                'media_id': media_id
            }
            all_messages[message.id] = message_dict

    with open('msg.json','w',encoding='utf-8') as file:
        # file.write(json.dumps(all_messages) + '\n' + json.dumps({'all_images_list' : all_images_list}))
        file.write(json.dumps(all_messages) + '\n')

with client:
    client.loop.run_until_complete(main())
    
