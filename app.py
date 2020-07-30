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

data = dbconnection.execute(numbers.select()).fetchall()
for d in data:
	result = t.call_method('importContacts',params = {'contacts':[{'phone_number':d[1]}]})
	result.wait()
	if result.update['user_ids'][0] != 0:
		dbconnection.execute(numbers.update().values(user_id = result.update['user_ids'][0]).where(numbers.c.number == d[1]))

data = dbconnection.execute(numbers.select()).fetchall()
for d in data:
	if d[2] != None:
		result = t.call_method('getUser',params = {'user_id' : d[2]})
		result.wait()
		if result.update['username']:
			dbconnection.execute(numbers.update().values(username = result.update['username']).where(numbers.c.user_id == d[2]))


