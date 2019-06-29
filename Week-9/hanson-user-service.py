# ============================================
# ; Title:  hanson-User-Service.py
# ; Author: Professor Krasso
# ; Date:  29 June 2019
# ; Modified By: Drew Hanson
# ; Description: querying and creating documents with Python and pymongo
# ;===========================================

from pymongo import MongoClient

import pprint

import datetime

client=MongoClient('localhost', 27017)

db=client.web335

user={
    "first_name": "billy",
    "last_name": "bob",
    "email": "billybob@gmail.com",
    "employee_id": "789456",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id

print(client)

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "789456"}))