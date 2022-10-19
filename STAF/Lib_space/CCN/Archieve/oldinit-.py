import clr
import os
import datetime
import time
import Lib_Space
print(os.path.dirname(os.path.abspath(__file__)))

clr.AddReference(os.path.dirname(os.path.abspath(__file__))+"\\GenerateTablesXML.dll")
clr.AddReference(os.path.dirname(os.path.abspath(__file__))+"\\ToolsCommMgr.dll")
from Lib_Space import *
from Lib_Space.CCN import *
from ToolsCommMgr import CCNAdapter
from ToolsCommMgr import ConnectionSettings

# from ToolsCommMgr import ConnectionSettings
import xml.etree.ElementTree as ET
from GenerateTablesXML import GenerateXML


class CCN_Adatper:

    # Create`s a CCN Adaptor with the user given settings and establishing a connection(Multiple CCN addaptor can be created by user)
    def __init__(self,sytype,BaudRate,NoOfTries,ResTimOut,DelayRestTimeOut,ID,ElemNo,AlarmAck,BusNo):
        settings = ConnectionSettings()
        settings.Type = sytype
        settings.BaudRate = BaudRate
        settings.NumberOfTries = NoOfTries
        settings.ResponseTimeout = ResTimOut
        settings.DelayedResponseTimeout = DelayRestTimeOut
        settings.ID = ID
        settings.ElementNumber = ElemNo                         # source Address or PC Address
        settings.AlarmAcknowledger = AlarmAck
        settings.BusNumber = BusNo                              # Bus Address or PC Bus
        self.CCN_instance = CCNAdapter()
        self.CCN_instance.Connect(settings)

        if os.path.isfile(os.path.dirname(os.path.abspath(__file__))+"\\DCT.xml") == True:
            dctxmltree = ET.parse(os.path.dirname(os.path.abspath(__file__))+"\\DCT.xml")
            self.dctxmlroot = dctxmltree.getroot()
            software_id = self.CCN_instance.GetSoftwareId().replace("software id: ",'')
            soft_id_xml =  self.dctxmlroot.attrib['SoftwareId']
            if soft_id_xml == software_id or software_id == 'failed to connect CCN. Err: -1':
                print ('DCT.xml file already exists')
            else:
                self.Generate_xml()
        else:
            self.Generate_xml()

    # Generate`s DCT.xml if it does not exists or the existing file does not match with the software ID
    def Generate_xml(self):
        tables = GenerateXML(self.CCN_instance)
        tables.CreateXMLDatabase('')
        print ('DCT.xml file generated')
        dctxmltree = ET.parse(os.path.dirname(os.path.abspath(__file__)) + "\\DCT.xml")
        self.dctxmlroot = dctxmltree.getroot()

    # Configure`s Destination address(User can configure multiple destination addresses for multiple CCN adaptors)
    def setDestination(self, sourceAddr, SourceBus, destAddr, destBus, forcelevel):
        self.CCN_instance.SetDestinationSettings(sourceAddr,SourceBus,destAddr,destBus,forcelevel)

    # Read`s CCN value from a Variable (with print)
    def CCN_ReadVarVal(self, varName):
        val =  self.CCN_instance.ReadVariableValue(varName)
        print("Read Variable '" + varName +"'[CCN] = "+ str(val) +"\t\t\t\t"+datetime.datetime.now().strftime("%I:%M:%S:%mS"))
        return val

    # Read`s CCN value from a Variable (with no print)
    def CCN_ReadVarValNo_print(self,varName):
        val = self.CCN_instance.ReadVariableValue(varName)
        return val

    # Read`s CCN value from a Table point (with print)
    def CCN_ReadTablePoint(self,PointName,BlockNum = 5):
        # type: (object, object) -> object
        point_path = ".//Variable[@Name=" + "'" + PointName + "']"
        pointcond = self.dctxmlroot.findall(point_path)
        table_path = ".//Variable[@Name=" + "'" + PointName + "']/.."
        table_con = self.dctxmlroot.findall(table_path)
        capvalue = self.CCN_instance.ReadBlockDataTest(table_con[0].attrib['Name'], BlockNum)
        # for i in range(0,len(capvalue)):
        #     print capvalue[i]

        print((type(capvalue)))
        for i in range(3):
            val = self.CCN_instance.ValueFromBlockTest(capvalue, int(pointcond[0].attrib['Offset']),
                                                   int(pointcond[0].attrib['Size']),
                                                   int(pointcond[0].attrib['Format']))
            if val != 'block data null or empty': break
            time.sleep(1)
        print("Read TablePoint '" + PointName + "'[CCN] = ", val + "\t\t\t\t" + datetime.datetime.now().strftime(
            "%I:%M:%S:%mS"))
        return val

    # Read`s CCN value from a Table point (with Table Name)
    def CCN_ReadTablePoint_with_TableName(self, PointName, TableName, BlockNum=5):
        point_path = ".//Variable[@Name=" + "'" + PointName + "']"
        pointcond = self.dctxmlroot.findall(point_path)
        table_path = ".//Variable[@Name=" + "'" + PointName + "']/.."
        table_con = self.dctxmlroot.findall(table_path)
        for i in range(len(table_con)):
            if table_con[i].attrib['Name'] == TableName:
                capvalue = self.CCN_instance.ReadBlockDataTest(table_con[i].attrib['Name'], BlockNum)
                val = self.CCN_instance.ValueFromBlockTest(capvalue, int(pointcond[i].attrib['Offset']),
                                                       int(pointcond[i].attrib['Size']),
                                                       int(pointcond[i].attrib['Format']))
                print("Read TablePoint '" + PointName + "'[CCN] = ", val + "\t\t\t\t" + datetime.datetime.now().strftime(
                    "%I:%M:%S:%mS"))
                return val

    # Read`s CCN value from a Table point (with no print)
    def CCN_ReadTablePoint_NoPrint(self, PointName, BlockNum=5):
        point_path = ".//Variable[@Name=" + "'" + PointName + "']"
        pointcond = self.dctxmlroot.findall(point_path)
        table_path = ".//Variable[@Name=" + "'" + PointName + "']/.."
        table_con = self.dctxmlroot.findall(table_path)
        capvalue = self.CCN_instance.ReadBlockDataTest(table_con[0].attrib['Name'], BlockNum)
        val = self.CCN_instance.ValueFromBlockTest(capvalue, int(pointcond[0].attrib['Offset']),
                                                   int(pointcond[0].attrib['Size']), int(pointcond[0].attrib['Format']))
        return val

    # Write`s CCN value to a Variable
    def CCN_WriteVarVal(self,varName,value):
        self.CCN_instance.WriteVariableValue(varName,value)
        print("Written Variable '" + varName + "'[CCN] = "+  str(value) + "\t\t\t\t" + datetime.datetime.now().strftime(
            "%I:%M:%S:%mS"))

    # Write`s CCN value to a Table point
    def CCN_WritePointinTable(self,PointName, writeVal, BlockNum = 5):
        point_path = ".//Variable[@Name=" + "'" + PointName + "']"
        pointcond = self.dctxmlroot.findall(point_path)
        table_path = ".//Variable[@Name=" + "'" + PointName + "']/.."
        table_con = self.dctxmlroot.findall(table_path)
        self.CCN_instance.WriteVariableInTableBlockTest(table_con[0].attrib['Name'], BlockNum,int(pointcond[0].attrib['Offset']),
                                                        int(pointcond[0].attrib['Size']), int(pointcond[0].attrib['Format']), str(writeVal))

        print("Written TablePoint '" + PointName + "'[CCN] = ", writeVal + "\t\t\t\t" + datetime.datetime.now().strftime(
            "%I:%M:%S:%mS"))

    # Riplica to the waituntil function of Smart Simulator
    def WaitUntil(self, variable, Expected, MaxDelay=300, condition='=', MinDelay=0, Tol=0):
        self.Tol = Tol
        self.variable = variable
        time.sleep(MinDelay)
        self.counttime = 0
        self.difftime = MaxDelay - MinDelay
        conditional_statement = ('val >= self.Expected_val-self.Tol and val <= self.Expected_val+self.Tol')

        try:
            self.Expected_val = float(Expected)
        except:
            self.Expected_val = Expected.lower()

        if type(Expected) == str:
            self.Expected_val = self.CCN_instance.ReadVariableValue(variable)
        else:
            self.Expected_val = float(Expected)

        if condition == '=':
            conditional_statement = ('val >= self.Expected_val-self.Tol and val <= self.Expected_val+self.Tol')
        elif condition == '>':
            conditional_statement = ('val > self.Expected_val')
        elif condition == '>=':
            conditional_statement = ('val >= self.Expected_val')
        elif condition == '<':
            conditional_statement = ('val < self.Expected_val')
        elif condition == '<=':
            conditional_statement = ('val <= self.Expected_val')

        return self.__ReadVarVal_elavuation(conditional_statement)

    # Read and compare according to the conditional evaluation
    def __ReadVarVal_elavuation(self, conditional_statement):
        while self.counttime < self.difftime:
            val = float(format(float(self.CCN_ReadVarValNo_print(self.variable)), '.2f'))
            if eval(conditional_statement):
                print("Read Variable '" + self.variable + "'[CCN] = " + str(
                    val) + "\t\t\t\t" + datetime.datetime.now().strftime("%I:%M:%S:%mS"))
                return True
            else:
                time.sleep(1)
                self.counttime = self.counttime + 1
        val = float(format(float(self.CCN_ReadVarValNo_print(self.variable)), '.2f'))
        print("Read Variable '" + self.variable + "'[CCN] = " + str(
            val) + "\t\t\t\t" + datetime.datetime.now().strftime("%I:%M:%S:%mS"))

        return False

    # Same as waituntil except for the variable is a Table point/String
    def WaitUntilPoint(self, variable, Expected, MaxDelay=300, condition='=', MinDelay=0, Tol=0):
        self.variable = variable

        try:
            self.Expected_val = float(Expected)
        except:
            self.Expected_val = Expected.upper()

        if type(self.Expected_val) == str:
            time.sleep(MinDelay)
            counttime = 0
            difftime = MaxDelay - MinDelay
            while counttime < difftime:
                val = self.CCN_ReadTablePoint_NoPrint(variable)
                val = val.upper()
                val = val.strip()
                if val == self.Expected_val:
                    print("Read Variable '" + variable + "'[CCN] = " + str(
                        val) + "\t\t\t\t" + datetime.datetime.now().strftime("%I:%M:%S:%mS"))

                    return True
                else:
                    time.sleep(1)
                    counttime = counttime + 1
            val = self.CCN_ReadTablePoint_NoPrint(variable)
            print("Read Variable '" + variable + "'[CCN] = " + str(
                val) + "\t\t\t\t" + datetime.datetime.now().strftime("%I:%M:%S:%mS"))
            return False
        else:
            #self.Expected_val = float(Expected)
            self.Tol = Tol
            time.sleep(MinDelay)
            self.counttime = 0
            self.difftime = MaxDelay - MinDelay
            if condition == '=':
                conditional_statement = ('val >= self.Expected_val-self.Tol and val <= self.Expected_val+self.Tol')
            elif condition == '>':
                conditional_statement = ('val > self.Expected_val')
            elif condition == '>=':
                conditional_statement = ('val >= self.Expected_val')
            elif condition == '<':
                conditional_statement = ('val < self.Expected_val')
            elif condition == '<=':
                conditional_statement = ('val <= self.Expected_val')

            return self.__ReadTablePoint_elavuation(conditional_statement, Tol)

    # Read and compare according to the conditional evaluation
    def __ReadTablePoint_elavuation(self, conditional_statement, Tol):

        while self.counttime < self.difftime:
            val = self.CCN_ReadTablePoint_NoPrint(self.variable)
            if val == 'block data null or empty':
                continue
            val = float(format(float(str(val)), '.2f'))
            if eval(conditional_statement):
                print("Read Variable '" + self.variable + "'[CCN] = " + str(
                    val) + "\t\t\t\t" + datetime.datetime.now().strftime("%I:%M:%S:%mS"))

                return True
            else:
                time.sleep(1)
                self.counttime = self.counttime + 1
        val = float(format(float(str(self.CCN_ReadTablePoint_NoPrint(self.variable))), '.2f'))
        print("Read Variable '" + self.variable + "'[CCN] = " + str(
            val) + "\t\t\t\t" + datetime.datetime.now().strftime("%I:%M:%S:%mS"))

        return False

    def CCN_TablePoint_Discription(self, varname):
        #self.dctxmlroot = tree.getroot()
        for child in self.dctxmlroot:
            root2 = child.getchildren()
            for child2 in root2:
                # element = child.findall('*//[@Name = "cpumpseq"]')
                if child2.attrib['Name'] == varname:
                    return child2.attrib['Description']
        return None
    
    def readVFD_Config(self):

        config_param = {}

        CNF1 = self.CCN_instance.ReadBlockDataTest("DRV_CNF1", 5)
        CNF2 = self.CCN_instance.ReadBlockDataTest("DRV_CNF2", 5)

        for i in range(30):     
            param_number = self.CCN_instance.ValueFromBlockTest(CNF1, 8*i,2,2)
            param_index = self.CCN_instance.ValueFromBlockTest(CNF1, 2+8*i,2,2)
            param_value1 = self.CCN_instance.ValueFromBlockTest(CNF1, 4+8*i,2,2)
            param_value2 = self.CCN_instance.ValueFromBlockTest(CNF1, 6+8*i,2,2)
            # param_key = "Param{}".format(i+1)
            param_key = param_number
            config_param.update({param_number:[param_index,param_value1,param_value2]})
            
        for i in range(30):
            param_number = self.CCN_instance.ValueFromBlockTest(CNF2, 8 * i, 2, 2)
            param_index = self.CCN_instance.ValueFromBlockTest(CNF2, 2 + 8 * i, 2, 2)
            param_value1 = self.CCN_instance.ValueFromBlockTest(CNF2, 4 + 8 * i, 2, 2)
            param_value2 = self.CCN_instance.ValueFromBlockTest(CNF2, 6 + 8 * i, 2, 2)
            # param_key = "Param{}".format(i+1)
            param_key = param_number
            config_param.update({param_number: [param_index, param_value1, param_value2]})

        return config_param

    # Disconnect`s the CCN connection
    def disconnect(self):
        self.CCN_instance.Disconnect()
