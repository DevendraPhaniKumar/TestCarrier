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

class BACnet_AV_Object_ForceLevel_NegativeTest(unittest.TestCase):

    def setUp(self):
        print ("\n********************************************************************************")
        print ("Setup Function - START")
        print ("********************************************************************************")
        self.bacnet = BACnet_Module.Adapter(dirnameutils + "\Lib_space\BACNET\Adpater_setting.ini")
        self.bacnet.set_destination(DataParameter.get("Config", "dut_address"))
        print ("********************************************************************************")
        print ("Setup Function - END")
        print ("********************************************************************************")
    
    
    def test_BACnet_AV_Obj_ForceLevelTest_func(self):
        
        failStr = ''        
        try:
            print('--------------------START-------------------------------')
            
            print('<----Read Analog Value of Instance :'+bacnet_analog_value_obj_instance+'--->')                                                        
            read_ouput = self.bacnet.readproperty('analogValue',  bacnet_analog_value_obj_instance, bacnet_analog_value_obj_propname[0])
            print (read_ouput)            
            self.assertEqual(read_ouput, '100.0', msg='Read Analog Value is not showing correctly')
            
            print('<----Write Force level negative test :AV ,Instance 553->write present value with Force 2=value 7--->')
            pres_Value = self.bacnet.writeproperty('analogValue',  bacnet_analog_value_obj_instance, 'presentValue', '7', priority=2)
            print (pres_Value)               
            
            print('<----Verify present value with Force 2=value 7 for AV ,Instance 553---->')
            read_ouput = self.bacnet.readproperty('analogValue',  bacnet_analog_value_obj_instance, bacnet_analog_value_obj_propname[0])
            print (read_ouput)            
            self.assertEqual(read_ouput, '7.0', msg='Read Analog Value is not showing correctly')
            
            print('<----Write Force level negative test :AV ,Instance 553->write present value with Force 4=value 14--->')
            pres_Value = self.bacnet.writeproperty('analogValue',  bacnet_analog_value_obj_instance, 'presentValue', '14', priority=4)
            print (pres_Value)               
            
            print('<----Verify present value with Force 4=value 14 for AV ,Instance 553---->')
            read_ouput = self.bacnet.readproperty('analogValue',  bacnet_analog_value_obj_instance, bacnet_analog_value_obj_propname[0])
            print (read_ouput)            
            self.assertEqual(read_ouput, '7.0', msg='Read Analog Value is not showing correctly')            
            self.assertNotEqual(read_ouput, '14.0', msg='Read Analog Value is showing correctly')            
                        
            print('<----Verify present value as Null with Force 2 and do relinquish for AV ,Instance 553---->')
            prop_val = self.bacnet.writeproperty('analogValue', bacnet_analog_value_obj_instance, 'presentValue', 'null', priority=2)
            print (prop_val)
            self.assertEqual(prop_val, 'ack', msg='Not able to write Analog Value')
            
            print('<----Verify present value with Force 4=value 14 for AV ,Instance 553---->')
            read_ouput = self.bacnet.readproperty('analogValue',  bacnet_analog_value_obj_instance, bacnet_analog_value_obj_propname[0])
            print (read_ouput)            
            self.assertEqual(read_ouput, '14.0', msg='Read Analog Value is not showing correctly')
            
            print('<----Write Force level negative test :AV ,Instance 553->write present value with Force 14=value 22--->')
            pres_Value = self.bacnet.writeproperty('analogValue',  bacnet_analog_value_obj_instance, 'presentValue', '22', priority=14)
            print (pres_Value)

            print('<----Verify present value with Force 14=value 22 for AV ,Instance 553---->')
            read_ouput = self.bacnet.readproperty('analogValue',  bacnet_analog_value_obj_instance, bacnet_analog_value_obj_propname[0])
            print (read_ouput)            
            self.assertEqual(read_ouput, '14.0', msg='Read Analog Value is not showing correctly')            
            self.assertNotEqual(read_ouput, '22.0', msg='Read Analog Value is showing correctly')            
            print('--------------------STOP--------------------------------\n')
            
            print('<----Verify present value as Null with Force 4 and do relinquish for AV ,Instance 553---->')
            prop_val = self.bacnet.writeproperty('analogValue', bacnet_analog_value_obj_instance, 'presentValue', 'null', priority=4)
            print (prop_val)
            self.assertEqual(prop_val, 'ack', msg='Not able to write Analog Value')
            
            print('<----Verify present value as Null with Force 14 and do relinquish for AV ,Instance 553---->')
            prop_val = self.bacnet.writeproperty('analogValue', bacnet_analog_value_obj_instance, 'presentValue', 'null', priority=14)
            print (prop_val)
            self.assertEqual(prop_val, 'ack', msg='Not able to write Analog Value')
                                    
            print('<----Read Analog Value of Instance :'+bacnet_analog_value_obj_instance+'--->')                                                        
            read_ouput = self.bacnet.readproperty('analogValue',  bacnet_analog_value_obj_instance, bacnet_analog_value_obj_propname[0])
            print (read_ouput)            
            self.assertEqual(read_ouput, '100.0', msg='Read Analog Value is not showing correctly')                                    
                                
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
