import pymongo

client = pymongo.MongoClient()
db = self.client.['noater-db']
collection = self.db['noats']

def build_crud(host, port, db_name, collection_name):
  client = pymongo.MongoClient(host, port)
  collection = client[db_name][collection_name]

  def create(self, data):
    for name, noat in data.items():
      collection.update({'name' : name}, {'$set' : noat}, upset = True)

  def read(self, data):
    return [collection.find_one({'name' : name }) for name in data]

  def update(self, data):
    for name, noat in data.items():
      collection.update({'name' : name}, {'$set' : noat}, upsert = False)

  def delete(self, data):
    for name in data:
      collection.remove ({'name' : name})

  return create, read, update, delete

