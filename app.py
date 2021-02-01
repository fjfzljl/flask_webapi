# -*- coding:utf-8 -*-

#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
import json

app = Flask(__name__)

stores = [
    {
        # 'id': 1,
        'name': u'Costco',
        'value': u'Burnaby'
    },
    {
        # 'id': 2,
        'name': u'Superstore',
        'value': u'Vancouver'
    },
    {
        # 'id': 3,
        'name': u'LondonDrug',
        'value': u'Surrey'
    },
    {
        # 'id': 4,
        'name': u'ShoppersDrug',
        'value': u'Richmond'
    },
    {
        'name': u'Walmart',
        'value': u'Vancouver'
    },
    {
        'name': u'CanadianTire',
        'value': u'Burnaby'
    }
]

# Index:
@app.route('/')
def index():
    return "Hello, World!"

# Create New Store
@app.route('/kvstore', methods=['POST'])
def create_store():
    if not request.json or not 'name' in request.json:
        abort(400)

    store = {
        'name': request.json['name'],
        'value': request.json.get('value', "")
    }

    for record in stores:
        if store['name'] == record['name']:
            abort(409)
    stores.append(store)
    return jsonify({'store': store}), 201

# Get All Stores
@app.route('/kvstore', methods=['GET'])
def get_stores():

    return jsonify({'stores': stores})

# Get Specific Store
@app.route('/kvstore/<string:store_name>', methods=['GET'])
def get_store(store_name):

    store = [store for store in stores if store['name'] == store_name]
    if len(store) == 0:
        abort(404)
    return jsonify({'store': store[0]})

# Update Store
@app.route('/kvstore', methods=['PUT'])
def update_store():

    # print("request result :  " + request.json)
    if not request.json or not 'name' in request.json:
        abort(400)

    store_up = json.loads(request.json)
    mystore = [store for store in stores if store['name'] == store_up['name']]
    if len(mystore) == 0:
        abort(404)

    for i, store in enumerate(stores):
        print(str(i) + ": " + store['name'] + "  " + store['value'])
        # if (store['name'] == store_up.get('name') and store['value'] == store_up.get('value')):
        #     abort(500,'No need to update')
        #     break
        if (store['name'] == store_up.get('name') and store['value'] != store_up.get('value')):
            stores[i]=store_up
            continue


    return jsonify({'store': store_up})


@app.route('/kvstore/<string:store_name>', methods=['DELETE'])
def delete_store(store_name):
    store = [store for store in stores if store['name'] == store_name]
    if len(store) == 0:
        abort(404)
    d_v = store[0]
    stores.remove(store[0])
    return jsonify({'store': d_v}), 200

@app.route('/kvstore', methods=['PATCH'])
def other_store():
    print("request method: " + request.method)
    # if (request.method != 'POST') and (request.method != 'GET') and (request.method != 'PUT') and (request.method != 'DELETE'):
    abort(405)
        # return 'Not request by POST, GET, PUT, DELETE'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(409)
def duplicate_record(error):
    return make_response(jsonify({'error': 'The name already exists'}), 409)

@app.errorhandler(405)
def not_permit_operation_record(error):
    return make_response(jsonify({'error': 'Method Not Allowed'}), 405)
    
if __name__ == '__main__':
    # app.run(debug=True)
    # app.run(host="0.0.0.0", port=80, debug=True)
    app.run(host='0.0.0.0', port=80)