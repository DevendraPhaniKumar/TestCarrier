from curses.ascii import *
import pyautogui as pa
import subprocess as sp
import paramiko
import time,wmi
import unittest
import pytesseract,os,sys
import HtmlTestRunner as HT

# Provide pytesseract for the exection software location
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\Tesseract.exe'
from PIL import ImageGrab
from win32 import win32gui
Timesess=2
Screendelay=5
dirnameutils = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dirnameutils)

# from KPI.Test_Using_Cygwin import *
# from KPI.Test_CPULoading import *
from KPI.ST_K01_HomeToAny import *
from KPI.ST_K02_MainToAutoTable import *
from KPI.ST_K03_AutoTablebackbuttonToMain import *
from KPI.ST_K04_HomeToAlarm import *
from KPI.ST_K05_AlarmToHome import *
from KPI.ST_K06_HomeToStartStop import *
from KPI.ST_K07_HomeToLogin import *
from KPI.ST_K08_LoginToPasswordOK import *
from KPI.ST_K09_AlarmToResetAlarm import *
from KPI.ST_K10_HomeToCircuitA import *
from KPI.ST_K11_CircuitAToHome import *
from KPI.ST_K12_ConfigmenuToFactoryConfig import *
from KPI.Test_AppBootuptime import *
from KPI.Test_TargetBootuptime import *


class KPI_Testing(unittest.TestCase):

    def test_01_ScreenTransistions(self):
        
        STobj01=ScreenTransTime1()
        #STobj01.start()
        STobj01.test_K01_HomeToAny()

        STobj02=ScreenTransTime2()
        #STobj02.start()
        STobj02.test_K02_MainToAutoTable()

        STobj03=ScreenTransTime3()
        #STobj03.start()
        STobj03.test_K03_AutoTablebackbuttonToMain()

        STobj04=ScreenTransTime4()
        #STobj04.start()
        STobj04.test_K04_HomeToAlarm()

        STobj05=ScreenTransTime5()
        #STobj05.start()
        STobj05.test_K05_AlarmToHome()

        STobj06=ScreenTransTime6()
        #STobj06.start()
        STobj06.test_K06_HomeToStartStop()

        STobj07=ScreenTransTime7()
        #STobj07.start()
        STobj07.test_K07_HomeToLogin()

        STobj08=ScreenTransTime8()
        #STobj08.start()
        STobj08.test_K08_LoginToPasswordOK()

        STobj09=ScreenTransTime9()
        #STobj09.start()
        STobj09.test_K09_AlarmToResetAlarm()

        STobj10=ScreenTransTime10()
        #STobj10.start()
        STobj10.test_K10_HomeToCircuitA()

        STobj11=ScreenTransTime11()
        #STobj11.start()
        STobj11.test_K11_CircuitAToHome()

        STobj12=ScreenTransTime12()
        #STobj12.start()
        STobj12.test_K12_ConfigmenuToFactoryConfig()

    # def test_02_FW_DownloadTime_With_Cygwin(self):

    #     FW=FwTestCygwin()
    #     FW.test_FWwithCygwin()

    def test_02_BootupTime(self):

         AppTime=ApplicationBootuptime()
         AppTime.test_appbootuptime()

         TarTime=TargetBootuptime()
         TarTime.test_targetbootuptime()

    




if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(KPI_Testing)
    #unittest.TextTestRunner(verbosity=1).run(suite)
    unittest.main(testRunner=HT.HTMLTestRunner(output=r'C:\E2E_HVAC_Testing\STAF\TestReports'))



