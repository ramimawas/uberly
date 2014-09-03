# MIT Licensed
# Copyright 2014 REM <rami.developer@gmail.com>.

from pymongo import MongoClient
from pymongo import DESCENDING
import utility
from porter import PorterStemmer

p = PorterStemmer()

client = MongoClient('localhost', 27017)
db = client.uberly
clt = db.uber_vocab_1

#db.uber_dictionary.find().limit(50).sort({value:-1}).pretty()
for entry in clt.find().sort([('value', DESCENDING)]):
  entry['stem'] = p.stem(entry['_id'], 0,len(entry['_id'])-1)
  clt.save(entry)
  print(entry['_id']), entry['stem']
  