# In the name of Allah

from sqlalchemy import MetaData,Table,Column,Integer,String,create_engine,Boolean
from dbinfo import host,port,username,password,name,system,driver

meta = MetaData()
engine = create_engine(f'{system}+{driver}://{username}:{password}@{host}/{name}')

numbers = Table(
    'numbers',meta,
    Column('id',Integer,primary_key=True),
    Column('number',String(14),nullable=False,unique=True),
    Column('user_id',Integer,nullable=True,default=None),
    Column('username',String(32),nullable=True)
)

meta.create_all(engine)

dbconnection = engine.connect()

# To add a new number uncomment lines below and run current file once

# new_number = numbers.insert().values(number = 'phone number here')
# dbconnection.execute(new_number)