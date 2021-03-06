import datetime
import json
import socket
from pymongo import MongoClient
import pyais
from pyais import FileReaderStream
from pyais.stream import UDPStream
from pyais import NMEAMessage

# NoSQL
client_mongo = MongoClient('localhost', 27017)
db_mongo = client_mongo.pymongo_ais_db

host = ""
port = 10110
counter = 0

for msg in UDPStream(host,port):
    counter += 1
    print(counter)
    try:
        message = msg.decode().to_json()
        message = json.loads(message)
        message['date'] = str(datetime.datetime.now())
        ais = db_mongo.ais
        result = ais.insert_one(message)
    except (AttributeError, OverflowError) as error:
        print ("Error: ",msg, error)
