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

class BACnet_MSV_Object_Negative_Test(unittest.TestCase):

    def setUp(self):
        print ("\n********************************************************************************")
        print ("Setup Function - START")
        print ("********************************************************************************")
        self.bacnet = BACnet_Module.Adapter(dirnameutils + "\Lib_space\BACNET\Adpater_setting.ini")
        self.bacnet.set_destination(DataParameter.get("Config", "dut_address"))
        print ("********************************************************************************")
        print ("Setup Function - END")
        print ("********************************************************************************")

    def test_BACnet_MSV_Obj_Read_Negative_func(self):
        failStr = ''
        MV = [
            ['113', 'timeDelay', 'Real', 'O'],
            ['87', 'priorityArray', 'PriorityArray', 'R'],
            ['104', 'relinquishDefault', 'Real', 'O']
            ]
        objList1 = [('multiStateValue', 21),('multiStateValue', 109)]
        print('***************************************')
        for objType, instNum in objList1:
            print(objType)
            print(instNum)

            list = MV
            for strpropID, strpropName, DataType, RW in list:
                try:
                    PropValue = self.bacnet.readproperty(objType, instNum, strpropID)
                    print(PropValue)
                    self.assertEqual(PropValue, None,msg='Property Value is: ' + strpropName + ' is not working')
                    print('Read Property of Object Name: ' + objType + '  PropertyValue: ' + strpropID + '  is: ' + str(PropValue))
                except Exception as e:
                    failStr = failStr + str(e.args[0]) + '.\n'
        if failStr != "":
            raise Exception(failStr)

    def tearDown(self):
        self.bacnet.disconnect()

    if __name__ == '__main__':
        unittest.main()