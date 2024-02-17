#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('my-mongo')
db = client.demo

count = db.users.count_documents({})
users = db.users.find()

print('--------------------------------')
print('connected to MongoDB')
print('--------------------------------')
print('Found {} users.'.format(count))

for document in users:
    print(document)
