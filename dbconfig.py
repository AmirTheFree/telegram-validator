# In the name of Allah

from sqlalchemy import MetaData,Table,Column,Integer,String,create_engine,Boolean
from dbinfo import host,port,username,password,name,system,driver

meta = MetaData()
engine = create_engine(f'{system}+{driver}://{username}:{password}@{host}/{name}')

numbers = Table(
    'numbers',meta,
    Column('id',Integer,primary_key=True),
    Column('number',String(14),nullable=False,unique=True),
    Column('has_telegram',Boolean,nullable=False,default=False),
    Column('username',String(32),nullable=True)
)

meta.create_all(engine)

dbconnection = engine.connect()