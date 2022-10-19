import CCN_Module
import VirSim_Module
import time
import xlrd
import json
from xlrd import open_workbook
from pathlib import Path, PureWindowsPath

#dirnameutils = Path("Automation_Suite/Utilities/")
#print(dirnameutils / "dct_xml/19dv/DCT_19DV_SCG-SB-20M200400.xml")
#dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#sys.path.append(dirnameutils + "/Utilities")


class CcnModule:

    def __init__(self):
        #ccn_handle = CCN_Module.CCN_Adatper(1, 3, 2, 50, 50, 1, 239, 0, 0, r"D:\!D-Drive\python\PythonTestFramework\test_pic6_connectivity_automation\dct_xml\pic6demo\DCT.xml")
        #ccn_handle = CCN_Module.CCN_Adatper(1, 3, 2, 50, 50, 1, 239, 0, 0, r"D:\!D-Drive\python\PythonTestFramework\test_pic6_connectivity_automation\dct_xml\19dv\DCT_19DV_SCG-SB-20M200400.xml")

        self.ccn_handle = CCN_Module.CCN_Adatper(1, 3, 2, 50, 50, 1, 239, 0, 0, r"D:\Automation\Automation_Suite\Utilities\dct_xml\pitbull\DCT.xml")
        self.ccn_handle.setDestination(220, 0, 1, 0, 4)
        #vir_sim_instance = VirSim_Module.Virtual_Simulator(220, 0, 15, 15, r"D:\!D-Drive\python\PythonTestFramework\test_pic6_connectivity_automation\pd5_xml\pic6demo\PIC6_demo_All_LEN_IOs.xml")
        self.vir_sim_instance = VirSim_Module.Virtual_Simulator(220, 0, 15, 15, r"D:\Automation\Automation_Suite\Utilities\pd5_xml\pitbull\ControlMapping_30XV_Pitbull_IMPERIAL_V10.xml")
        time.sleep(5)

    # write values of all CCN points
    def write_ccn_points(self, path, delay_time):
        path_of_workbook = path
        wb = open_workbook(path_of_workbook)
        json_data = []
        json_data1 = []
        data_list = []
        for sheet in wb.sheets():
            number_of_rows = sheet.nrows
            number_of_columns = sheet.ncols
            #print("number_of_columns in sheet", sheet, number_of_columns)
            curr_column = 1
            while curr_column < number_of_columns - 1:
                #print("curr_column = ", curr_column)
                curr_column += 1
                #print("curr_column += 1", curr_column)
                data = {}
                for curr_row in range(0, number_of_rows):
                    ccn_alias_name = sheet.cell(curr_row, 0).value
                    ccn_point_name = sheet.cell(curr_row, 1).value
                    ccn_point_value = sheet.cell(curr_row, curr_column).value
                    print("ccn_point_name = ", ccn_point_name, "ccn_point_value", ccn_point_value)
                    self.ccn_handle.CCN_WriteVarVal(ccn_point_name, ccn_point_value)
                    #time.sleep(1) #  is not required?
                    #ccn_handle.CCN_WritePointinTable(ccn_point_name, ccn_point_value)
                    data[ccn_alias_name] = ccn_point_value
                data['timestamp'] = int(time.time())
                time.sleep(delay_time)       # wait seconds before going into next sheet. sheet is basically a test cycle.
                data_list.append(data)
                #json_data = json.dumps(data_list)
                #json_data1 = json.loads(data_list)
                #print(json_data, json_data1)
        return data_list

    # read values of all Virtual simulator points via CCN
    def read_ccn_points(self, path):
        path_of_workbook = path
        wb = open_workbook(path_of_workbook)
        #json_data = []
        for sheet in wb.sheets():
            number_of_rows = sheet.nrows
            #data_list = []
            #data = {}
            for curr_row in range(0, number_of_rows):
                ccn_alias_name = sheet.cell(curr_row, 0).value
                ccn_point_name = sheet.cell(curr_row, 1).value
                ccn_point_value = self.ccn_handle.CCN_ReadVarVal(ccn_point_name)
                print(ccn_point_name, "  ", ccn_point_value)
                #data[ccn_alias_name] = ccn_point_value
                # print(data)
            #data['timestamp'] = int(time.time())
            #data_list.append(data)
            #json_data = json.loads(data_list)
        #return json_data