import pytest
import requests
import json
import urllib3

from operation.operation_message import operation_message, operation_message_Error

# url = 'http://localhost/kvstore'
KVSTORE_URL = 'http://localhost/kvstore'


# valid post : key not exists
def test_create_store():

    op_msg = operation_message(KVSTORE_URL)

    data = {'name':'tnt','value':'Metrotown'}

    try:
        spec = data["name"]
        response = op_msg.opd_delete(spec)
        print(response.status_code)
    except:
        print('delete data error')    

    response = op_msg.opd_post(data)
    print(response)  

    assert response.status_code == 201

    res = json.loads(response.content)    
    assert res["store"]["name"] == data["name"]



# invalid post : key already exists
def test_create_store_conflict():

    op_msg = operation_message(KVSTORE_URL)

    data = {'name':'tnt_1','value':'Metrotown'}

    response = op_msg.opd_post(data)
    response = op_msg.opd_post(data)
    
    assert response.status_code == 409

    res = json.loads(response.content)    
    assert res["error"] == "The name already exists"

# valid get all
def test_get_stores():
    op_msg = operation_message(KVSTORE_URL)

    response = op_msg.opd_get()

    assert response.status_code == 200

    res = json.loads(response.content)    
    assert len(res["stores"]) >= 0 

# valid get : key already exists
def test_get_store():
    op_msg = operation_message(KVSTORE_URL)

    data = {'name':'tnt_2','value':'Metrotown'}
    spec = data["name"]

    try:
        response = op_msg.opd_post(data)
        print(response.status_code)
    except:
        print('post data error')    

    response = op_msg.opd_get(spec)

    assert response.status_code == 200

    res = json.loads(response.content)    
    assert res["store"]["name"] == data["name"]


# invalid get : key not exists
def test_get_store_not_exist():

    op_msg = operation_message(KVSTORE_URL)

    spc = '/!@#9' 
    response = op_msg.opd_get(spc)

    assert response.status_code == 404

    res = json.loads(response.content)    
    assert res["error"] == "Not found"

# valid delete : key exists
def test_delete_store():
    op_msg = operation_message(KVSTORE_URL)

    data = {'name':'tnt_1','value':'Metrotown'}
    spec = data["name"]

    try:
        response = op_msg.opd_post(data)
        print(response.status_code)
    
    except:
        print('post data error')

    response = op_msg.opd_delete(spec)
    assert response.status_code == 200

    res = json.loads(response.content)    
    assert res["store"]["name"] == data["name"]

# invalid delete : key not exists
def test_delete_store_not_exist():

    op_msg = operation_message(KVSTORE_URL)

    spc = '!@$%^' 
    response = op_msg.opd_delete(spc)

    assert response.status_code == 404

    res = json.loads(response.content)    
    assert res["error"] == "Not found"

# valid put : key already exists
def test_update_store():

    op_msg = operation_message(KVSTORE_URL)

    data = {'name':'tnt_3','value':'Metrotown'}
    spec = data["name"]

    put_data= {}
    put_data["name"] = data["name"]
    put_data["value"] = "put change"

    try:
        response = op_msg.opd_post(data)
        print(response.status_code)
    except:
        print('post data error')    

    response = op_msg.opd_put(put_data)

    assert response.status_code == 200
    print(response.content)
    res = json.loads(response.content)    
    assert res["store"]["name"] == put_data["name"]
    assert res["store"]["value"] == put_data['value']


# invalid put : key not exists
def test_update_store_not_exist():

    op_msg = operation_message(KVSTORE_URL)

    put_data = {'name':'&^%$$&*=[]','value':'Metrotown'}
    spec = put_data["name"]

    response = op_msg.opd_put(put_data)

    assert response.status_code == 404

    res = json.loads(response.content)    
    assert res["error"] == "Not found"


# other request : PATCH, HEAD
def test_other_store():
    op_msg = operation_message(KVSTORE_URL)

    response = op_msg.opd_patch()

    assert response.status_code == 405


