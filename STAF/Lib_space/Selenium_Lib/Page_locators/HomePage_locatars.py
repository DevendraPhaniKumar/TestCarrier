from selenium.webdriver.common.by import By


class HomePageLocatars(object):
    TITLE = (By.XPATH, "//*[@id='top']/div[1]/div[1]/div[1]/div[2]")
    USER = (By.XPATH,  '//*[@id="top"]/div[1]/div[1]/div[1]/div[3]/ul[1]/li[2]')
    HOME = (By.XPATH, '//*[@id="top"]/div[1]/div[1]/div[1]/div[3]/ul[1]/li[8]/a[1]/img[1]')
    ####User profile###
    license_notify = (By.XPATH, '//*[@id="notificationModals"]/div[1]/div[1]/div[1]/div[2]/div[1]')
    profile_btn = (By.XPATH,'//*[@id="top"]/div/div[1]/div/div[3]/ul/li[2]/div[1]/span[2]/button')
    info_btn=(By.XPATH,'//*[@id="top"]/div[1]/div[1]/div[1]/div[3]/ul[1]/li[1]/div[1]/a[1]/img[1]')
    info_title  =(By.XPATH,'//*[@id="app-help"]/div[1]/div[1]/div[1]/div[2]/span[1]')
    app_version =(By.XPATH,'//*[@id="app-help"]/div[1]/div[1]/div[1]/div[2]/span[2]')
    eula_content = (By.XPATH,'//*[@id="app-help"]/div[1]/div[1]/div[2]')
    Profile_title = (By.XPATH,"//*[@id='mydiv']/div[2]/div[1]")
    License_label = (By.XPATH,"//*[@id='mydiv']/div[2]/div[2]/h3/label/em")
    License_level = (By.XPATH,"//*[@id='mydiv']/div[2]/div[2]/div/div[2]/p[1]")
    License_Validity = (By.XPATH,"//*[@id='mydiv']/div[2]/div[2]/div/div[2]/p[2]")
    License_Update_btn = (By.XPATH,"//*[@id='mydiv']/div[2]/div[2]/div/div[2]/p[3]")
    Profile_FirstName_lbl = (By.XPATH,"//*[@id='mydiv']/div[2]/div[3]/div[1]/label")
    Profile_LastName_lbl = (By.XPATH,"//*[@id='mydiv']/div[2]/div[3]/div[3]/label")
    Profile_FirstName_val = (By.XPATH,"//*[@id='mydiv']/div[2]/div[4]/div[1]/input")
    Profile_LastName_val = (By.XPATH,"//*[@id='mydiv']/div[2]/div[4]/div[3]/input")
    Profile_UsrName_lbl = (By.XPATH,"//*[@id='mydiv']/div[2]/div[5]/div/label")
    Profile_UsrName_val = (By.XPATH, "//*[@id='mydiv']/div[2]/div[6]/div/input")
    Profile_change_passwd_lbl = (By.XPATH,'//*[@id="mydiv"]/div[2]/div[7]/div[1]/label')
    Profile_change_passwd_val = (By.ID,'pwd')
    Profile_change_passwd_Confirm_lbl = (By.XPATH,'//*[@id="mydiv"]/div[2]/div[7]/div[3]/label')
    Profile_change_passwd_Confirm_val = (By.ID,'repwd')
    Passwd_error_msg = (By.XPATH,'//*[@id="mydiv"]/div[2]/div[9]/span')
    Role_txt= (By.XPATH,'//*[@id="mydiv"]/div[2]/span[1]')
    Fontsize_lbl = (By.XPATH,'//*[@id="divFontsize"]/div/label')
    Fontsize_sel = (By.XPATH, '//*[@id="btnFontsize"]')
    Fontsize_LOE = (By.XPATH, '//*[@id="divFontsize"]')
    Language_lbl = (By.XPATH,'//*[@id="divLanguage"]/div/label')
    Language_sel = (By.XPATH, '//*[@id="btnLanguage"]')
    Language_LOE = (By.XPATH, '//*[@id="divLanguage"]')
    Unit_type_lbl = (By.XPATH,'//*[@id="mydiv"]/div[2]/div[7]/div[3]/div/label')#//*[@id="btnTemperature"]
    Unit_type_sel = (By.XPATH,'//*[@id="btnTemperature"]')
    Unit_type_LOE = (By.XPATH,'//*[@id="mydiv"]/div[2]/div[7]/div[3]')
    Save_btn = (By.XPATH,'//*[@id="mydiv"]/div[2]/div[8]/div[1]/button')
    Logout_btn = (By.XPATH,'//*[@id="mydiv"]/div[2]/div[8]/div[2]/button')
    Save_btn_txt = (By.XPATH, '//*[@id="mydiv"]/div[2]/div[8]/div[1]')
    Logout_btn_txt = (By.XPATH, '//*[@id="mydiv"]/div[2]/div[8]/div[2]')
    First_error_msg = (By.XPATH,'//*[@id="mydiv"]/div[2]/div[4]/div[1]/span')
    LastName_err_msg = (By.XPATH,'//*[@id="mydiv"]/div[2]/div[4]/div[3]/span')
    Update_error_msg = (By.XPATH,'//*[@id="success-page-message"]')
    #notifications
    BACNet_popup=(By.XPATH,'')
    ######License screen####
    License_Update_title = (By.XPATH,'//*[@id="licensemodals"]/div/div/div/div[1]/div[1]')
    License_Update_close = (By.XPATH,'//*[@id="licensemodals"]/div/div/div/div[1]/div[2]')
    License_type_lbl = (By.XPATH,'//*[@id="licensemodals"]/div/div/div/div[2]/div[1]/div/p[1]/span[1]')
    License_type_txt = (By.XPATH, '//*[@id="licensemodals"]/div/div/div/div[2]/div[1]/div/p[1]/span[2]')
    License_Usr_lbl = (By.XPATH,'//*[@id="licensemodals"]/div/div/div/div[2]/div[1]/div/p[2]/span[1]')
    License_Usr_txt = (By.XPATH, '//*[@id="licensemodals"]/div/div/div/div[2]/div[1]/div/p[2]/span[2]')
    License_Expiry_lbl = (By.XPATH,'//*[@id="licensemodals"]/div/div/div/div[2]/div[1]/div/p[3]/span[1]')
    License_Expiry_txt = (By.XPATH, '//*[@id="licensemodals"]/div/div/div/div[2]/div[1]/div/p[3]/span[2]')
    License_key_update_title = (By.XPATH,'//*[@id="licensemodals"]/div/div/div/div[2]/div[2]/h3')
    Env_key_lbl = (By.XPATH,'//*[@id="licensemodals"]/div/div/div/div[2]/form/div[1]/label')
    Env_key_val = (By.ID,'copy')
    Env_key_copy = (By.XPATH,'//*[@id="licensemodals"]/div/div/div/div[2]/form/div[1]/span/i')
    License_key_val_lbl = (By.XPATH,'//*[@id="licensemodals"]/div/div/div/div[2]/form/div[2]/label')
    License_key_val = (By.XPATH,'//*[@id="licensemodals"]/div/div/div/div[2]/form/div[2]/input')
    License_error_msg = (By.XPATH,'//*[@id="licensemodals"]/div/div/div/div[2]/form/div[2]/span')
    License_cancel_btn = (By.XPATH,'//*[@id="licensemodals"]/div/div/div/div[2]/div[3]/ul/li[2]/a')
    License_apply_btn = (By.XPATH, '//*[@id="licensemodals"]/div/div/div/div[2]/div[3]/ul/li[1]/a')
    License_help_txt = (By.XPATH,'//*[@id="licensemodals"]/div/div/div/div[2]/form/div[3]/p')
    #####Home Page icon locators######
    home_screen_content =(By.XPATH,'//*[@id="content"]/div/div[1]/div[1]')
    home_ccn_connectivity = (By.XPATH,'//*[@id="content"]/div/div[1]/div[2]/div[1]/div[1]')
    home_bacnet_connectivity = (By.XPATH, '//*[@id="content"]/div/div[1]/div[2]/div[1]/div[2]')
    home_checklist = (By.XPATH,'//*[@id="content"]/div/div[1]/div[2]/div[2]/div[2]')
    home_chillerinfo = (By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div[1]/div[2]/div[1]')
    home_reports = (By.XPATH, '//*[@id="content"]/div/div[1]/div[2]/div[2]/div[1]')
    home_fwupdate = (By.XPATH,'//*[@id="content"]/div/div[1]/div[2]/div[1]/div[3]')

    ccn_connectivity_btn = (By.XPATH, '//*[@id="side"]/div/div[2]/ul/li[1]')
    bacnet_connectivity_btn = (By.XPATH, '//*[@id="side"]/div/div[2]/ul/li[2]')
    checklist_btn = (By.XPATH, '//*[@id="side"]/div/div[2]/ul/li[4]')
    Chiller_info_btn = (By.XPATH, '//*[@id="side"]/div/div[2]/ul/li[3]')
    reports_btn = (By.XPATH, '//*[@id="side"]/div/div[2]/ul/li[5]')
    reports_chart = (By.XPATH,'//*[@id="content"]/div/div[1]/div/div[1]/ul/li[1]/a')
    reports_trend_cfg = (By.XPATH,'//*[@id="content"]/div/div[1]/div/div[1]/ul/li[2]/a')
    reports_trace_history = (By.XPATH,'//*[@id="content"]/div/div[1]/div/div[1]/ul/li[3]/a')
    firmware_update_btn = (By.XPATH, '//*[@id="side"]/div/div[2]/ul/li[6]')

    firmware_update_text = (By.XPATH,'//*[@id="content"]/div/div[1]/div/div[1]/ul/li/a')
    Home_btn = (By.XPATH,'//*[@id="top"]/div/div[1]/div/div[3]/ul/li[8]/a')
    Features_btn = (By.XPATH, '//*[@id="side"]/div/div[1]/ul/li[2]')

    #########admin portal locators######
    admin_login_usr_txt = (By.XPATH,'//*[@id="form-username"]')
    admin_login_passwd_txt = (By.ID,'//*[@id="form-password"]')
    admin_login_btn = (By.XPATH,'/html/body/div/div/div/div[1]/div/div[2]/div/div[2]/form/button')
    admin_logout_btn = (By.XPATH,'/html/body/header/div/div/div/div/ul/li[3]')
    admin_home = (By.XPATH,'/html/body/header/div/div/div/div/ul/li[2]')
    admin_search_usr = (By.XPATH,'/html/body/div/div/div/div/div/form/div/h4/span/input[1]')
    admin_search_btn = (By.XPATH,'/html/body/div/div/div/div/div/form/div/h4/span/input[2]')
    admin_result_usr_name = (By.XPATH,'//*[@id="results"]/tbody/tr/td[4]')
    admin_view_license_btn = (By.XPATH,'//*[@id="results"]/tbody/tr/td[8]/a[3]')
    admin_license_new_btn = (By.XPATH,'/html/body/div/div/div[1]/div/p/a')
    admin_license_envkey_txt = (By.ID,'//*[@id="MachineKey"]')
    admin_license_check_envkey_btn = (By.ID,'//*[@id="btnMachineId"]')
    admin_license_validity = (By.ID, '//*[@id="ValidDate"]')
    admin_license_generate_btn = (By.XPATH,'/html/body/div/div/form/div/div[11]/div/input')
    admin_license_key_val = (By.ID,'//*[@id="LicenseKey"]')
    select_action =(By.XPATH,'//*[@id="CurrentStatus"]/option[text() = '']')
    dialog = (By.XPATH,'//*[@id="CloseButton"]')
    #************FIrmware update***********#
    update_control_sel_loe =(By.XPATH,'//*[@id="configdata"]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li')
    update_control_sel_btn = (By.XPATH,'//*[@id="dropdownMenu3"]')
    update_title = (By.XPATH,'//*[@id="configdata"]/div[1]/div[7]/div[1]/h4[1]')
    update_current_ver_lbl = (By.XPATH,'//*[@id="configdata"]/div/div[7]/div[1]/div[1]/div/div[1]/div[1]')
    update_current_ver = (By.XPATH,'//*[@id="configdata"]/div/div[7]/div[1]/div[1]/div/div[1]/div[2]')
    update_btn = (By.XPATH,'//*[@id="configdata"]/div[1]/div[7]/div[1]/div[1]/div[1]/div[2]/button[1]')
    update_fw_path = "D:\\Projects\\Service_Tools\\009_softwares\\Firmwares\\Firmwares"

    update_pic23_pop_title = (By.XPATH,'//*[@id="firmwaremodal"]/div/div/ng-include/div[1]/div[1]')
    update_pic23_pop_close = (By.XPATH, '//*[@id="firmwaremodal"]/div/div/ng-include/div[1]/div[2]/a[2]')
    update_pic23_pop_ver_lbl = (By.XPATH,'//*[@id="firmwaremodal"]/div/div/ng-include/div[2]/div[1]/p[1]')
    update_pic23_pop_sel_file_lbl = (By.XPATH,'//*[@id="firmwaremodal"]/div/div/ng-include/div[2]/div[2]/span[1]')
    update_pic23_pop_file_name_lbl =(By.XPATH,'//*[@id="firmwaremodal"]/div/div/ng-include/div[2]/div[2]/span['
                                           '2]/div/label')
    update_pic23_pop_file_browse = (By.XPATH, '//*[@id="firmwaremodal"]/div/div/ng-include/div[2]/div[2]/span[2]/div/span/button')
    update_pic23_file_in =  (By.XPATH,'//*[@id="firmwaremodal"]/div/div/ng-include/div[2]/div[2]/span[2]/div/input')
    pic23_fw_update_btn = (By.XPATH,'//*[@id="firmwaremodal"]/div[1]/div[1]/ng-include[1]/div[3]/button[1]')
    update_file_err_msg = (By.XPATH,'//*[@id="firmwaremodal"]/div[1]/div[1]/ng-include[1]/div[1]/div[2]')
    update_pic23_status_lbl = (By.XPATH,'//*[@id="firmwaremodal"]/div[1]/div[1]/ng-include[1]/div[2]/div[3]/div[1]')
    update_pic23_status_val = (By.XPATH,'//*[@id="firmwaremodal"]/div[1]/div[1]/ng-include[1]/div[2]/div[3]/div[2]')
    update_pic6_deviceip_lbl = (By.XPATH,'//*[@id="configdata"]/div[1]/div[2]/div[1]/div[1]/label[1]')
    update_pic6_deviceip_in = (By.XPATH,'//*[@id="configdata"]/div/div[2]/div/div[1]/div/input')
    update_pic6_usr_lbl = (By.XPATH,'//*[@id="configdata"]/div[1]/div[2]/div[1]/div[3]/label[1]')
    update_pic6_usr_in = (By.XPATH,'//*[@id="configdata"]/div/div[2]/div/div[3]/div/input')
    update_pic6_passwd_lbl = (By.XPATH,'//*[@id="configdata"]/div[1]/div[2]/div[1]/div[4]/label[1]')
    update_pic6_passwd_in = (By.XPATH,'//*[@id="configdata"]/div/div[2]/div/div[4]/div/input')
    update_pic6_login_btn = (By.XPATH,'//*[@id="configdata"]/div/div[2]/div/div[5]/button')

    update_pic6_filepath_edit_btn = (By.XPATH,'//*[@id="files"]/div[1]/div[1]/div[1]/div[1]/div[1]/span[2]/button[1]')
    update_pic6_filepath_save_btn = (By.XPATH, '//*[@id="files"]/div[1]/div[1]/div[1]/div[1]/div[1]/span[3]/button[1]')
    update_pic6_filepath_cancel_btn = (By.XPATH, '//*[@id="files"]/div[1]/div[1]/div[1]/div[1]/div[1]/span[3]/button[2]')
    update_pic6_save_pop_ok_btn=(By.XPATH,'//*[@id="commonMsgModal"]/div[1]/div[1]/div[1]/div[3]/ul/li/a')
    update_pic6_upload_pop_ok_btn=(By.XPATH,'//*[@id="uploadfailmodal"]/div/div/div/div[3]/ul/li/a')
    update_file_path_lbl=(By.XPATH,'//*[@id="files"]/div/div[1]/div')
    update_login_loader= (By.XPATH,'//*[@id="spanLoader"]')
    update_login_err =(By.XPATH,'//*[@id="configdata"]/div[1]/div[1]/div[3]')
    update_pic6_logout_btn= (By.XPATH,'//*[@id="configdata"]/div/div[2]/div/div[6]/button')
    update_pic6_conn_abrt  = (By.XPATH,'//*[@id="firmwarefailmodalpic6"]/div/div/div/div[2]/div[2]/p')
    update_pic6_status_tab_btn = (By.XPATH, '//*[@id="accordion"]/div[1]/div[1]/h4[1]')
    update_pic6_status_txt=(By.XPATH,'//*[@id="collapseCurrentPic6Details"]/div/div/div/div/div/div/table/tbody')
    update_pic6_iot_refresh=(By.XPATH,'//*[@id="collapseCurrentPic6Details"]/div/div/div/div/div/div/table/tbody/tr[3]/td[2]/span[2]/a')
    update_pic6_update_tab_btn = (By.XPATH,'//*[@id="accordion"]/div[4]/div[1]/h4[1]')
    update_pic6_file_upload_tab_btn = (By.XPATH, '//*[@id="accordion"]/div[2]/div[1]/h4[1]')
    update_pic6_file_download_tab_btn = (By.XPATH, '//*[@id="accordion"]/div[3]/div[1]/h4[1]')
    update_pic6_update_tab_title = (By.XPATH,'//*[@id="collapseThree"]/div/div/div/div/div[2]/div[3]/span[1]')
    update_pic6_file_upload_tab_title = (By.XPATH, '//*[@id="firmware"]/div[1]/div[6]/div')
    update_pic6_upload_btn =(By.XPATH,'//*[@id="collapseOne"]/div/div[5]/div[3]/button[2]')
    update_pic6_download_btn = (By.XPATH, '//*[@id="collapseTwo"]/div/div[2]/div/div/button')
    update_pic6_download_file_sel =(By.XPATH,'//*[@id="languageControl"]')
    update_pic6_download_ssl_file_sel = (By.XPATH, '//*[@id="sslFileControl"]')
    update_pic6_download_soft_file_sel = (By.XPATH, '//*[@id="control"]')
    update_pic6_upload_lang_btn = (By.XPATH,'//*[@id="collapseOne"]/div/div[5]/div[3]/button[1]')
    update_pic6_upload_lang_loe = (By.XPATH,'//*[@id="collapseOne"]/div/div[5]/div[2]/select')
    update_pic6_delete_btn =(By.XPATH,'//*[@id="collapseOne"]/div/div[1]/div/div[2]/a')
    update_pic6_file_download_tab_title = (By.XPATH, '//*[@id="firmware"]/div[1]/div[6]/div')
    update_pic6_current_ver = (By.XPATH,'//*[@id="collapseThree"]/div/div/div/div/div[2]/div[1]/p')

    # update_pic6_fw_update_btn =(By.XPATH,'//*[@id="firmware"]/div[2]/div[4]/span[2]/div/span/button')

    update_pic6_fw_file = (By.XPATH,'//*[@id="collapseThree"]/div/div/div/div/div/div[2]/span[2]/div/label')
    update_pic6_fw_menifest_content =(By.XPATH,'//*[@id="manifestmodal"]')
    update_pic6_fw_menifest_update = (By.XPATH, '//*[@id="manifestmodal"]/div/div/div/div[4]/ul/li[1]/a')

    update_pic6_fw_menifest_cancel = (By.XPATH, '//*[@id="manifestmodal"]/div/div/div/div[4]/ul/li[2]/a')
    # update_pic6_fw_menifest_ok =    (By.XPATH,'//*[@id="manifestmodal"]/div/div/div/div[4]/ul/li[3]/a')
    update_pic6_fw_file_error=(By.XPATH,'//*[@id="manifestcon"]')
    update_pic6_fw_menifest_err_accept = (By.XPATH, '//*[@id="manifestmodal"]/div/div/div/div[4]/ul/li[3]/a')
    update_pic6_fw_kp_cfg_lbl = (By.XPATH,'//*[@id="manifestmodal"]/div/div/div/div[3]')

    update_pic6_fw_kp_cfg_chk = (By.XPATH, '//*[@id="manifestmodal"]/div/div/div/div[3]/input')
    update_pic6_fw_erase_cfg_pop_msg =(By.XPATH,'//*[@id="keepconfigmodal"]/div/div/div/div[2]')
    update_pic6_fw_erase_cfg_pop_update = (By.XPATH, '//*[@id="keepconfigmodal"]/div/div/div/div[3]/ul/li[2]/a')
    update_pic6_fw_erase_cfg_pop_cancel = (By.XPATH, '//*[@id="keepconfigmodal"]/div/div/div/div[3]/ul/li[1]/a')
    update_pic6_fw_duration_msg=(By.XPATH,'//*[@id="collapseThree"]/div/div/div/div/div[1]/div[3]/h5/strong')
    update_pic6_download_progress_lbl =(By.XPATH,'//*[@id="collapseThree"]/div/div/div/div/div[1]/div[3]/div[1]')
    update_pic6_download_progress_val = (By.XPATH, '//*[@id="collapseThree"]/div/div/div/div/div[1]/div[3]/div[2]')
    update_pic6_update_progress_lbl = (By.XPATH, '//*[@id="collapseThree"]/div/div/div/div/div[1]/div[4]/div[1]')
    update_pic6_update_progress_val=(By.XPATH,'//*[@id="collapseThree"]/div/div/div/div/div[1]/div[4]/div[2]/div')
    update_pic6_fw_connection_abort_msg=(By.XPATH,'//*[@id="firmwarefailmodalpic6"]/div/div/div/div[2]/div[2]/p')
    update_pic6_fw_dt_error=(By.XPATH,'//*[@id="firmwareDateMismatch"]/div/div/div/div[2]/div/p')
    update_pic6_fw_dt_accept =(By.XPATH,'//*[@id="firmwareDateMismatch"]/div/div/div/div[3]/ul/li/a')
    update_pic6_fw_error=(By.XPATH,'//*[@id="firmwarefailmodalpic6"]/div/div/div')
    update_pic6_fw_hw_error=   (By.XPATH,'//*[@id="firmwarefailmodalpic6"]/div/div/div/div[2]/div[2]/p')
    update_pic6_fw_hw_err_accept =(By.XPATH,'//*[@id="firmwarefailmodalpic6"]/div/div/div/div[3]/ul/li/a')
    update_pic6_fw_connection_abort_msg_accept= (By.XPATH,'//*[@id="firmwarefailmodalpic6"]/div/div/div/div[3]/ul/li/a')
    update_pic6_fw_success_msg =(By.XPATH,'//*[@id="successmodal"]/div/div/div/div[2]/div[2]/p')
    update_pic6_fw_success_msg_accept =(By.XPATH,'//*[@id="successmodal"]/div/div/div/div[3]/ul/li/a')
    file_pic6_btn = (By.XPATH,'//*[@id="configdata"]/div/div[6]/div[1]/button[1]')
    file_xfer_pic5_upload_path = "C:\\Users\challau\Downloads"
    file_pic5_title = (By.XPATH,'//*[@id="configdata"]/div/div[7]/div[3]/h4')


    pic6_file_path_input = (By.XPATH,'//*[@id="txt_Default_PIC6_Upload"]')
    pic6_file_path_edit_btn= (By.XPATH,'//*[@id="files"]/div/div[2]/div[1]/div/div/div/span[2]/button')
    pic6_file_path_save_btn =(By.XPATH,'//*[@id="files"]/div/div[2]/div[1]/div/div/div/span[3]/button[1]')
    pic6_file_path_cancel_btn = (By.XPATH,'//*[@id="files"]/div/div[2]/div[1]/div/div/div/span[3]/button[2]')
    pic6_file_path_dialog = (By.XPATH,'//*[@id="commonMsgModal"]/div/div/div/div[2]/div/p')
    pic6_file_path_dialog_ok_btn =(By.XPATH,'//*[@id="commonMsgModal"]/div/div/div/div[3]/ul/li/a')
    pic23_file_path_input = (By.XPATH,'//*[@id="txt_Default_firmware_files"]')
    pic23_file_path_edit_btn = (By.XPATH, '//*[@id="configdata"]/div[1]/form/div[1]/div/div/div/span[2]/button')
    pic23_file_path_save_btn = (By.XPATH, '//*[@id="configdata"]/div[1]/form/div[1]/div/div/div/span[3]/button[1]')
    pic23_file_path_cancel_btn = (By.XPATH, '//*[@id="configdata"]/div[1]/form/div[1]/div/div/div/span[3]/button[2]')

    #***********File Paths*********#
    file_upload_exec_path =r"C:\E2E_HVAC_Testing\STAF\Utility\FileUpload.exe"
    explorer_start="C:\PIC6_data\start_filebrowser.bat"
    sservice_exec_path ="C:\Selenium_POM\\Utilities\S-Service_fw.exe"