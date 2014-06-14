import noater_db

import json
from functools import partial

from flask import Flask, request
from flask.ext.restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#400 bad request

def verify_names(json):
  'Verify that the names JSON is valid.'
  if not isinstance(json, list):
    return False
  for name in json:
    if not isinstance(name, str):
      return False
  return True

def verify_noats(json):
  'Verify that the noats JSON is valid.'
  if not isinstance(json, hash):
    return False
  for json_hash in json:
    if not set(json_hash.keys()) == set(['name', 'content']):
      return False
    if not all(lambda v : isinstance(v, str)):
      return False
    return True

#build_api(*noater_db.make_crud('localhost', 27017,'noater-db', 'noats')) # splat it in
def build_api(db_create, db_read, db_update, db_delete):
  def post(json):
    if self.verify_noats(json):
      db_create(json)
      return '', 200
    else:
      return 'invalid data', 400 

  def get(json):
    if verify_names(json):
      result = db_read(json) 
      return json.dumps(result), ''
    else:
      return 'invalid data', 400

  def put(json):
    if verify_noats(json):
      db_update(json)
      return '', 200
    else:
      return 'invalid data', 400

  def delete(json):
    if verify_names(json):
      result = db_delete(json)
      return '', 200
    else:
      return 'invalid data', 400

  return post, get, put, delete


# Have to make that into a resource class somehow
class NoatApi(Resource):
  def post(self, json):
    if self.verify_noats(json):
      db_create(json)
      return '', 200
    else:
      return 'invalid data', 400 

  def get(self, json):
    if verify_names(json):
      result = db_read(json) 
      return json.dumps(result), ''
    else:
      return 'invalid data', 400

  def put(self, json):
    if verify_noats(json):
      db_update(json)
      return '', 200
    else:
      return 'invalid data', 400

  def delete(self, json):
    if verify_names(json):
      result = db_delete(json)
      return '', 200
    else:
      return 'invalid data', 400

  
if __name__ == '__main__':
  app.run()
