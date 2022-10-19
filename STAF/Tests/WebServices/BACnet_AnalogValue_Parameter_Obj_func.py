'''
Created on Apr 12, 2020

@author: kattupd
'''
import unittest
import sys, os, time
import HtmlTestRunner

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))                      
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


from Data.BACNET.bacnet_config_data import *
from Lib_space.SOAPUI import webservutil


dirpath = os.getcwd()
foldername = os.path.basename(dirpath)

       
class MicroBlocks_BACnet_AnalogValue_Parameter_Object(unittest.TestCase):
    """The purpose of this test suite is to verify that the all properties functionality in the analog-value parameter object."""

    def setUp(self):
        print ("\n********************************************************************************")
        print ("Setup Function - START")
        self.bac_handl = webservutil.Webserv() 
        print ("Setup Function - END")
        print ("********************************************************************************")

    def test_00_BACnet_AnalogValue_Obj_BAVP_Pretest_Configuration(self):            
        print ('Configure pre-test configuration for analog-value parameter object')     
        failStr = ''
        print('--------------------START-------------------------------')        
        try:                   
            print('<----Write Event Alarm acked Value of BAVS:6--->')
            event_alrm_ack = self.bac_handl.buildSoapReq(type_param='set',paramval=ref_name+'/bavs_1/~event_alarm_acked.value',newval='false')                                    
            print (event_alrm_ack)

            print('<----Write Event Alarm acked Value of BAVS:6--->')            
            event_alrm_ack = self.bac_handl.buildSoapReq(type_param='get',paramval=ref_name+'/bavs_1/~event_alarm_acked.value')                                    
            print (event_alrm_ack)
            self.assertEqual(event_alrm_ack, 'false', msg='Event Alarm Ack Value is Not showing correctly')

            print('<----Write Event Alarm Return Value of BAVS:6--->')
            event_alrm_ack = self.bac_handl.buildSoapReq(type_param='set',paramval=ref_name+'/bavs_1/~event_return_acked.value',newval='false')                                    
            print (event_alrm_ack)

            print('<----Write Event Alarm Return Value of BAVS:6--->')            
            event_alrm_ack = self.bac_handl.buildSoapReq(type_param='get',paramval=ref_name+'/bavs_1/~event_return_acked.value')                                    
            print (event_alrm_ack)
            self.assertEqual(event_alrm_ack, 'false', msg='Event Alarm Ack Value is Not showing correctly')                               
        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'       

        if failStr != "":
            raise Exception(failStr)
           
    
    def tearDown(self):
            print ("********************************************************************************")
            print ("Teardown Function - START")
            print ("********************************************************************************")
            del self.bac_handl
            print ("********************************************************************************")
            print ("Teardown Function - END")
            print ("********************************************************************************")
  
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=dirnameutils + "\Results\\"+foldername))
