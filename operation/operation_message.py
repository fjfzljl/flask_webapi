import requests
import json
import urllib3


KVSTORE_URL = 'http://localhost/kvstore'

class operation_message_Error(Exception):
    """
        An exception class for operation_message
    """

class operation_message(object):
    """
     Webservice operation : GET, POST, DELETE, PUT, HEAD, PATCH
    """
    
    def __init__(self,url):
        self.url = url
    
    def opd_get(self,url_add = ''):
        if len(url_add) > 0:         
            get_url = self.url + '/'+ url_add
        else:
            get_url = self.url
        response = requests.get(get_url)
        return response
    
    def opd_post(self,data=''):
        response = requests.post(self.url, json=data)
        return response
        
    def opd_put(self,data=''):
        response = requests.put(self.url, json=json.dumps(data))
        return response

    def opd_delete(self,url_add = 'name'):
        delete_url = self.url + '/' + url_add
        response = requests.delete(delete_url)
        return response

    def opd_head(self):
        head_url = self.url
        response = requests.head(head_url)
        return response

    def opd_patch(self):
        patch_url = self.url
        response = requests.patch(patch_url)
        return response


    def opd_options(self):
        options_url = self.url
        response = requests.options(options_url)
        return response


if __name__ == '__main__':
    test_url = KVSTORE_URL
    operation = operation_message(test_url)

    print('---test get: ')
    r = operation.opd_get()
    print(r.content)

    print('---test post: ')
    post_data = {'name':'tnt','value':'Metrotown'}
    r = operation.opd_post(post_data)
    print(r.content)
    print(r.status_code)    

    spec = '/tnt'
    r = operation.opd_get(spec)
    print(r.content)
    

    print('---test put: ')
    put_data = {'name':'tnt','value':'North Vancouver'}
    r = operation.opd_put(put_data)
    print(r.content)
    print(r.status_code)    

    print('---put content')
    print(r.content)
    print(r.headers)

    r = operation.opd_get(spec)
    print(r.content)

    print('---test delete: ')
    r = operation.opd_delete(spec)
    print(r.content)
    print(r.status_code)    

    r = operation.opd_get(spec)
    print(r.content)

    print('---test head: ')
    r = operation.opd_head()
    print(r.content)
    print(r.status_code)    

    print('---test patch: ')
    r = operation.opd_patch()
    print(r.content)
    print(r.status_code)    

    print('---test options: ')
    r = operation.opd_options()
    print(r.content)
    print(r.status_code)    

    print('---test post special: ')
    post_data = {'name': 'tspu', 'value': ')(&'}
    r = operation.opd_post(post_data)
    print(r.content)
    print(r.status_code)    

    print('---test post special exists: ')
    post_data = {'name': 'tspu', 'value': ')(&'}
    r = operation.opd_post(post_data)
    print(r.content)
    print(r.status_code)    

    print('---test post empty: ')
    post_data = {'name': '', 'value': 'temp'}
    r = operation.opd_post(post_data)
    print(r.content)
    print(r.status_code)    
