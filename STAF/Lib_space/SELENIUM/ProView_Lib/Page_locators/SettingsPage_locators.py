from selenium.webdriver.common.by import By
#Updated by Uday 13-Oct-2018

class SettingPageLocators(object):
    home_setting_btn = (By.XPATH,'//*[@id="content"]/div[1]/div[1]/div[2]/div[1]/div[3]')
    setting_icon_btn = (By.XPATH,'//*[@id="side"]/div[1]/div[1]/ul[1]/li[3]')
    chiller_info_setting_btn = (By.XPATH,'//*[@id="content"]/div[1]/ng-include[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]')
    chiller_settings_title = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/h1[1]')
    datapoint_table_loe = (By.XPATH,'//*[@id="datapoint"]')
    display_text_title = (By.XPATH,'//*[@id="datapoint"]/div[1]/div[3]')
    dp_display_textname = (By.XPATH, '//*[@id="datapoint"]/div[2]/div[3]')
    table_chiller_vername = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]')
    chiller_model = (By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div/div/form/div[1]/ul/li[1]/div/input')
    chiller_version= (By.XPATH,'//*[@id="content"]/div/div[2]/div[2]/div/div/form/div[1]/ul/li[3]/div/input')
    chiller_cfg_title = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/ul[1]/li[1]/h1[1]')
    chiller_cfg_table_labels = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[1]')
    chiller_cfg_edit_title = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/div/h1')
    ccn_point_title = (By.XPATH, '//*[@id="datapoint"]/div[1]/div[6]')
    bacnet_point_title = (By.XPATH, '//*[@id="datapoint"]/div[1]/div[4]')
    display_text_dp =  (By.XPATH,'//*[@id="datapoint"]/div[2]/div[3]')
    dp_ccn_point = (By.XPATH, '//*[@id="datapoint"]/div[2]/div[3]')
    dp_bacnet_point = (By.XPATH, '//*[@id="datapoint"]/div[2]/div[3]')
    setting_cancel_btn = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[8]/ul[1]/li[1]/a')
    setting_save_btn = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[8]/ul[1]/li[2]/a')
    setting_download_cfg_btn = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[8]/ul[1]/li[3]/a')
    setting_cancel_yes_btn = (By.XPATH,'//*[@id="cancelmodal"]/div[1]/div[1]/div[1]/div[3]/ul[1]/li[1]/a[1]')
    setting_cancel_no_btn = (By.XPATH, '//*[@id="cancelmodal"]/div[1]/div[1]/div[1]/div[3]/ul[1]/li[2]/a[1]')
    point_search = (By.XPATH,'//*[@id="search"]')
    chiller_cfg_import =(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/div[1]/a[1]')
    chiller_cfg_action_export = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[5]/ul['
                                         '1]/li[1]/a[1]/i[1]')
    chiller_cfg_action_offline_info = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div['
                                                '5]/ul['
                                        '1]/li[2]/a[1]/i[1]')
    chiller_cfg_action_edit = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[5]/ul['
                                        '1]/li[3]/a[1]/i[1]')
    chiller_cfg_action_delete = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[5]/ul['
                                          '1]/li[4]/a[1]/i[1]')
    chiller_cfg_delete_yes = (By.XPATH,'//*[@id="deletemodal"]/div[1]/div[1]/div[1]/div[3]/ul/li[2]/a')
    chiller_cfg_delete_connected = (By.XPATH,'//*[@id="doNotDelete"]/div[1]/div[1]/div[1]/div[2]/div[2]/p[1]')
    chiller_cfg_delete_warn_accept = (By.XPATH, '//*[@id="doNotDelete"]/div[1]/div[1]/div[1]/div[3]/ul[1]/li[1]/a[1]')
    chiller_cfg_delete_no = (By.XPATH, '//*[@id="deletemodal"]/div[1]/div[1]/div[1]/div[3]/ul/li[1]')
    chiller_cfg_loe = (By.XPATH,'//div[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/*')
    chiller_cfg_page_loe = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/dir-pagination-controls[1]/ul/li')
    chiller_cfg_page_first = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/dir-pagination-controls[1]/ul[1]/li[1]')
    chiller_cfg_page_previous = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/dir-pagination-controls[1]/ul[1]/li[2]')
    #Datapoint edit#
    dp_edit = (By.XPATH,'//*[@id="datapoint"]/div[2]/div[8]/ul/li')
    dp_edit_title = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]')
    dp_edit_write_btn = (By.XPATH,'//*[@id="writablePoint"]')
    dp_edit_write_txt = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li[8]/div['
                                  '1]/label')
    dp_edit_trend_btn = (By.XPATH,'//*[@id="inlineCheckbox3"]')
    dp_edit_trend_txt = (By.XPATH, '//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li[8]/div[2]/label')
    dp_details_name_lbl = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/label')
    dp_details_text_lbl = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/label')
    dp_details_tablename_lbl = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/label')
    dp_details_bacnetobj_name_lbl = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul['
                                              '1]/li[4]/label')
    dp_details_bacnetobj_id_lbl = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li['
                                            '5]/label')
    dp_details_ccn_lbl = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div['
                                                         '1]/ul[1]/li[6]/label')
    dp_details_unit_lbl = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div['
                                                          '2]/div[1]/ul[1]/li[7]/label')
    dp_details_name_val = (By.XPATH,'//*[@id="display-text"]')
    dp_details_text_val = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/div[1]/input[1]')
    dp_details_tablename_val = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li[' \
                                        '3]/div[1]/input[1]')
    dp_details_bacnetobj_name_val = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li[' \
                                        '4]/div[1]/input[1]')
    dp_details_bacnetobj_id_val = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li[' \
                                        '5]/div[1]/input[1]')
    dp_details_ccn_val = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li[' \
                                        '6]/div[1]/input[1]')
    dp_details_unit_val =  (By.XPATH,'//*[@id="unit"]')
    dp_edit_save = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/button[1]')
    dp_edit_ccn_err_msg = (By.XPATH,'//*[@id="myModal"]/div/div/form/div/div[2]/div[1]/ul/li[6]/div[3]')
    dp_edit_ccn_field_mand_msg = (By.XPATH, '//*[@id="myModal"]/div/div/form/div/div[2]/div[1]/ul/li[6]/div[2]')
    dp_edit_close = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/a')
    ##Data point prognostics#
    prog_title = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/h1[1]')
    prog_exit = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]')
    prog_btn = (By.XPATH,'//*[@id="datapoint"]/div[2]/div[7]/a[1]')
    prog_rule_dialog_title = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]')
    prog_rule_close = (By.XPATH, '//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]')
    prog_rule_save = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[3]/button[1]')
    prog_new_rule = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/button[1]')
    prog_new_ref_rule = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[6]/div[2]/button[1]')
    prog_rule_color = (By.XPATH,'//*[@id="myModal"]/div/div/form/div/div[2]/div/ul/li[4]/div/div/span')
    prog_rule_loe = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div/ul/li')
    prog_unit_btn = (By.XPATH,'//*[@id="dropdownMenu3"]')
    prog_unit_loe =(By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div/ul/li[3]/div/div/ul/li')
    prog_unitrr_loe = (By.XPATH, '//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div/ul/li[3]/div/div/ul/li')
    prog_color_sel = (By.XPATH,'//*[@id="myModal"]/div/div/form/div/div[2]/div/ul/li[4]/div/div/div/div[2]/div/div/div/div[1]')
    dp_color_loe = (By.XPATH,'//*[@id="myModal"]/div/div/form/div/div[2]/div/ul/li[4]/div/div/span')
    prog_rule_message = (By.XPATH,'//*[@id="myModal"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/div[1]/textarea')
    prog_cond_btn = (By.XPATH,'//*[@id="dropdownMenu3"]')
    progn_cond_loe =(By.XPATH,'//*[@id="myModalRR"]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/div[1]/div[1]/ul[1]/li')
    color_string = ['000000', '884513', 'FF0000', 'FF8C00', 'FA8072', '808000', 'BDB76B', '008000', '00BFFF', '008080',
                    '0000FF', '000080', 'FF00FF', '800080', 'F4D03F', '4682B4']
    rule_labels =['Minimum Value:*','Maximum Value:*','Units:*','Color Indicator:*','Message:*']
    reference_labels = ['Value:*','Units:*','Condition:*','Color Indicator:*','Massage:*']
    prog_err_msg = (By.XPATH,'//*[@id="content"]/div/div[2]/div[2]/div/div/span')
    prog_rule_max_err_msg = (By.XPATH,'//*[@id="myModal"]/div/div/form/div/div[2]/div/ul/li[1]/div[2]')
    prog_rule_min_err_msg = (By.XPATH,'//*[@id="myModal"]/div/div/form/div/div[2]/div/ul/li[2]/div[2]')
    prog_rule_msg_err_msg = (By.XPATH, '//*[@id="myModal"]/div/div/form/div/div[2]/div/ul/li[5]/div[2]')
    prog_rule_val_err_msg = (By.XPATH, '//*[@id="myModalRR"]/div/div/form/div/div[2]/div/ul/li[1]/div[2]')
    prog_rule_con_err_msg = (By.XPATH, '//*[@id="myModalRR"]/div/div/form/div/div[2]/div/ul/li[3]/div[2]')
    prog_rule_msg_err_msg = (By.XPATH, '//*[@id="myModalRR"]/div/div/form/div/div[2]/div/ul/li[5]/div[2]')
