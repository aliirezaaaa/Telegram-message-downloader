from telethon.sync import TelegramClient, connection
import datetime
import pandas as pd
import socks
import requests

response = requests.get("https://ipinfo.io/json")
if response:
    print(response.json())
api_id = 20943743
api_hash = "6b97d1f4da545ab543b0a8c8831c1aee"

client =  TelegramClient('test', api_id, api_hash)
client.start()

chats = ['ManotoTV']
for message in client.get_messages(chats[0],limit=2):
    print(message.id, message.text)
    
# df = pd.DataFrame()


# for chat in chats:
#     with TelegramClient('test', api_id, api_hash) as client:
#         for message in client.iter_messages(chat, offset_date=datetime.date.today() , reverse=True):
#             print(message)
            # data = { "group" : chat, "sender" : message.sender_id, "text" : message.text, "date" : message.date}

            # temp_df = pd.DataFrame(data, index=[1])
            # df = df.append(temp_df)

# df['date'] = df['date'].dt.tz_localize(None)

# df.to_excel("C:\\crypto\\data_{}.xlsx".format(datetime.date.today()), index=False)