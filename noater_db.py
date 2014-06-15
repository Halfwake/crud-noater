import pymongo

def build_crud(host, port, db_name, collection_name):
  client = pymongo.MongoClient(host, port)
  collection = client[db_name][collection_name]

  def create(data):
    for name, noat in data.items():
      collection.update({'name' : name}, {'$set' : noat}, upset = True)

  def read(data):
    return [collection.find_one({'name' : name }) for name in data]

  def update(data):
    for name, noat in data.items():
      collection.update({'name' : name}, {'$set' : noat}, upsert = False)

  def delete(data):
    for name in data:
      collection.remove ({'name' : name})

  close = lambda : client.close()

  return (create, read, update, delete), close

