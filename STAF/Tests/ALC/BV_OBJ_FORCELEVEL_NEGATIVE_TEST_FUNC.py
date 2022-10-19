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

#print(dirnameutils)

from Lib_space.BACNET import BACnet_Module

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)

DataParameter = configparser.ConfigParser()
DataParameter.read(dirnameutils + '\\Data\\BACNET\\TestData.ini')
bacnet_binary_value_obj_instance = ast.literal_eval(DataParameter.get("Inputs", "bv_forcelevel_instance"))
bacnet_binary_value_obj_propname = ast.literal_eval(DataParameter.get("Inputs", "binary_value_obj_propname"))



class BACnet_BV_Object_ForceLevel_NegativeTest(unittest.TestCase):

    def setUp(self):
        print ("\n********************************************************************************")
        print ("Setup Function - START")
        print ("********************************************************************************")
        self.bacnet = BACnet_Module.Adapter(dirnameutils + "\Lib_space\BACNET\Adpater_setting.ini")
        self.bacnet.set_destination(DataParameter.get("Config", "dut_address"))
        print ("********************************************************************************")
        print ("Setup Function - END")
        print ("********************************************************************************")
    
    
    def test_BACnet_BV_Obj_ForceLevelTest_func(self):
        
        failStr = ''        
        try:
            print('--------------------START-------------------------------')            
            print('<----Read binary Value of Instance :'+bacnet_binary_value_obj_instance+'--->')                                                        
            read_ouput = self.bacnet.readproperty('binaryValue',  bacnet_binary_value_obj_instance, bacnet_binary_value_obj_propname)
            print (read_ouput)            
            self.assertEqual(read_ouput, 'inactive', msg='Read binary Value is not showing correctly')
            
            print('<----Write Force level negative test :BV ,Instance 123->write present value with Force 2=value 1--->')
            pres_Value = self.bacnet.writeproperty('binaryValue',  bacnet_binary_value_obj_instance, 'presentValue', 'active', priority=2)
            print (pres_Value)               
            
            print('<----Verify present value with Force 2=value 1 for BV ,Instance 123---->')
            read_ouput = self.bacnet.readproperty('binaryValue',  bacnet_binary_value_obj_instance, bacnet_binary_value_obj_propname)
            print (read_ouput)            
            self.assertEqual(read_ouput, 'active', msg='Read binary Value is not showing correctly')
                        
            print('<----Write Force level negative test :BV ,Instance 123->write present value with Force 4=value 0--->')
            pres_Value = self.bacnet.writeproperty('binaryValue',  bacnet_binary_value_obj_instance, 'presentValue', 'inactive', priority=4)
            print (pres_Value)               
            
            print('<----Verify present value with Force 4=value 0 for BV ,Instance 123---->')
            read_ouput = self.bacnet.readproperty('binaryValue',  bacnet_binary_value_obj_instance, bacnet_binary_value_obj_propname)
            print (read_ouput)            
            self.assertEqual(read_ouput, 'active', msg='Read binary Value is not showing correctly')            
            self.assertNotEqual(read_ouput, 'inactive', msg='Read binary Value is showing correctly')            
                        
            print('<----Verify present value as Null with Force 2 and do relinquish for BV ,Instance 123---->')
            prop_val = self.bacnet.writeproperty('binaryValue', bacnet_binary_value_obj_instance, 'presentValue', 'null', priority=2)
            print (prop_val)
            self.assertEqual(prop_val, 'ack', msg='Not able to write binary Value')
            
            print('<----Verify present value with Force 4=value 0 for BV ,Instance 123---->')
            read_ouput = self.bacnet.readproperty('binaryValue',  bacnet_binary_value_obj_instance, bacnet_binary_value_obj_propname)
            print (read_ouput)            
            self.assertEqual(read_ouput, 'inactive', msg='Read binary Value is not showing correctly')
            
            print('<----Write Force level negative test :BV ,Instance 123->write present value with Force 14=value 1--->')
            pres_Value = self.bacnet.writeproperty('binaryValue',  bacnet_binary_value_obj_instance, 'presentValue', 'active', priority=14)
            print (pres_Value)

            print('<----Verify present value with Force 14=value 1 for BV ,Instance 123---->')
            read_ouput = self.bacnet.readproperty('binaryValue',  bacnet_binary_value_obj_instance, bacnet_binary_value_obj_propname)
            print (read_ouput)            
            self.assertEqual(read_ouput, 'inactive', msg='Read binary Value is not showing correctly')            
            self.assertNotEqual(read_ouput, 'active', msg='Read binary Value is showing correctly')            
            print('--------------------STOP--------------------------------\n')
            
            print('<----Verify present value as Null with Force 4 and do relinquish for BV ,Instance 123---->')
            prop_val = self.bacnet.writeproperty('binaryValue', bacnet_binary_value_obj_instance, 'presentValue', 'null', priority=4)
            print (prop_val)
            self.assertEqual(prop_val, 'ack', msg='Not able to write binary Value')
            
            print('<----Verify present value as Null with Force 14 and do relinquish for BV ,Instance 553---->')
            prop_val = self.bacnet.writeproperty('binaryValue', bacnet_binary_value_obj_instance, 'presentValue', 'null', priority=14)
            print (prop_val)
            self.assertEqual(prop_val, 'ack', msg='Not able to write binary Value')
                                    
            print('<----Read binary Value of Instance :'+bacnet_binary_value_obj_instance+'--->')                                                        
            read_ouput = self.bacnet.readproperty('binaryValue',  bacnet_binary_value_obj_instance, bacnet_binary_value_obj_propname)
            print (read_ouput)            
            self.assertEqual(read_ouput, 'inactive', msg='Read binary Value is not showing correctly')                                    
                           
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
