from selenium.webdriver.common.by import By
#Updated by Uday 13-Oct-2018

class ChillerinfoPageLocators(object):
    chiller_model=(By.XPATH,'//*[@id="top"]/div[1]/div[1]/div[1]/div[3]/ul[1]/li[5]/div[1]/span[1]')
    chiller_cfg_btn=(By.XPATH,'//*[@id="content"]/div/ng-include/div/div/div/ul/li[1]/a')
    chiller_version = (By.XPATH,'//*[@id="top"]/div[1]/div[1]/div[1]/div[3]/ul[1]/li[5]/div[1]/span[2]')
    #chiller_srno = (By.XPATH,'//*[@id="content"]/div/ng-include/div/div/div/ul/li[2]/span[1]')
    #chiller_Loc_sw_ver =(By.XPATH,'//*[@id="content"]/div/ng-include/div/div/div/ul/li[2]/span[2]')
    chiller_connection = (By.XPATH,'//*[@id="content"]/div/ng-include/div/div/div/ul/li[3]')
    chillerinfo_btn = (By.XPATH, '//*[@id="side"]/div/div[2]/ul/li[3]')
    chiller_run_status = (By.XPATH,'//*[@id="content"]/div/div[2]/div[2]/div/div[1]/div/ul/li[2]')
    chiller_maint = (By.XPATH, '//*[@id="content"]/div/div[1]/div/div[1]/ul/li[2]')
    chiller_status = (By.XPATH, '//*[@id="content"]/div/div[2]/div/div[1]/ul/li[1]')
    chiller_status1 = (By.XPATH, '//*[@id="content"]/div/div[2]/div/div[1]/ul/li')
    chiller_cfg = (By.XPATH, '//*[@id="content"]/div/div[1]/div/div[1]/ul/li[3]')
    chiller_service = (By.XPATH, '//*[@id="content"]/div/div[1]/div/div[1]/ul/li[4]')
    chiller_setpoint = (By.XPATH, '//*[@id="content"]/div/div[1]/div/div[1]/ul/li[5]')
    dtable_LOE = (By.XPATH,'//*[@id="content"]/div/div[4]/div[3]/div/div/div/ul/li')
    dtable_title = (By.XPATH,'//*[@id="dataPointList"]/div[1]/div[1]/div[1]/value-display[1]/div[1]/div[1]/span[1]')
    table_text = (By.XPATH,'//*[@id="content"]/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div[1]/h3[1]')
    table_header = (By.XPATH,'//*[@id="content"]/div[1]/div[4]/div[3]/div[2]/div[1]')
    table_loe =(By.XPATH,'//*[@id="content"]/div[1]/div[4]/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr')
    dtable_Category_LOE = (By.XPATH,'//*[@id="content"]/div/div[1]/div[1]/div/ul')
    no_data_display =(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/h4[1]')
    loader= (By.XPATH,'//*[@id="spanLoader"]')
    #Trace Record
    trace_btn = (By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div/div[1]/div/ul/li[1]/button[1]')
    trace_btn_lbl = (By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div/div[1]/div/ul/li[1]/button[1]/cst')
    trace_history_btn = (By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div/div[1]/div/ul/li[1]/button[2]')

    refresh = (By.XPATH, '//*[@id="content"]/div[1]/div[3]/div[1]/div[2]/i[1]')
    search_object_input = (By.XPATH,'//*[@id="content"]/div[1]/div[3]/div[2]/div[1]/div[1]/input[1]')

    record_sts_icon = (By.XPATH,'//*[@id="top"]/div/div[1]/div/div[2]/ul/li[4]/a[1]')
    record_sts_popover_msg = (By.XPATH,'//*[@id="top"]/div/div[1]/div/div[2]/ul/li[4]/a[2]')
    record_type_lbl=(By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[1]/label')
    record_type_btn = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[1]/div/button')
    record_type_loe= (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[1]/div/ul/li')

    record_interval_lbl = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/b/b/div[3]/div/div[1]/label')
    record_interval_val=(By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/b/b/div[3]/div/div['
                                  '2]/span')

    record_interval_input = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/b/b/div[3]/div/div[2]/input')
    record_time_interval_input = (
    By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[5]/div[2]/input')

    record_strt_date_lbl =(By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div['                                 '1]/div[1]/label')

    record_strt_date_val=(By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[1]/div[2]/p/input')
    record_strt_date_btn = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[1]/div[2]/p/span/button')
    record_strt_date_cal= (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div['
                                   '1]/div[2]/p/div/ul')
    record_strt_date_cal_today = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[1]/div[2]/p/div/ul/li[2]/span/button[1]')
    record_strt_date_cal_close = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[1]/div[2]/p/div/ul/li[2]/button')
    record_strt_time_lbl=(By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[2]/div/div[1]/label')
    record_strt_time_hr=(By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/input')
    record_strt_time_min=(By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[2]/div/div[2]/table/tbody/tr[2]/td[3]/input')
    record_strt_time_ampm=(By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[2]/div/div[2]/table/tbody/tr[2]/td[6]/button')

    record_end_date_lbl = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div['
                                      '3]/div[1]/label')
    record_end_date_val = ( By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div['
                                      '3]/div[2]/p/input')
    record_end_date_cal = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div['
                                      '3]/div[2]/p/div/ul')
    record_end_date_btn = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div['
                                     '3]/div[2]/p/span/button')
    record_end_date_cal_today = (By.XPATH,
                                  '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[3]/div['
                                  '2]/p/div/ul/li[2]/span/button[1]')
    record_end_date_cal_close = (By.XPATH,
                                  '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[3]/div['
                                  '2]/p/div/ul/li[2]/button')
    record_end_time_lbl = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[4]/div/div[1]/label')
    record_end_time_hr = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[4]/div/div[2]/table/tbody/tr[2]/td[1]/input')
    record_end_time_min = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[4]/div/div[2]/table/tbody/tr[2]/td[3]/input')
    record_end_time_ampm = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[4]/div/div[2]/table/tbody/tr[2]/td[6]/button')

    record_stop_prompt_yes = (By.XPATH, '//*[@id="recordWarn"]/div/div/div[3]/ul/li[1]/a')
    record_stop_prompt_no = (By.XPATH, '//*[@id="recordWarn"]/div/div/div[3]/ul/li[2]/a')
    record_save_btn= (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/b/b/div[3]/button[1]')
    record_time_save_btn=(By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div['
                                  '6]/button[1]')

    record_exit=(By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/b/b/div[3]/button[2]')
    record_time_exit_btn = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div['
                                      '6]/button[1]')
    record_time_err_msg= (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/b/b/div[4]/div/span')
    record_err_msg =(By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/b/b/div[4]/div/span')
    ccn_point =(By.XPATH,"//*[@id='content']/div/div[2]/div/div[1]/ng-include/div/div[1]/\
                  div/div[2]/div/div[1]/div/value-display/div/div[2]/span[1]")
    month_name= ['January','February','March','April','May','June','July','August','September','October','November','December']
    month_pick =(By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[1]/div['
                          '2]/p/div/ul/li[1]/div/table/thead/tr[1]/th[2]/button')

    year_pick =(By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[2]/form/div[1]/div[2]/p/div/ul/li[1]/div/table/thead/tr/th[2]/button')
    record_data_table_lbl= (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include[1]/div[1]/div[2]/b[1]/b[1]/div[1]/div[1]/div[1]/div[1]')
    record_data_table_lst = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/b/b/div/div/div[1]/div['
                                      '2]/div')
    record_data_pts_lbl = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include[1]/div[1]/div[2]/b[1]/b[1]/div[1]/div[1]/div[2]/div[1]')
    record_data_pts_lst = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/b/b/div/div/div[2]/div['
                                    '2]/div')
    record_data_summary_pts_lbl = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include[1]/div[1]/div[2]/b[1]/b[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]')
    record_data_summary_pts_lst = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/b/b/div/div/div['
                                         '3]/div[2]/div')
    record_data_empty_msg = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include[1]/div[1]/div[2]/b[1]/b[1]/div[1]/div[1]/div[2]/div[2]')
    record_data_empty_msg_txt='Please select a table'
    record_data_summary_empty_msg = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include[1]/div[1]/div[2]/b[1]/b[1]/div[1]/div[1]/div[3]/div[2]')
    record_data_summary_empty_msg_txt = 'Selected datapoints displayed here.'
    record_data_selectall_lbl =(By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include[1]/div[1]/div[2]/b[1]/b[1]/div[1]/div[1]/div[2]/div[2]/div[1]/label[1]/span[1]')
    record_data_selectall_chk = (By.XPATH,
                                 '//*[@id="content"]/div[1]/div[2]/ng-include[1]/div[1]/div[2]/b[1]/b[1]/div[1]/div['
                                 '1]/div[2]/div[2]/div[1]/label[1]/input')
    record_data_summary_clrall = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include[1]/div[1]/div[2]/b[1]/b[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]')
    table_sel_list = ['SETPOINT','COMPRESS','HEAT_EX','MAINSTAT','ISM_STAT','STARTUP','GENUNIT','INPUTS',
                      'TEMP','PRESSURE','STATUS01','STATUS02','STATUS03','LEADLAG','HYDRALIC','OPTIONS']

    trig_err_msg = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/b/b/div[4]/div/span')
    trg_strt_lbl = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/div/b')
    trg_strt_dp_lbl = (
    By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[1]/div[1]/label')
    trg_strt_dp_val_btn = (
    By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[1]/div[2]/div/button')
    trg_strt_dp_val_search =(By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[1]/div[2]/div/ul/input')
    trg_strt_dp_val_lst = (
    By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[1]/div[2]/div/ul/li')
    trg_strt_cond_lbl = (
    By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[2]/div[1]/label')
    trg_strt_cond_btn = (
    By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[2]/div[2]/button')
    trg_strt_cond_lst = (
    By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[2]/div[2]/ul/li')
    trg_strt_val_lbl = (
    By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[3]/div[1]/label')
    trg_strt_val_input = (
    By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[3]/div[2]/input')
    trg_end_lbl = (
    By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[4]/div/b')
    trg_end_dp_lbl = (By.XPATH,
                      '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[4]/b/div[1]/div[1]/label')
    trg_end_dp_btn = (By.XPATH,
                          '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[4]/b/div[1]/div[2]/div/button')
    trg_end_dp_search = (
    By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[4]/b/div[1]/div[2]/div/ul/input')
    trg_end_dp_val_lst = (By.XPATH,
                          '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[4]/b/div[1]/div[2]/div/ul/li')
    trg_end_cond_lbl = (By.XPATH,
                        '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[4]/b/div[2]/div[1]/label')
    trg_end_cond_btn = (By.XPATH,
                        '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[4]/b/div[2]/div[2]/button')
    trg_end_cond_lst = (By.XPATH,
                        '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[4]/b/div[2]/div[2]/ul/li')
    trg_end_val_lbl = (By.XPATH,
                       '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[4]/b/div[3]/div[1]/label')
    trg_end_val_input = (By.XPATH,
                         '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/div[4]/b/div[3]/div[2]/input')
    trg_interval_lbl = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/b/div[1]/div[1]/label')
    trg_interval_in = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/b/div[1]/div[2]/input')
    trg_save_btn = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/b/div[2]/button[1]')
    trg_exit_btn = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ng-include/div/div[2]/div/div[3]/div/form/b/b/div[2]/button[2]')
    trace_hist_lbl = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include[1]/div[1]/div[1]/h1[1]')
    trace_hist_exit = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include[1]/div[1]/div[1]/ul[1]/li[1]/a[1]')
    trace_hist_search_input = (By.XPATH,'//*[@id="search"]')
    trace_history_search_btn = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include[1]/div[1]/div[1]/ul[1]/li['
                                         '2]/button')
    trace_hist_table_header = (By.XPATH,'//*[@id="content"]/div[1]/div[2]/ng-include[1]/div[1]/div[2]/div[1]/div[1]')
    trace_hist_table_list = (By.XPATH,'//div[@id="content"]/div[1]/div[2]/ng-include[1]/div[1]/div[2]/div/div[2]/div')
    trace_hist_status_complete = 'check_circle'
    trace_hist_status_recording = 'fiber_manual_record'
    trace_hist_status_error = 'error_outline'
    trace_hist_status_stop = 'stop'
    trace_hist_stop_record = (By.XPATH,'//*[@id="alertPopup"]/div/div/div/div[1]/div[1]')
    trace_hist_stop_record_txt = (By.XPATH,'//*[@id="alertPopup"]/div/div/div/div[2]/div[2]/p')
    trace_hist_stop_record_yes = (By.XPATH, '//*[@id="alertPopup"]/div[1]/div[1]/div[1]/div[3]/ul/li[1]')
    trace_hist_stop_record_no = (By.XPATH, '//*[@id="alertPopup"]/div[1]/div[1]/div[1]/div[3]/ul/li[2]')
    trace_hist_item_delete_title = (By.XPATH,'//*[@id="alertPopup"]/div/div/div/div[1]/div[1]')
    trace_hist_item_delete_txt = (By.XPATH, '//*[@id="alertPopup"]/div/div/div/div[2]/div[2]')
    trace_hist_item_delete_yes = (By.XPATH, '//*[@id="alertPopup"]/div/div/div/div[3]/ul/li[1]/a')
    trace_hist_item_delete_no = (By.XPATH, '//*[@id="alertPopup"]/div/div/div/div[3]/ul/li[2]/a')
    #*******Trace history reports
    trace_reports_search_input = (By.XPATH, '//*[@id="trendReport"]/div[9]/ng-include/div[1]/div[1]/ul/li[2]/input')
    trace_reports_search_btn = (By.XPATH, '//*[@id="trendReport"]/div[9]/ng-include/div[1]/div[1]/ul/li[2]/button')
    trace_reports_table_header = (By.XPATH, '//*[@id="trendReport"]/div[9]/ng-include/div[1]/div[2]/div/div[1]')

    trace_reports_status_complete = 'check_circle'
    trace_reports_status_recording = 'fiber_manual_record'
    trace_reports_status_error = 'error_outline'
    trace_reports_status_stop = 'stop'
    trace_reports_stop_record = (By.XPATH, '//*[@id="alertPopup"]/div/div/div/div[1]/div[1]')
    trace_reports_stop_record_txt = (By.XPATH, '//*[@id="alertPopup"]/div/div/div/div[2]/div[2]/p')
    trace_reports_stop_record_yes = (By.XPATH, '//*[@id="alertPopup"]/div/div/div/div[3]/ul/li[1]/a')
    trace_reports_stop_record_no = (By.XPATH, '//*[@id="alertPopup"]/div/div/div/div[3]/ul/li[2]/a')
    trace_reports_item_delete_title = (By.XPATH, '//*[@id="alertPopup"]/div[1]/div[1]/div[1]/div[1]/div[1]')
    trace_reports_item_delete_txt = (By.XPATH, '//*[@id="alertPopup"]/div[1]/div[1]/div[1]/div[2]/div[2]/p[1]')
    trace_reports_item_delete_yes = (By.XPATH, '//*[@id="alertPopup"]/div[1]/div[1]/div[1]/div[3]/ul/li[1]/a')
    trace_reports_item_delete_no = (By.XPATH, '//*[@id="alertPopup"]/div[1]/div[1]/div[1]/div[3]/ul/li[1]/a')
    trace_reports_lbl = (By.XPATH,'//*[@id="trendReport"]/div[9]/ng-include[1]/div[1]/div[1]/h1[1]')