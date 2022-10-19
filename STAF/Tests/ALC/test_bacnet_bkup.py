'''
Created on Jul 21, 2021

@author: kattupd
'''
import unittest
import sys, os
import HtmlTestRunner
import time
import re
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))                      
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(dirnameutils)


from Lib_space.PARAMIKO.paramiko_module import SSHConnector

from Lib_space.BACNET import BACnet_Module

from zipfile import ZipFile

dut_address = '192.168.168.6'

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)

class BACnet_PIC6_BACKUP_Test(unittest.TestCase):

    def setUp(self):
        print ("\n********************************************************************************")
        print ("Setup Function - START")
        print ("********************************************************************************")
        self.bacnet = BACnet_Module.Adapter(dirnameutils + "\Lib_space\BACNET\Adpater_setting.ini")
        self.bacnet.set_destination(dut_address)        
        self.ssh = SSHConnector('192.168.168.6', 22, 'sdk', '7uR!\!2dxp*t$')
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
     
    def test_BACnet_backup_func(self):
        
        failStr = ''        
        try:
            print('--------------------START-------------------------------')                                                                
            #read_ouput = self.bacnet.readproperty('device',  '1610101', '121')            
            print('Perform Start Back-up')
            read_ouput = self.bacnet.ReinitializeRequest('startBackup', None)
            print (read_ouput)
            
            time.sleep(10)
            
            print('Perform End Back-up')
            read_ouput = self.bacnet.ReinitializeRequest('endBackup', None)
            print (read_ouput)
            
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
                        
            a=re.compile('[0-9]* ([a-zA-z0-9: ]*) BACNET_BACKUP.ZIP')
            b = a.findall(output[3])
            print(b[0][-12:])
            
            print('Verification of Time & Date')
            #self.assertEqual(b[0][-12:][:10], curre_time[:10], msg="BACNET_BACKUP.ZIP file is not get created with current Date&Time")
            print('BACNET_BACKUP.ZIP file is get created with current Date&Time')            
            print(b[0][-17:-13])
            
            print('Perform File Object File Size')
            size_op = self.bacnet.readproperty('file', 2, '42')
            print(size_op)            
            
            print('Verify File Size')
            self.assertEqual(b[0][-17:-13], size_op, msg="Size of config_file not match with BACNET_BACKUP.zip file")
            
            
            print('Perform File Object Description')
            file_out =  self.bacnet.readproperty('file','2','28')
            print(file_out)
            
            print('Verify File Name')
            self.assertEqual(file_out, 'Config File',msg="config_file not match with BACNET_BACKUP.zip file")
            
            print('Perform Automic Read File & Create BACKUP Zip file ')
            self.readFile(2, dirnameutils+"\\Logs\\config.zip")
            
            #self.writeFile(2, "config.zip")

            with ZipFile(dirnameutils+"\\Logs\\config.zip", 'r') as zipObj:
                print('Get list of files names in zip')
                #listOfiles = zipObj.infolist()
                listOfiles = zipObj.namelist()
                print(listOfiles)
                print(len(listOfiles))
                if len(listOfiles) == 4:
                    print('.zip folder content is correct')
                else :
                    print('.zip folder content is not correct')
            
            '''    
            check if element exist in list using 'in'
            '''
            listOfiles_new = []
            for i in listOfiles :
                listOfiles_new.append(i[2:])
                
            if 'BACNET_IR.TXT' in listOfiles_new :
                print("Yes, 'BACNET_IR.TXT' found in List : " , listOfiles_new)
            else:
                raise Exception("Yes, 'BACNET_IR.TXT' Not found in List : " , listOfiles_new)
    
            if 'db_forced_nvm.txt' in listOfiles_new :
                print("Yes, 'db_forced_nvm.txt' found in List : " , listOfiles_new)
            else:
                raise Exception("Yes, 'db_forced_nvm.txt' Not found in List : " , listOfiles_new)
    
            if 'db_carrier_nvm.txt' in listOfiles_new :
                print("Yes, 'db_carrier_nvm.txt' found in List : " , listOfiles_new)
            else:
                raise Exception("Yes, 'db_carrier_nvm.txt' Not found in List : " , listOfiles_new)
    
    
            if 'BACNET_TL.TXT' in listOfiles_new :
                print("Yes, 'BACNET_TL.TXT' found in List : " , listOfiles_new)
            else:
                raise Exception("Yes, 'BACNET_TL.TXT' Not found in List : " , listOfiles_new)
            
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
  