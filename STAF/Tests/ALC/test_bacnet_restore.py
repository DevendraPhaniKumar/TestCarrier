'''
Created on Aug 6, 2021

@author: kattupd
'''
import unittest
import sys, os
import HtmlTestRunner
import time
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))                      
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(dirnameutils)

from Lib_space.PARAMIKO.paramiko_module import SSHConnector

from Lib_space.BACNET import BACnet_Module

from zipfile import ZipFile
import zipfile

dut_address = '192.168.168.6'

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)

class BACnet_PIC6_RESTORE_Test(unittest.TestCase):

    def setUp(self):
        print ("\n********************************************************************************")
        print ("Setup Function - START")
        print ("********************************************************************************")
        self.bacnet = BACnet_Module.Adapter(dirnameutils + "\Lib_space\BACNET\Adpater_setting.ini")
        self.bacnet.set_destination(dut_address)
        print ("********************************************************************************")
        print ("Setup Function - END")
        print ("********************************************************************************")

    def readFile(self, instance, path):
        print('Perform File Object File Size')
        size_op = self.bacnet.readproperty('file', str(instance), '42')
        print(size_op)
        print('Perform Automic Read File')
        fileContent = b''
        bytesRead = 0
        size = int(size_op)
        print(size)
        while bytesRead < size:
            atomicSize = 460 if (size - bytesRead) >= 460 else size - bytesRead
            atomicFile = self.bacnet.readatomicfile(str(instance), str(bytesRead), str(atomicSize))
            fileContent += atomicFile
            bytesRead += len(atomicFile)
        
        print(len(fileContent), fileContent)
        with open(path, "wb") as binaryFile:
            binaryFile.write(fileContent)
                    
    def writeFile(self,instance, path):
        with open(path, "rb") as binaryFile:
            writeOffset = 0;
            while True:
                chunk = binaryFile.read(420)
                if chunk:
                    print('Perform Automic Write File')
                    self.bacnet.writeatomicfile(str(instance), writeOffset, chunk)
                    writeOffset += len(chunk)
                    print (len(chunk), chunk)
                else:
                    break
     
    def test_BACnet_Restore_func(self):       
        failStr = ''        
        try:
            
            #Place restore_config file Under Logs Folder
            print('--------------------START-------------------------------')
            print('Perform Automic Write File')                                                                
            self.writeFile(2, dirnameutils+"\\Logs\\restore_config.zip")
            
            print('Perform Start Restore')
            read_ouput = self.bacnet.ReinitializeRequest('startRestore', None)
            print (read_ouput)
            
            time.sleep(10)
            
            print('Perform End Restore')
            read_ouput = self.bacnet.ReinitializeRequest('endRestore', None)
            print (read_ouput)
            
            time.sleep(180)
            
            self.ssh = SSHConnector('192.168.168.6', 22, 'sdk', '7uR!\!2dxp*t$')            
            curre_time = datetime.now().strftime('%b %d %H:%M')[:]
            print(curre_time)
            
            print('Login to the Device Shell')
            self.ssh.cmd_exec('login root')
            self.ssh.cmd_exec('X*rD8u!6nk')
            output = self.ssh.cmd_exec('ls -l /home/app/CONFIG/IVU')            
            print(output)
            
            
            print('Verify the BACKUP.ZIP File is Created or not')
            filter_object = filter(lambda a: 'BACNET_BACKUP.ZIP' in a, output)
            op = len(list(filter_object))
            print(op)
            self.assertEqual(op, 1, msg="BACNET_BACKUP.ZIP file not get created")            
            
            print('Perform Automic Read File & Create BACKUP Zip file ')
            self.readFile(2, dirnameutils+"\\Logs\\config_backup.zip")
            
            with ZipFile(dirnameutils+'\\Logs\\config_backup.zip', 'r') as zipObj:
                print('Get list of files names in zip')
                #listOfiles = zipObj.infolist()
                listOfiles = zipObj.namelist()
                print(listOfiles)
                print(len(listOfiles))
                if len(listOfiles) == 4:
                    print('.zip folder content is correct')
                else :
                    print('.zip folder content is not correct')
            
            zip = zipfile.ZipFile(dirnameutils+'\\Logs\\config_backup.zip')#           
            file = zip.read('2_db_forced_nvm.txt')
            #print(file)
            #print(type(file))
            op = file.decode("utf-8")
            print(op)
            if "PROTOCOL_CHIL_S_S;1;120" in op:
                print('Modified value is available after Restore is Success')
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
            self.ssh.close_ssh()
            print ("********************************************************************************")
            print ("Teardown Function - END")
            print ("********************************************************************************")
  
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=dirnameutils + "\Results\\"+foldername))                 
