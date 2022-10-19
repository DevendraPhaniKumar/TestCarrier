from selenium.webdriver.common.by import By


class PreStartPageLocators(object):
    prestart = (By.XPATH, '//*[@id="tabdivisonsid"]/ul/li/a/span[1]/i')
    prestart_filled = (By.XPATH, '//*[@id="tabdivisonsid"]/ul/li/a/span[2]/i')
    prestart_reset = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[1]/ul/li[2]/a')
    prestart_exit = (By.XPATH, '//*[@id="aExistingForm"]')
    prestart_save = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[4]/ul/li[2]/a')
    prestart_cancel = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[4]/ul/li[1]/a')
    save_form = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[4]/ul/li[2]/a')
    save_form_popup = (By.XPATH, '//*[@id="AlmostDoneModal"]/div/div/div/form/div[3]/div/button')
    save_form_close_X =(By.XPATH, '//*[@id="SavedSuccessfullyModel"]/div/div/a')
    # save_form_2 = (By.XPATH, '')
    M16_Default = (By.XPATH, '//*[@id="a"]')
    M16_IMP = 52
    M16_WMT_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M16_WMT_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    # M16_WMT_yes = (By.XPATH, '//*[@name="ab11"]')
    M16_leak_crt_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M16_leak_crt_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')

    # Record Pressure Drop
    M16_Cooler = 26
    M16_Condenser = 27
    M16_Absorber = 28

    # Charge Refrigerant
    M16_CR_Initial_charge = 29
    M16_CR_FinalCharge_After_Trim = 30

    # Charge LiBr
    M16_CL_Initial_charge = 31
    M16_CL_FinalCharge_After_Trim = 32

    # Inspect Wiring & Record Electrical Data:
    M16_Ratings = 33
    M16_Line_Voltages = 50
    M16_Controls = 51

    # Control:Safety,Operating, Etc:
    M16_Perform_control_test_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[7]/div/div/div/div/div/div/div[3]/ul/li[1]/label/span')
    M16_Perform_control_test_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[7]/div/div/div/div/div/div/div[3]/ul/li[2]/label/span[1]')

    # RUN MACHINE:
    M16_shut_down_machine_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M16_shut_down_machine_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M16_Chilled_Water_Flow_Switch_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M16_Chilled_Water_Flow_Switch_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M16_Cooling_Water_Flow_Switch_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M16_Cooling_Water_Flow_Switch_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M16_Pump_Interlocks_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    M16_Pump_Interlocks_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M16_GEN_Temperature_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[5]/div[3]/ul/li[1]/label/span')
    M16_GEN_Temperature_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[5]/div[3]/ul/li[2]/label/span[1]')
    M16_GEN_Pressure_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[6]/div[3]/ul/li[1]/label/span')
    M16_GEN_Pressure_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[6]/div[3]/ul/li[2]/label/span[1]')
    M16_LCWCO_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[7]/div[3]/ul/li[1]/label/span')
    M16_LCWCO_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[7]/div[3]/ul/li[2]/label/span[1]')

    # Initial Start:
    M16_Instruction_Manual_Values = 19
    M16_LiBr_Charged = 24
    M16_Refrigerant_Charged = 25
    M16_Solution_Pump_Rotation_and_Record_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    M16_Solution_Pump_Rotation_and_Record_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M16_Refrigerant_Pump_Rotation_and_Record_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[5]/div[3]/ul/li[1]/label/span')
    M16_Refrigerant_Pump_Rotation_and_Record_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[5]/div[3]/ul/li[2]/label/span[1]')
    M16_Pumps_and_Establish_Water_Flow_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[6]/div[3]/ul/li[1]/label/span')
    M16_Pumps_and_Establish_Water_Flow_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[6]/div[3]/ul/li[2]/label/span[1]')

    # Record Pressure Drop
    M17_M19XR_XRD_XRE_XRV_Default = (By.XPATH, '//*[@id="a"]')
    M17_M19XR_XRD_XRE_XRV_cooler = 19
    M17_M19XR_XRD_XRE_XRV_condenser = 32

    # Charge Refrigerant
    M17_M19XR_XRD_XRE_XRV_initial_charge = 33

    # Inspect Wiring & Record Electrical Data
    M17_M19XR_XRD_XRE_XRV_Motor_volt = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[1]/div/input')
    M17_M19XR_XRD_XRE_XRV_motor_amps = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[2]/div/input')
    M17_M19XR_XRD_XRE_XRV_oil_pump_volts = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[3]/div/input')
    M17_M19XR_XRD_XRE_XRV_LRA_rating = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[4]/div/input')
    M17_M19XR_XRD_XRE_XRV_line_volt = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[5]/div/input')
    M17_M19XR_XRD_XRE_XRV_oil_pump = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[6]/div/input')
    M17_M19XR_XRD_XRE_XRV_oil_heater = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[7]/div/input')

    # Pre-Start Checklist
    M17_M19XR_XRD_XRE_XRV_IMP = 34
    M17_M19XR_XRD_XRE_XRV_WMT_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_WMT_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M17_M19XR_XRD_XRE_XRV_leak_crted_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_leak_crted_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M17_M19XR_XRD_XRE_XRV_Mach_dehydrate_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_Mach_dehydrate_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')

    # Check Oil Level & Record
    M17_M19XR_XRD_XRE_XRV_Oil_sump_34 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[2]/label/span')
    M17_M19XR_XRD_XRE_XRV_Oil_sump_12 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[3]/label/span')
    M17_M19XR_XRD_XRE_XRV_Oil_sump_14 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[4]/label/span')
    M17_M19XR_XRD_XRE_XRV_Oil_sump_full = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[1]/label/span')
    M17_M19XR_XRD_XRE_XRV_Oil_sump_null = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[5]/label/span')
    M17_M19XR_XRD_XRE_XRV_strainer_housing_34 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[2]/label/span')
    M17_M19XR_XRD_XRE_XRV_strainer_housing_12 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[3]/label/span')
    M17_M19XR_XRD_XRE_XRV_strainer_housing_14 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[4]/label/span')
    M17_M19XR_XRD_XRE_XRV_strainer_housing_full = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[1]/label/span')
    M17_M19XR_XRD_XRE_XRV_strainer_housing_null = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[5]/label/span')
    M17_M19XR_XRD_XRE_XRV_add_oil_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_add_oil_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M17_M19XR_XRD_XRE_XRV_amount = 35

    # Control: Safety, Operating, Etc
    M17_M19XR_XRD_XRE_XRV_controls_test_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div/div/div/div/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_controls_test_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div/div/div/div/div[3]/ul/li[1]/label/span')

    # Pre-Start Check List
    M17_M19XR_XRD_XRE_XRV_condenser_water_pump_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_condenser_water_pump_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M17_M19XR_XRD_XRE_XRV_chilled_water_pump_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_chilled_water_pump_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M17_M19XR_XRD_XRE_XRV_condenser_water_flow_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_condenser_water_flow_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M17_M19XR_XRD_XRE_XRV_chilled_water_flow_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_chilled_water_flow_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    M17_M19XR_XRD_XRE_XRV_pump_interlocks_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[5]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_pump_interlocks_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[5]/div[3]/ul/li[1]/label/span')

    # Initialize Startup
    M17_M19XR_XRD_XRE_XRV_line_up_manual_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_line_up_manual_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M17_M19XR_XRD_XRE_XRV_start_WP_WF_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_start_WP_WF_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M17_M19XR_XRD_XRE_XRV_OL_OT_OK_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_OL_OT_OK_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M17_M19XR_XRD_XRE_XRV_check_oil_p_preassure_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_check_oil_p_preassure_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    M17_M19XR_XRD_XRE_XRV_check_comp_motor_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[5]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_check_comp_motor_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[5]/div[3]/ul/li[1]/label/span')
    M17_M19XR_XRD_XRE_XRV_clockwise_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[6]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_clockwise_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[6]/div[3]/ul/li[1]/label/span')
    M17_M19XR_XRD_XRE_XRV_restart_comp_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[7]/div[3]/ul/li[2]/label/span[1]')
    M17_M19XR_XRD_XRE_XRV_restart_comp_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[7]/div[3]/ul/li[1]/label/span')

    # 19 Model
    # Pre-Start Checklist
    M19PIC6_PIC5_Default = (By.XPATH, '//*[@id="a"]')
    M19PIC6_PIC5_IMP = 19
    M19PIC6_PIC5_WMT_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_WMT_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M19PIC6_PIC5_leak_crted_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_leak_crted_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M19PIC6_PIC5_Mach_dehydrate_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_Mach_dehydrate_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')

    # Check Oil Level & Record
    M19PIC6_PIC5_Oil_sump_34 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[2]/label/span')
    M19PIC6_PIC5_Oil_sump_12 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[3]/label/span')
    M19PIC6_PIC5_Oil_sump_14 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[4]/label/span')
    M19PIC6_PIC5_Oil_sump_full = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[1]/label/span')
    M19PIC6_PIC5_Oil_sump_null = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[5]/label/span')
    M19PIC6_PIC5_strainer_housing_34 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[2]/label/span')
    M19PIC6_PIC5_strainer_housing_12 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[3]/label/span')
    M19PIC6_PIC5_strainer_housing_14 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[4]/label/span')
    M19PIC6_PIC5_strainer_housing_full = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[1]/label/span')
    M19PIC6_PIC5_strainer_housing_null = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[5]/label/span')
    M19PIC6_PIC5_add_oil_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_add_oil_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M19PIC6_PIC5_amount = 32

    # Record Pressure Drop
    M19PIC6_PIC5_cooler = 33
    M19PIC6_PIC5_condenser = 34

    # Charge Refrigerant
    M19PIC6_PIC5_initial_charge = 35

    # Inspect Wiring & Record Electrical Data
    M19PIC6_PIC5_Motor_volt = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[1]/div/input')
    M19PIC6_PIC5_motor_amps = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[2]/div/input')
    M19PIC6_PIC5_oil_pump_volts = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[3]/div/input')
    M19PIC6_PIC5_LRS_rating = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[4]/div/input')
    M19PIC6_PIC5_line_volt = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[5]/div/input')
    M19PIC6_PIC5_oil_pump = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[6]/div/input')
    M19PIC6_PIC5_oil_heater = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[7]/div/input')

    # Record The Following Power On Checks:
    # Line Voltage:Phase-Phase
    M19PIC6_PIC5_phase_AB = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div[1]/div[1]/div/input')
    M19PIC6_PIC5_phase_BC = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div[1]/div[2]/div/input')
    M19PIC6_PIC5_phase_AC = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div[1]/div[3]/div/input')
    # Line Voltage:Phase-Ground
    M19PIC6_PIC5_ground_AG = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div[2]/div[1]/div/input')
    M19PIC6_PIC5_ground_BG = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div[2]/div[2]/div/input')
    M19PIC6_PIC5_ground_AG_ = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div[2]/div[3]/div/input')

    # Transformers Supplies Power Unit Information:
    M19PIC6_PIC5_delta_no_ground = 36
    M19PIC6_PIC5_delta_grounded = 37
    M19PIC6_PIC5_wye_centre_ground = 38
    M19PIC6_PIC5_wye_no_ground = 39
    M19PIC6_PIC5_transformer_size = 40

    # Control: Safety, Operating, Etc:
    M19PIC6_PIC5_Controls_test_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_Controls_test_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div/div[3]/ul/li[1]/label/span')

    # WATER/BRINE PUMP CONTROL: Can the carrier controls independently start the pumps?

    M19PIC6_PIC5_condenser_water_pump_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_condenser_water_pump_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M19PIC6_PIC5_chilled_water_pump_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_chilled_water_pump_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M19PIC6_PIC5_condenser_water_flow_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_condenser_water_flow_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M19PIC6_PIC5_chilled_water_flow_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_chilled_water_flow_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    M19PIC6_PIC5_pump_interlocks_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[5]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_pump_interlocks_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[5]/div[3]/ul/li[1]/label/span')

    # Initialize Startup
    M19PIC6_PIC5_line_up_manual_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_line_up_manual_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M19PIC6_PIC5_start_WP_WF_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_start_WP_WF_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M19PIC6_PIC5_OL_OT_OK_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_OL_OT_OK_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M19PIC6_PIC5_check_oil_p_preassure_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_check_oil_p_preassure_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    M19PIC6_PIC5_check_comp_motor_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[5]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_check_comp_motor_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[5]/div[3]/ul/li[1]/label/span')
    M19PIC6_PIC5_clockwise_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[6]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_clockwise_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[6]/div[3]/ul/li[1]/label/span')
    M19PIC6_PIC5_restart_comp_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[7]/div[3]/ul/li[2]/label/span[1]')
    M19PIC6_PIC5_restart_comp_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[7]/div[3]/ul/li[1]/label/span')

    # Pre-Start Checklist
    M19XL_Default = (By.XPATH, '//*[@id="a"]')
    M19XL_IMP = 19
    M19XL_WMT_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M19XL_WMT_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M19XL_leak_crted_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M19XL_leak_crted_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M19XL_Mach_dehydrate_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M19XL_Mach_dehydrate_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')

    # Check Oil Level & Record
    M19XL_Oil_sump_34 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[2]/label/span')
    M19XL_Oil_sump_12 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[3]/label/span')
    M19XL_Oil_sump_14 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[4]/label/span')
    M19XL_Oil_sump_full = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[1]/label/span')
    M19XL_Oil_sump_null = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[5]/label/span')
    M19XL_strainer_housing_34 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[2]/label/span')
    M19XL_strainer_housing_12 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[3]/label/span')
    M19XL_strainer_housing_14 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[4]/label/span')
    M19XL_strainer_housing_full = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[1]/label/span')
    M19XL_strainer_housing_null = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[5]/label/span')
    M19XL_add_oil_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M19XL_add_oil_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M19XL_amount = 32

    # Record Pressure Drop
    M19XL_cooler = 33
    M19XL_condenser = 34

    # Charge Refrigerant
    M19XL_initial_charge = 35
    M19XL_final_charge = 36

    # Inspect Wiring & Record Electrical Data
    M19XL_Motor_volt = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[1]/div/input')
    M19XL_motor_amps = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[2]/div/input')
    M19XL_oil_pump_volts = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[3]/div/input')
    M19XL_LRS_rating = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[4]/div/input')
    M19XL_line_volt = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[5]/div/input')
    M19XL_oil_pump = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[6]/div/input')
    M19XL_oil_heater = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[7]/div/input')

    # FIELD-INSTALLED STARTERS ONLY:
    M19XL_field_starters_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div[1]/ul/li/label/span')
    M19XL_field_starters_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div[2]/ul/li/label/span')

    # STARTER: Electro-Mechanical Solid-State
    M19XL_manufacturer = 37
    M19XL_serial_no = 38
    M19XL_motor_load_ratio = 39
    M19XL_signal_res = 40
    M19XL_transition_time = 41
    M19XL_add_dash_pot_oil_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[6]/div[3]/ul/li[2]/label/span[1]')
    M19XL_add_dash_pot_oil_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[6]/div[3]/ul/li[1]/label/span')
    M19XL_solid_state_overloads_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[7]/div[3]/ul/li[2]/label/span[1]')
    M19XL_solid_state_overloads_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[7]/div[3]/ul/li[1]/label/span')

    # Solid State Starter:
    M19XL_torque_setting = 46
    M19XL_ramp_setting = 47

    # Control: Safety, Operating, Etc:
    M19XL_Controls_test_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div/div[3]/ul/li[2]/label/span[1]')
    M19XL_Controls_test_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div/div[3]/ul/li[1]/label/span')

    # WATER/BRINE PUMP CONTROL: Can the carrier controls independently start the pumps?
    M19XL_condenser_water_flow_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M19XL_condenser_water_flow_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M19XL_chilled_water_flow_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M19XL_chilled_water_flow_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M19XL_pump_interlocks_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M19XL_pump_interlocks_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')

    # Initialize Startup
    M19XL_line_up_manual_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M19XL_line_up_manual_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M19XL_start_WP_WF_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M19XL_start_WP_WF_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M19XL_OL_OT_OK_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M19XL_OL_OT_OK_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M19XL_check_oil_p_preassure_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M19XL_check_oil_p_preassure_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    M19XL_check_comp_motor_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[5]/div[3]/ul/li[2]/label/span[1]')
    M19XL_check_comp_motor_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[5]/div[3]/ul/li[1]/label/span')
    M19XL_clockwise_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[6]/div[3]/ul/li[2]/label/span[1]')
    M19XL_clockwise_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[6]/div[3]/ul/li[1]/label/span')
    M19XL_restart_comp_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[7]/div[3]/ul/li[2]/label/span[1]')
    M19XL_restart_comp_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[7]/div[3]/ul/li[1]/label/span')

    # Pre-Start Checklist
    M23XL_Default = (By.XPATH, '//*[@id="a"]')
    M23XL_IMP = 19
    M23XL_WMT_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M23XL_WMT_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M23XL_leak_crted_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M23XL_leak_crted_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M23XL_Mach_dehydrate_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M23XL_Mach_dehydrate_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')

    # Check Oil Level & Record
    M23XL_Oil_sump_34 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[2]/label/span')
    M23XL_Oil_sump_12 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[3]/label/span')
    M23XL_Oil_sump_14 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[4]/label/span')
    M23XL_Oil_sump_full = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[1]/label/span')
    M23XL_Oil_sump_null = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[5]/label/span')
    M23XL_strainer_housing_34 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[2]/label/span')
    M23XL_strainer_housing_12 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[3]/label/span')
    M23XL_strainer_housing_14 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[4]/label/span')
    M23XL_strainer_housing_full = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[1]/label/span')
    M23XL_strainer_housing_null = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[5]/label/span')
    M23XL_add_oil_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M23XL_add_oil_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M23XL_amount = 32

    # Record Pressure Drop
    M23XL_cooler = 33
    M23XL_condenser = 34

    # Charge Refrigerant
    M23XL_initial_charge = 35
    M23XL_final_charge = 36

    # FIELD-INSTALLED STARTERS ONLY:
    M23XL_field_starters_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[7]/div/div/div[2]/ul/li/label/span')
    M23XL_field_starters_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[7]/div/div/div[1]/ul/li/label/span')

    # STARTER:
    M23XL_electro_mech_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M23XL_electro_mech_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M23XL_solid_state_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M23XL_solid_state_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M23XL_manufaturer = 41
    M23XL_serial_no = 42
    M23XL_motor_load_ratio = 43
    M23XL_solid_state_overloads_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[6]/div[3]/ul/li[2]/label/span[1]')
    M23XL_solid_state_overloads_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[6]/div[3]/ul/li[1]/label/span')

    # Control: Safety, Operating, Etc
    M23XL_controls_test_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[9]/div/div/div/div/div/div/div[3]/ul/li[2]/label/span[1]')
    M23XL_controls_test_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[9]/div/div/div/div/div/div/div[3]/ul/li[1]/label/span')

    # RUN MACHINE: Do these safeties shut down machine?
    M23XL_condenser_water_flow_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M23XL_condenser_water_flow_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M23XL_chilled_water_flow_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M23XL_chilled_water_flow_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M23XL_pump_interlocks_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M23XL_pump_interlocks_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')

    # INITIAL START
    M23XL_line_up_manual_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M23XL_line_up_manual_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M23XL_start_WP_WF_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M23XL_start_WP_WF_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M23XL_OL_OT_OK_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M23XL_OL_OT_OK_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M23XL_oil_preassure_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M23XL_oil_preassure_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    M23XL_restart_comp_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[5]/div[3]/ul/li[2]/label/span[1]')
    M23XL_restart_comp_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[3]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[5]/div[3]/ul/li[1]/label/span')

    # 23XRV
    # Pre-Start Checklist
    M23_XRV_Default = (By.XPATH, '//*[@id="a"]')
    M23_XRV_IMP = 19
    M23_XRV_WMT_yes = (By.XPATH,
                       '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_WMT_no = (By.XPATH,
                      '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M23_XRV_leak_crted_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_leak_crted_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M23_XRV_Mach_dehydrate_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_Mach_dehydrate_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')

    # Check Oil Level & Record
    M23_XRV_Oil_sump_34 = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[2]/label/span')
    M23_XRV_Oil_sump_12 = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[3]/label/span')
    M23_XRV_Oil_sump_14 = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[4]/label/span')
    M23_XRV_Oil_sump_full = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[1]/label/span')
    M23_XRV_Oil_sump_null = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[5]/label/span')
    M23_XRV_strainer_housing_34 = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[2]/label/span')
    M23_XRV_strainer_housing_12 = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[3]/label/span')
    M23_XRV_strainer_housing_14 = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[4]/label/span')
    M23_XRV_strainer_housing_full = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[1]/label/span')
    M23_XRV_strainer_housing_null = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[5]/label/span')
    M23_XRV_add_oil_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_add_oil_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M23_XRV_amount = 41

    # Record Pressure Drop
    M23_XRV_cooler = 42
    M23_XRV_condenser = 43

    # Charge Refrigerant
    M23_XRV_initial_charge = 44

    # Inspect Wiring & Record Electrical Data:
    M23_XRV_6inch_clearance_yes = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_6inch_clearance_no = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M23_XRV_inspenct_debries_yes = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_inspenct_debries_no = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')

    # Inspect Wiring & Record Electrical Data
    M23_XRV_Motor_volt = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div/div/div[1]/div/input')
    M23_XRV_motor_amps = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div/div/div[2]/div/input')
    M23_XRV_oil_pump_volts = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div/div/div[3]/div/input')
    M23_XRV_LRS_rating = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div/div/div[4]/div/input')
    M23_XRV_line_volt = (By.XPATH,
                         '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div/div/div[5]/div/input')
    M23_XRV_oil_pump = (By.XPATH,
                        '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div/div/div[6]/div/input')
    M23_XRV_oil_heater = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div/div/div[7]/div/input')

    # Record The Following Power On Checks:
    # Line Voltage:Phase-Phase
    M23_XRV_phase_AB = (By.XPATH,
                        '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div[1]/div[1]/div/input')
    M23_XRV_phase_BC = (By.XPATH,
                        '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div[1]/div[2]/div/input')
    M23_XRV_phase_AC = (By.XPATH,
                        '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div[1]/div[3]/div/input')
    # Line Voltage:Phase-Ground
    M23_XRV_ground_AG = (By.XPATH,
                         '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div[2]/div[1]/div/input')
    M23_XRV_ground_BG = (By.XPATH,
                         '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div[2]/div[2]/div/input')
    M23_XRV_ground_AG_ = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div[2]/div[3]/div/input')

    # Transformers Supplies Power Unit Information:
    M23_XRV_delta_no_ground = 32
    M23_XRV_delta_grounded = 33
    M23_XRV_wye_centre_ground = 34
    M23_XRV_wye_no_ground = 35
    M23_XRV_transformer_size = 40

    # Is this a field disassembled chiller?
    M23_XRV_Disassenble_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div[2]/ul/li/label/span')
    M23_XRV_Disassenble_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div[1]/ul/li/label/span')

    # Control:Safety,Operating, Etc:
    M23_XRV_verify_VFD_params_yes = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_verify_VFD_params_no = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M23_XRV_control_test_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_control_test_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')

    # WATER/BRINE PUMP CONTROL: Can the carrier controls independently start the pumps?
    M23_XRV_condenser_liq_pump_yes = (By.XPATH,
                                      '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_condenser_liq_pump_no = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M23_XRV_chilled_liq_pump_yes = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_chilled_liq_pump_no = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[12]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')

    # Isolation Valves
    M23_XRV_discharge_muffer_yes = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_discharge_muffer_no = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M23_XRV_cooler_inlet_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_cooler_inlet_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M23_XRV_hot_gas_bypass_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_hot_gas_bypass_no = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M23_XRV_vapourize_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_vapourize_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    M23_XRV_oil_pump_yes = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[5]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_oil_pump_no = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[5]/div[3]/ul/li[1]/label/span')
    M23_XRV_oil_filter_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[6]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_oil_filter_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[6]/div[3]/ul/li[1]/label/span')
    M23_XRV_oil_pressure_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[7]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_oil_pressure_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[7]/div[3]/ul/li[1]/label/span')
    M23_XRV_filter_next_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[8]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_filter_next_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[8]/div[3]/ul/li[1]/label/span')
    M23_XRV_filte_under_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[9]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_filte_under_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[9]/div[3]/ul/li[1]/label/span')
    M23_XRV_VFD_under_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[10]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_VFD_under_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[10]/div[3]/ul/li[1]/label/span')
    M23_XRV_VFD_between_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[11]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_VFD_between_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[13]/div/div/div/div/div/div[11]/div[3]/ul/li[1]/label/span')

    # Relief Valve Three-Way Valves
    M23_XRV_cooler_seated_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[14]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_cooler_seated_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[14]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M23_XRV_condenser_seated_yes = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[14]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_condenser_seated_no = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[14]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')

    # Service Valves
    M23_XRV_cooler_tree_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[15]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_cooler_tree_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[15]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M23_XRV_cooler_pumpour_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[15]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_cooler_pumpour_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[15]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M23_XRV_condenser_tree_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[15]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_condenser_tree_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[15]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M23_XRV_condenser_chanber_yes = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[15]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_condenser_chanber_no = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[15]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    M23_XRV_oil_sump_yes = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[15]/div/div/div/div/div/div[5]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_oil_sump_no = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[15]/div/div/div/div/div/div[5]/div[3]/ul/li[1]/label/span')

    # Initialize Startup
    M23_XRV_start_flow_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[16]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_start_flow_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[16]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M23_XRV_oil_level_ok_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[16]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_oil_level_ok_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[16]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M23_XRV_oil_preassure_ok_yes = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[16]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_oil_preassure_ok_no = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[16]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M23_XRV_restart_comp_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[16]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M23_XRV_restart_comp_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[16]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')


    # 32XR
    # Pre-Start Checklist
    M32XR_Default = (By.XPATH, '//*[@id="a"]')
    M32XR_IMP = 19
    M32XR_WMT_yes = (By.XPATH,
                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M32XR_WMT_no = (By.XPATH,
                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M32XR_leak_crted_yes = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M32XR_leak_crted_no = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M32XR_Mach_dehydrate_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M32XR_Mach_dehydrate_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')

    # Check Oil Level & Record
    M32XR_Oil_sump_34 = (By.XPATH,
                         '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[2]/label/span')
    M32XR_Oil_sump_12 = (By.XPATH,
                         '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[3]/label/span')
    M32XR_Oil_sump_14 = (By.XPATH,
                         '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[4]/label/span')
    M32XR_Oil_sump_full = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[1]/label/span')
    M32XR_Oil_sump_null = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[5]/label/span')
    M32XR_strainer_housing_34 = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[2]/label/span')
    M32XR_strainer_housing_12 = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[3]/label/span')
    M32XR_strainer_housing_14 = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[4]/label/span')
    M32XR_strainer_housing_full = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[1]/label/span')
    M32XR_strainer_housing_null = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[5]/label/span')
    M32XR_add_oil_yes = (By.XPATH,
                         '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M32XR_add_oil_no = (By.XPATH,
                        '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M32XR_amount = 32

    # Record Pressure Drop
    M32XR_cooler = 33
    M32XR_condenser = 34

    # Charge Refrigerant
    M32XR_initial_charge = 35
    M32XR_final_charge = 36

    # Inspect Wiring & Record Electrical Data
    M32XR_Motor_volt = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[1]/div/input')
    M32XR_motor_amps = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[2]/div/input')
    M32XR_oil_pump_volts = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[3]/div/input')
    M32XR_LRS_rating = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[4]/div/input')
    M32XR_line_volt = (By.XPATH,
                         '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[5]/div/input')
    M32XR_oil_pump = (By.XPATH,
                        '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[6]/div/input')
    M32XR_oil_heater = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[7]/div/input')

    # FIELD-INSTALLED STARTERS ONLY:
    M32XR_startes_installed_yes = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div[2]/ul/li/label/span')
    M32XR_startes_installed_no = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[7]/div/div/div[1]/ul/li/label/span')

    # STARTER:
    M32XR_electro_mech_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M32XR_electro_mech_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M32XR_solid_state_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M32XR_solid_state_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M32XR_manufaturer = 43
    M32XR_serial_no = 44
    M32XR_motor_load_ratio = 45
    M32XR_res_size = 46
    M32XR_transistion_time = 47
    M32XR_magnetic_overloads = 48
    M32XR_add_dash_pot_oil_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[10]/div[3]/ul/li[2]/label/span[1]')
    M32XR_add_dash_pot_oil_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[10]/div[3]/ul/li[1]/label/span')
    M32XR_solid_state_overloads_yes = (By.XPATH,
                                       '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[11]/div[3]/ul/li[2]/label/span[1]')
    M32XR_solid_state_overloads_no = (By.XPATH,
                                      '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[11]/div[3]/ul/li[1]/label/span')

    # Control: Safety, Operating, Etc
    M32XR_controls_test_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div/div[3]/ul/li[2]/label/span[1]')
    M32XR_controls_test_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div/div[3]/ul/li[1]/label/span')

    # RUN MACHINE: Do these safeties shut down machine?
    M32XR_condenser_water_flow_yes = (By.XPATH,
                                      '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M32XR_condenser_water_flow_no = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M32XR_chilled_water_flow_yes = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M32XR_chilled_water_flow_no = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M32XR_pump_interlocks_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M32XR_pump_interlocks_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[10]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')

    # INITIAL START
    M32XR_line_up_manual_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    M32XR_line_up_manual_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    M32XR_start_WP_WF_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    M32XR_start_WP_WF_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    M32XR_OL_OT_OK_yes = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    M32XR_OL_OT_OK_no = (By.XPATH,
                         '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    M32XR_oil_preassure_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    M32XR_oil_preassure_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    M32XR_restart_comp_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[5]/div[3]/ul/li[2]/label/span[1]')
    M32XR_restart_comp_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div[11]/div/div/div/div/div/div[5]/div[3]/ul/li[1]/label/span')

    # 38AU
    # OUTDOOR UNIT
    M38AU_shipping_damage_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[3]/ul[1]/li[2]/label/span')
    M38AU_shipping_damage_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[3]/ul[1]/li[1]/label/span')
    M38AU_damage_prevent_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[3]/ul[1]/li[2]/label/span')
    M38AU_damage_prevent_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[3]/ul[1]/li[1]/label/span')
    M38AU_power_supply_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div[3]/ul[1]/li[2]/label/span')
    M38AU_power_supply_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div[3]/ul[1]/li[1]/label/span')
    M38AU_ground_conn_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[5]/div[3]/ul[1]/li[2]/label/span')
    M38AU_ground_conn_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[5]/div[3]/ul[1]/li[1]/label/span')
    M38AU_circiut_protect_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[6]/div[3]/ul[1]/li[2]/label/span')
    M38AU_circiut_protect_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[6]/div[3]/ul[1]/li[1]/label/span')
    M38AU_power_wires_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[7]/div[3]/ul[1]/li[2]/label/span')
    M38AU_power_wires_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[7]/div[3]/ul[1]/li[1]/label/span')

    # CONTROLS
    M38AU_thermostats_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[3]/div/div/div/div/div[1]/div[3]/ul[1]/li[2]/label/span')
    M38AU_thermostats_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[3]/div/div/div/div/div[1]/div[3]/ul[1]/li[1]/label/span')
    M38AU_terminals_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[3]/div/div/div/div/div[2]/div[3]/ul[1]/li[2]/label/span')
    M38AU_terminals_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[3]/div/div/div/div/div[2]/div[3]/ul[1]/li[1]/label/span')
    M38AU_crankcase_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/ul[1]/li[2]/label/span')
    M38AU_crankcase_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/ul[1]/li[1]/label/span')

    # INDOOR UNIT
    M38AU_drainage_yes = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[4]/div/div/div/div/div[1]/div[3]/ul[1]/li[2]/label/span')
    M38AU_drainage_no = (By.XPATH,
                         '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[4]/div/div/div/div/div[1]/div[3]/ul[1]/li[1]/label/span')
    M38AU_air_filters_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[4]/div/div/div/div/div[2]/div[3]/ul[1]/li[2]/label/span')
    M38AU_air_filters_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[4]/div/div/div/div/div[2]/div[3]/ul[1]/li[1]/label/span')
    M38AU_fan_motor_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[4]/div/div/div/div/div[3]/div[3]/ul[1]/li[2]/label/span')
    M38AU_fan_motor_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[4]/div/div/div/div/div[3]/div[3]/ul[1]/li[1]/label/span')
    M38AU_fan_belts_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[4]/div/div/div/div/div[4]/div[3]/ul[1]/li[2]/label/span')
    M38AU_fan_belts_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[4]/div/div/div/div/div[4]/div[3]/ul[1]/li[1]/label/span')
    M38AU_fan_rotation_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[4]/div/div/div/div/div[5]/div[3]/ul[1]/li[2]/label/span')
    M38AU_fan_rotation_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[4]/div/div/div/div/div[5]/div[3]/ul[1]/li[1]/label/span')

    # PIPING
    M38AU_solenoid_req_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[5]/div/div/div/div/div[1]/div[3]/ul[1]/li[2]/label/span')
    M38AU_solenoid_req_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[5]/div/div/div/div/div[1]/div[3]/ul[1]/li[1]/label/span')
    M38AU_leak_chck_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[5]/div/div/div/div/div[2]/div[3]/ul[1]/li[2]/label/span')
    M38AU_leak_chck_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[5]/div/div/div/div/div[2]/div[3]/ul[1]/li[1]/label/span')
    M38AU_line_open_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[5]/div/div/div/div/div[4]/div[3]/ul[1]/li[2]/label/span')
    M38AU_line_open_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[5]/div/div/div/div/div[4]/div[3]/ul[1]/li[1]/label/span')
    M38AU_vapour_line_open_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[5]/div/div/div/div/div[5]/div[3]/ul[1]/li[2]/label/span')
    M38AU_vapour_line_open_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[5]/div/div/div/div/div[5]/div[3]/ul[1]/li[1]/label/span')

    # CHECK VOLTAGE IMBALANCE
    M38AU_Line_voltsAB = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[6]/div/div/div[1]/div[1]/div/div/input')
    M38AU_Line_voltsAC = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[6]/div/div/div[1]/div[2]/div/div/input')
    M38AU_Line_voltsBC = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[6]/div/div/div[1]/div[3]/div/div/input')
    M38AU_avg_volts = (By.XPATH,
                       '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[6]/div/div/div[2]/div/div/div/input')
    M38AU_max_avg_volts = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[6]/div/div/div[3]/div/div/div/input')
    M38AU_volts_imbalacne = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[6]/div/div/div[4]/div/div/div/input')
    M38AU_Default = (By.XPATH, '//*[@id="a"]')
    M38AU_indoor_fan_speed = 36
    M38AU_outdoor_fan_speen = 37
    M38AU_vapour_pressure_cooling = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[1]/div[1]/div/div/input')
    M38AU_suc_temp_cooling = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[2]/div[1]/div/div/input')
    M38AU_liq_pressure_cooling = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[3]/div[1]/div/div/input')
    M38AU_liq_temp_cooling = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[4]/div[1]/div/div/input')
    M38AU_entering_outdoor_ait_temp_cooling = (By.XPATH,
                                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[5]/div[1]/div/div/input')
    M38AU_leaving_outdoor_air_temp_cooling = (By.XPATH,
                                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[6]/div[1]/div/div/input')
    M38AU_dry_air_DB_temp_cooling = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[7]/div[1]/div/div/input')
    M38AU_wet_air_DB_temp_cooling = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[8]/div[1]/div/div/input')
    M38AU_air_DB_temp_cooling = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[9]/div[1]/div/div/input')
    M38AU_air_WB_temp_cooling = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[10]/div[1]/div/div/input')
    M38AU_vapour_pressure_heating = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[1]/div[2]/div/div/input')
    M38AU_suc_temp_heating = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[2]/div[2]/div/div/input')
    M38AU_liq_pressure_heating = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[3]/div[2]/div/div/input')
    M38AU_liq_temp_heating = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[4]/div[2]/div/div/input')
    M38AU_entering_outdoor_ait_temp_heating = (By.XPATH,
                                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[5]/div[2]/div/div/input')
    M38AU_leaving_outdoor_air_temp_heating = (By.XPATH,'//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[6]/div[2]/div/div/input')
    M38AU_dry_air_DB_temp_heating = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[7]/div[2]/div/div/input')
    M38AU_wet_air_DB_temp_heating = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[8]/div[2]/div/div/input')
    M38AU_air_DB_temp_heating = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[9]/div[2]/div/div/input')
    M38AU_air_WB_temp_heating = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[10]/div[2]/div/div/input')
    M38AU_comp_amps_l1 = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[11]/div[1]/div/div/input')
    M38AU_comp_amps_l2 = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[11]/div[2]/div/div/input')
    M38AU_comp_amps_l3 = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div/div[2]/div/div/div/div[8]/div/div/div[11]/div[3]/div/div/input')

    #39MN
    # CONTROLS
    M39MN_thermostats_checked_yes = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_thermostats_checked_no = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_wire_termonals_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_wire_termonals_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[1]/label/span')

    # AIR HANDLER
    M39MN_remove_debris_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_remove_debris_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_inspect_damage_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_inspect_damage_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_inspect_flanges_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_inspect_flanges_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_caulk_yes = (By.XPATH,
                       '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_caulk_no = (By.XPATH,
                      '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_door_latches_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_door_latches_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_release_fan_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[6]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_release_fan_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[6]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_check_fan_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[7]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_check_fan_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[7]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_hand_turn_fan_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[8]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_hand_turn_fan_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[8]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_fan_alliengment_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[9]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_fan_alliengment_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[9]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_fan_tension_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[10]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_fan_tension_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[10]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_proper_filters_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[11]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_proper_filters_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[11]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_wiring_terminals_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[12]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_wiring_terminals_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[12]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_drain_pan_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[13]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_drain_pan_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[13]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_duct_connected_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[14]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_duct_connected_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[14]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_verify_wiring_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[15]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_verify_wiring_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[15]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_field_wiring_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[16]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_field_wiring_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[16]/div[2]/div[2]/ul[1]/li[1]/label/span')

    # PIPING
    M39MN_leak_checks_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_leak_checks_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_air_blend_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_air_blend_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_freeze_protection_yes = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_freeze_protection_no = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MN_DXsystem_yes = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MN_DXsystem_no = (By.XPATH,
                         '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[1]/label/span')

    # 39MW
    # CONTROLS
    M39MW_indoor_fan_yes = (By.XPATH,
               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_indoor_fan_no = (By.XPATH,
              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_wire_termonals_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_wire_termonals_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[1]/label/span')

    # AIR HANDLER
    M39MW_remove_debris_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_remove_debris_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_inspect_damage_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_inspect_damage_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_inspect_flanges_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_inspect_flanges_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_caulk_yes = (By.XPATH,
                       '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_caulk_no = (By.XPATH,
                      '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_door_latches_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_door_latches_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[1]/label/span')

    M39MW_roof_joint1_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div[1]/div/div/ul/li[2]/label/span')
    M39MW_roof_joint2_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div[2]/div/div/ul/li[2]/label/span')
    M39MW_roof_joint3_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div[3]/div/div/ul/li[2]/label/span')
    M39MW_roof_joint4_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div[4]/div/div/ul/li[2]/label/span')
    M39MW_roof_joint5_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div[5]/div/div/ul/li[2]/label/span')
    M39MW_roof_joint6_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div[6]/div/div/ul/li[2]/label/span')
    M39MW_roojoint_joint1_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[5]/div/div/div/div[1]/div/div/ul/li[2]/label/span')
    M39MW_roojoint_joint2_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[5]/div/div/div/div[2]/div/div/ul/li[2]/label/span')
    M39MW_roojoint_joint3_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[5]/div/div/div/div[3]/div/div/ul/li[2]/label/span')
    M39MW_roojoint_joint4_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[5]/div/div/div/div[4]/div/div/ul/li[2]/label/span')
    M39MW_roojoint_joint5_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[5]/div/div/div/div[5]/div/div/ul/li[2]/label/span')
    M39MW_roojoint_joint6_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[5]/div/div/div/div[6]/div/div/ul/li[2]/label/span')
    M39MW_bolted_joint1_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div[1]/div/div/ul/li[2]/label/span')
    M39MW_bolted_joint2_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div[2]/div/div/ul/li[2]/label/span')
    M39MW_bolted_joint3_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div[3]/div/div/ul/li[2]/label/span')
    M39MW_bolted_joint4_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div[4]/div/div/ul/li[2]/label/span')
    M39MW_bolted_joint5_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div[5]/div/div/ul/li[2]/label/span')
    M39MW_bolted_joint6_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div[6]/div/div/ul/li[2]/label/span')
    M39MW_tightened_joint1_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[7]/div/div/div/div[1]/div/div/ul/li[2]/label/span')
    M39MW_tightened_joint2_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[7]/div/div/div/div[2]/div/div/ul/li[2]/label/span')
    M39MW_tightened_joint3_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[7]/div/div/div/div[3]/div/div/ul/li[2]/label/span')
    M39MW_tightened_joint4_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[7]/div/div/div/div[4]/div/div/ul/li[2]/label/span')
    M39MW_tightened_joint5_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[7]/div/div/div/div[5]/div/div/ul/li[2]/label/span')
    M39MW_tightened_joint6_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[7]/div/div/div/div[6]/div/div/ul/li[2]/label/span')
    M39MW_gasketed_joint1_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[8]/div/div/div/div[1]/div/div/ul/li[2]/label/span')
    M39MW_gasketed_joint2_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[8]/div/div/div/div[2]/div/div/ul/li[2]/label/span')
    M39MW_gasketed_joint3_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[8]/div/div/div/div[3]/div/div/ul/li[2]/label/span')
    M39MW_gasketed_joint4_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[8]/div/div/div/div[4]/div/div/ul/li[2]/label/span')
    M39MW_gasketed_joint5_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[8]/div/div/div/div[5]/div/div/ul/li[2]/label/span')
    M39MW_gasketed_joint6_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[8]/div/div/div/div[6]/div/div/ul/li[2]/label/span')
    M39MW_seam_joint1_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[9]/div/div/div/div[1]/div/div/ul/li[2]/label/span')
    M39MW_seam_joint2_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[9]/div/div/div/div[2]/div/div/ul/li[2]/label/span')
    M39MW_seam_joint3_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[9]/div/div/div/div[3]/div/div/ul/li[2]/label/span')

    M39MW_seam_joint4_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[9]/div/div/div/div[4]/div/div/ul/li[2]/label/span')
    M39MW_seam_joint5_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[9]/div/div/div/div[5]/div/div/ul/li[2]/label/span')
    M39MW_seam_joint6_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[9]/div/div/div/div[6]/div/div/ul/li[2]/label/span')
    M39MW_bracket_CCH1_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[10]/div/div/div/div[1]/div/div/ul/li[2]/label/span')
    M39MW_bracket_CCH2_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[10]/div/div/div/div[2]/div/div/ul/li[2]/label/span')
    M39MW_bracket_CCH3_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[10]/div/div/div/div[3]/div/div/ul/li[2]/label/span')
    M39MW_flashings_CCH1_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[11]/div/div/div/div[1]/div/div/ul/li[2]/label/span')
    M39MW_flashings_CCH2_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[11]/div/div/div/div[2]/div/div/ul/li[2]/label/span')
    M39MW_flashings_CCH3_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[11]/div/div/div/div[3]/div/div/ul/li[2]/label/span')
    M39MW_CCH_CCH1_yes = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[12]/div/div/div/div[1]/div/div/ul/li[2]/label/span')
    M39MW_CCH_CCH2_yes = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[12]/div/div/div/div[2]/div/div/ul/li[2]/label/span')
    M39MW_CCH_CCH3_yes = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[12]/div/div/div/div[3]/div/div/ul/li[2]/label/span')
    M39MW_roof_joint1_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div[1]/div/div/ul/li[1]/label/span')
    M39MW_roof_joint2_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div[2]/div/div/ul/li[1]/label/span')
    M39MW_roof_joint3_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div[3]/div/div/ul/li[1]/label/span')
    M39MW_roof_joint4_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div[4]/div/div/ul/li[1]/label/span')
    M39MW_roof_joint5_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div[5]/div/div/ul/li[1]/label/span')
    M39MW_roof_joint6_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[4]/div/div/div/div[6]/div/div/ul/li[1]/label/span')
    M39MW_roojoint_joint1_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[5]/div/div/div/div[1]/div/div/ul/li[1]/label/span')
    M39MW_roojoint_joint2_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[5]/div/div/div/div[2]/div/div/ul/li[1]/label/span')
    M39MW_roojoint_joint3_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[5]/div/div/div/div[3]/div/div/ul/li[1]/label/span')
    M39MW_roojoint_joint4_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[5]/div/div/div/div[4]/div/div/ul/li[1]/label/span')
    M39MW_roojoint_joint5_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[5]/div/div/div/div[5]/div/div/ul/li[1]/label/span')
    M39MW_roojoint_joint6_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[5]/div/div/div/div[6]/div/div/ul/li[1]/label/span')
    M39MW_bolted_joint1_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div[1]/div/div/ul/li[1]/label/span')
    M39MW_bolted_joint2_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div[2]/div/div/ul/li[1]/label/span')
    M39MW_bolted_joint3_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div[3]/div/div/ul/li[1]/label/span')
    M39MW_bolted_joint4_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div[4]/div/div/ul/li[1]/label/span')
    M39MW_bolted_joint5_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div[5]/div/div/ul/li[1]/label/span')
    M39MW_bolted_joint6_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div[6]/div/div/ul/li[1]/label/span')
    M39MW_tightened_joint1_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[7]/div/div/div/div[1]/div/div/ul/li[1]/label/span')
    M39MW_tightened_joint2_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[7]/div/div/div/div[2]/div/div/ul/li[1]/label/span')
    M39MW_tightened_joint3_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[7]/div/div/div/div[3]/div/div/ul/li[1]/label/span')
    M39MW_tightened_joint4_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[7]/div/div/div/div[4]/div/div/ul/li[1]/label/span')
    M39MW_tightened_joint5_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[7]/div/div/div/div[5]/div/div/ul/li[1]/label/span')
    M39MW_tightened_joint6_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[7]/div/div/div/div[6]/div/div/ul/li[1]/label/span')
    M39MW_gasketed_joint1_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[8]/div/div/div/div[1]/div/div/ul/li[1]/label/span')
    M39MW_gasketed_joint2_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[8]/div/div/div/div[2]/div/div/ul/li[1]/label/span')
    M39MW_gasketed_joint3_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[8]/div/div/div/div[3]/div/div/ul/li[1]/label/span')
    M39MW_gasketed_joint4_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[8]/div/div/div/div[4]/div/div/ul/li[1]/label/span')
    M39MW_gasketed_joint5_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[8]/div/div/div/div[5]/div/div/ul/li[1]/label/span')
    M39MW_gasketed_joint6_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[8]/div/div/div/div[6]/div/div/ul/li[1]/label/span')
    M39MW_seam_joint1_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[9]/div/div/div/div[1]/div/div/ul/li[1]/label/span')
    M39MW_seam_joint2_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[9]/div/div/div/div[2]/div/div/ul/li[1]/label/span')
    M39MW_seam_joint3_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[9]/div/div/div/div[3]/div/div/ul/li[1]/label/span')
    M39MW_seam_joint4_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[9]/div/div/div/div[4]/div/div/ul/li[1]/label/span')
    M39MW_seam_joint5_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[9]/div/div/div/div[5]/div/div/ul/li[1]/label/span')
    M39MW_seam_joint6_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[9]/div/div/div/div[6]/div/div/ul/li[1]/label/span')
    M39MW_bracket_CCH1_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[10]/div/div/div/div[1]/div/div/ul/li[1]/label/span')
    M39MW_bracket_CCH2_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[10]/div/div/div/div[2]/div/div/ul/li[1]/label/span')
    M39MW_bracket_CCH3_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[10]/div/div/div/div[3]/div/div/ul/li[1]/label/span')
    M39MW_flashings_CCH1_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[11]/div/div/div/div[1]/div/div/ul/li[1]/label/span')
    M39MW_flashings_CCH2_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[11]/div/div/div/div[2]/div/div/ul/li[1]/label/span')
    M39MW_flashings_CCH3_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[11]/div/div/div/div[3]/div/div/ul/li[1]/label/span')
    M39MW_CCH_CCH1_no = (By.XPATH,
                         '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[12]/div/div/div/div[1]/div/div/ul/li[1]/label/span')
    M39MW_CCH_CCH2_no = (By.XPATH,
                         '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[12]/div/div/div/div[2]/div/div/ul/li[1]/label/span')
    M39MW_CCH_CCH3_no = (By.XPATH,
                         '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[12]/div/div/div/div[3]/div/div/ul/li[1]/label/span')

    M39MW_release_fan_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_release_fan_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_check_fan_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_check_fan_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_fan_bearings_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_fan_bearings_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_hand_turn_fan_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_hand_turn_fan_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_fan_alliengment_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_fan_alliengment_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_fan_tension_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[6]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_fan_tension_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[6]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_proper_filters_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[7]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_proper_filters_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[7]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_wiring_terminals_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[8]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_wiring_terminals_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[8]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_drain_pan_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[9]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_drain_pan_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[9]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_duct_connected_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[10]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_duct_connected_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[10]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_verify_wiring_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[11]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_verify_wiring_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[11]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_field_wiring_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[12]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_field_wiring_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[13]/div/div/div/div/div[12]/div[2]/div[2]/ul[1]/li[1]/label/span')

    # PIPING
    M39MW_leak_checks_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[14]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_leak_checks_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[14]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_air_blend_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[14]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_air_blend_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[14]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_freeze_protection_yes = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[14]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_freeze_protection_no = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[14]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M39MW_DXsystem_yes = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[14]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M39MW_DXsystem_no = (By.XPATH,
                         '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[14]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[1]/label/span')

    # 48A2
    M48A2_M48A3_M50A3_verify_packaging_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48A2_M48A3_M50A3_remove_comp_bolts_yes = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48A2_M48A3_M50A3_verify_economizer_yes = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48A2_M48A3_M50A3_verify_options_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48A2_M48A3_M50A3_verify_transducers_yes = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48A2_M48A3_M50A3_verify_terminals_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[6]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48A2_M48A3_M50A3_verify_sensors_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[7]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48A2_M48A3_M50A3_check_gas_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[8]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48A2_M48A3_M50A3_check_air_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[9]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48A2_M48A3_M50A3_verify_drainage_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[10]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48A2_M48A3_M50A3_check_fan_wheels_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[11]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48A2_M48A3_M50A3_verify_fan_sheaves_yes = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[12]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48A2_M48A3_M50A3_verify_suction_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[13]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48A2_M48A3_M50A3_verify_crankcase_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[14]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48A2_M48A3_M50A3_verify_packaging_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48A2_M48A3_M50A3_remove_comp_bolts_no = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48A2_M48A3_M50A3_verify_economizer_no = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48A2_M48A3_M50A3_verify_options_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48A2_M48A3_M50A3_verify_transducers_no = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48A2_M48A3_M50A3_verify_terminals_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[6]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48A2_M48A3_M50A3_verify_sensors_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[7]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48A2_M48A3_M50A3_check_gas_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[8]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48A2_M48A3_M50A3_check_air_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[9]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48A2_M48A3_M50A3_verify_drainage_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[10]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48A2_M48A3_M50A3_check_fan_wheels_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[11]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48A2_M48A3_M50A3_verify_fan_sheaves_no = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[12]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48A2_M48A3_M50A3_verify_suction_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[13]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48A2_M48A3_M50A3_verify_crankcase_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[14]/div[2]/div[2]/ul[1]/li[1]/label/span')

    # 48HC
    M48HC_48TC_verify_jobsite_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_verify_material_yes = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_verify_hood_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_remove_bolts_yes = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_verify_instructions_yes = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_verify_fuel_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[6]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_check_ref_piping_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[7]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_check_gas_piping_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[8]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_check_ele_conections_yes = (By.XPATH,
                                      '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[9]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_verify_gas_pressure_yes = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[10]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_check_indoor_air_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[11]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_check_outdoor_air_yes = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[12]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_verify_unit_level_yes = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[13]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_check_fan_wheels_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[14]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_check_ele_wirings_yes = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[15]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_check_pully_allign_yes = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[16]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_verify_scroll_yes = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[17]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_verif_thermostat_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[18]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_verify_cranckcase_yes_yes = (By.XPATH,
                                       '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[19]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48HC_48TC_verify_jobsite_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_verify_material_no = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_verify_hood_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_remove_bolts_no = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_verify_instructions_no = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_verify_fuel_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[6]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_check_ref_piping_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[7]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_check_gas_piping_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[8]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_check_ele_conections_no = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[9]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_verify_gas_pressure_no = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[10]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_check_indoor_air_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[11]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_check_outdoor_air_no = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[12]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_verify_unit_level_no = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[13]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_check_fan_wheels_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[14]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_check_ele_wirings_no = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[15]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_check_pully_allign_no = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[16]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_verify_scroll_no = (By.XPATH,
                              '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[17]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_verif_thermostat_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[18]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48HC_48TC_verify_cranckcase_no = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[19]/div[2]/div[2]/ul[1]/li[1]/label/span')

    # 48LC
    M48LC_verify_packaging_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48LC_verify_outdoor_air_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48LC_verify_fuel_exhaust_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48LC_verify_instructions_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48LC_verify_elec_connections_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48LC_verify_gas_pressure_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[6]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48LC_check_gas_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[7]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48LC_check_indoor_air_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[8]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48LC_check_outdoor_air_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[9]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48LC_verify_unitlevel_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[10]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48LC_check_fan_wheels_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[11]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48LC_verify_fan_sheaves_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[12]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48LC_verify_scrool_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[13]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48LC_verify_thermostat_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[14]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48LC_verify_crankcase_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[15]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M48LC_verify_packaging_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48LC_verify_outdoor_air_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48LC_verify_fuel_exhaust_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48LC_verify_instructions_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48LC_verify_elec_connections_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48LC_verify_gas_pressure_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[6]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48LC_check_gas_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[7]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48LC_check_indoor_air_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[8]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48LC_check_outdoor_air_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[9]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48LC_verify_unitlevel_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[10]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48LC_check_fan_wheels_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[11]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48LC_verify_fan_sheaves_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[12]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48LC_verify_scrool_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[13]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48LC_verify_thermostat_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[14]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M48LC_verify_crankcase_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[15]/div[2]/div[2]/ul[1]/li[1]/label/span')

    # 50HC
    M50HC_verify_packaging_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50HC_verify_condenstate_yes = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50HC_verify_fuel_hood_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50HC_check_ele_cons_yes = (By.XPATH,
                                '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50HC_check_wires_yes = (By.XPATH,
                             '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50HC_check_gas_piping_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[6]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50HC_check_air_yes = (By.XPATH,
                           '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[7]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50HC_verify_unit_level_yes = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[8]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50HC_check_fan_wheels_yes = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[9]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50HC_verify_pully_allign_yes = (By.XPATH,
                                     '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[10]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50HC_verify_packaging_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M50HC_verify_condenstate_no = (By.XPATH,
                                   '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M50HC_verify_fuel_hood_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M50HC_check_ele_cons_no = (By.XPATH,
                               '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M50HC_check_wires_no = (By.XPATH,
                            '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M50HC_check_gas_piping_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[6]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M50HC_check_air_no = (By.XPATH,
                          '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[7]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M50HC_verify_unit_level_no = (By.XPATH,
                                  '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[8]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M50HC_check_fan_wheels_no = (By.XPATH,
                                 '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[9]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M50HC_verify_pully_allign_no = (By.XPATH,
                                    '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[10]/div[2]/div[2]/ul[1]/li[1]/label/span')

    # 50PC_PS
    M50PC_PS_volt_availableg_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50PC_PS_terminals_tight_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50PC_PS_heat_exchanger_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50PC_PS_valves_open_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50PC_PS_trap_installed_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50PC_PS_filter_installed_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[6]/div[2]/div[2]/ul[1]/li[2]/label/span')
    M50PC_PS_volt_availableg_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M50PC_PS_terminals_tight_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M50PC_PS_heat_exchanger_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M50PC_PS_valves_open_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M50PC_PS_trap_installed_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/div[2]/ul[1]/li[1]/label/span')
    M50PC_PS_filter_installed_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[6]/div[2]/div[2]/ul[1]/li[1]/label/span')