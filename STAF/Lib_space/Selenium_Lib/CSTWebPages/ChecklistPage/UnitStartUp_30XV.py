import re
import os
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import datetime
dirnameutils = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dirnameutils)
# sys.path.append(dirnameutils+'\Selenium_Lib')
from Lib_Space.Selenium_Lib.BaseClass import Page
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPagelocators.UnitStartUp_locators import UnitStartUp_locators
from Lib_Space.Selenium_Lib.Page_locators.ChecklistPagelocators.ChecklistPage_locators import ChecklistPageLocators
from . import Checklist
from selenium.webdriver.common.by import By
import unittest
import time
sys.path.append(dirnameutils+'\TestCasesEtoE')
import read_csv
driver = object
delay = 75
assertion = unittest.TestCase('__init__')

class UnitStartUp_30XV(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(UnitStartUp_30XV, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()

    def locator_name(self):
        ##########################################################  30XV  ##########################################################
        self.M30XV_INIT_write = []
        self.M30XV_INIT_swrite = ['M30XV_INITCHECK_Default','M30XV_INITCHECK_7AB_Val','M30XV_INITCHECK_7AC_Val',
                                 'M30XV_INITCHECK_7BC_Val','M30XV_INITCHECK_7MAXDEV_Val','M30XV_INITCHECK_8A_Val','M30XV_INITCHECK_8B_Val','M30XV_INITCHECK_8C_Val','M30XV_INITCHECK_8D_Val','M30XV_INITCHECK_8E_Val','M30XV_INITCHECK_8F_Val']
        self.M30XV_INIT_tog = ['M30XV_INITCHECK_1A_No','M30XV_INITCHECK_1A_Yes','M30XV_INITCHECK_2V_No',
                               'M30XV_INITCHECK_2V_Yes','M30XV_INITCHECK_3A_No','M30XV_INITCHECK_3A_Yes',
                               'M30XV_INITCHECK_4E_No','M30XV_INITCHECK_4E_Yes','M30XV_INITCHECK_5O_No',
                               'M30XV_INITCHECK_5O_Yes','M30XV_INITCHECK_6L_No','M30XV_INITCHECK_6L_Yes',
                               ' M30XV_INITCHECK_7V_Yes',' M30XV_INITCHECK_7V_No','M30XV_INITCHECK_7ISTHE_No','M30XV_INITCHECK_7ISTHE_Yes','M30XV_INITCHECK_8VCFR_No','M30XV_INITCHECK_8VCFR_Yes']
        self.M30XV_SOM_write = ['M30XV_SOM_TOUCHPILOT_Val']
        self.M30XV_SOM_swrite =[]# ['M30XV_SOM_Default','M30XV_SOM_TOUCHPILOT_Val']

        self.M30XV_SOM_tog = ['M30XV_SOM_1C_No','M30XV_SOM_1C_Yes','M30XV_SOM_2O_No','M30XV_SOM_2O_Yes','M30XV_SOM_3O_No','M30XV_SOM_3O_Yes','M30XV_SOM_4C_No','M30XV_SOM_4C_Yes','M30XV_SOM_5R_No','M30XV_SOM_5R_Yes','M30XV_SOM_6R_No','M30XV_SOM_6R_Yes','M30XV_SOM_7P_No','M30XV_SOM_7P_Yes','M30XV_SOM_OILCHARGE_ANo','M30XV_SOM_OILCHARGE_AYes','M30XV_SOM_OILCHARGE_BNo','M30XV_SOM_OILCHARGE_BYes','M30XV_SOM_REFCHARGE_ANo','M30XV_SOM_REFCHARGE_AYes','M30XV_SOM_REFCHARGE_BNo','M30XV_SOM_REFCHARGE_BYes']
        self.M30XV_RCI_swrite = []
        self.M30XV_RCI_write = ['M30XV_RCI_BFS_Val','M30XV_RCI_BMFT_Val','M30XV_RCI_CFRV_Val','M30XV_RCI_CFT_Val',
                                'M30XV_RCI_CHDS_Val','M30XV_RCI_CIS_Val','M30XV_RCI_CSP1_Val','M30XV_RCI_CSP2_Val','M30XV_RCI_CNRV_Val','M30XV_RCI_CONDFT_Val','M30XV_RCI_COU_Val','M30XV_RCI_CPN_Val','M30XV_RCI_CPO_Val','M30XV_RCI_CPS_Val','M30XV_RCI_CRDV_Val','M30XV_RCI_CRL_Val','M30XV_RCI_CRS_Val','M30XV_RCI_CSP1_Val','M30XV_RCI_DCS_Val','M30XV_RCI_DFRV_Val','M30XV_RCI_DLT_Val','M30XV_RCI_DNRV_Val','M30XV_RCI_DPGV_Val','M30XV_RCI_EASN_Val','M30XV_RCI_EBSN_Val','M30XV_RCI_EFC_Val','M30XV_RCI_EMM_Val','M30XV_RCI_EOCA_Val','M30XV_RCI_EOCB_Val','M30XV_RCI_EWT_Val','M30XV_RCI_EXVA_Val','M30XV_RCI_EXVB_Val','M30XV_RCI_FACTPASS_Val','M30XV_RCI_FANOFFA_Val','M30XV_RCI_FANOFFB_Val','M30XV_RCI_FCI_Val','M30XV_RCI_FCR_Val','M30XV_RCI_FLN_Val','M30XV_RCI_FOO_Val','M30XV_RCI_FSS_Val','M30XV_RCI_IME_Val','M30XV_RCI_IPGV_Val','M30XV_RCI_LANG_Val','M30XV_RCI_LCD_Val','M30XV_RCI_LCT_Val','M30XV_RCI_LCTIMER_Val','M30XV_RCI_LLBD_Val','M30XV_RCI_LLS_Val','M30XV_RCI_LLST_Val','M30XV_RCI_LMRT_Val','M30XV_RCI_LPT_Val','M30XV_RCI_LUPC_Val','M30XV_RCI_MCT_Val','M30XV_RCI_MES_Val','M30XV_RCI_METRIC_Val','M30XV_RCI_MPL_Val','M30XV_RCI_MSL_Val','M30XV_RCI_MSS_Val','M30XV_RCI_NCL_Val','M30XV_RCI_NFDA_Val','M30XV_RCI_NFDB_Val','M30XV_RCI_NME_Val','M30XV_RCI_NMS_Val','M30XV_RCI_NVC_Val','M30XV_RCI_OFRV_Val','M30XV_RCI_ONRV_Val','M30XV_RCI_PAR_Val','M30XV_RCI_PFS_Val','M30XV_RCI_PLS_Val','M30XV_RCI_PPGV_Val','M30XV_RCI_PSP_Val','M30XV_RCI_PSV_Val','M30XV_RCI_QMC_Val','M30XV_RCI_RFI_Val','M30XV_RCI_RLS_Val','M30XV_RCI_SCDC_Val','M30XV_RCI_SERVPASS_Val','M30XV_RCI_SFDC_Val','M30XV_RCI_SFRV_Val','M30XV_RCI_SIEH_Val','M30XV_RCI_SLS1_Val','M30XV_RCI_SLS2_Val','M30XV_RCI_SLS3_Val','M30XV_RCI_SLVADD_Val','M30XV_RCI_SNRV_Val','M30XV_RCI_SP_Val','M30XV_RCI_SPD_Val','M30XV_RCI_UNITCAP_Val','M30XV_RCI_UNITS_Val','M30XV_RCI_UNITTYPE_Val','M30XV_RCI_UOT_Val','M30XV_RCI_USERPASS_Val','M30XV_RCI_VMAXS_Val','M30XV_RCI_VMINS_Val']
        self.M30XV_RCI_write_auto = ["M30XV_RCI_SP_Val",	"M30XV_RCI_CPS_Val",	"M30XV_RCI_RLS_Val",	"M30XV_RCI_UOT_Val",	"M30XV_RCI_DLT_Val",	"M30XV_RCI_NMS_Val",	"M30XV_RCI_NME_Val",	"M30XV_RCI_NCL_Val",	"M30XV_RCI_IME_Val",	"M30XV_RCI_CPS1_Val",	"M30XV_RCI_PAR_Val",	"M30XV_RCI_PSP_Val",	"M30XV_RCI_SPD_Val",	"M30XV_RCI_FCI_Val",	"M30XV_RCI_CPO_Val",	"M30XV_RCI_USERPASS_Val",	"M30XV_RCI_ONRV_Val",	"M30XV_RCI_OFRV_Val",	"M30XV_RCI_DNRV_Val",	"M30XV_RCI_DFRV_Val",	"M30XV_RCI_CNRV_Val",	"M30XV_RCI_CFRV_Val",	"M30XV_RCI_SNRV_Val",	"M30XV_RCI_SFRV_Val",	"M30XV_RCI_CRDV_Val",	"M30XV_RCI_UNITTYPE_Val",	"M30XV_RCI_UNITCAP_Val",	"M30XV_RCI_PFS_Val",	"M30XV_RCI_PSV_Val",	"M30XV_RCI_EMM_Val",	"M30XV_RCI_MSL_Val",	"M30XV_RCI_CPN_Val",	"M30XV_RCI_MES_Val",	"M30XV_RCI_DCS_Val",	"M30XV_RCI_EXVA_Val",	"M30XV_RCI_EXVB_Val",	"M30XV_RCI_EASN_Val",	"M30XV_RCI_EBSN_Val",	"M30XV_RCI_NFDA_Val",	"M30XV_RCI_NFDB_Val",	"M30XV_RCI_CFT_Val",	"M30XV_RCI_FSS_Val",	"M30XV_RCI_CONDFT_Val",	"M30XV_RCI_EFC_Val",	"M30XV_RCI_BFS_Val",	"M30XV_RCI_BMFT_Val",	"M30XV_RCI_PPGV_Val",	"M30XV_RCI_IPGV_Val",	"M30XV_RCI_DPGV_Val",	"M30XV_RCI_EWT_Val",	"M30XV_RCI_LCTIMER_Val",	"M30XV_RCI_RFI_Val",	"M30XV_RCI_METRIC_Val",	"M30XV_RCI_SFDC_Val",	"M30XV_RCI_SCDC_Val",	"M30XV_RCI_CHDS_Val",	"M30XV_RCI_FANOFFA_Val",	"M30XV_RCI_FANOFFB_Val",	"M30XV_RCI_FOO_Val",	"M30XV_RCI_QMC_Val",	"M30XV_RCI_MSS_Val",	"M30XV_RCI_SLVADD_Val",	"M30XV_RCI_LLS_Val",	"M30XV_RCI_LLBD_Val",	"M30XV_RCI_LLST_Val",	"M30XV_RCI_LPT_Val",	"M30XV_RCI_SIEH_Val",	"M30XV_RCI_LMRT_Val",	"M30XV_RCI_LUPC_Val",	"M30XV_RCI_CIS_Val",	"M30XV_RCI_CSP1_Val",	"M30XV_RCI_CSP2_Val",	"M30XV_RCI_CISP_Val ",	"M30XV_RCI_CRL_Val",	"M30XV_RCI_SLS1_Val",	"M30XV_RCI_SLS2_Val",	"M30XV_RCI_SLS3_Val"]
        self.M30XV_RCI_tog = []
        self.M30XV_CT_swrite = []
        self.M30XV_CT_write = ['M30XV_CT_ARS1_Val','M30XV_CT_ARS2_Val','M30XV_CT_CAEP_Val','M30XV_CT_CAOS_Val',
                                'M30XV_CT_CARO_Val','M30XV_CT_CASV1_Val','M30XV_CT_CASV2_Val','M30XV_CT_CBEP_Val','M30XV_CT_CBOS_Val','M30XV_CT_CBRO_Val','M30XV_CT_CBSV1_Val','M30XV_CT_CBSV2_Val','M30XV_CT_CCAO_Val','M30XV_CT_CCBO_Val','M30XV_CT_CH_Val','M30XV_CT_CP1_Val','M30XV_CT_CP2_Val','M30XV_CT_CTO_Val','M30XV_CT_EBF_Val','M30XV_CT_EEPCA_Val','M30XV_CT_EEPCB_Val','M30XV_CT_IVPA_Val','M30XV_CT_IVPB_Val','M30XV_CT_OHCA_Val','M30XV_CT_OHCB_Val','M30XV_CT_QTE_Val','M30XV_CT_RRS_Val','M30XV_CT_SFS_Val','M30XV_CT_SRS_Val','M30XV_CT_VSA_Val','M30XV_CT_VSB_Val','M30XV_CT_VSPC_Val']
        self.M30XV_CT_tog = []
        self.M30XV_OPDATA_swrite = []
        self.M30XV_OPDATA_write = ['M30XV_OD_CAPACITY_Val','M30XV_OD_CEF_Val',
                                   'M30XV_OD_CHWS_Val','M30XV_OD_CA1_click','M30XV_OD_CA1L1_Val','M30XV_OD_CA1L2_Val',
                                   'M30XV_OD_CA1L3_Val','M30XV_OD_CB1_click','M30XV_OD_CB1L1_Val','M30XV_OD_CB1L2_Val',
                                   'M30XV_OD_CB1L3_Val','M30XV_OD_CLF_Val','M30XV_OD_CP_Val','M30XV_OD_CSA_Val',
                                   'M30XV_OD_CSB_Val','M30XV_OD_DGTA_Val','M30XV_OD_DGTB_Val','M30XV_OD_EXVA_Val',
                                   'M30XV_OD_EXVB_Val','M30XV_OD_FMA1_click','M30XV_OD_FMA1L1_Val','M30XV_OD_FMA1L2_Val','M30XV_OD_FMA1L3_Val','M30XV_OD_FMA2_click','M30XV_OD_FMA2L1_Val','M30XV_OD_FMA2L2_Val','M30XV_OD_FMA2L3_Val','M30XV_OD_FMA3_click','M30XV_OD_FMA3L1_Val','M30XV_OD_FMA3L2_Val','M30XV_OD_FMA3L3_Val','M30XV_OD_FMA4_click','M30XV_OD_FMA4L1_Val','M30XV_OD_FMA4L2_Val','M30XV_OD_FMA4L3_Val','M30XV_OD_FMA5_click','M30XV_OD_FMA5L1_Val','M30XV_OD_FMA5L2_Val','M30XV_OD_FMA5L3_Val','M30XV_OD_FMA6_click','M30XV_OD_FMA6L1_Val','M30XV_OD_FMA6L2_Val','M30XV_OD_FMA6L3_Val','M30XV_OD_FMA7_click','M30XV_OD_FMA7L1_Val','M30XV_OD_FMA7L2_Val','M30XV_OD_FMA7L3_Val','M30XV_OD_FMA8_click','M30XV_OD_FMA8L1_Val','M30XV_OD_FMA8L2_Val','M30XV_OD_FMA8L3_Val','M30XV_OD_FMA9_click','M30XV_OD_FMA9L1_Val','M30XV_OD_FMA9L2_Val','M30XV_OD_FMA9L3_Val','M30XV_OD_FMB1_click','M30XV_OD_FMB1L1_Val','M30XV_OD_FMB1L2_Val','M30XV_OD_FMB1L3_Val','M30XV_OD_FMB2_click','M30XV_OD_FMB2L1_Val','M30XV_OD_FMB2L2_Val','M30XV_OD_FMB2L3_Val','M30XV_OD_FMB3_click','M30XV_OD_FMB3L1_Val','M30XV_OD_FMB3L2_Val','M30XV_OD_FMB3L3_Val','M30XV_OD_FMB4_click','M30XV_OD_FMB4L1_Val','M30XV_OD_FMB4L2_Val','M30XV_OD_FMB4L3_Val','M30XV_OD_FMB5_click','M30XV_OD_FMB5L1_Val','M30XV_OD_FMB5L2_Val','M30XV_OD_FMB5L3_Val','M30XV_OD_FMB6_click','M30XV_OD_FMB6L1_Val','M30XV_OD_FMB6L2_Val','M30XV_OD_FMB6L3_Val','M30XV_OD_FMB7_click','M30XV_OD_FMB7L1_Val','M30XV_OD_FMB7L2_Val','M30XV_OD_FMB7L3_Val','M30XV_OD_FMB8_click','M30XV_OD_FMB8L1_Val','M30XV_OD_FMB8L2_Val','M30XV_OD_FMB8L3_Val','M30XV_OD_FMB9_click','M30XV_OD_FMB9L1_Val','M30XV_OD_FMB9L2_Val','M30XV_OD_FMB9L3_Val','M30XV_OD_LTA_Val','M30XV_OD_LTB_Val','M30XV_OD_MTA_Val','M30XV_OD_MTB_Val','M30XV_OD_OAT_Val','M30XV_OD_SCTA_Val','M30XV_OD_SCTB_Val','M30XV_OD_SLA_Val','M30XV_OD_SLB_Val','M30XV_OD_SSA_Val','M30XV_OD_SSB_Val']

        self.M30XV_OPDATA_tog = []

        self.prefix = {'initial': 'M30XV_INIT', 'start': 'M30XV_SOM', 'operating': 'M30XV_OPDATA', 'record1': 'M30XV_RCI',
                   'component': 'M30XV_CT'}

    def write_data(self, Data):
        self.prefix = {'initial': 'M30XV_INIT', 'start': 'M30XV_SOM', 'operating': 'M30XV_OPDATA','record1':'M30XV_RCI','component': 'M30XV_CT'}
        for y in range(len(eval('self.' + self.prefix[Data['Model']] + '_tog'))):
            if eval('self.' + self.prefix[Data['Model']] + '_tog')[y][-3:] == 'Yes':
                xpath = eval('self.' + self.prefix[Data['Model']] + '_tog')[y]
                self.checklist.click(xpath, page_locators="UnitStartUp_locators")
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),y, 'Written UnitStartUp data of ' \
                                                                               ''+self.prefix[Data['Model']] + xpath + ' =', 'Yes')
        for i in range(len(eval("self." + self.prefix[Data['Model']] + "_write"))):
            if "_Val" in eval("self." + self.prefix[Data['Model']] + "_write[i]") or "_val" in eval(
                    "self." + self.prefix[Data['Model']] + "_write[i]"):
                xpath = eval("UnitStartUp_locators." + eval("self." + self.prefix[Data['Model']] + "_write[i]"))
                try:
                    self.checklist.write(xpath, Data)
                except:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),i,"Error : ", eval("self." + self.prefix[Data['Model']] + "_write[i]"))
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),i,'Written UnitStartUp data of ' + eval("self." + self.prefix[Data['Model']] +
                                                                         "_write[i]") + ' =', \
                    Data['testdata'])
            elif "click" in eval("self." + self.prefix[Data['Model']] + "_write[i]"):
                self.checklist.click(eval("self." + self.prefix[Data['Model']] + "_write[i]"), "UnitStartUp_locators")
        try:
            xpath = eval("UnitStartUp_locators." + eval("self."+self.prefix[Data['Model']]+"_swrite[0]"))
            xpath = self.find_elements(*xpath)
            for i in range(len(eval("self."+self.prefix[Data['Model']]+"_swrite"))):
                if "_Default" not in eval("self."+self.prefix[Data['Model']]+"_swrite[i]"):
                    # self.checklist.write_similar_element(xpath= xpath, index= eval("UnitStartUp_locators." + eval("self."+self.prefix[Data['Model']]+"_swrite[i]")), Data= Data)
                    self.checklist.write(xpath=eval("UnitStartUp_locators." + eval("self."+self.prefix[Data['Model']]+"_swrite[i]")),  Data=Data)
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),i,'Written UnitStartUp data to ' + str(eval("self."+self.prefix[Data['Model']]+"_swrite[i]")) \
                           + ' =', Data['testdata'])
        except IndexError as e:
            print(e)


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
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'Read UnitStartUP Data (' + ele + ')' + ' =', value)
                    except Exception as e:
                        print(ele, '-Float AssertionError',\
                            "********************************************************************************************************************************\n" \
                              "88888888888888888888888888888888888888888888888888888888888   ERROR   8888888888888888888888888888888888888888888888888888888888\n" \
                              "********************************************************************************************************************************")
                        #print(e.message)
                elif '_val' in ele[-6:]:
                    try:
                        assertion.assertEqual(value == str(Data['testdata'][:eval(ele[-2:])]), True)
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'Read Chiller Name Plate Data Information(' + ele + ')' + ' =', value)
                    except Exception as e:
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),ele,'- String AssertionError',\
                            "********************************************************************************************************************************\n" \
                              "88888888888888888888888888888888888888888888888888888888888   ERROR   8888888888888888888888888888888888888888888888888888888888\n" \
                              "********************************************************************************************************************************")
                        # print(e.message)
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'- Read UnitStartUP Data (' + ele + ')' + ' =', value)
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
                try:
                    assertion.assertEqual(value == 'true', True)
                    print(datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"), 'Read UnitStartUp Information of ' + ele + ' = ', value)
                except Exception as e:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),ele, 'Yes check AssertionError'       )
            elif ele[-2:] == 'No':
                try:
                    assertion.assertEqual(value == None, True)
                    print(datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"), 'Read UnitStartUp Information of ' + ele + ' = ', value)
                except Exception as e:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Yes check AssertionError')

    def read_autofill_data(self,Data):
        for ele in eval("self." + self.prefix[Data['Model']] + "_write_auto"):
            if ele != self.prefix[Data['Model']] + "_Default":
                common_xpath = eval(
                    "UnitStartUp_locators." + eval("self." + self.prefix[Data['Model']] + "_write_auto[0]"))
                common_xpath = self.find_elements(*common_xpath)
                val1 = self.find_element('xpath', eval('UnitStartUp_locators.' + ele)[-1]).get_attribute('class')
                if 'autoFillHighlight' in val1:
                    value = self.checklist.read(ele, common_xpath, Data, 'read_normal',
                                            page_locators="UnitStartUp_locators")
                ccn = read_csv.CCN_read()
                ccn_val = ccn.read_ccn_val(ele,ele[1:5])
                # ccn_val= read_csv(ele)

                if '_Val' in ele[-6:]:
                    try:
                        # if assertion.assertEqual(float(value) == float(ccn_val), True):
                        #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        #       'Read UnitStartUP Data (' + ele + ')' + ' =',ccn_val, value)
                        # elif assertion.assertEqual(str(value) == str(ccn_val), True):
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                  'Read UnitStartUP Data (' + ele + ')' + ' =', f"Controller value:{ccn_val} , Checklist value:{ value}")
                    except Exception as e:
                        # print(ele, '- AssertionError\n',e, "\n", "*"*10, "\n   ERROR   \n", "*"*10, f'\nController Val:{ccn_val}, AutoFill Val:{value}')
                        print(ele, 'Error\n', e, "\n", "*" * 10, "\n   ERROR   \n", "*" * 10,
                              f'\nController Val:{ccn_val}, AutoFill Val:{value}')
                        # print(e.message)

                elif '_val' in ele[-6:]:
                    try:
                        # assertion.assertEqual(value == str(ccn_val), True)
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                              'Read Chiller Name Plate Data Information(' + ele + ')' + ' =',ccn_val, value)
                    except Exception as e:
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ele, '- String AssertionError', "*" *10, "\n   ERROR   \n", "*"*10, f'Controller Val:{ccn_val}, AutoFill Val:{value}')
                        # print(e.message)
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                              '- Read UnitStartUP Data (' + ele + ')' + ' =', value)
                elif 'Val' in ele[-3:]:
                    pass# assertion.assertEqual(value == str(Data['testdata'][:eval(ele[-2:])]), True)

        for ele in eval("self." + self.prefix[Data['Model']] + "_tog"):
            value = self.checklist.read(ele, None, Data, 'yes|no', page_locators="UnitStartUp_locators")
            if ele[-3:] == 'Yes':
                try:
                    assertion.assertEqual(value == 'true', True)
                    print(datetime.datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"), 'Read UnitStartUp Information of ' + ele + ' = ', value)
                except Exception as e:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ele, 'Yes check AssertionError')
            elif ele[-2:] == 'No':
                try:
                    assertion.assertEqual(value == None, True)
                    print(datetime.datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"), 'Read UnitStartUp Information of ' + ele + ' = ', value)
                except Exception as e:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Yes check AssertionError')

    def read_reset_data(self, Data):
        for ele in eval("self." + self.prefix[Data['Model']] + "_write"):
            if ele != self.prefix[Data['Model']] + "_Default":
                common_xpath = eval(
                    "UnitStartUp_locators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read_normal',
                                            page_locators="UnitStartUp_locators", index_assert=5)

                if 'CheckBox' in ele[-8:]:
                    pass
                elif '_Val' in ele[-6:] or '_val' in ele[-6:]:
                    try:
                        assertion.assertEqual(value == '', True)
                        print(datetime.datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"), 'Read UnitStartUP Data of ' + ele + ' = ', 'Null' if value == '' else value)
                    except:
                        try:
                            assertion.assertEqual(value == None, True)
                        except Exception as e:
                            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ele, 'Value AssertionError',\
                                                                                         "********************************************************************************************************************************\n" \
                                  "88888888888888888888888888888888888888888888888888888888888   ERROR   8888888888888888888888888888888888888888888888888888888888\n" \
                                  "*************************************************************************************************************************", value)



        for ele in eval("self."+self.prefix[Data['Model']]+"_tog"):
            value = self.checklist.read(ele, None, Data, 'reset_yes|no', page_locators="UnitStartUp_locators")
            if ele[-3:] == 'Yes':
                try:
                    assertion.assertEqual(value == None, True)
                    print(datetime.datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"), 'Read UnitStartUp Information of ' + ele + ' = ', value)
                except Exception as e:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), eval("self." + self.prefix[
                        Data['Model']] + "_tog"), 'Yes check AssertionError')
            elif ele[-2:] == 'No':
                try:
                    assertion.assertEqual(value == 'true', True)
                    print(datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"), 'Read UnitStartUp Information of ' + ele + ' = ', value)
                except Exception as e:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), eval("self." + self.prefix[
                    Data['Model']] + "_tog"), 'No check AssertionError')


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

    def autofill(self):
        if self.find_element(*UnitStartUp_locators.unitstartup_autofill).is_enabled():
            self.find_element(*UnitStartUp_locators.unitstartup_autofill).click()
        else:
            print(" Autofill button disabled")
        time.sleep(10)
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