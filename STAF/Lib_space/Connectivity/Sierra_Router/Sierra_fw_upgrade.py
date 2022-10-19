import os
import time
import unittest
from subprocess import Popen, PIPE

dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
path = dirnameutils + "\\Utilities\\SierraPackage\\ccs_gw_fx30_4g_1.1.4\\"
print(path)
os.chdir(path)
#p = Popen("C:\\End to End\\Python3_app\\Utilities\\SierraPackage\\ccs_gw_fx30_4g_1.1.4\\RouterConfig.bat",cwd='C:\\End to End\\Python3_app\\Utilities\\SierraPackage\\ccs_gw_fx30_4g_1.1.4\\')
p = Popen("RouterConfig.bat", stdin=PIPE, stdout=PIPE, universal_newlines=True)

'''
stdout, stderr = p.communicate()
print("*********stdout***********")
print(stdout)
print("*********stdout***********")
print(stderr)
'''


class TestCases(unittest.TestCase):

    def setUp(self):
        pass

    def test_sierra_fw_upgrade_connected_to_internet(self):
        internet_is_present = "Internet Connectivity established"
        counter = 0
        while True:
            line = p.stdout.readline()
            if not line:
                break
            print("test:", str(line.rstrip()))
            if str(line.rstrip()) == internet_is_present:
                print("unit test")
                self.assertEqual(str(line.rstrip()), internet_is_present)
            print(p.returncode)
            if "PIC6 Connection" in str(line.rstrip()):
                counter += 1
            if counter > 1:
                break

        time.sleep(10)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
