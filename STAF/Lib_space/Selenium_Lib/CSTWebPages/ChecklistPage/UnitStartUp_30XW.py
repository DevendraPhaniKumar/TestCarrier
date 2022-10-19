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
from Page_locators.ChecklistPagelocators.UnitStartUp_locators import UnitStartUp_locators
from Page_locators.ChecklistPagelocators.ChecklistPage_locators import ChecklistPageLocators
from . import Checklist
from selenium.webdriver.common.by import By
import unittest
import datetime

driver = object
delay = 75
assertion = unittest.TestCase('__init__')

class UnitStartUp_30XW(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(UnitStartUp_30XW, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()

    def locator_name(self):
        ##########################################################  30XW  ##########################################################
        self.M30XW_INIT_write = []
        self.M30XW_INIT_tog = ['M30XW_INITCHECK_1A_Yes','M30XW_INITCHECK_1A_No','M30XW_INITCHECK_2A_Yes',
                               'M30XW_INITCHECK_2A_No','M30XW_INITCHECK_3A_Yes','M30XW_INITCHECK_3A_No','M30XW_INITCHECK_4A_Yes','M30XW_INITCHECK_4A_No','M30XW_INITCHECK_5A_Yes','M30XW_INITCHECK_5A_No','M30XW_INITCHECK_6E_Yes','M30XW_INITCHECK_6E_No','M30XW_INITCHECK_7O_Yes','M30XW_INITCHECK_7O_No','M30XW_INITCHECK_8R_Yes','M30XW_INITCHECK_8R_No','M30XW_INITCHECK_9R_Yes','M30XW_INITCHECK_9R_No','M30XW_INITCHECK_10L_Yes','M30XW_INITCHECK_10L_No','M30XW_INITCHECK_11V_Yes','M30XW_INITCHECK_11V_No','M30XW_INITCHECK_11ISTHE_Yes','M30XW_INITCHECK_11ISTHE_No','M30XW_INITCHECK_12VEFR_Yes','M30XW_INITCHECK_12VEFR_No','M30XW_INITCHECK_13VCFR_Yes','M30XW_INITCHECK_13VCFR_No']

        self.M30XW_INIT_swrite = ['M30XW_INITCHECK_Default','M30XW_INITCHECK_11AVGVOL_Val','M30XW_INITCHECK_11MAXDEV_Val','M30XW_INITCHECK_11VOLTIMB_Val','M30XW_INITCHECK_12A_Val','M30XW_INITCHECK_12B_Val','M30XW_INITCHECK_12C_Val','M30XW_INITCHECK_12D_Val','M30XW_INITCHECK_12EVAP_Val','M30XW_INITCHECK_13A_Val','M30XW_INITCHECK_13B_Val','M30XW_INITCHECK_13C_Val','M30XW_INITCHECK_13D_Val','M30XW_INITCHECK_CFR_Val']

        self.M30XW_SOM_swrite = []#['M30XW_SOM_Default', 'M30XW_SOM_5R_Val']
        self.M30XW_SOM_write = ['M30XW_SOM_5R_Val']
        self.M30XW_SOM_tog = [
'M30XW_SOM_1C_Yes','M30XW_SOM_1C_No','M30XW_SOM_2C_Yes','M30XW_SOM_2C_No','M30XW_SOM_3R_Yes','M30XW_SOM_3R_No','M30XW_SOM_4R_Yes','M30XW_SOM_4R_No','M30XW_SOM_REFCHARGE_AYes','M30XW_SOM_REFCHARGE_ANo','M30XW_SOM_REFCHARGE_BYes','M30XW_SOM_REFCHARGE_BNo','M30XW_SOM_OILCHARGE_AYes','M30XW_SOM_OILCHARGE_ANo','M30XW_SOM_OILCHARGE_BYes','M30XW_SOM_OILCHARGE_BNo'
]

        self.M30XW_RCISW_swrite = []
        self.M30XW_RCISW_tog = []
        self.M30XW_RCISW_write = ['M30XW_RSV_SPN_val2']

        self.M30XW_RCICFG_swrite = []
        self.M30XW_RCICFG_tog = []
        self.M30XW_RCICFG_write =['M30XW_RCI_PF60_btn_click','M30XW_RCI_PF60_Yes_click','M30XW_RCI_PF60_No',
                                  'M30XW_RCI_WDSS_btn_click','M30XW_RCI_WDSS_Yes_click','M30XW_RCI_WDSS_No',
                                  'M30XW_RCI_EMM_btn_click','M30XW_RCI_EMM_Yes_click','M30XW_RCI_EMM_No','M30XW_RCI_PASSENAB_btn_click','M30XW_RCI_PASSENAB_Yes_click','M30XW_RCI_PASSENAB_No','M30XW_RCI_MDOS_val','M30XW_RCI_LANGSEL_val','M30XW_RCI_UNITTYP_Val','M30XW_RCI_UCM_Val','M30XW_RCI_PSV_Val','M30XW_RCI_MTACA_Val','M30XW_RCI_MTARCA_Val','M30XW_RCI_MTACB_Val','M30XW_RCI_MTARCB_Val','M30XW_RCI_S1CSCA_Val','M30XW_RCI_S1CSRCA_Val',
'M30XW_RCI_S1CSCB_Val','M30XW_RCI_S1CSRCB_Val','M30XW_RCI_FACTPASS_Val','M30XW_RCI_CWVS_btn_click',
                                  'M30XW_RCI_CWVS_Yes_click','M30XW_RCI_CWVS_No','M30XW_RCI_HGBS_btn_click',
                                  'M30XW_RCI_HGBS_Yes_click','M30XW_RCI_HGBS_No','M30XW_RCI_HTDS_btn_click',
                                  'M30XW_RCI_HTDS_Yes_click','M30XW_RCI_HTDS_No','M30XW_RCI_CPN_Val',
                                  'M30XW_RCI_HCS_btn_click','M30XW_RCI_HCS_Yes_click','M30XW_RCI_HCS_No','M30XW_RCI_COOLFT_btn_click','M30XW_RCI_COOLFT_Water_click','M30XW_RCI_COOLFT_Brine','M30XW_RCI_CONDFT_btn_click','M30XW_RCI_CONDFT_Water_click','M30XW_RCI_CONDFT_Brine','M30XW_RCI_EXVMS_Val','M30XW_RCI_HPT_Val','M30XW_RCI_EXVASS_Val','M30XW_RCI_EXVBSS_Val','M30XW_RCI_EFC_btn_click','M30XW_RCI_EFC_Yes_click','M30XW_RCI_EFC_No','M30XW_RCI_ASWSML_btn_click','M30XW_RCI_ASWSML_Yes_click','M30XW_RCI_ASWSML_No','M30XW_RCI_BMFT_Val','M30XW_RCI_BFS_Val','M30XW_RCI_FLS_Val','M30XW_RCI_EWTPO_btn_click','M30XW_RCI_EWTPO_Yes_click','M30XW_RCI_EWTPO_No','M30XW_RCI_MAXC_btn_click','M30XW_RCI_MAXC_Yes_click','M30XW_RCI_MAXC_No','M30XW_RCI_ELEMENT_Val','M30XW_RCI_BUS_Val','M30XW_RCI_BAUD_Val','M30XW_RCI_CLS_Val','M30XW_RCI_SLS_Val','M30XW_RCI_RLS_btn_click','M30XW_RCI_RLS_Yes_click','M30XW_RCI_RLS_No','M30XW_RCI_UOTOD_Val','M30XW_RCI_ICEME_btn_click','M30XW_RCI_ICEME_Enable_click','M30XW_RCI_ICEME_Disable','M30XW_RCI_CONDPS_Val','M30XW_RCI_COOLPS_Val','M30XW_RCI_PARD_Val','M30XW_RCI_PSP_No','M30XW_RCI_PSP_btn_click','M30XW_RCI_PSP_Yes_click','M30XW_RCI_SPDS_No','M30XW_RCI_SPDS_btn_click','M30XW_RCI_SPDS_Yes_click','M30XW_RCI_FCIFCON_No','M30XW_RCI_FCIFCON_btn_click','M30XW_RCI_FCIFCON_Yes_click','M30XW_RCI_STATHOUR_Val','M30XW_RCI_ENDHOUR_Val','M30XW_RCI_CAPLIM_Val','M30XW_RCI_RAR_No','M30XW_RCI_RAR_btn_click','M30XW_RCI_RAR_Yes_click','M30XW_RCI_CLS1_No','M30XW_RCI_CLS1_btn_click','M30XW_RCI_CLS1_Yes_click','M30XW_RCI_CURRLIM_Val','M30XW_RCI_CRS_Val','M30XW_RCI_DLTS_Val','M30XW_RCI_MAFOR100_Val','M30XW_RCI_MAFOR0_Val','M30XW_RCI_MSS_Val','M30XW_RCI_SLAVEADD_Val','M30XW_RCI_LLSELECT_Val','M30XW_RCI_LLBAL_Val','M30XW_RCI_LST_Val','M30XW_RCI_SIEH_Val','M30XW_RCI_LMRT_Val','M30XW_RCI_LUPC_Val','M30XW_RCI_LPT_Val','M30XW_RCI_CHILLIS_No','M30XW_RCI_CHILLIS_btn_click','M30XW_RCI_CHILLIS_Yes_click','M30XW_RCI_COOLSP1_Val','M30XW_RCI_COOLSP2_Val','M30XW_RCI_COOLIS_Val','M30XW_RCI_CNRV_Val','M30XW_RCI_CFRV_Val','M30XW_RCI_DNRV_Val','M30XW_RCI_DFRV_Val','M30XW_RCI_ONRV_Val','M30XW_RCI_OFRV_Val','M30XW_RCI_SNRV_Val','M30XW_RCI_SFRV_Val','M30XW_RCI_CRDV_Val','M30XW_RCI_CRL_Val','M30XW_RCI_HSP1_Val','M30XW_RCI_HSP2_Val','M30XW_RCI_CCNRV_Val','M30XW_RCI_CCFRV_Val','M30XW_RCI_CDNRV_Val','M30XW_RCI_CDFRV_Val','M30XW_RCI_CONRV_Val','M30XW_RCI_COFRV_Val','M30XW_RCI_CHRDV_Val','M30XW_RCI_CHCS_Val','M30XW_RCI_CHRL_Val','M30XW_RCI_SLSP1_Val','M30XW_RCI_SLSP2_Val','M30XW_RCI_SLSP3_Val','M30XW_RCI_WVCS_Val','M30XW_RCI_NONE_Val','M30XW_RCI_SS_Val','M30XW_RCI_HS_Val']

        self.M30XW_CTMST_swrite = []
        self.M30XW_CTMST_tog = []
        self.M30XW_CTMST_write = ['M30XW_CT_STE_btn_click','M30XW_CT_STE_On_click','M30XW_CT_STE_Off',
                                  'M30XW_CT_CAO_btn_click','M30XW_CT_CAO_On_click','M30XW_CT_CAO_Off',
                                  'M30XW_CT_SVCA_Off','M30XW_CT_CBO_btn_click','M30XW_CT_CBO_On_click',
                                  'M30XW_CT_CBO_Off','M30XW_CT_SVCB_Val','M30XW_CT_QTE_btn_click',
                                  'M30XW_CT_QTE_On_click','M30XW_CT_QTE_Off','M30XW_CT_CAEP_Val','M30XW_CT_CBEP_Val',
                                  'M30XW_CT_CAEEP_Val','M30XW_CT_CBEEP_Val','M30XW_CT_CAFS_Val','M30XW_CT_CBFS_Val','M30XW_CT_CAVP_Val','M30XW_CT_CBVP_Val','M30XW_CT_CAOH_btn_click','M30XW_CT_CAOH_On_click','M30XW_CT_CAOH_Off','M30XW_CT_CASV1_btn_click','M30XW_CT_CASV1_On_click','M30XW_CT_CASV1_Off','M30XW_CT_CASV2_btn_click','M30XW_CT_CASV2_On_click','M30XW_CT_CASV2_Off','M30XW_CT_CAHGB_btn_click','M30XW_CT_CAHGB_On_click','M30XW_CT_CAHGB_Off','M30XW_CT_CAOS_btn_click','M30XW_CT_CAOS_On_click','M30XW_CT_CAOS_Off','M30XW_CT_CADCS_btn_click','M30XW_CT_CADCS_On_click','M30XW_CT_CADCS_Off','M30XW_CT_CBOH_btn_click','M30XW_CT_CBOH_On_click','M30XW_CT_CBOH_Off','M30XW_CT_CBSV1_btn_click','M30XW_CT_CBSV1_On_click','M30XW_CT_CBSV1_Off','M30XW_CT_CBSV2_btn_click','M30XW_CT_CBSV2_On_click','M30XW_CT_CBSV2_Off','M30XW_CT_CBHGB_btn_click','M30XW_CT_CBHGB_On_click','M30XW_CT_CBHGB_Off','M30XW_CT_CBOS_btn_click','M30XW_CT_CBOS_On_click','M30XW_CT_CBOS_Off','M30XW_CT_CBDCS_btn_click','M30XW_CT_CBDCS_On_click','M30XW_CT_CBDCS_Off','M30XW_CT_WEP1_btn_click','M30XW_CT_WEP1_On_click','M30XW_CT_WEP1_Off','M30XW_CT_WEP2_btn_click','M30XW_CT_WEP2_On_click','M30XW_CT_WEP2_Off','M30XW_CT_CHO_btn_click','M30XW_CT_CHO_On_click','M30XW_CT_CHO_Off','M30XW_CT_CAHBV_btn_click','M30XW_CT_CAHBV_Open_click','M30XW_CT_CAHBV_Close','M30XW_CT_CBHBV_btn_click','M30XW_CT_CBHBV_Open_click','M30XW_CT_CBHBV_Close','M30XW_CT_CRS_btn_click','M30XW_CT_CRS_On_click','M30XW_CT_CRS_Off','M30XW_CT_CRO_btn_click','M30XW_CT_CRO_On_click','M30XW_CT_CRO_Off','M30XW_CT_CSO_btn_click','M30XW_CT_CSO_On_click','M30XW_CT_CSO_Off','M30XW_CT_CHILCI_Val','M30XW_CT_ALARMRO_btn_click','M30XW_CT_ALARMRO_On_click','M30XW_CT_ALARMRO_Off','M30XW_CT_ALERTRO_btn_click','M30XW_CT_ALERTRO_On_click','M30XW_CT_ALERTRO_Off']


        self.M30XW_OPDATA_swrite = []
        self.M30XW_OPDATA_tog = []
        self.M30XW_OPDATA_write = ['M30XW_OD_1C_Val','M30XW_OD_2C_Val','M30XW_OD_3C_Val','M30XW_OD_4C_Val','M30XW_OD_5C_Val','M30XW_OD_6C_Val','M30XW_OD_7LL_Val','M30XW_OD_CIRA_click','M30XW_OD_SCTA_Val','M30XW_OD_SSTA_Val','M30XW_OD_SGTA_Val','M30XW_OD_SUPA_Val','M30XW_OD_ECTA_Val','M30XW_OD_ESHA_Val','M30XW_OD_CTPA_Val','M30XW_OD_EXVA_Val','M30XW_OD_ECOA_Val','M30XW_OD_CIRB_click','M30XW_OD_SCTB_Val','M30XW_OD_SSTB_Val','M30XW_OD_SGTB_Val','M30XW_OD_SUPB_Val','M30XW_OD_ECTB_Val','M30XW_OD_ESHB_Val','M30XW_OD_CTPB_Val','M30XW_OD_EXVB_Val','M30XW_OD_ECOB_Val','M30XW_OD_A1_click','M30XW_OD_A1L1_Val','M30XW_OD_A1L2_Val','M30XW_OD_A1L3_Val','M30XW_OD_B1_click','M30XW_OD_B1L1_Val','M30XW_OD_B1L2_Val','M30XW_OD_B1L3_Val']

        self.prefix = {'initial': 'M30XW_INIT', 'start': 'M30XW_SOM', 'record1': 'M30XW_RCISW', 'record2': 'M30XW_RCICFG','component': 'M30XW_CTMST','operating': 'M30XW_OPDATA' }
    def write_data(self, Data):
        for i in range(len(eval("self." + self.prefix[Data['Model']] + "_write"))):
            if "_Val" in eval("self." + self.prefix[Data['Model']] + "_write[i]") or "_val" in eval(
                    "self." + self.prefix[Data['Model']] + "_write[i]"):
                xpath = eval("UnitStartUp_locators." + eval("self." + self.prefix[Data['Model']] + "_write[i]"))
                try:
                    self.checklist.write(xpath, Data)
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),i,'Written UnitStartUp data of '  + eval(
                        "self." + self.prefix[Data['Model']] + "_write[i]") + ' =', \
                        Data['testdata'])
                except:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),i, "Error: ",\
                        eval("self." +      self.prefix[Data[  'Model']] +"_write[i]"),"=",Data['testdata'])
            elif "click" in eval("self." + self.prefix[Data['Model']] + "_write[i]"):
                self.checklist.click(eval("self." + self.prefix[Data['Model']] + "_write[i]"), "UnitStartUp_locators")
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), i, 'Selected UnitStartUp data of ' \
                                                                                 + eval("self." + self.prefix[Data['Model']] + "_write[i]"))
        try:
            xpath = eval("UnitStartUp_locators." + eval("self."+self.prefix[Data['Model']]+"_swrite[0]"))
            xpath = self.find_elements(*xpath)
            for i in range(len(eval("self."+self.prefix[Data['Model']]+"_swrite"))):
                if "_Default" not in eval("self."+self.prefix[Data['Model']]+"_swrite[i]"):
                    self.checklist.write_similar_element(xpath= xpath, index= eval("UnitStartUp_locators." + eval("self."+self.prefix[Data['Model']]+"_swrite[i]")), Data= Data)
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),i,'Written UnitStartUp data to ' + str(eval("self."+self.prefix[Data['Model']]+"_swrite[i]")) \
                           + ' =', Data['testdata'])
        except IndexError as e:
            print(e.message)

        for y in range(len(eval('self.' + self.prefix[Data['Model']] + '_tog'))):
            if eval('self.' + self.prefix[Data['Model']] + '_tog')[y][-3:] == 'Yes':
                xpath = eval('self.' + self.prefix[Data['Model']] + '_tog')[y]
                self.checklist.click(xpath, page_locators="UnitStartUp_locators")
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),y,'Written UnitStartUp data of ' + xpath\
                                                                               + ' =', 'Yes')

    def read_data(self, Data):
        for ele in eval("self." + self.prefix[Data['Model']] + "_write"):
            if ele != self.prefix[Data['Model']] + "_Default":
                common_xpath = eval(
                    "UnitStartUp_locators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read_normal',
                                            page_locators="UnitStartUp_locators")
                if '_Val' in ele[-6:]:
                    try:
                        assertion.assertEqual(float(value) == float(
                            ''.join(filter(str.isdigit, str(Data['testdata'])[:8]))), True)
                        print('Read UnitStartUP Data (' + ele + ')' + ' =', value)
                    except Exception as e:
                        print("********************************************************************************************************************************\n" \
                              "88888888888888888888888888888888888888888888888888888888888   ERROR   8888888888888888888888888888888888888888888888888888888888\n" \
                              "********************************************************************************************************************************")
                        print(e.message)
                        print('Read UnitStartUP Data (' + ele + ')' + ' =', value)
                elif '_val' in ele[-6:]:
                    try:
                        assertion.assertEqual(value == str(Data['testdata'])[:8], True)
                        print('Read Chiller Name Plate Data Information(' + ele + ')' + ' =', value)
                    except Exception as e:
                        print("********************************************************************************************************************************\n" \
                              "88888888888888888888888888888888888888888888888888888888888   ERROR   8888888888888888888888888888888888888888888888888888888888\n" \
                              "********************************************************************************************************************************")
                        print(e.message)
                        print('Read UnitStartUP Data (' + ele + ')' + ' =', value)
                elif 'drop' in ele[-4:]:
                    pass
                elif 'Desc' in ele[-4:]:
                    pass
                elif 'Val' in ele[-3:]:
                    assertion.assertEqual(value == str(Data['testdata'][:eval(ele[-2:])]), True)
                elif 'CheckBox' in ele[-8:]:
                    pass
                elif 'time' in ele[-4:]:
                    pass
                elif 'Btn' in ele[-3:]:
                    pass

        for ele in eval("self."+self.prefix[Data['Model']]+"_tog"):
            value = self.checklist.read(ele, None, Data, 'yes|no', page_locators="UnitStartUp_locators")
            if ele[-3:] == 'Yes':
                assertion.assertEqual(value == 'true', True)
            elif ele[-2:] == 'No':
                assertion.assertEqual(value == None, True)
            print('Read UnitStartUP Information of '+ ele+' = ', value)

    def read_reset_data(self, Data):
        for ele in eval("self." + self.prefix[Data['Model']] + "_write"):
            if ele != self.prefix[Data['Model']] + "_Default":
                common_xpath = eval(
                    "UnitStartUp_locators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read_normal',
                                            page_locators="UnitStartUp_locators", index_assert=5)
                if 'drop' in ele[-4:]:
                    pass
                elif 'CheckBox' in ele[-8:]:
                    pass
                elif '_Val' in ele[-6:] or '_val' in ele[-6:]:
                    try:
                        assertion.assertEqual(value == '', True)
                    except:
                        try:
                            assertion.assertEqual(value == None, True)
                        except Exception as e:
                            print("********************************************************************************************************************************\n" \
                                  "88888888888888888888888888888888888888888888888888888888888   ERROR   8888888888888888888888888888888888888888888888888888888888\n" \
                                  "********************************************************************************************************************************")
                            print(e.message)

                print('Read UnitStartUP Data of ' + ele + ' = ', 'Null' if value == '' else value)

        for ele in eval("self."+self.prefix[Data['Model']]+"_tog"):
            value = self.checklist.read(ele, None, Data, 'reset_yes|no', page_locators="UnitStartUp_locators")
            if ele[-3:] == 'Yes':
                assertion.assertEqual(value == None, True)
            elif ele[-2:] == 'No':
                assertion.assertEqual(value == 'true', True)
            print('Read UnitStartUp Information of ' + ele + ' = ', value)

    def unitstartup_exit(self):
        self.find_element(*UnitStartUp_locators.unitstartup_exit).click()

    def unitstartup_savesubmenu(self):
        self.find_element(*UnitStartUp_locators.unitstartup_savesubmenu).click()

    def unitstartup_savemainmenu(self):
        self.find_element(*UnitStartUp_locators.unitstartup_savemainmenu).click()

    def unitstartup_save(self):
        self.find_element(*UnitStartUp_locators.unitstartup_save).click()

    def unitstartup_cancel(self):
        self.find_element(*UnitStartUp_locators.unitstartup_cancel).click()

    def startup_form_cancle(self):
        self.find_element(*ChecklistPageLocators.unitstartup_cancel).click()

    def startup_form_reset(self):
        self.find_element(*ChecklistPageLocators.unitstartup_exit).click()

    def startup_form_exit(self):
        self.find_element(*ChecklistPageLocators.unitstartup_exit).click()

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