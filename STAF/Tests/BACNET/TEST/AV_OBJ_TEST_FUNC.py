'''
Created on Aug 14, 2020

@author: kattupd
'''

import unittest
import sys, os
import HtmlTestRunner
import configparser,ast


sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))                      
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Lib_space.BACNET import BACnet_Module

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)

DataParameter = configparser.ConfigParser()
DataParameter.read(dirnameutils + '\\Data\\BACNET\\TestData.ini')
bacnet_analog_value_obj_instance = ast.literal_eval(DataParameter.get("Inputs", "analog_value_obj_instance"))
bacnet_analog_value_obj_propname = ast.literal_eval(DataParameter.get("Inputs", "analog_value_obj_propname"))
bacnet_analog_value_obj_output = ast.literal_eval(DataParameter.get("Outputs", "analog_value_obj_read_outputs"))



#DataParameter["Config"] ["dut_address"]
#DataParameter["Inputs"]["analog_value_obj_instance"]

#DataParameter.get("Config", "dut_address")


class BACnet_AnalogValue_Object_Test(unittest.TestCase):

    def setUp(self):
        print ("\n********************************************************************************")
        print ("Setup Function - START")
        print ("********************************************************************************")
        self.bacnet = BACnet_Module.Adapter(dirnameutils + "\Lib_space\BACNET\Adpater_setting.ini")
        self.bacnet.set_destination(DataParameter.get("Config", "dut_address"))
        print ("********************************************************************************")
        print ("Setup Function - END")
        print ("********************************************************************************")
    
    
    def test_BACnet_AnalogValue_Obj_Read_func(self):
        
        failStr = ''
        
        try:
            print('--------------------START-------------------------------')
            print('<----Read Analog Value of Instance :'+bacnet_analog_value_obj_instance[1]+'--->')                                                        
            read_ouput = self.bacnet.readproperty('analogValue',  bacnet_analog_value_obj_instance[1], bacnet_analog_value_obj_propname[0])
            print (read_ouput)
            self.assertEqual(read_ouput, DataParameter['Outputs']['analog_value_obj_read_output'], msg='Read Analog Value is not showing correctly')
            self.assertEqual(read_ouput, bacnet_analog_value_obj_output[0], msg='Read Analog Value is not showing correctly')
            print('--------------------STOP--------------------------------\n')
                                
        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'

        if failStr != "":
            raise Exception(failStr)
    
    def test_BACnet_AnalogValue_Obj_Write_func(self):
        
        failStr = ''
        
        try:
            print('--------------------START-------------------------------')
            print('<----Write Analog Value of Instance :'+bacnet_analog_value_obj_instance[1]+'--->')                                                        
            write_ouput = self.bacnet.writeproperty('analogValue',  bacnet_analog_value_obj_instance[1], bacnet_analog_value_obj_propname[1],DataParameter['Inputs']['analog_value_obj_prop_value'])
            print (write_ouput)
            self.assertEqual(write_ouput, DataParameter['Outputs']['analog_value_obj_output_ack'], msg='Not able to write Analog Value')
           
            print('<----Read Analog Value of Instance :'+bacnet_analog_value_obj_instance[1]+'--->')                                                        
            read_ouput = self.bacnet.readproperty('analogValue',  bacnet_analog_value_obj_instance[1], bacnet_analog_value_obj_propname[1])
            print (read_ouput)
            self.assertEqual(read_ouput, DataParameter['Inputs']['analog_value_obj_prop_value'], msg='Read Analog Value is not showing correctly')
            print('--------------------STOP--------------------------------\n')
                                
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