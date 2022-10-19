#@author: Pramodh kalidindi
import clr
import os
import time
clr.AddReference(os.path.dirname(os.path.abspath(__file__))+r'\VirtualSimDemo\bin\Debug\VirtualSim.dll')
from System import DateTime
from VirtualSim import DataManager

class Virtual_Simulator:
    
    def __init__(self,int_PCAddrees,int_pcbus,int_pd5elementno,int_pd5bus,pathVsimxml):
        self.PCAddress = int_PCAddrees
        self.pcbus = int_pcbus
        self.pd5elementNo = int_pd5elementno
        self.pd5bus = int_pd5bus
        self.pathVsimxml = pathVsimxml
        self.vir_sim_instance = DataManager()
        ret = self.vir_sim_instance.Connect()
        print("Connection Status : ", ret)
        self.vir_sim_instance.SetSourceAndDestinationAddress(int_PCAddrees, int_pcbus, int_pd5elementno, int_pd5bus)
        ret = self.vir_sim_instance.LoadXML(pathVsimxml)
        print("XML Loading Status : " + str(ret))
        key = bytearray([0x0B, 0x04, 0x05, 0x07, 0x08])
        #self.vir_sim_instance.StartWritingTables(key)
        self.vir_sim_instance.WriteInitialValues(key)

    def VirSim_Write(self, strPoint,intVal):
        self.vir_sim_instance.UpdatePointValue(strPoint, intVal)
        print("Written Variable '" +strPoint+"' [Virtual Simulator] = " + str(intVal))

    def reloadXML(self):
        self.vir_sim_instance = DataManager()
        ret = self.vir_sim_instance.Connect()
        print("Connection Status : ", ret)
        self.vir_sim_instance.SetSourceAndDestinationAddress(self.PCAddress, self.pcbus, self.pd5elementNo, self.pd5bus)
        ret = self.vir_sim_instance.LoadXML(self.pathVsimxml)
        print("XML Loading Status : " + str(ret))
        key = bytearray([0x0B, 0x04, 0x05, 0x07, 0x08])
        # self.vir_sim_instance.StartWritingTables(key)
        self.vir_sim_instance.WriteInitialValues(key)
        time.sleep(20)
