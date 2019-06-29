# ============================================
# ; Title:  hanson-User-Service.py
# ; Author: Professor Krasso
# ; Date:  29 June 2019
# ; Modified By: Drew Hanson
# ; Description: updating and deleting documents with Python and pymongo
# ;===========================================

from pymongo import MongoClient

import pprint

import datetime

client=MongoClient('localhost', 27017)

db=client.web335

db.users.update_one(
    {"employee_id": "789456"},
    {
        "$set": {
            "email": "billybobUPDATE@gmail.com"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id": "789456"}))