from Lib_space.PIC6_API import pic6_api
import time
import unittest
assertions = unittest.TestCase('__init__')
import configparser
TestParameters = configparser.ConfigParser()
TestParameters.read(r"C:\E2E_HVAC_Testing\STAF\Utility\\TestParamaters.ini")
# Factory = TestParameters.get("TEST_PARAMETERS", "Factory")


def setup():
    pic6_api.init('https://169.254.1.1')
    TestParameters.read(r"C:\E2E_HVAC_Testing\STAF\Utility\\TestParamaters.ini")
    password = TestParameters.get("TEST_PARAMETERS", "factory")
    # print(password)
    status = pic6_api.login('factory',password)
    return status

def ss_rest_read(pointname):
    setup()
    pntVal = pic6_api.read(pointname)
    teardown()
    return pntVal

def ss_rest_read_check(pointname,expected):
    setup()
    pntVal = pic6_api.read(pointname)
    assertions.assertEqual(pntVal, expected)
    teardown()
    return pntVal

def ss_rest_write(pointname,value):
    #global value_w
    value_w = value
    setup()
    pntVal = pic6_api.write(pointname,value)
    teardown()
    return pntVal

def teardown():
     pic6_api.logout()
     return "tear down success"

# print(ss_rest_write('ALARMRST_RST_ALM','1'))
# # print(ss_rest_read('ALARMRST_RST_ALM',1))
# print(ss_rest_read('FACTORY_unitsize'))
'''
print(ss_rest_write('CTL_COMP_isRd2Go','1'))
time.sleep(2)
print(ss_rest_read('FACTORY_unitsize'))

print(ss_rest_write('CTL_COMP_isRd2St','0'))
'''
'''
print(ss_rest_write('INPUTS_EXV_FBK','100'))
'''
#while True:
#print(ss_rest_read('INPUTS_HPS_A'))
#while True:
#print(ss_rest_write('DRVA1STS_SPD','25'))
#print(ss_rest_read('INPUTS_HPS_A'))
#print(ss_rest_read('CTRLID_SERIALNB'))
#print(ss_rest_write('CTRLID_SERIALNB','1111Q'))
#print(ss_rest_read('CTRLID_SERIALNB'))
#print(ss_rest_write('STRTSTS_un_volt','0'))
#print(ss_rest_read('DRVA1STS_BUS_V'))
#print(ss_rest_read('STRTSTS_un_volt'))

#TEMP_DGT

'''
print(ss_rest_write('CTL_COMP_isEnable','1'))
print(ss_rest_write('CTL_COMP_cmd','10'))
print(ss_rest_read('CTL_COMP_cmd'))
print(ss_rest_write('CTL_COMP_cmd','11'))
print(ss_rest_read('CTL_COMP_cmd'))
print(ss_rest_write('CTL_MODE_CMP_Md','1'))
'''

#print(ss_rest_read('STARTER_grnd_flt'))
#print(ss_rest_write('STRT_CFG_ct_ratio','105'))     
#print(ss_rest_read('STRT_CFG_ct_ratio'))
#print(ss_rest_read('CTL_SLDV_isEnable'))
#print(ss_rest_write('PRESSURE_OIL_PD','0'))    
#print(ss_rest_write('STARTER_start_ok','15'))  
#print(ss_rest_read('PRESSRE_OIL_PD'))
#print(ss_rest_read('STARTER_start_ok'))
#print(ss_rest_read('PROTOCOL_NET_S_S'))
#print(ss_rest_read('STRT_CFG_ct_ratio'))
#print(ss_rest_write('STRT_CFG_ct_ratio','15'))
#print(ss_rest_read('STRT_CFG_ct_ratio'))
#print(ss_rest_read('VFD_INV_T'))
#print(ss_rest_write('VFD_INV_T','15'))
#print(ss_rest_read('VFD_INV_T'))
