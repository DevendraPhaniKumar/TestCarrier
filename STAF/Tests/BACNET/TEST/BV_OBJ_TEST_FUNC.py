'''
Created on Aug 14, 2020

@author: kattupd
'''
import unittest
import sys, os
import HtmlTestRunner


sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))                      
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Lib_space.BACNET import BACnet_Module
from Data.BACNET.TestData import *

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)


class BACnet_BinaryValue_Object_Test(unittest.TestCase):

    def setUp(self):
        print ("\n********************************************************************************")
        print ("Setup Function - START")
        print ("********************************************************************************")
        self.bacnet = BACnet_Module.Adapter(dirnameutils + "\Lib_space\BACNET\Adpater_setting.ini")
        self.bacnet.set_destination(dut_address)
        print ("********************************************************************************")
        print ("Setup Function - END")
        print ("********************************************************************************")
    
    
    def test_BACnet_BinaryValue_Obj_Read_func(self):
        
        failStr = ''
        
        try:
            print('--------------------START-------------------------------')
            print('<----Read Binary Value of Instance :'+binary_value_obj_instance[1]+'--->')                                                        
            read_ouput = self.bacnet.readproperty('binaryValue',  binary_value_obj_instance[1], binary_value_obj_propname[0])
            print (read_ouput)
            self.assertEqual(read_ouput, binary_value_obj_read_output, msg='Read binary Value is not showing correctly')
            self.assertEqual(read_ouput, binary_value_obj_read_outputs[0], msg='Read binary Value is not showing correctly')
            print('--------------------STOP--------------------------------\n')
                                
        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'

        if failStr != "":
            raise Exception(failStr)
    
    
    def test_BACnet_BinaryValue_Obj_Write_func(self):
        
        failStr = ''
        
        try:
            print('--------------------START-------------------------------')
            print('<----Write binary Value of Instance :'+binary_value_obj_instance[1]+'--->')                                                        
            write_ouput = self.bacnet.writeproperty('binaryValue',  binary_value_obj_instance[1], binary_value_obj_propname[1],binary_value_obj_prop_value)
            print (write_ouput)
            self.assertEqual(write_ouput, binary_value_obj_output_ack, msg='Not able to write binary Value')
           
            print('<----Read binary Value of Instance :'+binary_value_obj_instance[1]+'--->')                                                        
            read_ouput = self.bacnet.readproperty('binaryValue',  binary_value_obj_instance[1], binary_value_obj_propname[1])
            print (read_ouput)
            self.assertEqual(read_ouput, binary_value_obj_prop_value, msg='Read binary Value is not showing correctly')
            self.assertEqual(read_ouput, binaryValue_test_parameters.binary_value_obj_prop_value, msg='Read binary Value is not showing correctly')
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