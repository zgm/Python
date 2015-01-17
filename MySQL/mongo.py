
import pymongo
from pymongo import MongoClient

#conn = MongoClient('localhost',27017)
conn = pymongo.Connection(host='localhost',port=27017)
print conn.database_names()

db = conn.test
print db
collection = db.collection_names()
print collection

table = db.testData
print table
for document in table.find(): print document
print table.find_one()

table.update({'insert':'py'},{'insert':'py3'})
#table.insert({'insert':'py'})

