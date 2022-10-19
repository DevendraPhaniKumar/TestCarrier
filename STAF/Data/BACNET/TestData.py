'''
Created on Aug 14, 2020

@author: kattupd
'''

dut_address = '169.254.1.1'
dut_address1 = '192.168.168.6'

binary_value_obj_instance = ['1','2','3','4','5','6','7','8','9','10']

analog_value_obj_instance = ['1','2','3','4','5','6','7','8','9','10']

binary_value_obj_propname   = ['presentValue','description']
binary_value_obj_prop_value = 'HRDC' 


binary_value_obj_read_output = 'inactive'
binary_value_obj_read_outputs =['inactive','active']
binary_value_obj_output_ack = 'ack'

class analogValue_test_parameters(object):
    '''
    Define analogValue Object Test Data
    '''
    Cooling_stpt_wr_presentValue = '41.0'
    Analog_wr_presentValue = '1.0'
    Analog_rd_presentValue = '0.0'
	
class binaryValue_test_parameters(object):
    '''
    Define binaryValue Parameters
    '''
    binary_value_obj_prop_value = 'HRDC'
    Chiller_command_wr_on_presentValue = 'active'
    Chiller_command_wr_off_presentValue = 'inactive'
    
analog_value_obj_multiple_list = [{'2':('554', 'presentValue')}, {'2':('554', 'description')}]
analog_value_obj_multiple_output_list = [0.0, 'Setpoint Select']


analog_value_obj_multiple_write_list = [{'2':('554', 'presentValue','1')}]
analog_value_obj_multiple_write_read_list = [1]

binary_value_obj_multiple_list = [{'5':('123', 'presentValue')}, {'5':('123', 'description')}]
binary_value_obj_multiple_output_list = ['inactive', 'Chiller Start/Stop']

binary_value_obj_multiple_write_list = [{'binaryValue':('123', 'presentValue','active')}]
binary_value_obj_multiple_write_read_list = ['active']

objList = [{'AV':('analogValue', 554)},{'AV':('analogValue', 546)},
           {'BV':('binaryValue', 123)},{'BV':('binaryValue', 128)}]

Bacnet_objTypes = ({
0:'analog-input',
1:'analog-output',
2:'analogValue',
3:'binary-input',
4:'binary-output',
5:'binaryValue',
6:'calendar',
7:'command',
8:'device',
9:'event-enrollment',
10:'file',
11:'group',
12:'loop',
13:'multi-state-input',
14:'multi-state-output',
15:'notification-class',
16:'program',
17:'schedule',
18:'averaging',
19:'multi-state-value',
20:'trendLog',
21:'life-safety-point',
22:'life-safety-zone',
23:'accumulator',
24:'pulse-converter'
})

# Device according to 135-2004
#    Property ID     Property Name                             Datatype                                 Access
DEV=[
    ['75',            'Object_Identifier',                   'ObjectIdentifier',                       'R'],
    ['77',            'Object_Name',                         'CharacterString',                        'R'],
    ['79',            'Object_Type',                         'ObjectType',                             'O'],
    ['76',            'Object_List',                         'BACnetARRAYNofBACnetObjectIdentifier',   'R'],
    ['70',            'Model_Name',                          'CharacterString',                        'R'],
    ['58',            'Location',                            'CharacterString',                        'O']
    ]

# Analog-Value according to 135-2004
#    Property ID        Property Name                           Datatype                              Access
AV=[
    ['75',            'objectIdentifier',                   'ObjectIdentifier',                       'R'],
    ['77',            'objectName',                         'CharacterString',                        'R'],
    ['79',            'objectType',                         'ObjectType',                             'R'],
    ['85',            'presentValue',                       'Real',                                   'O'],
    ['28',            'description',                        'CharacterString',                        'O'],
    ['111',           'statusFlags',                        'StatusFlags',                            'R'],
    ['36',            'eventState',                         'EventState',                             'R'],
    ['81',            'outOfService',                       'Boolean',                                'O']
]

BV=[
    ['75',            'objectIdentifier',                   'ObjectIdentifier',                       'R'],
    ['77',            'objectName',                         'CharacterString',                        'R'],
    ['79',            'objectType',                         'ObjectType',                             'R'],
    ['85',            'presentValue',                       'Real',                                   'O'],
    ['28',            'description',                        'CharacterString',                        'O'],
    ['111',           'statusFlags',                        'StatusFlags',                            'R'],
    ['36',            'eventState',                         'EventState',                             'R'],
    ['81',            'outOfService',                       'Boolean',                                'O']]

