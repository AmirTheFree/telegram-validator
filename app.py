# In the name of Allah

from dbconfig import numbers,dbconnection
from telegram.client import Telegram
from tinfo import api_id,api_hash,data_base_encryption_key,phone#,proxy_server,proxy_type,proxy_port

t = Telegram(
    api_id=api_id,
    api_hash=api_hash,
    phone=phone,
    database_encryption_key=data_base_encryption_key#,
    # proxy_type=proxy_type,
    # proxy_server=proxy_server,
    # proxy_port=proxy_port
    )
t.login()

def new_message_handler(update):
    print('New message!')

t.add_message_handler(new_message_handler)
t.idle()