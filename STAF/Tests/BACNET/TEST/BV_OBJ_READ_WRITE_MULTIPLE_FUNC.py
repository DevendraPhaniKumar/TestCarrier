'''
Created on Aug 14, 2020

@author: kattupd
'''
import unittest
import sys, os
import HtmlTestRunner
from logging import raiseExceptions


sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))                      
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Lib_space.BACNET import BACnet_Module
from Data.BACNET.TestData import *

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)



class BACnet_BinaryValue_Object_Multiple_Test(unittest.TestCase):

    def setUp(self):
        print ("\n********************************************************************************")
        print ("Setup Function - START")
        print ("********************************************************************************")
        self.bacnet = BACnet_Module.Adapter(dirnameutils + "\Lib_space\BACNET\Adpater_setting.ini")
        self.bacnet.set_destination(dut_address)
        print ("********************************************************************************")
        print ("Setup Function - END")
        print ("********************************************************************************")
    
    
    def test_BACnet_BinaryValue_Obj_ReadMultiple_func(self):
        
        failStr = ''
        
        op_list = []
        try:
            print('--------------------START-------------------------------')
            print('<----Read binary Value of Instance :'+str(binary_value_obj_multiple_list)+'--->')
            for item in binary_value_obj_multiple_list:
                for k,v in item.items():            
                    read_ouput =  self.bacnet.readmultiple([(int(k), v[0], v[1])])
                    print (read_ouput)
                    op_list.append(read_ouput[0])
            print(op_list)
            print (binary_value_obj_multiple_output_list)
            
            if set(binary_value_obj_multiple_output_list) == set(op_list) :                
                print ('Read Value is showing correctly')
            else:
                raiseExceptions ('Read Value is not showing correctly')            
            print('--------------------STOP--------------------------------\n')
                                
        except Exception as e:
            failStr = failStr + str(e.args[0]) + '.\n'

        if failStr != "":
            raise Exception(failStr)
    
    
    def test_BACnet_binaryValue_Obj_WriteMultiple_func(self):
        
        failStr = ''
        
        try:
            print('--------------------START-------------------------------')
            print('<----Write binary Value of Instance :'+str(binary_value_obj_multiple_write_list)+'--->')
            for item in binary_value_obj_multiple_write_list:
                for k,v in item.items():      
                        write_ouput =  self.bacnet.writemultiple([(int(k), v[0], v[1],'c:'+v[2])])                        
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