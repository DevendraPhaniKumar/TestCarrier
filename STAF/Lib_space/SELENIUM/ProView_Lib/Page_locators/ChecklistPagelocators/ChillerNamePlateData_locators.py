from selenium.webdriver.common.by import By


class ChillerNamePlateDataPageLocators(object):
    chiller_name_plate_data = (By.XPATH, '//*[@id="tabdivisonsid"]/ul/li/a/span[1]/i')
    chiller_name_plate_data_filled = (By.XPATH, '//*[@id="tabdivisonsid"]/ul/li/a/span[2]/i')
    chiller_name_plate_data_reset = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[1]/ul/li[2]/a')
    chiller_name_plate_data_exit = (By.XPATH, '//*[@id="aExistingForm"]')
    chiller_name_plate_data_save = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[4]/ul/li[2]/a')
    chiller_name_plate_data_cancel = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[4]/ul/li[1]/a')
    save_form = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[4]/ul/li[2]/a')
    save_form_popup = (By.XPATH, '//*[@id="AlmostDoneModal"]/div/div/div/form/div[3]/div/button')
    save_form_close_X = (By.XPATH, '//*[@id="SavedSuccessfullyModel"]/div/div/a')


    # same xpaths for 19PIC6, 19XL, 19XR, 19XRE, 19XRD, 19XRPIC5, 19XRV
    M17_compressor_volts = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/input')
    M17_compressor_rla = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/input')
    M17_compressor_olta = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/div/div/input')
    M17_starter_mfg_15 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/input')
    M17_starter_type_15 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/input')
    M17_starter_sno_15 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[3]/div/div/input')
    M17_oilpump_volts = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/div[1]/div[1]/div/div/input')
    M17_oilpump_rla = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/div[1]/div[2]/div/div/input')
    M17_oilpump_olta = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/div[1]/div[3]/div/div/input')

    M23XRV_ciller_data_line_voltage = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/input')
    M23XRV_ciller_data_line_amps = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/input')
    M23XRV_ciller_data_trip_amps = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/div/div/input')
    M23XRV_vfd_data_input_rating = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/input')
    M23XRV_vfd_data_trip_amps = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/input')
    M23XRV_vfd_info_id_no_15 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/div[1]/div[1]/div/div/input')
    M23XRV_vfd_info_s_no_15 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/div[1]/div[2]/div/div/input')
    M23XRV_vfd_info_mfct_in_15 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/div[1]/div[3]/div/div/input')
    M23XRV_vfd_info_mfct_date = (By.XPATH, '')

    M32XR_compressor_volts = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/input')
    M32XR_compressor_rla = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/input')
    M32XR_compressor_olta = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/div/div/input')
    M32XR_starter_mfg_15 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/input')
    M32XR_starter_type_15 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/input')
    M32XR_starter_sno_15 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[3]/div/div/input')
    M32XR_oilpump_volts = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/div[1]/div[1]/div/div/input')
    M32XR_oilpump_rla = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/div[1]/div[2]/div/div/input')
    M32XR_oilpump_olta = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/div[1]/div[3]/div/div/input')
    M32XR_control_volts_115 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[5]/div/div/div[1]/div[3]/div/input')
    M32XR_control_volts_230 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[5]/div/div/div[1]/div[4]/div/input')
    M32XR_ref_type_15 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[6]/div/div/div[1]/div[1]/div/div/input')
    M32XR_ref_charge_15 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div/div/div[6]/div/div/div[1]/div[2]/div/div/input')

