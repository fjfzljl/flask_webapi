# API Automation Framework

## Table of Contents
1. [Overview](#overview)
2. [System](#system)
3. [Setup](#setup)
    1. [Webservice](#web-service)
    2. [Unit test](#unit-test)
    3. [Sanity test](#sanity-test)
    4. [Auto test with data](#auto-test-with-data)
4. [File Structure](#file-structure)
    1. [Requirement](#requirements)
    2. [Testcases](#test-cases)


---

## Overview
flaskapi_test implements automate webservice POST,GET,PUT,DELETE test

---

## System
1. flaskapi_test works on windows 10, MacOS and Linux
2. flaskapi_test is implemented in Python 3.7 and required Python modules are listed requirements.txt

```
pip install requirements.txt
```

---

## Setup 

### Web service
Run app.py to setup webservice

```
sudo python app.py
```


### Unit test
test_app.py used to automation test app.py function

```
pytest
```

or

```
pytest test_app.py::<function name>
```

### Sanity test
operation/operation_message.py : used to sanity test, also includes operation Function : opd_get(), opd_post(), opd_delete(), opd_put()


### Auto test with data
operation/autotest_api.py : test with autotest_data.csv, output result to test_result.csv file

operation/autotest_api.csv : auto test input data (test data prepare not finished)

test_result.csv : auto test result 

operation/kvstore_concurrent.py : test for concurrently from multiple clients. 


---

## File Structure

### Requirements
documents/CodingTest_AutomationEngineerTest.docx : Requirements 

### Test Cases
documents/test_cases.xlsx : Test Cases 


---
Contact: jenny.liu.ca@gmail.com