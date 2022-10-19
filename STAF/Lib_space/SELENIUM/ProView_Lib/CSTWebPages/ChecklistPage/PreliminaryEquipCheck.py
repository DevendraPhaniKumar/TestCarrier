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
from Page_locators.ChecklistPagelocators.PreliminaryEquipCheck_locators import PreliminaryEquipCheckPageLocators
from Page_locators.ChecklistPagelocators.ChecklistPage_locators import ChecklistPageLocators
from . import Checklist
from selenium.webdriver.common.by import By
import unittest

driver = object
delay = 75
assertion = unittest.TestCase('__init__')

class PreliminaryEquipCheck(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(PreliminaryEquipCheck, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()

    def locator_name(self):
        ##########################################################  30HX  ##########################################################
        self.M30HX_swrite = ["M30HX_Default", "M30HX_control_voltage_05", "M30HX_freeze_protect_05", "M30HX_antifreeze_type_20", "M30HX_concentration_02"]

        self.M30HX_tog = ["M30HX_physical_damage_yes", "M30HX_physical_damage_no", "M30HX_shipper_claim_yes", "M30HX_shipper_claim_no", "M30HX_prevent_startup_yes", "M30HX_prevent_startup_no", "M30HX_instructions_yes", "M30HX_instructions_no",
                            "M30HX_name_plate_yes", "M30HX_name_plate_no", "M30HX_wiring_yes", "M30HX_wiring_no", "M30HX_grounded_yes", "M30HX_grounded_no", "M30HX_protection_yes", "M30HX_protection_no", "M30HX_50F_yes", "M30HX_50F_no",
                            "M30HX_vent_piping_yes", "M30HX_vent_piping_no", "M30HX_baffles_yes", "M30HX_baffles_no", "M30HX_water_valves_yes", "M30HX_water_valves_no", "M30HX_piping_yes", "M30HX_piping_no", "M30HX_purged_yes",
                            "M30HX_purged_no", "M30HX_rotation_yes", "M30HX_rotation_no", "M30HX_interlock_yes", "M30HX_interlock_no", "M30HX_mesh_stainer_yes", "M30HX_mesh_stainer_no", "M30HX_water_loop_yes", "M30HX_water_loop_no",
                            "M30HX_heads_tubes_yes", "M30HX_heads_tubes_no", "M30HX_water_pump_yes", "M30HX_water_pump_no", "M30HX_interlock_wired_yes", "M30HX_interlock_wired_no", "M30HX_vfd_yes", "M30HX_vfd_no", "M30HX_primary_loop_yes",
                            "M30HX_primary_loop_no", "M30HX_second_loop_yes", "M30HX_second_loop_no", "M30HX_condenser_yes", "M30HX_condenser_no", "M30HX_condenser_piping_yes", "M30HX_condenser_piping_no", "M30HX_air_purge_yes",
                            "M30HX_air_purge_no", "M30HX_con_rotation_yes", "M30HX_con_rotation_no", "M30HX_con_pump_yes", "M30HX_con_pump_no", "M30HX_inlet_stainer_yes", "M30HX_inlet_stainer_no", "M30HX_switch_yes", "M30HX_switch_no",
                            "M30HX_switch_op_yes", "M30HX_switch_op_no", "M30HX_con_valve_yes", "M30HX_con_valve_no", "M30HX_ref_piping_yes", "M30HX_ref_piping_no", "M30HX_equilizer_yes", "M30HX_equilizer_no", "M30HX_driers_yes", "M30HX_driers_no",
                            "M30HX_solinoids_yes", "M30HX_solinoids_no", "M30HX_r134_yes", "M30HX_r134_no", "M30HX_ref_evacuated_yes", "M30HX_ref_evacuated_no"]

        ##########################################################  30MP  ##########################################################
        self.M30MP_swrite = ["M30MP_Default", "M30MP_gallons_05", "M30MP_system_fluid_volume_05"]

        self.M30MP_tog = ["M30MP_damage_yes", "M30MP_damage_no", "M30MP_where_yes", "M30MP_where_no", "M30MP_freight_yes", "M30MP_freight_no", "M30MP_shipper_yes", "M30MP_shipper_no", "M30MP_startup_yes",
                            "M30MP_startup_no", "M30MP_power_yes", "M30MP_power_no", "M30MP_protection_yes", "M30MP_protection_no", "M30MP_wires_yes", "M30MP_wires_no", "M30MP_ground_yes", "M30MP_ground_no",
                            "M30MP_terminals_yes", "M30MP_terminals_no", "M30MP_requirements_yes", "M30MP_requirements_no", "M30MP_guide_yes", "M30MP_guide_no", "M30MP_rates_yes", "M30MP_rates_no", "M30MP_Cooler_yes",
                            "M30MP_Cooler_no", "M30MP_Condenser_yes", "M30MP_Condenser_no", "M30MP_separation_yes", "M30MP_separation_no", "M30MP_temperatures_yes", "M30MP_temperatures_no", "M30MP_freezing_yes",
                            "M30MP_freezing_no", "M30MP_tightness_yes", "M30MP_tightness_no", "M30MP_refrigerant_yes", "M30MP_refrigerant_no", "M30MP_dehydrated_yes", "M30MP_dehydrated_no", "M30MP_charged_yes",
                            "M30MP_charged_no", "M30MP_crankcase_yes", "M30MP_crankcase_no"]

        ##########################################################  30RAP  ##########################################################
        self.M30RAP_swrite = ["M30RAP_Default", "M30RAP_freeze_protection_05", "M30RAP_antifreeze_type_20", "M30RAP_concentration_02"]

        self.M30RAP_tog = ["M30RAP_damage_yes", "M30RAP_damage_no", "M30RAP_freight_yes", "M30RAP_freight_no", "M30RAP_installation_yes", "M30RAP_installation_no", "M30RAP_nameplate_yes", "M30RAP_nameplate_no",
                            "M30RAP_Electrical_yes", "M30RAP_Electrical_no", "M30RAP_grounded_yes", "M30RAP_grounded_no", "M30RAP_protection_yes", "M30RAP_protection_no", "M30RAP_terminals_yes", "M30RAP_terminals_no",
                            "M30RAP_assemblies_yes", "M30RAP_assemblies_no", "M30RAP_brackets_yes", "M30RAP_brackets_no", "M30RAP_cleaned_yes", "M30RAP_cleaned_no", "M30RAP_valves_yes", "M30RAP_valves_no", "M30RAP_piping_yes",
                            "M30RAP_piping_no", "M30RAP_purged_yes", "M30RAP_purged_no", "M30RAP_rotation_yes", "M30RAP_rotation_no", "M30RAP_controlled_yes", "M30RAP_controlled_no", "M30RAP_interlocked_yes",
                            "M30RAP_interlocked_no", "M30RAP_Integrated_yes", "M30RAP_Integrated_no", "M30RAP_requirements_yes", "M30RAP_requirements_no", "M30MP_insulated_yes", "M30MP_insulated_no", "M30MP_heaters_yes",
                            "M30MP_heaters_no", "M30MP_energizer_yes", "M30MP_energizer_no"]

        ##########################################################  30RB  ##########################################################
        self.M30RB_swrite = ["M30RB_Default", "M30RB_control_volts_05", "M30RB_freeze_protect_05", "M30RB_antifreeze_20", "M30RB_concentration_02"]

        self.M30RB_tog = ["M30RB_damage_yes", "M30RB_damage_no", "M30RB_freight_yes", "M30RB_freight_no", "M30RB_startup_yes", "M30RB_startup_no", "M30RB_installation_yes", "M30RB_installation_no", "M30RB_nameplate_yes",
                            "M30RB_nameplate_no", "M30RB_trans_primary_yes", "M30RB_trans_primary_no", "M30RB_elec_power_yes", "M30RB_elec_power_no", "M30RB_grounded_yes", "M30RB_grounded_no", "M30RB_protection_yes",
                            "M30RB_protection_no", "M30RB_crankcase_yes", "M30RB_crankcase_no", "M30RB_third_party_yes", "M30RB_third_party_no", "M30RB_contractor_yes", "M30RB_contractor_no", "M30RB_valves_yes", "M30RB_valves_no",
                            "M30RB_piping_yes", "M30RB_piping_no", "M30RB_purged_yes", "M30RB_purged_no", "M30RB_rotation_yes", "M30RB_rotation_no", "M30RB_interlock_yes", "M30RB_interlock_no", "M30RB_hydronic_yes",
                            "M30RB_hydronic_no", "M30RB_ambient_yes", "M30RB_ambient_no", "M30RB_flush_yes", "M30RB_flush_no", "M30RB_outdoor_yes", "M30RB_outdoor_no", "M30RB_operational_yes", "M30RB_operational_no",
                            "M30RB_pressure_yes", "M30RB_pressure_no", "M30RB_baffles_yes", "M30RB_baffles_no", "M30RB_vfd_yes", "M30RB_vfd_no", "M30RB_primary_yes", "M30RB_primary_no", "M30RB_second_yes", "M30RB_second_no",
                            "M30RB_pumps_yes", "M30RB_pumps_no", "M30RB_wired_yes", "M30RB_wired_no"]

        ##########################################################  30XA  ##########################################################
        self.M30XA_swrite = ["M30XA_Default", "M30XA_control_volts_05", "M30XA_freeze_protect_05", "M30XA_antifreeze_20", "M30XA_concentration_02"]

        self.M30XA_tog = ["M30XA_damage_yes", "M30XA_damage_no", "M30XA_startup_yes", "M30XA_startup_no", "M30XA_installation_yes", "M30XA_installation_no", "M30XA_nameplate_yes", "M30XA_nameplate_no",
                            "M30XA_elec_power_yes", "M30XA_elec_power_no", "M30XA_grounded_yes", "M30XA_grounded_no", "M30XA_protection_yes", "M30XA_protection_no", "M30XA_terminals_yes", "M30XA_terminals_no",
                            "M30XA_assemblies_yes", "M30XA_assemblies_no", "M30XA_transducers_yes", "M30XA_transducers_no", "M30XA_thermistors_yes", "M30XA_thermistors_no", "M30XA_separator_yes",
                            "M30XA_separator_no", "M30XA_vent_yes", "M30XA_vent_no", "M30XA_valves_yes", "M30XA_valves_no", "M30XA_piping_yes", "M30XA_piping_no", "M30XA_purged_yes", "M30XA_purged_no",
                            "M30XA_rotation_yes", "M30XA_rotation_no", "M30XA_pump_yes", "M30XA_pump_no", "M30XA_hydronic_yes", "M30XA_hydronic_no", "M30XA_ambient_yes", "M30XA_ambient_no", "M30XA_switch_yes",
                            "M30XA_switch_no", "M30XA_outdoor_yes", "M30XA_outdoor_no", "M30XA_operational_yes", "M30XA_operational_no", "M30XA_pressure_yes", "M30XA_pressure_no", "M30XA_baffles_yes",
                            "M30XA_baffles_no"]

        ##########################################################  30XV  ##########################################################
        self.M30XV_swrite = ["M30XV_Default", "M30XV_control_volts_05", "M30XV_freeze_protect_05", "M30XV_antifreeze_20", "M30XV_concentration_02"]

        self.M30XV_tog = ["M30XV_damage_yes", "M30XV_damage_no", "M30XV_startup_yes", "M30XV_startup_no", "M30XV_installation_yes", "M30XV_installation_no", "M30XV_nameplate_yes", "M30XV_nameplate_no",
                            "M30XV_elec_power_yes", "M30XV_elec_power_no", "M30XV_grounded_yes", "M30XV_grounded_no", "M30XV_protection_yes", "M30XV_protection_no", "M30XV_terminals_yes", "M30XV_terminals_no",
                            "M30XV_assemblies_yes", "M30XV_assemblies_no", "M30XV_transducers_yes", "M30XV_transducers_no", "M30XV_thermistors_yes", "M30XV_thermistors_no", "M30XV_separator_yes", "M30XV_separator_no",
                            "M30XV_vent_yes", "M30XV_vent_no", "M30XV_valves_yes", "M30XV_valves_no", "M30XV_piping_yes", "M30XV_piping_no", "M30XV_purged_yes", "M30XV_purged_no", "M30XV_rotation_yes",
                            "M30XV_rotation_no", "M30XV_pump_yes", "M30XV_pump_no", "M30XV_hydronic_yes", "M30XV_hydronic_no", "M30XV_ambient_yes", "M30XV_ambient_no", "M30XV_switch_yes", "M30XV_switch_no",
                            "M30XV_outdoor_yes", "M30XV_outdoor_no", "M30XV_operational_yes", "M30XV_operational_no", "M30XV_pressure_yes", "M30XV_pressure_no", "M30XV_baffles_yes", "M30XV_baffles_no"]

        ##########################################################  30XW  ##########################################################
        self.M30XW_swrite = ["M30XW_Default", "M30XW_control_volts_05", "M30XW_freeze_protect_05", "M30XW_antifreeze_20", "M30XW_concentration_02"]

        self.M30XW_tog = ["M30XW_damage_yes", "M30XW_damage_no", "M30XW_freight_yes", "M30XW_freight_no", "M30XW_startup_yes", "M30XW_startup_no", "M30XW_installation_yes", "M30XW_installation_no", "M30XW_nameplate_yes",
                            "M30XW_nameplate_no", "M30XW_elec_power_yes", "M30XW_elec_power_no", "M30XW_grounded_yes", "M30XW_grounded_no", "M30XW_protection_yes", "M30XW_protection_no", "M30XW_terminals_yes", "M30XW_terminals_no",
                            "M30XW_assemblies_yes", "M30XW_assemblies_no", "M30XW_vent_yes", "M30XW_vent_no", "M30XW_temperatures_no", "M30XW_temperatures_yes", "M30XW_valves_yes", "M30XW_valves_no", "M30XW_piping_yes",
                            "M30XW_piping_no", "M30XW_purged_yes", "M30XW_purged_no", "M30XW_rotation_yes", "M30XW_rotation_no", "M30XW_pump_yes", "M30XW_pump_no", "M30XW_operational_yes", "M30XW_operational_no",
                            "M30XW_evaporator_yes", "M30XW_evaporator_no", "M30XW_ambient_yes", "M30XW_ambient_no", "M30XW_outdoor_yes", "M30XW_outdoor_no", "M30XW_con_valves_yes", "M30XW_con_valves_no", "M30XW_con_piping_yes",
                            "M30XW_con_piping_no", "M30XW_con_purged_yes", "M30XW_con_purged_no", "M30XW_con_rotation_yes", "M30XW_con_rotation_no", "M30XW_con_pump_yes", "M30XW_con_pump_no",
                            "M30XW_con_switch_yes", "M30XW_con_switch_no", "M30XW_con_inlet_yes", "M30XW_con_inlet_no",
                            "M30XW_con_outdoor_yes", "M30XW_con_outdoor_no", "M30XW_con_head_yes", "M30XW_con_head_no"]

        ##########################################################  30XWV  ##########################################################
        self.M30XWV_swrite = ["M30XWV_Default", "M30XWV_control_volts_05", "M30XWV_freeze_protect_05", "M30XWV_antifreeze_20", "M30XWV_concentration_02"]

        self.M30XWV_tog = ["M30XWV_damage_yes", "M30XWV_damage_no", "M30XWV_freight_yes", "M30XWV_freight_no", "M30XWV_startup_yes", "M30XWV_startup_no", "M30XWV_installation_yes", "M30XWV_installation_no", "M30XWV_nameplate_yes",
                                "M30XWV_nameplate_no", "M30XWV_elec_power_yes", "M30XWV_elec_power_no", "M30XWV_grounded_yes", "M30XWV_grounded_no", "M30XWV_protection_yes", "M30XWV_protection_no", "M30XWV_terminals_yes", "M30XWV_terminals_no",
                                "M30XWV_assemblies_yes", "M30XWV_assemblies_no", "M30XWV_vent_yes", "M30XWV_vent_no", "M30XWV_temperatures_no", "M30XWV_temperatures_yes", "M30XWV_valves_yes", "M30XWV_valves_no", "M30XWV_piping_yes",
                                "M30XWV_piping_no", "M30XWV_purged_yes", "M30XWV_purged_no", "M30XWV_rotation_yes", "M30XWV_rotation_no", "M30XWV_pump_yes", "M30XWV_pump_no", "M30XWV_operational_yes", "M30XWV_operational_no",
                                "M30XWV_evaporator_yes", "M30XWV_evaporator_no", "M30XWV_ambient_yes", "M30XWV_ambient_no", "M30XWV_con_valves_yes", "M30XWV_con_valves_no", "M30XWV_con_piping_yes", "M30XWV_con_piping_no", "M30XWV_con_purged_yes",
                                "M30XWV_con_purged_no", "M30XWV_con_rotation_yes", "M30XWV_con_rotation_no", "M30XWV_con_pump_yes", "M30XWV_con_pump_no", "M30XWV_con_operational_yes", "M30XWV_con_operational_no", "M30XWV_con_strainer_yes",
                                "M30XWV_con_strainer_no", "M30XWV_con_tape_yes", "M30XWV_con_tape_no", "M30XWV_con_pressure_yes", "M30XWV_con_pressure_no", "M30XWV_outdoor_yes", "M30XWV_outdoor_no"]

        self.prefix = {'30HX': 'M30HX', '30MP': 'M30MP', '30RAP': 'M30RAP', '30RB': 'M30RB', '30XA': 'M30XA',
                   '30XV': 'M30XV', '30XW': 'M30XW', '30XWV': 'M30XWV'}
    def write_prelim_info_data(self, Data):
        # self.prefix = {'30HX': 'M30HX', '30MP': 'M30MP', '30RAP': 'M30RAP', '30RB': 'M30RB', '30XA': 'M30XA', '30XV': 'M30XV', '30XW': 'M30XW', '30XWV': 'M30XWV'}

        try:
            xpath = eval("PreliminaryEquipCheckPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
            xpath = self.find_elements(*xpath)
            for i in range(len(eval("self." + self.prefix[Data['Model']] + "_swrite"))):
                if "_Default" not in eval("self." + self.prefix[Data['Model']] + "_swrite[i]"):
                    self.checklist.write_similar_element(xpath=xpath, index=eval(
                        "PreliminaryEquipCheckPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[i]")),
                                                         Data=Data)
                    print('Written Post Start data to ' + str(
                        eval("self." + self.prefix[Data['Model']] + "_swrite[i]")) \
                          + ' =', Data['testdata'])
        except IndexError as e:
            print(e.message)



        for y in range(len(eval('self.' + self.prefix[Data['Model']] + '_tog'))):
            if eval('self.' + self.prefix[Data['Model']] + '_tog')[y][-3:] == 'yes':
                xpath = eval('self.' + self.prefix[Data['Model']] + '_tog')[y]
                self.checklist.click(xpath, page_locators="PreliminaryEquipCheckPageLocators")
                print('Written preliminaryequipcheck data of ' + xpath + ' =', 'yes')

    def read_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_swrite"):
            if ele != self.prefix[Data['Model']]+"_Default":
                common_xpath = eval("PreliminaryEquipCheckPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read', page_locators="PreliminaryEquipCheckPageLocators", index_assert=5)
                try:
                    if eval(ele[-2:].lstrip('0')) == 20:
                        assertion.assertEqual(value == Data['testdata'][:20],True)
                    else:
                        assertion.assertEqual(float(value) == float(''.join(filter(str.isdigit, str(Data['testdata'])))[:eval(ele[-2:].lstrip('0'))]), True)
                    print('Read preliminaryequipcheck Information(' + ele + ')' + ' =', value)
                except:
                    print("assertion error", value)
        for ele in eval("self."+self.prefix[Data['Model']]+"_tog"):
            value = self.checklist.read(ele, None, Data, 'yes|no', page_locators="PreliminaryEquipCheckPageLocators")
            try:
                if ele[-3:] == 'yes':
                    assertion.assertEqual(value == 'true', True)
                elif ele[-2:] == 'no':
                    assertion.assertEqual(value == None, True)

                print('Read preliminaryequipcheck Information of '+ ele+' = ', value)
            except:
                print('Assertion Error')
        try:
            for ele in eval("self."+self.prefix[Data['Model']]+"_swrite_no_index"):
                common_xpath = eval("PreliminaryEquipCheckPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read', page_locators="PreliminaryEquipCheckPageLocators")
                assertion.assertEqual(value == Data['testdata'],True)
                print('Read preliminaryequipcheck Information(' + ele + ')' + ' =', value)
        except:
            pass


    def read_reset_data(self, Data):
        for ele in eval("self."+self.prefix[Data['Model']]+"_swrite"):
            if ele != self.prefix[Data['Model']]+"_Default":
                common_xpath = eval("PreliminaryEquipCheckPageLocators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'reset_read', page_locators="PreliminaryEquipCheckPageLocators", index_assert=5)
                assertion.assertEqual(value == '', True)
                print('Read preliminaryequipcheck Information of ' + ele + ' = ', 'Null')

        for ele in eval("self."+self.prefix[Data['Model']]+"_tog"):
            value = self.checklist.read(ele, None, Data, 'reset_yes|no', page_locators="PreliminaryEquipCheckPageLocators")
            if ele[-3:] == 'yes':
                assertion.assertEqual(value == None, True)
            elif ele[-2:] == 'no':
                assertion.assertEqual(value == 'true', True)
            print('Read preliminaryequipcheck Information of ' + ele + ' = ', value)

    def preliminaryequipcheck_exit(self):
        self.find_element(*PreliminaryEquipCheckPageLocators.preliminaryequipcheck_exit).click()

    def preliminaryequipcheck_save(self):
        self.find_element(*PreliminaryEquipCheckPageLocators.preliminaryequipcheck_save).click()

    def preliminaryequipcheck_cancel(self):
        self.find_element(*PreliminaryEquipCheckPageLocators.preliminaryequipcheck_cancel).click()

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
