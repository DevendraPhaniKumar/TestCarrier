# United technologies Corporation
# Author: Jainth, B

import BAC0
import time
import json
import xlrd
from xlrd import open_workbook


class ClassBacnetModule:

    def __init__(self):
        self.bacnet = BAC0.connect(ip='192.168.100.200', bokeh_server=False)
        self.deviceIPAddress = '192.168.100.100'
        self.deviceInstance = 1610101
        self.my_obj_list = [('analogValue', 1),
                            ('analogValue', 5),
                            ('analogValue', 6),
                            ('analogValue', 7),
                            ('analogValue', 8),
                            ('analogValue', 9),
                            ('analogValue', 10),
                            ('analogValue', 11),
                            ('analogValue', 19),
                            ('analogValue', 20),
                            ('analogValue', 21),
                            ('analogValue', 22),
                            ('analogValue', 23),
                            ('analogValue', 24),
                            ('analogValue', 25),
                            ('analogValue', 26),
                            #('analogValue', 27),
                            ('analogValue', 28),
                            ('analogValue', 29),
                            ('analogValue', 30),
                            ('analogValue', 31),
                            ('analogValue', 32),
                            ('analogValue', 33),
                            ('analogValue', 34),
                            ('analogValue', 35),
                            #('analogValue', 36),
                            ('analogValue', 37),
                            ('analogValue', 38),
                            ('analogValue', 39),
                            ('analogValue', 40),
                            ('analogValue', 41),
                            ('analogValue', 42),
                            ('analogValue', 43),
                            ('analogValue', 44),
                            #('analogValue', 45),
                            ('analogValue', 46),
                            ('analogValue', 47),
                            ('analogValue', 48),
                            ('analogValue', 49),
                            ('analogValue', 50),
                            ('analogValue', 51),
                            ('analogValue', 52),
                            ('analogValue', 53),
                            ('analogValue', 54),
                            #('analogValue', 55),
                            ('analogValue', 56),
                            ('analogValue', 57),
                            ('analogValue', 58),
                            ('analogValue', 79),
                            ('binaryValue', 2),
                            ('binaryValue', 4),
                            ('binaryValue', 12),
                            ('binaryValue', 13),
                            ('binaryValue', 14),
                            #('binaryValue', 15),
                            ('binaryValue', 59),
                            ('binaryValue', 60),
                            ('binaryValue', 61),
                            ('binaryValue', 62),
                            ('binaryValue', 63),
                            ('binaryValue', 64),
                            ('binaryValue', 65),
                            ('binaryValue', 66),
                            ('binaryValue', 67),
                            ('binaryValue', 68),
                            ('binaryValue', 69),
                            ('binaryValue', 70),
                            ('binaryValue', 71),
                            ('binaryValue', 72),
                            ('binaryValue', 73),
                            ('binaryValue', 74),
                            ('binaryValue', 75),
                            ('binaryValue', 76),
                            ('binaryValue', 77),
                            ('binaryValue', 78),
                            ('multiStateValue', 3),
                            ('multiStateValue', 16),
                            ('multiStateValue', 17),
                            ('multiStateValue', 18)]

        self.controller = BAC0.device(self.deviceIPAddress, self.deviceInstance, self.bacnet, segmentation_supported=False, object_list=self.my_obj_list)

    #def terminate(self):
    #    #self.controller.save()
    #    self.bacnet.disconnect()
    #    print("It's over")
    #    #self.addfinalizer(terminate)
    #    return self.controller

    def read_bacnet_point_present_value(self, bacnet_point_name):
        return self.controller[bacnet_point_name]

    def write_bacnet_point_present_value(self, bacnet_point_name, bacnet_point_value):
        self.controller[bacnet_point_name] = bacnet_point_value
        return None

    def write_bacnet_points(self, path):
        path_of_workbook = path
        wb = open_workbook(path_of_workbook)
        data_list = []
        for sheet in wb.sheets():
            number_of_rows = sheet.nrows
            number_of_columns = sheet.ncols
            #print("number_of_columns in sheet", sheet, number_of_columns)
            curr_column = 1
            while curr_column < number_of_columns - 1:
                #print("curr_column = ", curr_column)
                curr_column += 1
                data = {}
                #print("curr_column += 1", curr_column)
                for curr_row in range(0, number_of_rows):
                    bacnet_alias_name = sheet.cell(curr_row, 0).value
                    bacnet_point_name = sheet.cell(curr_row, 1).value
                    bacnet_point_value = sheet.cell(curr_row, curr_column).value
                    print("bacnetpointname = ", bacnet_point_name, "bacnetpointvalue", bacnet_point_value)
                    self.write_bacnet_point_present_value(bacnet_point_name, bacnet_point_value)
                    data[bacnet_alias_name] = bacnet_point_value
                data['timestamp'] = int(time.time())
                time.sleep(10)       # wait seconds before going into next sheet. sheet is basically a test cycle.
                data_list.append(data)
                #json_data = json.dumps(data_list)
                #print(json_data)
        return data_list

    # read values of all bacnet points
    def read_bacnet_points(self, path):
        path_of_workbook = path
        wb = open_workbook(path_of_workbook)
        json_data = []
        for sheet in wb.sheets():
            number_of_rows = sheet.nrows
            data_list = []
            data = {}
            for curr_row in range(0, number_of_rows):
                bacnet_alias_name = sheet.cell(curr_row, 0).value
                bacnet_point_name = sheet.cell(curr_row, 1).value
                bacnet_point_value = self.read_bacnet_point_present_value(bacnet_point_name)
                print(bacnet_point_name, "  ", bacnet_point_value)
                data[bacnet_alias_name] = bacnet_point_value
                # print(data)
            data['timestamp'] = int(time.time())
            data_list.append(data)
            json_data = json.dumps(data_list)
        return json_data
