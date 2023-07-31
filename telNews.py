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


# proxy = (socks.SOCKS5, '178.33.3.163', '8080')
# # proxies = {
# #     'https' : 'https://10.2.6.222:8080'
# # }

connection = connection.ConnectionTcpMTProxyRandomizedIntermediate
client =  TelegramClient('test', api_id, api_hash, connection=connection, proxy=('Unknown', 443, 'eeda411655b684fe87abf58ec2235e28167765622e62616c652e6972'))
# client =  TelegramClient('test', api_id, api_hash)
client.start()

chats = ['alliirrreza']
# for message in client.iter_messages("alliirrreza"):
#     print(message.id, message.text)
    
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