from selenium.webdriver.common.by import By


class ChecklistPageLocators(object):
    checklist = (By.XPATH, '//*[@id="content"]/div/div[1]/div[2]/div[2]/div[2]')

    comment_box=(By.XPATH,'')
    # table_properties = (By.XPATH, '//table[@class="divrow-container existing-scroll-area scrollarea"]/tbody/tr')
    existing_form = (By.XPATH, '//*[@id="main_ExistingForm"]')
    All_forms = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[2]/div/div[2]/h1')
    customer_name = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[2]/div/div[3]/div[2]/div/div[2]')
    form_type = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[2]/div/div[3]/div[2]/div/div[2]')
    edit_form = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[2]/div/div[3]/div[2]/div/div[2]')
    mail_form = (
    By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[2]/div/div[3]/div[2]/div/div[2]/div[1]/div[7]/ul/li[2]/a/i')
    export_form = (
    By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[2]/div/div[3]/div[2]/div/div[2]/div[1]/div[7]/ul/li[3]/a/i')

    delete_form = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[2]/div/div[3]/div[2]/div/div[2]')
    select_form = (
    By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[2]/div/div[3]/div[2]/div/div[2]/div[1]/div[7]/ul/li[6]/input')
    delete_form_yes = (By.XPATH, '//*[@id="deleteModal"]/div/div/div[3]/ul/li[2]/a')
    delete_form_no = (By.XPATH, '//*[@id="deleteModal"]/div/div/div[3]/ul/li[1]/a')
    reset = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[1]/ul/li[2]/a')

    search_form = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[2]/div/div[2]/div/button')
    search_form_input=(By.XPATH,'//*[@id="search"]')
    search_customer_name=(By.XPATH,'//*[@id="content"]/div/div[2]/ng-include[2]/div/div[3]/div[2]/div/div[2]/div[1]/div[7]/ul/li[1]/a/i')
    select_all_chk = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[2]/div/div[3]/div[1]/div[5]/input')
    export_json = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[2]/div/div[3]/div[1]/div[7]/a')
    import_json = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[2]/div/div[3]/div[1]/div[8]/a')
    export_json_pop = (By.XPATH, '//*[@id="TradeModalWindow"]/div/div/div')
    import_json_file_input = (By.XPATH, '//*[@id="TradeModalWindow"]/div/div/div/div/input')
    # page element checker
    create_new_form_text = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[2]/div/div[2]/h1')
    # New form creation
    new_form = (By.XPATH, '//*[@id="content"]/div/div[1]/div/div[1]/ul/li[3]')
    startup_form = (By.XPATH, '//*[@id="StartUpForm"]')
    ehs_form = (By.XPATH, '//*[@id="EHSForm"]')
    refregeration_form = (By.XPATH, '//*[@id="Refrigerationform"]')
    job_name = (
    By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[3]/div/div[3]/form/div[1]/div[1]/ul[1]/li[1]/div/input')
    importfile_path = r'C:\Users\challau\Documents\Carrier\ProView\ExportedChecklist'
    job_no = (
    By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[3]/div/div[3]/form/div[1]/div[1]/ul[1]/li[2]/div/input')
    cust_name = (
    By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[3]/div/div[3]/form/div[1]/div[1]/ul[1]/li[4]/div/input')

    address = (
    By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[3]/div/div[3]/form/div[1]/div[1]/ul[2]/li[1]/div/textarea')

    model_no = (By.XPATH,
                '//*[@id="content"]/div/div[2]/ng-include[3]/div/div[3]/form/div[1]/div[1]/ul[1]/li[3]/div/div/div/button')

    model_no_dropdown = (    By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[3]/div/div[3]/form/div[1]/div[1]/ul[1]/li[3]/div/div/div/ul')
    serial_no = (
    By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[3]/div/div[3]/form/div[1]/div[1]/ul[1]/li[5]/div/input')

    create_form = (By.XPATH, '//*[@id="Create"]')
    create_ref_form = (By.XPATH, '//*[@id="CreateRef"]')
    cancel_form = (By.XPATH, '//*[@id="Cancel"]')
    proceed = (By.XPATH, '//*[@id="Startuppopupmodal"]/div/div/div/button')
    # page load check elements
    caution = (By.XPATH, '//*[@id="Startuppopupmodal"]/div/div/div/div/i')
    form_info = (By.XPATH, '//*[@id="tabdivisonsid"]/ul/li[1]')
    # Save button for any form
    save_form = (
    By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div[1]/div[2]/div/ul/li[2]/a')
    save_form_2_old = (
    By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div/div[4]/ul/li[2]/a')
    save_form_2 = (
    By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div/div[4]/ul/li[2]/a')
    save_form_popup = (By.XPATH, '//*[@id="AlmostDoneModal"]/div/div/div/form/div[4]/div/button')
    save_form_pop_name=(By.XPATH,'//*[@id="inputEmail3"]')
    save_form_pop_date=(By.XPATH,'//*[@id="dateSubmitted"]')
    save_form_popup_19 = (By.XPATH, '//*[@id="AlmostDoneModal"]/div/div/div/form/div[4]/div/button')
    save_successfull_msg_19 = (By.XPATH, '//*[@id="SavedSuccessfullyModel"]/div/div/div/p[1]')
    exit_success_popup_msg_19 = (By.XPATH, '//*[@id="SavedSuccessfullyModel"]/div/div/a')
    exit_save_form_popup_19 = (By.XPATH, '//*[@id="AlmostDoneModal"]/div/div/a')
    # Cancel button for any form
    cancel_save_form = (
    By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div/div[4]/ul/li[1]/a')
    # Start up check list home page
    startup_page_exit = (By.XPATH, '//*[@id="aExistingForm"]')
    startup_page_save = (
    By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div/div[4]/ul/li[2]/a')
    startup_page_cancel = (
    By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div/div[4]/ul/li[1]/a')
    # Customer details locators
    custinfo_icon =(By.XPATH,'//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[1]/ul/li[4]/a')
    custinfo_title =(By.XPATH,'//*[@id="CustomerDetailsNew"]/div/div/div/p')
    custinfo_cname=(By.XPATH,'//*[@id="customerName"]')
    custinfo_poc =(By.XPATH,'//*[@id="pointOfContact"]')
    custinfo_phno =(By.XPATH,'//*[@id="phoneNumber"]')
    custinfo_compname =(By.XPATH,'//*[@id="companyName"]')
    custinfo_email = (By.XPATH,'//*[@id="emailAddress"]')
    custinfo_save = (By.XPATH,'//*[@id="CustomerDetailsBtn"]')

    # Design information entry page 19XRV
    design_data = (By.XPATH, '//*[@id="tabdivisonsid"]/ul/li/a/span[1]')
    design_data_two = (By.XPATH, '//*[@id="tabdivisonsid"]/ul/li/a/span[2]/i')
    design_data_three = (By.XPATH, '//*[@id="tabdivisonsid"]/ul/li/a/span[1]/i')
    #auto-fill
    autofill_tab=(By.XPATH,'//*[@id="content"]/div/div[1]/div/div[1]/ul/li[1]/a')
    autofill_protocol_lbl=(By.XPATH,'//*[@id="content"]/div/div[2]/ng-include[1]/div/div[1]/div[1]')
    autofill_protocol_btn=(By.XPATH,'//*[@id="content"]/div/div[2]/ng-include[1]/div/div[1]/div[2]/div/button')
    autofill_protocol_lst=(By.XPATH,'//*[@id="content"]/div/div[2]/ng-include[1]/div/div[1]/div[2]/div/ul/li')

    autofill_ccn_name_lbl=(By.XPATH,'//*[@id="content"]/div/div[2]/ng-include[1]/div/div[2]/div[1]')
    autofill_ccn_name_btn=(By.XPATH,'//*[@id="content"]/div/div[2]/ng-include[1]/div/div[2]/div[2]/div/button')
    autofill_ccn_name_lst=(By.XPATH,'//*[@id="content"]/div/div[2]/ng-include[1]/div/div[2]/div[2]/div/ul/li')

    autofill_ccn_ctrl_lbl = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[1]/div/div[4]/div[1]')
    autofill_ccn_ctrl_btn = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[1]/div/div[4]/div[2]/div/button')
    autofill_ccn_ctrl_lst = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[1]/div/div[4]/div[2]/div/ul/li')

    autofill_bacnet_ctrl_lbl = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[1]/div/div[3]/div[1]')
    autofill_bacnet_ctrl_btn = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[1]/div/div[3]/div[2]/div/button')
    autofill_bacnet_ctrl_lst = (By.XPATH, '//*[@id="content"]/div/div[2]/ng-include[1]/div/div[3]/div[2]/div/ul/li')
    autofill_save_btn=(By.XPATH,'//*[@id="content"]/div/div[2]/ng-include[1]/div/div[5]/div/button')
    autofill_save_msg=(By.XPATH,'//*[@id="content"]/div/div[2]/ng-include[1]/div/div[6]')
    # Tons
    M19_cooler_ref_tons = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/input')
    # Brine
    M19_cooler_ref_brine = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/input')
    # Flow Rate
    M19_cooler_ref_flowrate = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/div/div/input')
    # Pressure Drop
    M19_cooler_ref_presdrop = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[4]/div/div/input')
    # Pass
    M19_cooler_ref_pass = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[5]/div/div/input')
    # Suction Temp
    M19_cooler_ref_suctemp = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[6]/div/div/input')
    # Temp IN
    M19_cooler_ref_tempin = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[3]/div[2]/div/div/div/div[1]/input')
    # Temp OUT
    M19_cooler_ref_tempout = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[3]/div[2]/div/div/div/div[2]/input')
    # Tons
    M19_condenser_ref_tons = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/input')
    # Brine
    M19_condenser_ref_brine = (By.XPATH,'//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/input')
    # Flow Rate
    M19_condenser_ref_flowrate = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[3]/div/div/input')
    # Pressure Drop
    M19_condenser_ref_presdrop = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[4]/div/div/input')
    # Pass
    M19_condenser_ref_pass = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[5]/div/div/input')
    # Suction Temp
    M19_condenser_ref_suctemp = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[6]/div/div/input')
    # Temp IN
    M19_condenser_ref_tempin = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[3]/div[2]/div/div/div/div[1]/input')
    # Temp OUT
    M19_condenser_ref_tempout = (By.XPATH,'//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[3]/div[2]/div/div/div/div[2]/input')


    # Supply steam preasure
    M16_supply_steam_preasure = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/input')
    # Steam preasure at generator
    M16_supply_preasure_generator = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/input')
    # Electrical Data
    M16_electrical_data = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/div/div/input')
    # INHIBITOR
    M16_inhibitor = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[4]/div/div/input')

    # Tons
    M16_cooler_ref_tons = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/input')
    # Flow Rate
    M16_cooler_ref_flowrate = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/input')
    # Pressure Drop
    M16_cooler_ref_presdrop = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[3]/div/div/input')
    # Pass
    M16_cooler_ref_pass = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[4]/div/div/input')
    # Temp IN
    M16_cooler_ref_tempin = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[3]/div[2]/div/div/div/div[1]/input')
    # Temp OUT
    M16_cooler_ref_tempout = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[3]/div[2]/div/div/div/div[2]/input')

    # Tons
    M16_evaporator_ref_tons = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div[1]/div/div/input')
    # Flow Rate
    M16_evaporator_ref_flowrate = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div[2]/div/div/input')
    # Pressure Drop
    M16_evaporator_ref_presdrop = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div[3]/div/div/input')
    # Pass
    M16_evaporator_ref_pass = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div[4]/div/div/input')
    # Temp IN
    M16_evaporator_ref_tempin = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div[2]/div/div/div/div[1]/input')
    # Temp OUT
    M16_evaporator_ref_tempout = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div[2]/div/div/div/div[2]/input')

    # Tons
    M16_absorber_ref_tons = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[5]/div/div/div[1]/div[1]/div/div/input')
    # Flow Rate
    M16_absorber_ref_flowrate = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[5]/div/div/div[1]/div[2]/div/div/input')
    # Pressure Drop
    M16_absorber_ref_presdrop = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[5]/div/div/div[1]/div[3]/div/div/input')
    # Pass
    M16_absorber_ref_pass = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[5]/div/div/div[1]/div[4]/div/div/input')
    # Temp IN
    M16_absorber_ref_tempin = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[5]/div/div/div[3]/div[2]/div/div/div/div[1]/input')
    # Temp OUT
    M16_absorber_ref_tempout = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[5]/div/div/div[3]/div[2]/div/div/div/div[2]/input')


    # Equipment
    M30HX_equip_model_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/input')
    M30HX_equip_serial_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/input')

    # Chiller
    M30MP_chiller_model_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/input')
    M30MP_chiller_serial_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/input')
    M30MP_comp_model_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/input')
    M30MP_comp_serial_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/input')

    # 30RAP
    M30RAP_capcity = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/input')
    M30RAP_ceat = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/input')
    M30RAP_ewt = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/div/div/input')
    M30RAP_lwt = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[4]/div/div/input')
    M30RAP_fluid_type = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[5]/div/div/input')
    M30RAP_flowrate = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[6]/div/div/input')
    M30RAP_PD = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[7]/div/div/input')
    # unit
    M30RAP_model_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/input')
    M30RAP_serial_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/input')

    # 30RB
    # Unit
    M30RB_unit_model_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/input')
    M30RB_unit_serial_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/input')
    # Cooler
    M30RB_cooler_model_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/input')
    M30RB_cooler_serial_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/input')
    # Compressor Type Selection A, B, C
    ###### CLICKS ##########
    M30RB_Comp_type_A1 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[2]/div[1]/ul/li/a')
    M30RB_Comp_type_A2 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[2]/div[2]/ul/li/a')
    M30RB_Comp_type_A3 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[2]/div[3]/ul/li/a')
    M30RB_Comp_type_A4 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[2]/div[4]/ul/li/a')
    M30RB_Comp_type_B1 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[2]/div[1]/ul/li/a')
    M30RB_Comp_type_B2 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[2]/div[2]/ul/li/a')
    M30RB_Comp_type_B3 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[2]/div[3]/ul/li/a')
    M30RB_Comp_type_B4 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[2]/div[4]/ul/li/a')
    M30RB_Comp_type_C1 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[2]/div[1]/ul/li/a')
    M30RB_Comp_type_C2 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[2]/div[2]/ul/li/a')
    M30RB_Comp_type_C3 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[2]/div[3]/ul/li/a')
    M30RB_Comp_type_C4 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[2]/div[4]/ul/li/a')
    ######## TEXT EDITS ########
    M30RB_A4_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[6]/div/div[1]/div/div/input')
    M30RB_A4_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[6]/div/div[2]/div/div/input')
    M30RB_A4_SMP_Address = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[6]/div/div[3]/div/div/input')
    M30RB_B4_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[6]/div/div[1]/div/div/input')
    M30RB_B4_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[6]/div/div[2]/div/div/input')
    M30RB_B4_SMP_Address = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[6]/div/div[3]/div/div/input')
    M30RB_C4_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[6]/div/div[1]/div/div/input')
    M30RB_C4_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[6]/div/div[2]/div/div/input')
    M30RB_C4_SMP_Address = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[6]/div/div[3]/div/div/input')
    M30RB_A3_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[5]/div/div[1]/div/div/input')
    M30RB_A3_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[5]/div/div[2]/div/div/input')
    M30RB_A3_SMP_Address = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[5]/div/div[3]/div/div/input')
    M30RB_B3_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[5]/div/div[1]/div/div/input')
    M30RB_B3_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[5]/div/div[2]/div/div/input')
    M30RB_B3_SMP_Address = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[5]/div/div[3]/div/div/input')
    M30RB_C3_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[5]/div/div[1]/div/div/input')
    M30RB_C3_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[5]/div/div[2]/div/div/input')
    M30RB_C3_SMP_Address = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[5]/div/div[3]/div/div/input')
    M30RB_A2_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[4]/div/div[1]/div/div/input')
    M30RB_A2_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[4]/div/div[2]/div/div/input')
    M30RB_A2_SMP_Address = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[4]/div/div[3]/div/div/input')
    M30RB_B2_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[4]/div/div[1]/div/div/input')
    M30RB_B2_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[4]/div/div[2]/div/div/input')
    M30RB_B2_SMP_Address = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[4]/div/div[3]/div/div/input')
    M30RB_C2_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[4]/div/div[1]/div/div/input')
    M30RB_C2_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[4]/div/div[2]/div/div/input')
    M30RB_C2_SMP_Address = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[4]/div/div[3]/div/div/input')
    M30RB_A1_ModelNo = (By.XPATH,'//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[3]/div/div[1]/div/div/input')
    M30RB_A1_SerialNo = (By.XPATH,'//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[3]/div/div[2]/div/div/input')
    M30RB_A1_SMP_Address = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[3]/div/div[3]/div/div/input')
    M30RB_B1_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[3]/div/div[1]/div/div/input')
    M30RB_B1_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[3]/div/div[2]/div/div/input')
    M30RB_B1_SMP_Address = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div[3]/div/div[3]/div/div/input')
    M30RB_C1_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[3]/div/div[1]/div/div/input')
    M30RB_C1_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[3]/div/div[2]/div/div/input')
    M30RB_C1_SMP_Address = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div[3]/div/div[3]/div/div/input')
    # Hydronic package
    # Compressor Type
    ###### CLICKS ##########
    M30RB_comp_type_P1 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div/div[2]/div[1]/ul/li/a')
    M30RB_comp_type_P2 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div/div[2]/div[2]/ul/li/a')
    ######## TEXT EDITS ########
    M30RB_P1_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div/div[3]/div/div[1]/div/div/input')
    M30RB_P1_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div/div[3]/div/div[2]/div/div/input')
    M30RB_P2_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div/div[4]/div/div[1]/div/div/input')
    M30RB_P2_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[6]/div/div/div/div/div[4]/div/div[2]/div/div/input')

    # 30XA
    # Cooler
    M30XA_30XV_cooler_cap = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/input')
    M30XA_30XV_cooler_ewt = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/input')
    M30XA_30XV_cooler_lwt = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/div/div/input')
    M30XA_30XV_cooler_fluid_type = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[4]/div/div/input')
    M30XA_30XV_cooler_flow_rate = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[5]/div/div/input')
    M30XA_30XV_cooler_PD = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[6]/div/div/input')
    M30XA_30XV_cooler_ambient = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[7]/div/div/input')
    # unit
    M30XA_30XV_unit_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/input')
    M30XA_30XV_unit_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/input')
    # cooler
    M30XA_30XV_cooler_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div[1]/div/div/input')
    M30XA_30XV_cooler_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div[2]/div/div/input')
    # compressor A
    M30XA_30XV_comp_A_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[5]/div/div/div[1]/div[1]/div/div/input')
    M30XA_30XV_comp_A_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[5]/div/div/div[1]/div[2]/div/div/input')
    # compressor B
    M30XA_30XV_comp_B_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[5]/div/div/div[2]/div[1]/div/div/input')
    M30XA_30XV_comp_B_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[5]/div/div/div[2]/div[2]/div/div/input')

    # 30XW
    # Evaporator
    M30XW_30XWV_evaporator_cap = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/input')
    M30XW_30XWV_evaporator_ewt = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/input')
    M30XW_30XWV_evaporator_lwt = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/div/div/input')
    M30XW_30XWV_evaporator_fluid_type = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[4]/div/div/input')
    M30XW_30XWV_evaporator_flow_rate = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[5]/div/div/input')
    M30XW_30XWV_evaporator_PD = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[6]/div/div/input')
    # Condenser
    M30XW_30XWV_condenser_cap = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/input')
    M30XW_30XWV_condenser_ewt = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/input')
    M30XW_30XWV_condenser_lwt = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[3]/div/div/input')
    M30XW_30XWV_condenser_fluid_type = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[4]/div/div/input')
    M30XW_30XWV_condenser_flow_rate = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[5]/div/div/input')
    M30XW_30XWV_condenser_PD = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div[6]/div/div/input')
    # UNIT
    M30XW_30XWV_unit_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div[1]/div/div/input')
    M30XW_30XWV_unit_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div[2]/div/div/input')
    # Compressor A
    M30XW_30XWV_comp_A_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[5]/div/div/div[1]/div[1]/div/div/input')
    M30XW_30XWV_comp_A_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[5]/div/div/div[1]/div[2]/div/div/input')
    # Compressor B
    M30XW_30XWV_comp_B_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[6]/div/div/div[1]/div[1]/div/div/input')
    M30XW_30XWV_comp_B_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[6]/div/div/div[1]/div[2]/div/div/input')
    # Evap
    M30XW_30XWV_evaporator_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[7]/div/div/div[1]/div[1]/div/div/input')
    M30XW_30XWV_evaporator_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[7]/div/div/div[1]/div[2]/div/div/input')
    # Comp
    M30XW_30XWV_condenser_ModelNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[8]/div/div/div[1]/div[1]/div/div/input')
    M30XW_30XWV_condenser_SerialNo = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[8]/div/div/div[1]/div[2]/div/div/input')
    
    # Reset
    design_data_reset = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div[1]/div[1]/ul/li[2]/a')
    design_data_reset_two = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[1]/ul/li[2]/a')
    # Exit
    design_data_exit = (By.XPATH, '//*[@id="aExistingForm"]/i')
    # Save'
    design_data_save = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div[1]/div[2]/div/ul/li[2]/a')
    design_data_save_one = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div/div[2]/form/div/div[4]/ul/li[2]/a')
    # Cancel
    design_data_cancel = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[3]/div[1]/div[2]/div/ul/li[1]/a')

    # Chiller name plate data 19XRV
    chiller_npd_data = (By.XPATH, '//*[@id="tabdivisonsid"]/ul/li/a/span[1]/i')
    # Volts
    chiller_npd_data_cmp_volts = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/input')
    # RLS
    chiller_npd_data_cmp_rla = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/input')
    # OLTA
    chiller_npd_data_cmp_olta = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/div/div/input')
    # MFG
    chiller_npd_data_starter_mfg = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/input')
    # Type
    chiller_npd_data_starter_type = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/input')
    # S/N
    chiller_npd_data_starter_sno = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[3]/div/div/input')
    # Volts
    chiller_npd_data_oil_volts = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div/div[4]/div/div/div[1]/div[1]/div/div/input')
    # RLA
    chiller_npd_data_oil_rla = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div/div[4]/div/div/div[1]/div[2]/div/div/input')
    # OLTA
    chiller_npd_data_oil_olta = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div/div[4]/div/div/div[1]/div[3]/div/div/input')
    # Reset
    chiller_npd_data_reset = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[1]/ul/li[2]/a')
    # Save
    chiller_npd_data_save = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[4]/ul/li[2]/a')
    # Exit
    chiller_npd_data_exit = (By.XPATH, '//*[@id="aExistingForm"]/i')
    # Cancel
    chiller_npd_data_cancel = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[4]/ul/li[1]/a')

    # Carrier Obligations & Job Data Checklist 19XRV
    carrier_ojdc = (By.XPATH, '//*[@id="tabdivisonsid"]/ul/li/a/span[1]/i')
    # Assemble
    carrier_ojdc_assemble_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span')
    carrier_ojdc_assemble_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    # Leak Test
    carrier_ojdc_leaktest_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span')
    carrier_ojdc_leaktest_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    # Dehydrate
    carrier_ojdc_dehydrate_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span')
    carrier_ojdc_dehydrate_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    # Charging
    carrier_ojdc_charging_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span')
    carrier_ojdc_charging_no = (By.XPATH,'//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    # Operating Instructions
    carrier_ojdc_op_intrs = (By.XPATH, '//*[@id="a"]')
    # Machine Installation Instructions
    carrier_ojdc_mii_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span')
    # Machine Assembly, wiring & piping diagrams
    carrier_ojdc_mawpd_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span')
    # Starting equipment details and wiring diagrams
    carrier_ojdc_sedwd_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span')
    # Applicable design data
    carrier_ojdc_add_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span')
    # Diagrams & Instructions for special controls
    carrier_ojdc_disc_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div[5]/div[3]/ul/li[2]/label/span')
    # Machine Installation Instructions
    carrier_ojdc_mii_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    # Machine Assembly, wiring & piping diagrams
    carrier_ojdc_mawpd_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    # Starting equipment details and wiring diagrams
    carrier_ojdc_sedwd_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    # Applicable design data
    carrier_ojdc_add_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    # Diagrams & Instructions for special controls
    carrier_ojdc_disc_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[3]/div[2]/div/div/div/div[3]/div/div/div/div/div[5]/div[3]/ul/li[1]/label/span')
    # reset
    carrier_ojdc_reset = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[1]/ul/li[2]')
    # exit
    carrier_ojdc_exit = (By.XPATH, '//*[@id="aExistingForm"]')
    # save
    carrier_ojdc_save = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[4]/ul/li[2]/a')
    # cancel
    carrier_ojdc_cancel = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[4]/ul/li[1]/a')


    # Pre-Start Checklist
    prestart_checklist_select = (By.XPATH, '//*[@id="tabdivisonsid"]/ul/li/a/span[1]/i')
    # Initial Machine Pressure
    prestart_cl_imp = (By.XPATH, '//*[@id="a"]')
    # Was Machine Tight?
    prestart_cl_wmt_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl__wmt_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    # If not, were leaks corrected?
    prestart_cl_leak_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_leak_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    # Was machine dehydrated after repairs?
    prestart_cl_dehydrate_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_dehydrate_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    # Oil sump sight glass
    prestart_cl_ossg_full = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[1]/label/span')
    prestart_cl_ossg_null = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[5]/label/span')
    prestart_cl_ossg_3by4 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[2]/label/span')
    prestart_cl_ossg_1by2 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[3]/label/span')
    prestart_cl_ossg_1by4 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/ul[2]/li[4]/label/span')
    # Strainer housing sight glass
    prestart_cl_shsg_full = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[1]/label/span')
    prestart_cl_shsg_null = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[5]/label/span')
    prestart_cl_shsg_3by4 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[2]/label/span')
    prestart_cl_shsg_1by2 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[3]/label/span')
    prestart_cl_shsg_1by4 = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[3]/ul[2]/li[4]/label/span')
    # Add oil
    prestart_cl_add_oil_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_add_oil_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    # Amount
    prestart_cl_amount = (By.XPATH, '//*[@id="a"]')
    # Cooler
    prestart_cl_cooler = (By.XPATH, '//*[@id="a"]')
    # Condenser
    prestart_cl_condenser = (By.XPATH, '//*[@id="a"]')
    # Initial charge
    prestart_cl_ic = (By.XPATH, '//*[@id="a"]')
    # Motor Voltage
    prestart_cl_mv = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[1]/div/input')
    # Motor Amps
    prestart_cl_ma = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[2]/div/input')
    # Oil Pump Voltage
    prestart_cl_opv = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[3]/div/input')
    # Starter LRA Rating
    prestart_cl_slra_rating = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[4]/div/input')
    # Line Voltage:Motor
    prestart_cl_lvm = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[5]/div/input')
    # Line Voltage:Oil Pump
    prestart_cl_lvop = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[6]/div/input')
    # Controls/Oil Heater
    prestart_cl_coh = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[6]/div/div/div/div/div[7]/div/input')
    # Perform controls test:
    prestart_cl_pct_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[7]/div/div/div/div/div/div/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_pct_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[7]/div/div/div/div/div/div/div[3]/ul/li[1]/label/span')
    # Condenser water pump
    prestart_cl_cwp_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_cwp_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    # Chilled water pump
    prestart_cl_chwp_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_chwp_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    # Condenser water flow
    prestart_cl_cwf_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_cwf_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    # Chilled water flow
    prestart_cl_chwf_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_chwf_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    # Pump interlocks
    prestart_cl_pi_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[5]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_pi_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[8]/div/div/div/div/div/div[5]/div[3]/ul/li[1]/label/span')
    # Line up all valves in accordance with instruction manual
    prestart_cl_lineup_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[1]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_lineup_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    # Start water pumps & establish water flow
    prestart_cl_wpwf_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[2]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_wpwf_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[2]/div[3]/ul/li[1]/label/span')
    # Oil level OK & Oil level temperature OK
    prestart_cl_olot_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[3]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_olot_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    # Check oil pump rotation pressure
    prestart_cl_oprp_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[4]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_oprp_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    # Check compressor motor rotation(Motor end sight glass) and record
    prestart_cl_cmrr_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[5]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_cmrr_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[5]/div[3]/ul/li[1]/label/span')
    # Clockwise
    prestart_cl_clockw_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[6]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_clockw_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[6]/div[3]/ul/li[1]/label/span')
    # Restart compressor, bring up to speed. Shut down, any abnormal coastdown noise?
    prestart_cl_restart_comp_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[7]/div[3]/ul/li[2]/label/span[1]')
    prestart_cl_restart_comp_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[4]/div[2]/div/div/div/div[9]/div/div/div/div/div/div[7]/div[3]/ul/li[1]/label/span')
    prestart_cl_reset = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[1]/ul/li[2]/a/i')
    prestart_cl_exit = (By.XPATH, '//*[@id="aExistingForm"]/i')
    prestart_cl_save = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[4]/ul/li[2]/a')
    prestart_cl_cancel = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div/div[4]/ul/li[1]/a')

    # Post-Start Checklist
    poststart_cl_select = (By.XPATH, '//*[@id="tabdivisonsid"]/ul/li/a/span[1]/i')
    # Trim charge and record under charge refrigerant section.
    poststart_cl_trim_chrge_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[5]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[3]/ul/li[2]/label/span')
    poststart_cl_trim_chrge_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[5]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[3]/ul/li[1]/label/span')
    # Final charge after trim:
    poststart_cl_final_chrge = (By.XPATH, '//*[@id="a"]')
    # Complete any remaining control calibartion & record under control section
    poststart_cl_contrl_cal_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[5]/div[2]/div/div/div/div[2]/div/div/div/div[3]/div[3]/ul/li[2]/label/span')
    poststart_cl_contrl_cal_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[5]/div[2]/div/div/div/div[2]/div/div/div/div[3]/div[3]/ul/li[1]/label/span')
    # For unit mounted VFD complete.
    poststart_cl_VFD_comp_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[5]/div[2]/div/div/div/div[2]/div/div/div/div[4]/div[3]/ul/li[2]/label/span')
    poststart_cl_VFD_comp_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[5]/div[2]/div/div/div/div[2]/div/div/div/div[4]/div[3]/ul/li[1]/label/span')
    # Take atleast two sets of operation log reading & record.
    poststart_cl_2sets_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[5]/div[2]/div/div/div/div[2]/div/div/div/div[5]/div[3]/ul/li[2]/label/span')
    poststart_cl_2sets_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[5]/div[2]/div/div/div/div[2]/div/div/div/div[5]/div[3]/ul/li[1]/label/span')
    # After machine has been succefully run & setup, shutdown & mark shutdown oil & refrigerant level.
    poststart_cl_mark_or_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[5]/div[2]/div/div/div/div[2]/div/div/div/div[6]/div[3]/ul/li[2]/label/span')
    # noinspection PyPep8
    poststart_cl_mark_or_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[5]/div[2]/div/div/div/div[2]/div/div/div/div[6]/div[3]/ul/li[1]/label/span')
    # Give operating instructions to owners operating personnel.
    poststart_cl_owner_mnl_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[5]/div[2]/div/div/div/div[2]/div/div/div/div[7]/div[3]/ul/li[2]/label/span')
    poststart_cl_owner_mnl_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[5]/div[2]/div/div/div/div[2]/div/div/div/div[7]/div[3]/ul/li[1]/label/span')
    # Hours given:
    poststart_cl_hours_given = (By.XPATH, '//*[@id="a"]')
    # Call your carrier factory representative to report chiller startup.
    poststart_cl_call_report_yes = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[5]/div[2]/div/div/div/div[2]/div/div/div/div[9]/div[3]/ul/li[2]/label/span')
    poststart_cl_call_report_no = (By.XPATH, '//*[@id="content"]/div/div[2]/check-list[2]/ng-include[2]/div/div[2]/form/div[2]/div[5]/div[2]/div/div/div/div[2]/div/div/div/div[9]/div[3]/ul/li[1]/label/span')
