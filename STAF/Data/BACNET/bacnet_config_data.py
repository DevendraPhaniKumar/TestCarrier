'''
Created on Mar 22, 2020

@author: kattupd

'''

dut_address = '192.168.168.11'
dut_device_instance = '240011'
webCTRL_address= '192.168.168.12'
bacnet_adapter_address='192.168.168.4'


ref_name= '#bacnet_obj_automation_test'
relay_test_ref_name= '#relay_test'
convert_test_ref_name= '#convert_test'
misc_test_ref_name= '#misc_test'
log_test_ref_name = '#digitaltrend'


class analogValue_obj_test(object):
    '''
    Define analogValue Object Test Data
    '''
    High_limit = '10'
    Low_limit = '5'
    Deadband = '2'
    TimeDelay = '2'
    HighLimt_cond = '12'
    HightoLowNormal_cond = '7'
    LowLimt_cond = '4'
    LowtoHighNormal_cond = '8'
    presentValue = '8'
    priority4Value = '4'
    relinquishDefault = '8'
    covIncrement = '2'
    covIncrement_prv ='7'