'''
Created on Aug 18, 2021

@author: kattupd
'''

import unittest
import sys, os
import HtmlTestRunner
import configparser,ast

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))                      
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Lib_space.BACNET import BACnet_Module

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)

DataParameter = configparser.ConfigParser()
DataParameter.read(dirnameutils + '\\Data\\BACNET\\TestData.ini')
bacnet_analog_value_obj_instance = ast.literal_eval(DataParameter.get("Inputs", "av_forcelevel_instance"))
bacnet_analog_value_obj_propname = ast.literal_eval(DataParameter.get("Inputs", "analog_value_obj_propname"))

class BACnet_AV_Object_OUTOFRANGE_NegativeTest(unittest.TestCase):

    def setUp(self):
        print ("\n********************************************************************************")
        print ("Setup Function - START")
        print ("********************************************************************************")
        self.bacnet = BACnet_Module.Adapter(dirnameutils + "\Lib_space\BACNET\Adpater_setting.ini")
        self.bacnet.set_destination(DataParameter.get("Config", "dut_address"))
        print ("********************************************************************************")
        print ("Setup Function - END")
        print ("********************************************************************************")
    
    
    def test_BACnet_AV_Obj_OutofRangeTest_func(self):
        
        failStr = ''        
        try:
            print('--------------------START-------------------------------')
                
            print('<----Read Analog Value of Instance :'+bacnet_analog_value_obj_instance+'--->')
            pres_Value = self.bacnet.writeproperty('analogValue',  bacnet_analog_value_obj_instance, bacnet_analog_value_obj_propname[0], '-1')                                                                    
            print (pres_Value)            
            self.assertEqual(pres_Value, None, msg='Read Analog Value is not showing correctly')
            
        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'

        if failStr != "":
            raise Exception(failStr)
   
        
    def tearDown(self):
            print ("********************************************************************************")
            print ("Teardown Function - START")
            print ("********************************************************************************")
            self.bacnet.disconnect()
            print ("********************************************************************************")
            print ("Teardown Function - END")
            print ("********************************************************************************")
  
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=dirnameutils + "\Results\\"+foldername))
