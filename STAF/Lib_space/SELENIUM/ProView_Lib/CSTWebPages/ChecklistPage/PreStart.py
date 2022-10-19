import re
import os
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dirnameutils)
sys.path.append(dirnameutils+'\Selenium_Lib')
from Selenium_Lib.BaseClass import Page
from Page_locators.ChecklistPagelocators.PrestartPage_locators import PreStartPageLocators
from Page_locators.ChecklistPagelocators.ChecklistPage_locators import ChecklistPageLocators
from . import Checklist
from selenium.webdriver.common.by import By
import unittest

driver = object
delay = 75
assertion = unittest.TestCase('__init__')

class PreStart(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(PreStart, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)

    # def goto_pre_start(self, Data):
    #     self.wait_until_element(PreStartPageLocators.prestart)
    #     element = self.find_elements(*PreStartPageLocators.prestart)
    #     try:
    #         element[int(Data['Checklist index'])].click()
    #     except:
    #         element = self.find_elements(*PreStartPageLocators.prestart_filled)
    #         element[int(Data['Checklist index'])].click()

        ######## 16JT and 16JB ##########
        self.M16_clickables = ["M16_WMT_no", "M16_WMT_yes", "M16_leak_crt_no", "M16_leak_crt_yes",
                               "M16_Perform_control_test_no", "M16_Perform_control_test_yes",
                               "M16_shut_down_machine_no", "M16_shut_down_machine_yes",
                               "M16_Chilled_Water_Flow_Switch_no", "M16_Chilled_Water_Flow_Switch_yes",
                               "M16_Cooling_Water_Flow_Switch_no", "M16_Cooling_Water_Flow_Switch_yes",
                               "M16_Pump_Interlocks_no", "M16_Pump_Interlocks_yes",
                               "M16_GEN_Temperature_no", "M16_GEN_Temperature_yes", "M16_GEN_Pressure_no",
                               "M16_GEN_Pressure_yes", "M16_LCWCO_no", "M16_LCWCO_yes",
                               "M16_Solution_Pump_Rotation_and_Record_no", "M16_Solution_Pump_Rotation_and_Record_yes",
                               "M16_Refrigerant_Pump_Rotation_and_Record_no",
                               "M16_Refrigerant_Pump_Rotation_and_Record_yes", "M16_Pumps_and_Establish_Water_Flow_no",
                               "M16_Pumps_and_Establish_Water_Flow_yes", ]
        self.M16_same_writables = ["M16_Default", "M16_Instruction_Manual_Values", "M16_LiBr_Charged", "M16_Refrigerant_Charged",
                                   "M16_Cooler", "M16_Condenser", "M16_Absorber",
                                   "M16_CR_Initial_charge", "M16_CR_FinalCharge_After_Trim", "M16_CL_Initial_charge",
                                   "M16_CL_FinalCharge_After_Trim", "M16_Ratings",
                                   "M16_Line_Voltages", "M16_Controls", "M16_IMP"]
        self.M16_writables = []

        ######## 17DA 19XR 19XRD 19XRE 19XRV #########
        self.M17_M19XR_XRD_XRE_XRV_clickables = ["M17_M19XR_XRD_XRE_XRV_WMT_yes", "M17_M19XR_XRD_XRE_XRV_WMT_no",
                               "M17_M19XR_XRD_XRE_XRV_leak_crted_yes", "M17_M19XR_XRD_XRE_XRV_leak_crted_no",
                               "M17_M19XR_XRD_XRE_XRV_Mach_dehydrate_yes", "M17_M19XR_XRD_XRE_XRV_Mach_dehydrate_no",
                               "M17_M19XR_XRD_XRE_XRV_Oil_sump_34", "M17_M19XR_XRD_XRE_XRV_Oil_sump_12",
                               "M17_M19XR_XRD_XRE_XRV_Oil_sump_14", "M17_M19XR_XRD_XRE_XRV_Oil_sump_full",
                               "M17_M19XR_XRD_XRE_XRV_Oil_sump_null", "M17_M19XR_XRD_XRE_XRV_strainer_housing_34",
                               "M17_M19XR_XRD_XRE_XRV_strainer_housing_12", "M17_M19XR_XRD_XRE_XRV_strainer_housing_14",
                               "M17_M19XR_XRD_XRE_XRV_strainer_housing_full",
                               "M17_M19XR_XRD_XRE_XRV_strainer_housing_null", "M17_M19XR_XRD_XRE_XRV_add_oil_yes",
                               "M17_M19XR_XRD_XRE_XRV_add_oil_no", "M17_M19XR_XRD_XRE_XRV_controls_test_yes",
                               "M17_M19XR_XRD_XRE_XRV_controls_test_no",
                               "M17_M19XR_XRD_XRE_XRV_condenser_water_pump_yes",
                               "M17_M19XR_XRD_XRE_XRV_condenser_water_pump_no",
                               "M17_M19XR_XRD_XRE_XRV_chilled_water_pump_yes",
                               "M17_M19XR_XRD_XRE_XRV_chilled_water_pump_no",
                               "M17_M19XR_XRD_XRE_XRV_condenser_water_flow_yes",
                               "M17_M19XR_XRD_XRE_XRV_condenser_water_flow_no",
                               "M17_M19XR_XRD_XRE_XRV_chilled_water_flow_yes",
                               "M17_M19XR_XRD_XRE_XRV_chilled_water_flow_no",
                               "M17_M19XR_XRD_XRE_XRV_pump_interlocks_yes", "M17_M19XR_XRD_XRE_XRV_pump_interlocks_no",
                               "M17_M19XR_XRD_XRE_XRV_line_up_manual_yes",
                               "M17_M19XR_XRD_XRE_XRV_line_up_manual_no", "M17_M19XR_XRD_XRE_XRV_start_WP_WF_yes",
                               "M17_M19XR_XRD_XRE_XRV_start_WP_WF_no", "M17_M19XR_XRD_XRE_XRV_OL_OT_OK_yes",
                               "M17_M19XR_XRD_XRE_XRV_OL_OT_OK_no", "M17_M19XR_XRD_XRE_XRV_check_oil_p_preassure_yes",
                               "M17_M19XR_XRD_XRE_XRV_check_oil_p_preassure_no",
                               "M17_M19XR_XRD_XRE_XRV_check_comp_motor_yes",
                               "M17_M19XR_XRD_XRE_XRV_check_comp_motor_no", "M17_M19XR_XRD_XRE_XRV_clockwise_yes",
                               "M17_M19XR_XRD_XRE_XRV_clockwise_no",
                               "M17_M19XR_XRD_XRE_XRV_restart_comp_yes", "M17_M19XR_XRD_XRE_XRV_restart_comp_no"]
        self.M17_M19XR_XRD_XRE_XRV_same_writables = ["M17_M19XR_XRD_XRE_XRV_Default","M17_M19XR_XRD_XRE_XRV_cooler", "M17_M19XR_XRD_XRE_XRV_condenser",
                                   "M17_M19XR_XRD_XRE_XRV_initial_charge", "M17_M19XR_XRD_XRE_XRV_IMP", "M17_M19XR_XRD_XRE_XRV_amount"]
        self.M17_M19XR_XRD_XRE_XRV_writables = ["M17_M19XR_XRD_XRE_XRV_Motor_volt", "M17_M19XR_XRD_XRE_XRV_motor_amps",
                              "M17_M19XR_XRD_XRE_XRV_oil_pump_volts", "M17_M19XR_XRD_XRE_XRV_LRA_rating",
                              "M17_M19XR_XRD_XRE_XRV_line_volt", "M17_M19XR_XRD_XRE_XRV_oil_pump",
                              "M17_M19XR_XRD_XRE_XRV_oil_heater"]
        ####### 19PIC6 and 19 PIC5 ########
        self.M19PIC6_PIC5_clickables = ["M19PIC6_PIC5_WMT_yes", "M19PIC6_PIC5_WMT_no", "M19PIC6_PIC5_leak_crted_yes",
                               "M19PIC6_PIC5_leak_crted_no", "M19PIC6_PIC5_Mach_dehydrate_yes",
                               "M19PIC6_PIC5_Mach_dehydrate_no", "M19PIC6_PIC5_Oil_sump_34", "M19PIC6_PIC5_Oil_sump_12",
                               "M19PIC6_PIC5_Oil_sump_14", "M19PIC6_PIC5_Oil_sump_full",
                               "M19PIC6_PIC5_Oil_sump_null", "M19PIC6_PIC5_strainer_housing_34",
                               "M19PIC6_PIC5_strainer_housing_12", "M19PIC6_PIC5_strainer_housing_14",
                               "M19PIC6_PIC5_strainer_housing_full", "M19PIC6_PIC5_strainer_housing_null",
                               "M19PIC6_PIC5_add_oil_yes", "M19PIC6_PIC5_add_oil_no",
                               "M19PIC6_PIC5_Controls_test_yes", "M19PIC6_PIC5_Controls_test_no",
                               "M19PIC6_PIC5_condenser_water_pump_yes", "M19PIC6_PIC5_condenser_water_pump_no",
                               "M19PIC6_PIC5_chilled_water_pump_yes", "M19PIC6_PIC5_chilled_water_pump_no",
                               "M19PIC6_PIC5_condenser_water_flow_yes", "M19PIC6_PIC5_condenser_water_flow_no",
                               "M19PIC6_PIC5_chilled_water_flow_yes", "M19PIC6_PIC5_chilled_water_flow_no",
                               "M19PIC6_PIC5_pump_interlocks_yes", "M19PIC6_PIC5_pump_interlocks_no",
                               "M19PIC6_PIC5_line_up_manual_yes", "M19PIC6_PIC5_line_up_manual_no",
                               "M19PIC6_PIC5_start_WP_WF_yes", "M19PIC6_PIC5_start_WP_WF_no",
                               "M19PIC6_PIC5_OL_OT_OK_yes",
                               "M19PIC6_PIC5_OL_OT_OK_no", "M19PIC6_PIC5_check_oil_p_preassure_yes",
                               "M19PIC6_PIC5_check_oil_p_preassure_no", "M19PIC6_PIC5_check_comp_motor_yes",
                               "M19PIC6_PIC5_check_comp_motor_no", "M19PIC6_PIC5_clockwise_yes",
                               "M19PIC6_PIC5_clockwise_no", "M19PIC6_PIC5_restart_comp_yes",
                               "M19PIC6_PIC5_restart_comp_no"]
        self.M19PIC6_PIC5_same_writables = ["M19PIC6_PIC5_Default", "M19PIC6_PIC5_IMP", "M19PIC6_PIC5_amount", "M19PIC6_PIC5_cooler",
                                   "M19PIC6_PIC5_condenser", "M19PIC6_PIC5_initial_charge",
                                   "M19PIC6_PIC5_delta_no_ground", "M19PIC6_PIC5_delta_grounded",
                                   "M19PIC6_PIC5_wye_centre_ground", "M19PIC6_PIC5_wye_no_ground",
                                   "M19PIC6_PIC5_transformer_size"]
        self.M19PIC6_PIC5_writables = ["M19PIC6_PIC5_Motor_volt", "M19PIC6_PIC5_motor_amps", "M19PIC6_PIC5_oil_pump_volts",
                              "M19PIC6_PIC5_LRS_rating",
                              "M19PIC6_PIC5_line_volt", "M19PIC6_PIC5_oil_pump", "M19PIC6_PIC5_oil_heater",
                              "M19PIC6_PIC5_phase_AB",
                              "M19PIC6_PIC5_phase_BC", "M19PIC6_PIC5_phase_AC", "M19PIC6_PIC5_ground_AG",
                              "M19PIC6_PIC5_ground_BG", "M19PIC6_PIC5_ground_AG_"]
        ############  19XL  #############
        self.M19XL_clickables = ["M19XL_WMT_yes", "M19XL_WMT_no", "M19XL_leak_crted_yes", "M19XL_leak_crted_no",
                               "M19XL_Mach_dehydrate_yes", "M19XL_Mach_dehydrate_no",
                               "M19XL_Oil_sump_34", "M19XL_Oil_sump_12", "M19XL_Oil_sump_14", "M19XL_Oil_sump_full",
                               "M19XL_Oil_sump_null", "M19XL_strainer_housing_34",
                               "M19XL_strainer_housing_12", "M19XL_strainer_housing_14", "M19XL_strainer_housing_full",
                               "M19XL_strainer_housing_null", "M19XL_add_oil_yes",
                               "M19XL_add_oil_no", "M19XL_add_dash_pot_oil_yes", "M19XL_add_dash_pot_oil_no",
                               "M19XL_solid_state_overloads_yes", "M19XL_solid_state_overloads_no",
                               "M19XL_Controls_test_yes", "M19XL_Controls_test_no",
                               "M19XL_condenser_water_flow_yes", "M19XL_condenser_water_flow_no",
                               "M19XL_chilled_water_flow_yes", "M19XL_chilled_water_flow_no",
                               "M19XL_pump_interlocks_yes", "M19XL_pump_interlocks_no", "M19XL_line_up_manual_yes",
                               "M19XL_line_up_manual_no", "M19XL_start_WP_WF_yes",
                               "M19XL_start_WP_WF_no", "M19XL_OL_OT_OK_yes", "M19XL_OL_OT_OK_no",
                               "M19XL_check_oil_p_preassure_yes", "M19XL_check_oil_p_preassure_no",
                               "M19XL_check_comp_motor_yes", "M19XL_check_comp_motor_no", "M19XL_clockwise_yes",
                               "M19XL_clockwise_no", "M19XL_restart_comp_yes", "M19XL_restart_comp_no"]
        self.M19XL_same_writables = ["M19XL_Default", "M19XL_IMP",
                                   "M19XL_signal_res", "M19XL_transition_time",
                                   "M19XL_torque_setting", "M19XL_ramp_setting", "M19XL_amount", "M19XL_cooler",
                                   "M19XL_condenser", "M19XL_initial_charge", "M19XL_final_charge"]
        self.M19XL_same_writables_no_index = ["M19XL_manufacturer", "M19XL_serial_no", "M19XL_motor_load_ratio"]
        self.M19XL_writables = ["M19XL_Motor_volt", "M19XL_motor_amps", "M19XL_oil_pump_volts", "M19XL_LRS_rating",
                              "M19XL_line_volt", "M19XL_oil_pump", "M19XL_oil_heater"]
        ####### 23XL ########
        self.M23XL_writables = []
        self.M23XL_same_writables = ["M23XL_Default", "M23XL_IMP", "M23XL_cooler", "M23XL_condenser", "M23XL_initial_charge",
                                     "M23XL_final_charge", "M23XL_amount"]
        self.M23XL_same_writables_no_index = ["M23XL_manufaturer", "M23XL_serial_no",
                                     "M23XL_motor_load_ratio"]
        self.M23XL_clickables = ["M23XL_WMT_yes", "M23XL_WMT_no", "M23XL_leak_crted_yes", "M23XL_leak_crted_no",
                                  "M23XL_Mach_dehydrate_yes", "M23XL_Mach_dehydrate_no",
                                  "M23XL_Oil_sump_34", "M23XL_Oil_sump_12", "M23XL_Oil_sump_14", "M23XL_Oil_sump_full",
                                  "M23XL_Oil_sump_null", "M23XL_strainer_housing_34",
                                  "M23XL_strainer_housing_12", "M23XL_strainer_housing_14",
                                  "M23XL_strainer_housing_full", "M23XL_strainer_housing_null", "M23XL_add_oil_yes",
                                  "M23XL_add_oil_no",
                                  "M23XL_electro_mech_yes", "M23XL_electro_mech_no",
                                  "M23XL_solid_state_yes", "M23XL_solid_state_no", "M23XL_solid_state_overloads_yes",
                                  "M23XL_solid_state_overloads_no", "M23XL_controls_test_yes",
                                  "M23XL_controls_test_no", "M23XL_condenser_water_flow_yes",
                                  "M23XL_condenser_water_flow_no", "M23XL_chilled_water_flow_yes",
                                  "M23XL_chilled_water_flow_no", "M23XL_pump_interlocks_yes",
                                  "M23XL_pump_interlocks_no", "M23XL_line_up_manual_yes", "M23XL_line_up_manual_no",
                                  "M23XL_start_WP_WF_yes", "M23XL_start_WP_WF_no", "M23XL_OL_OT_OK_yes",
                                  "M23XL_OL_OT_OK_no", "M23XL_oil_preassure_yes", "M23XL_oil_preassure_no",
                                  "M23XL_restart_comp_yes", "M23XL_restart_comp_no"]
        ####### 23XRV ############
        self.M23_XRV_writables = ["M23_XRV_Motor_volt", "M23_XRV_motor_amps", "M23_XRV_oil_pump_volts",
                                 "M23_XRV_LRS_rating", "M23_XRV_line_volt", "M23_XRV_oil_pump",
                                 "M23_XRV_oil_heater", "M23_XRV_phase_AB", "M23_XRV_phase_BC", "M23_XRV_phase_AC",
                                 "M23_XRV_ground_AG", "M23_XRV_ground_BG", "M23_XRV_ground_AG_"]
        self.M23_XRV_same_writables = ["M23_XRV_Default", "M23_XRV_delta_no_ground", "M23_XRV_delta_grounded", "M23_XRV_wye_centre_ground",
                                      "M23_XRV_wye_no_ground", "M23_XRV_transformer_size",
                                      "M23_XRV_amount", "M23_XRV_cooler", "M23_XRV_condenser", "M23_XRV_initial_charge",
                                      "M23_XRV_IMP"]
        self.M23_XRV_clickables = ["M23_XRV_WMT_yes", "M23_XRV_WMT_no", "M23_XRV_leak_crted_yes",
                                   "M23_XRV_leak_crted_no", "M23_XRV_Mach_dehydrate_yes", "M23_XRV_Mach_dehydrate_no",
                                   "M23_XRV_Oil_sump_34", "M23_XRV_Oil_sump_12", "M23_XRV_Oil_sump_14",
                                   "M23_XRV_Oil_sump_full", "M23_XRV_Oil_sump_null", "M23_XRV_strainer_housing_34",
                                   "M23_XRV_strainer_housing_12", "M23_XRV_strainer_housing_14",
                                   "M23_XRV_strainer_housing_full", "M23_XRV_strainer_housing_null",
                                   "M23_XRV_add_oil_yes",
                                   "M23_XRV_add_oil_no", "M23_XRV_6inch_clearance_yes", "M23_XRV_6inch_clearance_no",
                                   "M23_XRV_inspenct_debries_yes", "M23_XRV_inspenct_debries_no",
                                   "M23_XRV_verify_VFD_params_yes",
                                   "M23_XRV_verify_VFD_params_no", "M23_XRV_control_test_yes",
                                   "M23_XRV_control_test_no", "M23_XRV_condenser_liq_pump_yes",
                                   "M23_XRV_condenser_liq_pump_no", "M23_XRV_chilled_liq_pump_yes",
                                   "M23_XRV_chilled_liq_pump_no",
                                   "M23_XRV_discharge_muffer_yes", "M23_XRV_discharge_muffer_no",
                                   "M23_XRV_cooler_inlet_yes", "M23_XRV_cooler_inlet_no", "M23_XRV_hot_gas_bypass_yes",
                                   "M23_XRV_hot_gas_bypass_no", "M23_XRV_vapourize_yes", "M23_XRV_vapourize_no",
                                   "M23_XRV_oil_pump_yes", "M23_XRV_oil_pump_no", "M23_XRV_oil_filter_yes",
                                   "M23_XRV_oil_filter_no", "M23_XRV_oil_pressure_yes", "M23_XRV_oil_pressure_no",
                                   "M23_XRV_filter_next_yes", "M23_XRV_filter_next_no", "M23_XRV_filte_under_yes",
                                   "M23_XRV_filte_under_no", "M23_XRV_VFD_under_yes", "M23_XRV_VFD_under_no",
                                   "M23_XRV_VFD_between_yes", "M23_XRV_VFD_between_no", "M23_XRV_cooler_seated_yes",
                                   "M23_XRV_cooler_seated_no", "M23_XRV_condenser_seated_yes",
                                   "M23_XRV_condenser_seated_no", "M23_XRV_cooler_tree_yes", "M23_XRV_cooler_tree_no",
                                   "M23_XRV_cooler_pumpour_yes", "M23_XRV_cooler_pumpour_no",
                                   "M23_XRV_condenser_tree_yes", "M23_XRV_condenser_tree_no",
                                   "M23_XRV_condenser_chanber_yes",
                                   "M23_XRV_condenser_chanber_no", "M23_XRV_oil_sump_yes", "M23_XRV_oil_sump_no",
                                   "M23_XRV_start_flow_yes", "M23_XRV_start_flow_no", "M23_XRV_oil_level_ok_yes",
                                   "M23_XRV_oil_level_ok_no", "M23_XRV_oil_preassure_ok_yes",
                                   "M23_XRV_oil_preassure_ok_no", "M23_XRV_restart_comp_yes", "M23_XRV_restart_comp_no"]
        ######## 32XR #########
        self.M32XR_same_writables = ["M32XR_Default","M32XR_IMP", "M32XR_amount", "M32XR_cooler", "M32XR_condenser", "M32XR_initial_charge",
                                     "M32XR_final_charge"]
        self.M32XR_same_writables_no_index = ["M32XR_manufaturer", "M32XR_serial_no", "M32XR_motor_load_ratio",
                                     "M32XR_res_size", "M32XR_transistion_time", "M32XR_magnetic_overloads"]
        self.M32XR_clickables = ["M32XR_WMT_yes", "M32XR_WMT_no", "M32XR_leak_crted_yes", "M32XR_leak_crted_no", "M32XR_Mach_dehydrate_yes",
                                "M32XR_Mach_dehydrate_no", "M32XR_Oil_sump_34", "M32XR_Oil_sump_12", "M32XR_Oil_sump_14", "M32XR_Oil_sump_full",
                                "M32XR_Oil_sump_null", "M32XR_strainer_housing_34", "M32XR_strainer_housing_12", "M32XR_strainer_housing_14",
                                "M32XR_strainer_housing_full", "M32XR_strainer_housing_null", "M32XR_add_oil_yes", "M32XR_add_oil_no",
                                "M32XR_startes_installed_yes", "M32XR_electro_mech_yes", "M32XR_electro_mech_no",
                                "M32XR_solid_state_yes", "M32XR_solid_state_no", "M32XR_add_dash_pot_oil_yes", "M32XR_add_dash_pot_oil_no",
                                "M32XR_solid_state_overloads_yes", "M32XR_solid_state_overloads_no", "M32XR_controls_test_yes", "M32XR_controls_test_no",
                                "M32XR_condenser_water_flow_yes", "M32XR_condenser_water_flow_no", "M32XR_chilled_water_flow_yes", "M32XR_chilled_water_flow_no",
                                "M32XR_pump_interlocks_yes", "M32XR_pump_interlocks_no", "M32XR_line_up_manual_yes", "M32XR_line_up_manual_no", "M32XR_start_WP_WF_yes",
                                "M32XR_start_WP_WF_no", "M32XR_OL_OT_OK_yes", "M32XR_OL_OT_OK_no", "M32XR_oil_preassure_yes", "M32XR_oil_preassure_no",
                                "M32XR_restart_comp_yes", "M32XR_restart_comp_no"]
        self.M32XR_writables = ["M32XR_Motor_volt", "M32XR_motor_amps", "M32XR_oil_pump_volts", "M32XR_LRS_rating", "M32XR_line_volt", "M32XR_oil_pump", "M32XR_oil_heater"]

        self.M38AU_same_writables = ["M38AU_Default", "M38AU_indoor_fan_speed", "M38AU_outdoor_fan_speen"]
        self.M38AU_clickables = ["M38AU_shipping_damage_yes", "M38AU_shipping_damage_no", "M38AU_damage_prevent_yes", "M38AU_damage_prevent_no", "M38AU_power_supply_yes",
                                "M38AU_power_supply_no", "M38AU_ground_conn_yes", "M38AU_ground_conn_no", "M38AU_circiut_protect_yes", "M38AU_circiut_protect_no",
                                "M38AU_power_wires_yes", "M38AU_power_wires_no", "M38AU_thermostats_yes", "M38AU_thermostats_no", "M38AU_terminals_yes", "M38AU_terminals_no",
                                "M38AU_crankcase_yes", "M38AU_crankcase_no", "M38AU_drainage_yes", "M38AU_drainage_no", "M38AU_air_filters_yes", "M38AU_air_filters_no",
                                "M38AU_fan_motor_yes", "M38AU_fan_motor_no", "M38AU_fan_belts_yes", "M38AU_fan_belts_no", "M38AU_fan_rotation_yes", "M38AU_fan_rotation_no",
                                "M38AU_solenoid_req_yes", "M38AU_solenoid_req_no", "M38AU_leak_chck_yes", "M38AU_leak_chck_no", "M38AU_line_open_yes", "M38AU_line_open_no",
                                "M38AU_vapour_line_open_yes", "M38AU_vapour_line_open_no"]
        self.M38AU_writables = ["M38AU_vapour_pressure_cooling", "M38AU_suc_temp_cooling", "M38AU_liq_pressure_cooling", "M38AU_liq_temp_cooling",
                                "M38AU_entering_outdoor_ait_temp_cooling", "M38AU_leaving_outdoor_air_temp_cooling", "M38AU_dry_air_DB_temp_cooling",
                                "M38AU_wet_air_DB_temp_cooling", "M38AU_air_DB_temp_cooling", "M38AU_air_WB_temp_cooling", "M38AU_vapour_pressure_heating",
                                "M38AU_suc_temp_heating", "M38AU_liq_pressure_heating", "M38AU_liq_temp_heating", "M38AU_entering_outdoor_ait_temp_heating",
                                "M38AU_leaving_outdoor_air_temp_heating", "M38AU_dry_air_DB_temp_heating", "M38AU_wet_air_DB_temp_heating", "M38AU_air_DB_temp_heating",
                                "M38AU_air_WB_temp_heating", "M38AU_comp_amps_l1", "M38AU_comp_amps_l2", "M38AU_comp_amps_l3", "M38AU_Line_voltsAB", "M38AU_Line_voltsAC",
                                "M38AU_Line_voltsBC", "M38AU_avg_volts", "M38AU_max_avg_volts"]

        self.M39MN_clickables = ["M39MN_thermostats_checked_yes", "M39MN_thermostats_checked_no", "M39MN_wire_termonals_yes", "M39MN_wire_termonals_no", "M39MN_remove_debris_yes",
                                "M39MN_remove_debris_no", "M39MN_inspect_damage_yes", "M39MN_inspect_damage_no", "M39MN_inspect_flanges_yes", "M39MN_inspect_flanges_no",
                                "M39MN_caulk_yes", "M39MN_caulk_no", "M39MN_door_latches_yes", "M39MN_door_latches_no", "M39MN_release_fan_yes", "M39MN_release_fan_no",
                                "M39MN_check_fan_yes", "M39MN_check_fan_no", "M39MN_hand_turn_fan_yes", "M39MN_hand_turn_fan_no", "M39MN_fan_alliengment_yes",
                                "M39MN_fan_alliengment_no", "M39MN_fan_tension_yes", "M39MN_fan_tension_no", "M39MN_proper_filters_yes", "M39MN_proper_filters_no", "M39MN_wiring_terminals_yes",
                                "M39MN_wiring_terminals_no", "M39MN_drain_pan_yes", "M39MN_drain_pan_no", "M39MN_duct_connected_yes", "M39MN_duct_connected_no", "M39MN_verify_wiring_yes",
                                "M39MN_verify_wiring_no", "M39MN_field_wiring_yes", "M39MN_field_wiring_no", "M39MN_leak_checks_yes", "M39MN_leak_checks_no", "M39MN_air_blend_yes",
                                "M39MN_air_blend_no", "M39MN_freeze_protection_yes", "M39MN_freeze_protection_no", "M39MN_DXsystem_yes", "M39MN_DXsystem_no"]
        self.M39MN_same_writables = []
        self.M39MN_writables = []
        self.M39MW_same_writables = []
        self.M39MW_writables = []
        self.M39MW_clickables = ["M39MW_indoor_fan_yes", "M39MW_indoor_fan_no", "M39MW_wire_termonals_yes", "M39MW_wire_termonals_no", "M39MW_remove_debris_yes",
                                "M39MW_remove_debris_no", "M39MW_inspect_damage_yes", "M39MW_inspect_damage_no", "M39MW_inspect_flanges_yes", "M39MW_inspect_flanges_no",
                                "M39MW_caulk_yes", "M39MW_caulk_no", "M39MW_door_latches_yes", "M39MW_door_latches_no", "M39MW_roof_joint1_yes", "M39MW_roof_joint2_yes",
                                "M39MW_roof_joint3_yes", "M39MW_roof_joint4_yes", "M39MW_roof_joint5_yes", "M39MW_roof_joint6_yes", "M39MW_roojoint_joint1_yes",
                                "M39MW_roojoint_joint2_yes", "M39MW_roojoint_joint3_yes", "M39MW_roojoint_joint4_yes", "M39MW_roojoint_joint5_yes", "M39MW_roojoint_joint6_yes",
                                "M39MW_bolted_joint1_yes", "M39MW_bolted_joint2_yes", "M39MW_bolted_joint3_yes", "M39MW_bolted_joint4_yes", "M39MW_bolted_joint5_yes",
                                "M39MW_bolted_joint6_yes", "M39MW_tightened_joint1_yes", "M39MW_tightened_joint2_yes", "M39MW_tightened_joint3_yes", "M39MW_tightened_joint4_yes",
                                "M39MW_tightened_joint5_yes", "M39MW_tightened_joint6_yes", "M39MW_gasketed_joint1_yes", "M39MW_gasketed_joint2_yes", "M39MW_gasketed_joint3_yes",
                                "M39MW_gasketed_joint4_yes", "M39MW_gasketed_joint5_yes", "M39MW_gasketed_joint6_yes", "M39MW_seam_joint1_yes", "M39MW_seam_joint2_yes",
                                "M39MW_seam_joint3_yes", "M39MW_seam_joint4_yes", "M39MW_seam_joint5_yes", "M39MW_seam_joint6_yes", "M39MW_bracket_CCH1_yes", "M39MW_bracket_CCH2_yes",
                                "M39MW_bracket_CCH3_yes", "M39MW_flashings_CCH1_yes", "M39MW_flashings_CCH2_yes", "M39MW_flashings_CCH3_yes", "M39MW_CCH_CCH1_yes",
                                "M39MW_CCH_CCH2_yes", "M39MW_CCH_CCH3_yes", "M39MW_roof_joint1_no", "M39MW_roof_joint2_no", "M39MW_roof_joint3_no", "M39MW_roof_joint4_no",
                                "M39MW_roof_joint5_no", "M39MW_roof_joint6_no", "M39MW_roojoint_joint1_no", "M39MW_roojoint_joint2_no", "M39MW_roojoint_joint3_no",
                                "M39MW_roojoint_joint4_no", "M39MW_roojoint_joint5_no", "M39MW_roojoint_joint6_no", "M39MW_bolted_joint1_no", "M39MW_bolted_joint2_no",
                                "M39MW_bolted_joint3_no", "M39MW_bolted_joint4_no", "M39MW_bolted_joint5_no", "M39MW_bolted_joint6_no", "M39MW_tightened_joint1_no",
                                "M39MW_tightened_joint2_no", "M39MW_tightened_joint3_no", "M39MW_tightened_joint4_no", "M39MW_tightened_joint5_no", "M39MW_tightened_joint6_no",
                                "M39MW_gasketed_joint1_no", "M39MW_gasketed_joint2_no", "M39MW_gasketed_joint3_no", "M39MW_gasketed_joint4_no", "M39MW_gasketed_joint5_no",
                                "M39MW_gasketed_joint6_no", "M39MW_seam_joint1_no", "M39MW_seam_joint2_no", "M39MW_seam_joint3_no", "M39MW_seam_joint4_no", "M39MW_seam_joint5_no",
                                "M39MW_seam_joint6_no", "M39MW_bracket_CCH1_no", "M39MW_bracket_CCH2_no", "M39MW_bracket_CCH3_no", "M39MW_flashings_CCH1_no",
                                "M39MW_flashings_CCH2_no", "M39MW_flashings_CCH3_no", "M39MW_CCH_CCH1_no", "M39MW_CCH_CCH2_no", "M39MW_CCH_CCH3_no", "M39MW_release_fan_yes",
                                "M39MW_release_fan_no", "M39MW_check_fan_yes", "M39MW_check_fan_no", "M39MW_hand_turn_fan_yes", "M39MW_hand_turn_fan_no", "M39MW_fan_alliengment_yes",
                                "M39MW_fan_alliengment_no", "M39MW_fan_tension_yes", "M39MW_fan_tension_no", "M39MW_proper_filters_yes", "M39MW_proper_filters_no",
                                "M39MW_wiring_terminals_yes", "M39MW_wiring_terminals_no", "M39MW_drain_pan_yes", "M39MW_drain_pan_no", "M39MW_duct_connected_yes",
                                "M39MW_duct_connected_no", "M39MW_verify_wiring_yes", "M39MW_verify_wiring_no", "M39MW_field_wiring_yes", "M39MW_field_wiring_no",
                                "M39MW_leak_checks_yes", "M39MW_leak_checks_no", "M39MW_air_blend_yes", "M39MW_air_blend_no", "M39MW_freeze_protection_yes",
                                "M39MW_freeze_protection_no", "M39MW_DXsystem_yes", "M39MW_DXsystem_no", "M39MW_fan_bearings_yes", "M39MW_fan_bearings_no"]
        self.M48A2_M48A3_M50A3_clickables = ["M48A2_M48A3_M50A3_verify_packaging_yes" ,"M48A2_M48A3_M50A3_remove_comp_bolts_yes" ,"M48A2_M48A3_M50A3_verify_economizer_yes" ,
                                "M48A2_M48A3_M50A3_verify_options_yes" ,"M48A2_M48A3_M50A3_verify_transducers_yes" ,"M48A2_M48A3_M50A3_verify_terminals_yes" ,
                                "M48A2_M48A3_M50A3_verify_sensors_yes" ,"M48A2_M48A3_M50A3_check_gas_yes" ,"M48A2_M48A3_M50A3_check_air_yes" ,
                                "M48A2_M48A3_M50A3_verify_drainage_yes" ,"M48A2_M48A3_M50A3_check_fan_wheels_yes" ,"M48A2_M48A3_M50A3_verify_fan_sheaves_yes" ,
                                "M48A2_M48A3_M50A3_verify_suction_yes" ,"M48A2_M48A3_M50A3_verify_crankcase_yes" ,"M48A2_M48A3_M50A3_verify_packaging_no" ,
                                "M48A2_M48A3_M50A3_remove_comp_bolts_no" ,"M48A2_M48A3_M50A3_verify_economizer_no" ,"M48A2_M48A3_M50A3_verify_options_no" ,
                                "M48A2_M48A3_M50A3_verify_transducers_no" ,"M48A2_M48A3_M50A3_verify_terminals_no" ,"M48A2_M48A3_M50A3_verify_sensors_no" ,
                                "M48A2_M48A3_M50A3_check_gas_no" ,"M48A2_M48A3_M50A3_check_air_no" ,"M48A2_M48A3_M50A3_verify_drainage_no" ,
                                "M48A2_M48A3_M50A3_check_fan_wheels_no" ,"M48A2_M48A3_M50A3_verify_fan_sheaves_no" ,"M48A2_M48A3_M50A3_verify_suction_no" ,
                                "M48A2_M48A3_M50A3_verify_crankcase_no"]
        self.M48A2_M48A3_M50A3_same_writables = []
        self.M48A2_M48A3_M50A3_writables = []
        self.M48HC_48TC_clickables = ["M48HC_48TC_verify_jobsite_yes", "M48HC_48TC_verify_material_yes", "M48HC_48TC_verify_hood_yes", "M48HC_48TC_remove_bolts_yes",
                                    "M48HC_48TC_verify_instructions_yes", "M48HC_48TC_verify_fuel_yes", "M48HC_48TC_check_ref_piping_yes", "M48HC_48TC_check_gas_piping_yes",
                                    "M48HC_48TC_check_ele_conections_yes", "M48HC_48TC_verify_gas_pressure_yes", "M48HC_48TC_check_indoor_air_yes",
                                    "M48HC_48TC_check_outdoor_air_yes", "M48HC_48TC_verify_unit_level_yes", "M48HC_48TC_check_fan_wheels_yes", "M48HC_48TC_check_ele_wirings_yes",
                                    "M48HC_48TC_check_pully_allign_yes", "M48HC_48TC_verify_scroll_yes", "M48HC_48TC_verif_thermostat_yes",
                                    "M48HC_48TC_verify_cranckcase_yes_yes", "M48HC_48TC_verify_jobsite_no", "M48HC_48TC_verify_material_no",
                                    "M48HC_48TC_verify_hood_no", "M48HC_48TC_remove_bolts_no", "M48HC_48TC_verify_instructions_no", "M48HC_48TC_verify_fuel_no",
                                    "M48HC_48TC_check_ref_piping_no", "M48HC_48TC_check_gas_piping_no", "M48HC_48TC_check_ele_conections_no", "M48HC_48TC_verify_gas_pressure_no",
                                    "M48HC_48TC_check_indoor_air_no", "M48HC_48TC_check_outdoor_air_no", "M48HC_48TC_verify_unit_level_no", "M48HC_48TC_check_fan_wheels_no",
                                    "M48HC_48TC_check_ele_wirings_no", "M48HC_48TC_check_pully_allign_no", "M48HC_48TC_verify_scroll_no", "M48HC_48TC_verif_thermostat_no",
                                    "M48HC_48TC_verify_cranckcase_no"]
        self.M48HC_48TC_same_writables = []
        self.M48HC_48TC_writables = []
        self.M48LC_clickables = ["M48LC_verify_packaging_yes", "M48LC_verify_outdoor_air_yes",
        "M48LC_verify_fuel_exhaust_yes", "M48LC_verify_instructions_yes", "M48LC_verify_elec_connections_yes", "M48LC_verify_gas_pressure_yes",
        "M48LC_check_gas_yes", "M48LC_check_indoor_air_yes", "M48LC_check_outdoor_air_yes", "M48LC_verify_unitlevel_yes", "M48LC_check_fan_wheels_yes",
        "M48LC_verify_fan_sheaves_yes", "M48LC_verify_scrool_yes", "M48LC_verify_thermostat_yes", "M48LC_verify_crankcase_yes", "M48LC_verify_packaging_no",
        "M48LC_verify_outdoor_air_no", "M48LC_verify_fuel_exhaust_no", "M48LC_verify_instructions_no", "M48LC_verify_elec_connections_no",
        "M48LC_verify_gas_pressure_no", "M48LC_check_gas_no", "M48LC_check_indoor_air_no", "M48LC_check_outdoor_air_no", "M48LC_verify_unitlevel_no",
        "M48LC_check_fan_wheels_no", "M48LC_verify_fan_sheaves_no", "M48LC_verify_scrool_no", "M48LC_verify_thermostat_no", "M48LC_verify_crankcase_no"]
        self.M48LC_same_writables = []
        self.M48LC_writables = []

        self.M50HC_clickables = ["M50HC_verify_packaging_yes", "M50HC_verify_condenstate_yes", "M50HC_verify_fuel_hood_yes", "M50HC_check_ele_cons_yes",
        "M50HC_check_wires_yes", "M50HC_check_gas_piping_yes", "M50HC_check_air_yes", "M50HC_verify_unit_level_yes",
        "M50HC_check_fan_wheels_yes", "M50HC_verify_pully_allign_yes", "M50HC_verify_packaging_no", "M50HC_verify_condenstate_no",
        "M50HC_verify_fuel_hood_no", "M50HC_check_ele_cons_no", "M50HC_check_wires_no", "M50HC_check_gas_piping_no", "M50HC_check_air_no",
        "M50HC_verify_unit_level_no", "M50HC_check_fan_wheels_no", "M50HC_verify_pully_allign_no"]
        self.M50HC_same_writables = []
        self.M50HC_writables = []

        self.M50PC_PS_clickables = ["M50PC_PS_volt_availableg_yes",
        "M50PC_PS_terminals_tight_yes", "M50PC_PS_heat_exchanger_yes", "M50PC_PS_valves_open_yes", "M50PC_PS_trap_installed_yes",
        "M50PC_PS_filter_installed_yes", "M50PC_PS_volt_availableg_no", "M50PC_PS_terminals_tight_no", "M50PC_PS_heat_exchanger_no",
        "M50PC_PS_valves_open_no", "M50PC_PS_trap_installed_no", "M50PC_PS_filter_installed_no"]
        self.M50PC_PS_same_writables = []
        self.M50PC_PS_writables = []

    def write_prestart_info_data(self, Data):
        self.prefix = {'16JT':'M16', '16JB':'M16', '17DA':'M17_M19XR_XRD_XRE_XRV', '19XR':'M17_M19XR_XRD_XRE_XRV', '19PIC6': 'M19PIC6_PIC5', '19XRPIC5':'M19PIC6_PIC5',
                       '19XL':'M19XL', '23XL':'M23XL', '23XRV': 'M23_XRV', '32XR': 'M32XR', '38AU': 'M38AU', '39MN': 'M39MN', '39MW': 'M39MW', '19XRD':'M17_M19XR_XRD_XRE_XRV',
                       '48A2': 'M48A2_M48A3_M50A3', '50A3': 'M48A2_M48A3_M50A3', '48A3': 'M48A2_M48A3_M50A3','48HC': 'M48HC_48TC', '48TC': 'M48HC_48TC', '48LC': 'M48LC',
                       '50HC': 'M50HC', '50PC/PS': 'M50PC_PS', '19XRE':'M17_M19XR_XRD_XRE_XRV', '19XRV':'M17_M19XR_XRD_XRE_XRV'}

        try:
            xpath = eval("PreStartPageLocators." + eval("self."+self.prefix[Data['Model']]+"_same_writables[0]"))
            xpath = self.find_elements(*xpath)
            for i in range(len(eval("self."+self.prefix[Data['Model']]+"_same_writables"))):
                if "_Default" not in eval("self."+self.prefix[Data['Model']]+"_same_writables[i]"):
                    self.checklist.write_similar_element(xpath= xpath, index= eval("PreStartPageLocators." + eval("self."+self.prefix[Data['Model']]+"_same_writables[i]")), Data= Data)
                    print('Written Pre Start data to ' + str(eval("self."+self.prefix[Data['Model']]+"_same_writables[i]")) \
                           + ' =', Data['testdata'])
        except IndexError as e:
            print(e.message)

        # count = 0
        # for ele in range(len(xpath)):
        #     try:
        #         xpath[ele].send_keys(Data['testdata'])
        #         xpath[ele].send_keys(Keys.ENTER)
        #         print eval("self." + self.prefix[Data['Model']] + "_same_writables[count]"), ele
        #         count = count + 1
        #     except:
        #         pass

        for y in range(len(eval('self.'+self.prefix[Data['Model']]+'_clickables'))):
            if eval('self.'+self.prefix[Data['Model']]+'_clickables')[y][-3:] == 'yes':
                xpath = eval('self.'+self.prefix[Data['Model']]+'_clickables')[y]
                self.checklist.click(xpath, page_locators="PreStartPageLocators")
                print('Written Prestart data of ' + xpath + ' =', 'yes')

        for i in range(len(eval("self."+self.prefix[Data['Model']]+"_writables"))):
            xpath = eval("PreStartPageLocators." + eval("self." + self.prefix[Data['Model']] + "_writables[i]"))
            self.checklist.write(xpath, Data)
            print('Written Prestart data of ' + eval("self." + self.prefix[Data['Model']] + "_writables[i]") + ' =', Data['testdata'])

    def read_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_same_writables"):
            if ele != self.prefix[Data['Model']]+"_Default":
                common_xpath = eval("PreStartPageLocators." + eval("self." + self.prefix[Data['Model']] + "_same_writables[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read', page_locators="PreStartPageLocators", index_assert=5)
                assertion.assertEqual(float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:5]), True)
                print('Read Prestart Information(' + ele + ')' + ' =', value)

        for ele in eval("self."+self.prefix[Data['Model']]+"_clickables"):
            value = self.checklist.read(ele, None, Data, 'yes|no', page_locators="PreStartPageLocators")
            if ele[-3:] == 'yes':
                assertion.assertEqual(value == 'true', True)
            elif ele[-2:] == 'no':
                assertion.assertEqual(value == None, True)
            print('Read Prestart Information of '+ ele+' = ', value)

        for ele in eval("self."+self.prefix[Data['Model']]+"_writables"):
            value = self.checklist.read(ele, None, Data, 'read_normal', page_locators="PreStartPageLocators")
            assertion.assertEqual(float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:5]), True)
            # assertion.assertEqual(value == Data['testdata'], True)
            print('Read Prestart Information(' + ele + ')' + ' =', value)

        try:
            for ele in eval("self."+self.prefix[Data['Model']]+"_same_writables_no_index"):
                common_xpath = eval("PreStartPageLocators." + eval("self." + self.prefix[Data['Model']] + "_same_writables[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read', page_locators="PreStartPageLocators")
                assertion.assertEqual(value == Data['testdata'],True)
                print('Read Prestart Information(' + ele + ')' + ' =', value)
        except:
            pass

    def read_reset_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_same_writables"):
            if ele != self.prefix[Data['Model']]+"_Default":
                common_xpath = eval("PreStartPageLocators." + eval("self." + self.prefix[Data['Model']] + "_same_writables[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'reset_read', page_locators="PreStartPageLocators", index_assert=5)
                assertion.assertEqual(value == '', True)
                print('Read Prestart Information of ' + ele + ' = ', 'Null')

        for ele in eval("self."+self.prefix[Data['Model']]+"_clickables"):
            value = self.checklist.read(ele, None, Data, 'reset_yes|no', page_locators="PreStartPageLocators")
            if ele[-3:] == 'yes':
                assertion.assertEqual(value == None, True)
            elif ele[-2:] == 'no':
                assertion.assertEqual(value == 'true', True)
            print('Read Prestart Information of ' + ele + ' = ', value)

    def prestart_exit(self):
        self.find_element(*PreStartPageLocators.prestart_exit).click()

    def prestart_save(self):
        self.find_element(*PreStartPageLocators.prestart_save).click()

    def prestart_cancel(self):
        self.find_element(*PreStartPageLocators.prestart_cancel).click()

    def startup_form_cancle(self):
        self.find_element(*ChecklistPageLocators.startup_page_cancel).click()

    def startup_form_reset(self):
        self.find_element(*ChecklistPageLocators.startup_page_exit).click()

    def startup_form_exit(self):
        self.find_element(*ChecklistPageLocators.startup_page_exit).click()

    def wait_until_element(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, element[-1])))
        except TimeoutException:
            print("Loading took too much time!")

    def wait_unit_visible(self, element):
        try:
            WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, element[-1])))
        except TimeoutException:
            print("Loading took too much time!")
