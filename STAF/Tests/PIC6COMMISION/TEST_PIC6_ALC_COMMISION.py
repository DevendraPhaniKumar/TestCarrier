'''
Created on Dec 8, 2020

@author: kattupd
'''
import unittest
import sys, os, time
import HtmlTestRunner

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))                      
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Lib_space.BACNET import BACnet_Module
from Data.BACNET.TestData import *


dirpath = os.getcwd()
foldername = os.path.basename(dirpath)

       
class PIC6_Commision_ALC_BACnet_test(unittest.TestCase):

    def setUp(self):
        self.bacnet = BACnet_Module.Adapter(dirnameutils + "\Lib_space\BACNET\Adpater_setting.ini")
        self.bacnet.set_destination(dut_address)        

        
    def test_read_write_AV_BACnet_Points_Functionality(self):
        failStr = ''
             
        print('--------------------START-------------------------------')        
        try:			
            print('<----Write Cooling stpt 2_Writ Value--->')                        
            pres_Value = self.bacnet.writeproperty('analogValue',  analog_value_obj_instance[0], 'presentValue', analogValue_test_parameters.Cooling_stpt_wr_presentValue)
            print (pres_Value)   
            self.assertEqual(pres_Value, 'ack', msg='Not Able to Write pres_Value')
            print ('<----Read Cooling stpt 2_Rd Value--->')
            time.sleep(60)
            pres_Value = self.bacnet.readproperty('analogValue',  analog_value_obj_instance[2], 'presentValue')
            print(pres_Value)
            self.assertEqual(pres_Value, analogValue_test_parameters.Cooling_stpt_wr_presentValue, msg='Not showing pres_Value correctly')

            print('<----Write GENUNIT_SP_SEL_WR Value--->')                        
            pres_Value = self.bacnet.writeproperty('analogValue',  analog_value_obj_instance[7], 'presentValue', analogValue_test_parameters.Analog_wr_presentValue)
            print (pres_Value)   
            self.assertEqual(pres_Value, 'ack', msg='Not Able to Write pres_Value')
            print ('<----Read GENUNIT_SP_SEL_WR Value--->')
            time.sleep(60)
            pres_Value = self.bacnet.readproperty('analogValue',  analog_value_obj_instance[8], 'presentValue')
            print(pres_Value)
            self.assertEqual(pres_Value, analogValue_test_parameters.Analog_wr_presentValue, msg='Not showing pres_Value correctly')
            
            print ('<----Read GENUNIT_SP_SEL_rd Value--->')            
            pres_Value = self.bacnet.readproperty('analogValue',  analog_value_obj_instance[9], 'presentValue')
            print(pres_Value)
            self.assertEqual(pres_Value, analogValue_test_parameters.Analog_rd_presentValue, msg='Not showing pres_Value correctly')
            
        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'            
        
        if failStr != "":
            raise Exception(failStr)
    
    def test_read_write_BV_BACnet_Points_Functionality(self):
        failStr = ''
             
        print('--------------------START-------------------------------')        
        try:			
            print('<----Write Chiller Command_Write Value to Active--->')                        
            pres_Value = self.bacnet.writeproperty('binaryValue',  binary_value_obj_instance[3], 'presentValue', binaryValue_test_parameters.Chiller_command_wr_on_presentValue)
            print (pres_Value)   
            self.assertEqual(pres_Value, 'ack', msg='Not Able to Write pres_Value')
            print ('<----Read Chiller Command_Rd Value--->')
            time.sleep(60)
            pres_Value = self.bacnet.readproperty('binaryValue',  binary_value_obj_instance[1], 'presentValue')
            print(pres_Value)
            self.assertEqual(pres_Value, binaryValue_test_parameters.Chiller_command_wr_on_presentValue, msg='Not showing pres_Value correctly')

            print('<----Write Chiller Command_Write Value to InActive--->')                        
            pres_Value = self.bacnet.writeproperty('binaryValue',  binary_value_obj_instance[3], 'presentValue', binaryValue_test_parameters.Chiller_command_wr_off_presentValue)
            print (pres_Value)   
            self.assertEqual(pres_Value, 'ack', msg='Not Able to Write pres_Value')
            print ('<----Read Chiller Command_Rd Value--->')
            time.sleep(60)
            pres_Value = self.bacnet.readproperty('binaryValue',  binary_value_obj_instance[1], 'presentValue')
            print(pres_Value)
            self.assertEqual(pres_Value, binaryValue_test_parameters.Chiller_command_wr_off_presentValue, msg='Not showing pres_Value correctly')            

            print('<----Write GENUNIT_SP_OCC_wr Value to Active--->')                        
            pres_Value = self.bacnet.writeproperty('binaryValue',  binary_value_obj_instance[4], 'presentValue', binaryValue_test_parameters.Chiller_command_wr_on_presentValue)
            print (pres_Value)   
            self.assertEqual(pres_Value, 'ack', msg='Not Able to Write pres_Value')
            print ('<----Read GENUNIT_SP_OCC_wr_Rd Value--->')
            time.sleep(60)
            pres_Value = self.bacnet.readproperty('binaryValue',  binary_value_obj_instance[6], 'presentValue')
            print(pres_Value)
            self.assertEqual(pres_Value, binaryValue_test_parameters.Chiller_command_wr_on_presentValue, msg='Not showing pres_Value correctly')

            print ('<----Read GENUNIT_SP_OCC_rd Value--->')
            pres_Value = self.bacnet.readproperty('binaryValue',  binary_value_obj_instance[5], 'presentValue')
            print(pres_Value)
            self.assertEqual(pres_Value, binaryValue_test_parameters.Chiller_command_wr_on_presentValue, msg='Not showing pres_Value correctly')
            
        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'            
        
        if failStr != "":
            raise Exception(failStr)
    
       
    def tearDown(self):
            self.bacnet.disconnect()
  
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=dirnameutils + "\Results\\"+foldername))
