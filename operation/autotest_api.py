# -*- coding:utf-8 -*-
import requests
import json
import urllib3
import csv
import yaml

from operation_message import operation_message, operation_message_Error

KVSTORE_URL = "http://localhost/kvstore"
TEST_DATA_FILE = 'autotest_data.csv'
TEST_RESULT_FILE = 'test_result.csv'


class api_test(object):

    def __init__(self, opd, url=KVSTORE_URL, spec='', data='', expected_status_code='200',description = ''):

        self.opd = opd
        self.url = url 
        self.spec = spec
        self.data = data
        self.expected_status_code = int(expected_status_code)
        self.description = description

    def test_and_compare_resut(self):
        
        op_msg = operation_message(KVSTORE_URL)

        test_case_record = {}

        test_case_record["operation"] = self.opd
        test_case_record["url"] = self.url
        test_case_record['data'] = self.data 
        test_case_record['expected_status_code'] = self.expected_status_code

        print('---------')
        print(test_case_record)
        print('---------')

        if self.opd == 'POST':
            
            response = op_msg.opd_post(self.data)
        
        elif self.opd == 'GET':
            if self.spec:
                response = op_msg.opd_get(self.spec)
            else:
                response = op_msg.opd_get()
        
        elif self.opd == 'PUT':
            response = op_msg.opd_put(self.data)

        elif self.opd == 'DELETE':
            response = op_msg.opd_delete(self.spec)            
        
        else:
            response = op_msg.opd_patch()            

        test_case_record['actual_status_code'] = response.status_code

        if test_case_record['expected_status_code'] != test_case_record['actual_status_code']:
            test_case_record['result'] = 'Fail'
        else:
            test_case_record['result'] = 'pass'

        test_case_record['spec'] = self.spec
        test_case_record['description'] = self.description

        return test_case_record


def main():
    csv_file = open(TEST_DATA_FILE, "r")
    dict_reader = csv.DictReader(csv_file)

    test_cases =  list(dict_reader)
    test_cases_result = []

    for test_case in test_cases:
        print('test case information : ')
        ts = dict(test_case)
        print(ts)

        # print(ts['opd'])

        ts_opd = ts['opd'] 
        ts_spec = ts['spec']
        # tmpstr = ts['data'][0:len(ts['data'])]
        # print(ts_data_str)

        # tmpstr = str(ts['data']).strip().replace("'","\"")
        print("data:" + ts['data'])
        # print("datastr:" + tmpstr)
        d = yaml.load(ts['data'])
        ts_data = d
        ts_expected = ts['expected_status_code']
        ts_description = ts['description']

        print('test case data :')
        print(ts)

        api_t = api_test(opd=ts_opd,spec=ts_spec,data=ts_data,expected_status_code=ts_expected, description=ts_description)

        print('test case result:')
        test_result_record = api_t.test_and_compare_resut()
        print(test_result_record)

        test_cases_result.append(test_result_record)

    print('test_cases_result:---------')
    print(test_cases_result)
    result_hearder = ['operation', 'url', 'spec','data', 'expected_status_code', 'actual_status_code', 'result','description']
    with open(TEST_RESULT_FILE, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=result_hearder)
        writer.writeheader()
        writer.writerows(test_cases_result)

    return


if __name__=='__main__':
    main()

