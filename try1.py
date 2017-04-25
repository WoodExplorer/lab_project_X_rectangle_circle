from flask import Flask
from sqlalchemy import (create_engine, Table, Column, Integer, 
    String, MetaData)
from sqlalchemy.sql import select

app = Flask(__name__)

eng = create_engine("mysql://root:root@localhost/happykimi")


@app.route('/')
def hello_world():
    return 'Hello, World!!!!!!!!'

@app.route('/test_alchemy')
def test_alchemy():

    with eng.connect() as con:

        meta = MetaData(eng)
        user = Table('ot_user', meta, autoload=True)  

        print dir(user.c)
        stm = select([user.c.UE_ID, user.c.UE_account]).limit(3)
        rs = con.execute(stm) 

        print rs.fetchall()

    return 'Hello, World!!!!!!!!'