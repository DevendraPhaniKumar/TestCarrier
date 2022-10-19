'''
Created on June 1, 2021

@author: kattupd
'''

import unittest
import sys, os
#import HtmlTestRunner
import configparser,ast


sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Lib_space.BACNET import BACnet_Module

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)

DataParameter = configparser.ConfigParser()
DataParameter.read(dirnameutils + '\\Data\\BACNET\\TestData.ini')

class BACnet_AnalogValue_Object_Negative_Test(unittest.TestCase):

    def setUp(self):
        print ("\n********************************************************************************")
        print ("Setup Function - START")
        print ("********************************************************************************")
        self.bacnet = BACnet_Module.Adapter(dirnameutils + "\Lib_space\BACNET\Adpater_setting.ini")
        self.bacnet.set_destination(DataParameter.get("Config", "dut_address"))
        print ("********************************************************************************")
        print ("Setup Function - END")
        print ("********************************************************************************")

    def test_BACnet_AnalogValue_Obj_Write_Negative_func(self):
        
        failStr = ''
        inst_list=[545,546]
        prop_list={'description':'test','objectName':'test','outOfService':'True','units':'degreesCelsius','eventState':'normal','statusFlags':'[0, 0, 0, 0]','objectIdentifier':"""('analogValue', 545)""",'objectType':'analogValue'}
        try:
            print('--------------------START-------------------------------')
            print('<----Write AnalogValue Propertys --->')
            for i in range(0,len(inst_list)):
                for k, v in prop_list.items():
                    Op_Value = self.bacnet.writeproperty('analogValue', int(inst_list[i]), str(k), v)
                    print (Op_Value)
                    self.assertEqual(Op_Value, None, msg='Able to Write Value')
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
    pass
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=dirnameutils + "\Results\\"+foldername))
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=dirnameutils + "\Results\\" + foldername))pass