'''
Created on Aug 14, 2020

@author: kattupd
'''
import unittest
import sys, os
import HtmlTestRunner
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))                      
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Lib_space.BACNET import BACnet_Module
from Data.BACNET.TestData import *

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)


bacnet_df = pd.read_csv(dirnameutils +"\\Data\\BACNET\\TestData.csv")
A=bacnet_df[['obj_name','obj_type', 'obj_inst','access','prop_id','config value']]

class BACnet_Object_Tests(unittest.TestCase):

    def setUp(self):
        print ("\n********************************************************************************")
        print ("Setup Function - START")
        print ("********************************************************************************")
        self.bacnet = BACnet_Module.Adapter(dirnameutils + "\Lib_space\BACNET\Adpater_setting.ini")
        self.bacnet.set_destination(dut_address)
        print ("********************************************************************************")
        print ("Setup Function - END")
        print ("********************************************************************************")
    
    
    def test_BACnet_Obj_Read_Write_func(self):
        
        failStr = ''
        
        try:
            for index, row in A.iterrows():
                
                if row["access"] == 1:
                    if row["obj_type"] == 2:
                        print (row["obj_inst"])
                        print (row["prop_id"])                
                        obj_name= self.bacnet.readproperty('analogValue', str(row["obj_inst"]), str(row["prop_id"]))      
                        print ("Object:analogValue--> Object Name for Instance: " +str(row["obj_inst"])+ " is "  + obj_name +'\n')
                  
                    elif row["obj_type"] == 5:
                        print (row["obj_inst"])
                        print (row["prop_id"])                
                        obj_name= self.bacnet.readproperty('binaryValue', str(row["obj_inst"]), str(row["prop_id"]))      
                        print ("Object:binaryValue--> Object Name for Instance: " +str(row["obj_inst"])+ " is "  + obj_name +'\n')
                  
                if row["access"] == 3:
                  
                    if row["obj_type"] == 2:
                        print (row["obj_inst"])
                        print (row["prop_id"])
                        print(row["config value"])
                        self.bacnet.writeproperty('analogValue', row["obj_inst"], row["prop_id"], row["config value"])
                        #self.bacnet.writeproperty('analogValue', 5001, '28', 'c:ALC')          
                              
                    if row["obj_type"] == 5:
                        print (row["obj_inst"])
                        print (row["prop_id"])
                        print(row["config value"])    
                        self.bacnet.writeproperty('binaryValue', row["obj_inst"], row["prop_id"], row["config value"])
                              
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