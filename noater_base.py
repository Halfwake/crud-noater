#!/usr/bin/env python 

import noater_db

from flask import Flask, jsonify

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

def build_api(db_create, db_read, db_update, db_delete):
  invalid_data_message = jsonify({'error' : 'invalid data'})
  invalid_data_response = (invalid_data_message, 400)
  def post(json):
    if self.verify_noats(json):
      db_create(json)
      return '', 200
    else:
      return invalid_data_response

  def get(json):
    if verify_names(json):
      result = db_read(json) 
      return jsonify(result), ''
    else:
      return invalid_data_response

  def put(json):
    if verify_noats(json):
      db_update(json)
      return '', 200
    else:
      return invalid_data_response

  def delete(json):
    if verify_names(json):
      result = db_delete(json)
      return '', 200
    else:
      return invalid_data_response

  return post, get, put, delete

if __name__ == '__main__':

  app = Flask(__name__)
  api = Api(app)

  db_crud, db_close = noater_db.make_crud('localhost', 27017, 'noater-db', 'noats')
  post, get, put, delete = build_api(*crud)

  @app.route('/api/v0.1/create', methods = ['POST'])
  def create_noat():
    return post(request.json)

  @app.route('/api/v0.1/read', methods = ['GET'])
  def get_handler():
    return get(request.json)

  @app.route('/api/v0.1/update', methods = ['PUT'])
  def put_handler():
    return put(request.json)

  @app.route('/api/v0.1/delete', methods = ['DELETE'])
  def delete_handler():
    return delete(request.json)

  try:
    app.run()
  finally:
    db_close()

