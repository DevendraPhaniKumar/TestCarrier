######################################################################
#!/usr/bin/python                                                    #
#Copyright (c) 2017 Automated Logic Corporation                      #
#Author            : dayananda                                       # 
#File Description  : To Define classes and functions to use          #
#                    in the framework                                #
#History           : Created on Mar 27 , 2018                        # 
######################################################################

import time
import requests
import xml.etree.ElementTree as ET

###########################################  SOAP Web Servives Variables  #####################

url="http://localhost:83/_common/services/EvalService?wsdl"

GET_REQ_TEMPLATE = """<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">                  
    <Body>                                                                                          
        <getValue xmlns:xsi="http://localhost:83/_common/services/EvalService">                         
            <user>admin</user>                                                                      
            <passwd>password</passwd>                                                               
            <expression>%s</expression>                                                             
        </getValue>                                                                                 
    </Body>
</Envelope>"""

SET_REQ_TEMPLATE = """<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
    <Body>
        <setValue xmlns="http://localhost:83/_common/services/EvalService">
            <user>admin</user>
            <passwd>password</passwd>
            <expression>%s</expression>
            <newValue>%s</newValue>
            <changeReason>Update new value</changeReason>
        </setValue>
    </Body>
</Envelope>"""
###################################Closed#####################################################

SET_REQ_TEMPLATE_NULL = """<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
    <Body>
        <setValue xmlns="http://localhost:83/_common/services/EvalService">
            <user>admin</user>
            <passwd>password</passwd>
            <expression>%s</expression>
            <newValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true" />
            <changeReason>Update new value</changeReason>
        </setValue>
    </Body>
</Envelope>"""

#<newValue>%s</newValue>
# The below class is used to define the operations perform in the webctrl SOAP Web Services.
class Webserv():

    def buildSoapReq(self,type_param='', paramval='', newval=''):

        if type_param == 'get':
            SoapMessage = GET_REQ_TEMPLATE % (paramval)
            #print (SoapMessage)
        else:
            SoapMessage = SET_REQ_TEMPLATE % (paramval, newval)
            #print (SoapMessage)

        encoded_request = SoapMessage.encode('utf-8')
        headers = {'content-type': 'text/xml',
                   "SOAPAction": ""}
        response = requests.post(url=url,
                                 headers=headers,
                                 data=encoded_request)
        time.sleep(2)
        # print response.status_code
        # print response.content

        # Parsing the Soap Response
        if type_param == 'get':
            tree = ET.fromstring(response.content)
            spotter = tree.find('.//getValueReturn')
            return spotter.text

        else:
            return response.status_code


    def buildSoapReq_Set_NullValue(self,type_param='', paramval=''):

        if type_param == 'get':
            SoapMessage = GET_REQ_TEMPLATE % (paramval)
            #print (SoapMessage)
        else:
            SoapMessage = SET_REQ_TEMPLATE_NULL % (paramval)
            #print (SoapMessage)

        encoded_request = SoapMessage.encode('utf-8')
        headers = {'content-type': 'text/xml',
                   "SOAPAction": ""}
        response = requests.post(url=url,
                                 headers=headers,
                                 data=encoded_request)
        time.sleep(2)
        # print response.status_code
        # print response.content

        # Parsing the Soap Response
        if type_param == 'get':
            tree = ET.fromstring(response.content)
            spotter = tree.find('.//getValueReturn')
            return spotter.text

        else:
            return response.status_code
