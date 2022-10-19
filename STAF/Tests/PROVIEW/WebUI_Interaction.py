from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import time
import configparser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import requests
import urllib3


import json
import adal
import os,sys


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
try:
    #Get the QR Code from PIC6 through API
    header ={"Content-Type":"application/json"}
    params ={"password":"0","username":"basic"}
    pic6_login = requests.post(url='https://169.254.1.1/PIC6/api/auth/login',json=params,headers = header,verify=False)
    pic6_token=str(json.loads(pic6_login.content)[0]['token'])

    params= {"pathlist":[{"widgetType":"PointValue","path":"db/fact_QR_code_string//active-text"}],"token":pic6_token}
    qrcode_result=requests.post(url='https://169.254.1.1/PIC6/api/point_value/getpointvalue',json=params,headers = header,verify=False)
    qrcode_val = json.loads(qrcode_result.content)['pathlist'][0]['value']
    qrcode_val = str(qrcode_val.replace(" ", ""))

    print("PIC6 QR-code: " ,qrcode_val)
    params = {"token":pic6_token}
    pic6_login = requests.post(url='https://169.254.1.1/PIC6/api/auth/logout', json=params, headers=header, verify=False)
    # qrcode_val = "oksx037m5nmvnxwe"
    #Get the bearer token with client id, username and password, working code uses dev environment#
    cloud_url = 'https://smartchillerapidev.azure-api.net/passwordmanagement/generatedevicePassword?code='+qrcode_val+'&subscription-key=764c62200f624042a467b7a7a0d2ad3f'

    #prod'https://cscapiprod.azure-api.net/passwordmanagement/generatedevicePassword?code='+qrcode_val+'&subscription-key=aac84bca998d4500aa0b02c005b021d0'                                                                                                                    #test # 'https://smartchillerpasswordmanagementapidev-test.azurewebsites.net/generatedevicePassword?code='+qrcode_val+'&subscription-key=764c62200f624042a467b7a7a0d2ad3f'

    #Authentication parameters for bearer token
    parameters = {
        "resource": "d382cc7b-1c6b-4e19-bc00-d7dbf1e34950",
        "tenant": 'utccloud.onmicrosoft.com',
        "authorityHostUrl": "https://login.microsoftonline.com",
        "clientId": "eb0037a6-dc22-49f6-a453-d87f9741b5aa",
        "username": "yogeshkumar.thumati@carrier.com",
        "password": "Yogi@123",#"Smart@2021",
        "clientSecret": "x/D61TsK6WzfVMyo3hZj?dM[dXhzqqS["
    }

    authority_url = (parameters['authorityHostUrl'] + '/' + parameters['tenant'])
    GRAPH_RESOURCE = '00000002-0000-0000-c000-000000000000'
    RESOURCE = parameters.get('resource', GRAPH_RESOURCE)


    ### Main logic begins
    context = adal.AuthenticationContext(
        authority_url, validate_authority=parameters['tenant'] != 'adfs',
    )

    token = context.acquire_token_with_username_password(
        RESOURCE,
        parameters["username"],
        parameters["password"],
        parameters['clientId']
        )

    auth_token ='Bearer '+token['accessToken']
    print("Bearer Token: ", auth_token)
    auth_token_url =cloud_url+"&Authorization="+auth_token
    #get the password from API using api url, qr code, subscription key and auth token
    time.sleep(5)
    pass_rd = requests.get(url=cloud_url,headers={"Authorization":auth_token})
    rolling_password = json.loads(pass_rd.content)["Password"]
    print("Rolling Password: ",rolling_password)

except:
    print("exception occured")



