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

class UnitStartUp_30RAP(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(UnitStartUp_30RAP, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()

    def locator_name(self):
        ##########################################################  30RAP  ##########################################################
        self.M30RAP_INIT_write = []
        self.M30RAP_INIT_swrite = ['M30RAP_INIT_Default','M30RAP_INIT_CVI_Val','M30RAP_INIT_10AB_Val',
                                   'M30RAP_INIT_10AC_Val',
                                   'M30RAP_INIT_10BC_Val','M30RAP_INIT_AVGVOL_Val','M30RAP_INIT_MAXDEV_Val','M30RAP_INIT_VOLIMB_Val','M30RAP_INIT_PEC_Val','M30RAP_INIT_PLC_Val','M30RAP_INIT_CPD_Val','M30RAP_INIT_PSI_Val','M30RAP_INIT_KPA_Val','M30RAP_INIT_COOLER_Val' ]
        self.M30RAP_INIT_tog = ['M30RAP_INIT_1A_Yes','M30RAP_INIT_1A_No','M30RAP_INIT_2A_Yes','M30RAP_INIT_2A_No','M30RAP_INIT_3C_Yes','M30RAP_INIT_3C_No','M30RAP_INIT_4V_Yes','M30RAP_INIT_4V_No','M30RAP_INIT_5V_Yes','M30RAP_INIT_5V_No','M30RAP_INIT_6L_Yes','M30RAP_INIT_6L_No','M30RAP_INIT_7V_Yes','M30RAP_INIT_7V_No','M30RAP_INIT_8C_Yes','M30RAP_INIT_8C_No','M30RAP_INIT_VOLIMB2_Yes','M30RAP_INIT_VOLIMB2_No','M30RAP_INIT_COLFLOWRAT_Yes','M30RAP_INIT_COLFLOWRAT_No','M30RAP_INIT_FSOC_Yes','M30RAP_INIT_FSOC_No']


        self.M30RAP_SOM_swrite = []#['M30RAP_SOM_Default', 'M30RAP_SOM_6P_Val']
        self.M30RAP_SOM_write = ['M30RAP_SOM_6P_Val']
        self.M30RAP_SOM_tog = ['M30RAP_SOM_1C_Yes','M30RAP_SOM_1C_No','M30RAP_SOM_2C_Yes','M30RAP_SOM_2C_No','M30RAP_SOM_3R_Yes','M30RAP_SOM_3R_No','M30RAP_SOM_4R_Yes','M30RAP_SOM_4R_No','M30RAP_SOM_5R_Yes','M30RAP_SOM_5R_No']

        self.M30RAP_RCISW_swrite = []
        self.M30RAP_RCISW_tog = []
        self.M30RAP_RCISW_write = ['M30RAP_RCISW_MBB1_val','M30RAP_RCISW_MBB2_val','M30RAP_RCISW_MBB3_val','M30RAP_RCISW_EXV1_val','M30RAP_RCISW_EXV2_val','M30RAP_RCISW_EXV3_val','M30RAP_RCISW_AUX1_val','M30RAP_RCISW_AUX2_val','M30RAP_RCISW_AUX3_val','M30RAP_RCISW_EMM1_val','M30RAP_RCISW_EMM2_val','M30RAP_RCISW_EMM3_val','M30RAP_RCISW_MARQ1_val','M30RAP_RCISW_MARQ2_val','M30RAP_RCISW_MARQ3_val',
'M30RAP_RCISW_NAVI1_val','M30RAP_RCISW_NAVI2_val','M30RAP_RCISW_NAVI3_val','M30RAP_RCISW_CXB1_val','M30RAP_RCISW_CXB2_val','M30RAP_RCISW_CXB3_val']
        self.M30RAP_RCIUNIT_swrite = []
        self.M30RAP_RCIUNIT_tog = []
        self.M30RAP_RCIUNIT_write =['M30RAP_RCIUNIT_SIZE_Val','M30RAP_RCIUNIT_SZA1_Val','M30RAP_RCIUNIT_SZA2_Val',
                                    'M30RAP_RCIUNIT_SZA3_Val','M30RAP_RCIUNIT_SZB1_Val','M30RAP_RCIUNIT_SZB2_Val',
                                    'M30RAP_RCIUNIT_SZB3_Val','M30RAP_RCIUNIT_SHSP_Val','M30RAP_RCIUNIT_FANS_Val','M30RAP_RCIUNIT_MAXT_Val','M30RAP_RCIUNIT_VLTS_Val','M30RAP_RCIUNIT_FPOL_Val',
                                    'M30RAP_RCIUNIT_EXV_btn_click','M30RAP_RCIUNIT_EXV_Yes_click', 'M30RAP_RCIUNIT_EXV_No',
                                    'M30RAP_RCIUNIT_A1TY_btn_click','M30RAP_RCIUNIT_A1TY_Yes_click',
                                    'M30RAP_RCIUNIT_A1TY_No', 'M30RAP_RCIUNIT_FNSQ_btn_click','M30RAP_RCIUNIT_FNSQ_Yes_click',
                                    'M30RAP_RCIUNIT_FNSQ_No']
        self.M30RAP_RCIOP1_swrite = []
        self.M30RAP_RCIOP1_tog = []
        self.M30RAP_RCIOP1_write = ['M30RAP_OPTIONS1_FLUD_Val','M30RAP_OPTIONS1_PMSL_Val','M30RAP_OPTIONS1_PMDY_Val',
                                    'M30RAP_OPTIONS1_PMDT_Val','M30RAP_OPTIONS1_PMPO_Val','M30RAP_OPTIONS1_PMHT_Val',
                                    'M30RAP_OPTIONS1_CNDT_Val','M30RAP_OPTIONS1_MOPS_Val','M30RAP_OPTIONS1_APPR_Val',
                                    'M30RAP_OPTIONS1_MLVS_btn_click','M30RAP_OPTIONS1_MLVS_Yes_click',
                                    'M30RAP_OPTIONS1_MLVS_No','M30RAP_OPTIONS1_CSBE_btn_click',
                                  'M30RAP_OPTIONS1_CSBE_Enable_click','M30RAP_OPTIONS1_CSBE_Disable',
                                    'M30RAP_OPTIONS1_CPC_btn_click',
                                  'M30RAP_OPTIONS1_CPC_On_click','M30RAP_OPTIONS1_CPC_Off',
                                    'M30RAP_OPTIONS1_PM1E_btn_click',
                                   'M30RAP_OPTIONS1_PM1E_Yes_click','M30RAP_OPTIONS1_PM1E_No',
                                    'M30RAP_OPTIONS1_PM2E_btn_click','M30RAP_OPTIONS1_PM2E_Yes_click',
                                    'M30RAP_OPTIONS1_PM2E_No','M30RAP_OPTIONS1_PMPS_btn_click',
                                    'M30RAP_OPTIONS1_PMPS_Yes_click','M30RAP_OPTIONS1_PMPS_No',
                                    'M30RAP_OPTIONS1_ROTP_btn_click','M30RAP_OPTIONS1_ROTP_Yes_click',
                                    'M30RAP_OPTIONS1_ROTP_No','M30RAP_OPTIONS1_EMM_btn_click',
                                    'M30RAP_OPTIONS1_EMM_Yes_click','M30RAP_OPTIONS1_EMM_No']

        self.M30RAP_RCIOP2_swrite = []
        self.M30RAP_RCIOP2_tog = []
        self.M30RAP_RCIOP2_write = ['M30RAP_OPTIONS2_CTRL_Val','M30RAP_OPTIONS2_LOAD_Val','M30RAP_OPTIONS2_LLCS_Val',
                                    'M30RAP_OPTIONS2_LLWT_Val','M30RAP_OPTIONS2_DELY_Val','M30RAP_OPTIONS2_LSMD_Val',
                                    'M30RAP_OPTIONS2_LSST_Val','M30RAP_OPTIONS2_LSND_Val','M30RAP_OPTIONS2_LSLT_Val',
                                    'M30RAP_OPTIONS2_ALRC_Val','M30RAP_OPTIONS2_ICEM_btn_click',
                                    'M30RAP_OPTIONS2_ICEM_Enable_click','M30RAP_OPTIONS2_ICEM_Disable',
                                    'M30RAP_OPTIONS2_SERT_btn_click','M30RAP_OPTIONS2_SERT_Enable_click',
                                    'M30RAP_OPTIONS2_SERT_Disable']

        self.M30RAP_RCICCN_swrite = []
        self.M30RAP_RCICCN_tog = []
        self.M30RAP_RCICCN_write = ['M30RAP_RCICCN_CCNA_Val','M30RAP_RCICCN_CCNB_Val','M30RAP_RCICCN_BAUD_Val']

        self.M30RAP_RCIEXVA_swrite = []
        self.M30RAP_RCIEXVA_tog = []
        self.M30RAP_RCIEXVA_write = ['M30RAP_RCIEXVA_EXVL_Val','M30RAP_RCIEXVA_LWTL_Val','M30RAP_RCIEXVA_EXVH_Val','M30RAP_RCIEXVA_LWTH_Val','M30RAP_RCIEXVA_MINA_Val','M30RAP_RCIEXVA_RNGA_Val','M30RAP_RCIEXVA_SPDA_Val','M30RAP_RCIEXVA_POFA_Val','M30RAP_RCIEXVA_MINA_Val','M30RAP_RCIEXVA_MAXA_Val','M30RAP_RCIEXVA_OVRA_Val','M30RAP_RCIEXVA_TYPA_Val','M30RAP_RCIEXVA_HSCT_Val','M30RAP_RCIEXVA_XPCT_Val','M30RAP_RCIEXVA_XPER_Val','M30RAP_RCIEXVA_APCT_Val','M30RAP_RCIEXVA_MPCT_Val','M30RAP_RCIEXVA_SPCT_Val','M30RAP_RCIEXVA_DELY_Val','M30RAP_RCIEXVA_LDLT_Val','M30RAP_RCIEXVA_SHRT_Val','M30RAP_RCIEXVA_LEXM_Val']

        self.M30RAP_RCIEXVB_swrite = []
        self.M30RAP_RCIEXVB_tog = []
        self.M30RAP_RCIEXVB_write = ['M30RAP_RCIEXVB_MINB_Val','M30RAP_RCIEXVB_RNGB_Val','M30RAP_RCIEXVB_SPDB_Val','M30RAP_RCIEXVB_POFB_Val','M30RAP_RCIEXVB_MINB1_Val','M30RAP_RCIEXVB_MAXB_Val','M30RAP_RCIEXVB_OVRB_Val','M30RAP_RCIEXVB_TYPB_Val']

        self.M30RAP_RCIMM_swrite = []
        self.M30RAP_RCIMM_tog = []
        self.M30RAP_RCIMM_write = ['M30RAP_RCIMM_MMRS_Val','M30RAP_RCIMM_PGAN_Val','M30RAP_RCIMM_IGAN_Val','M30RAP_RCIMM_DGAN_Val','M30RAP_RCIMM_MINS_Val']

        self.M30RAP_RCIRSET_swrite = []
        self.M30RAP_RCIRSET_tog = []
        self.M30RAP_RCIRSET_write = ['M30RAP_RCIRSET_CRST_Val','M30RAP_RCIRSET_MADG_Val',
                                     'M30RAP_RCIRSET_RMNO_Val','M30RAP_RCIRSET_RMF_Val','M30RAP_RCIRSET_RMDG_Val',
                                     'M30RAP_RCIRSET_RTNO_Val','M30RAP_RCIRSET_RTF_Val','M30RAP_RCIRSET_RTDG_Val',
                                     'M30RAP_RCIRSET_DMDC_Val','M30RAP_RCIRSET_DM20_Val',
                                     'M30RAP_RCIRSET_SHNM_Val','M30RAP_RCIRSET_SHDL_Val',
                                     'M30RAP_RCIRSET_SHTM_Val','M30RAP_RCIRSET_DLS1_Val',
                                     'M30RAP_RCIRSET_DLS2_Val','M30RAP_RCIRSET_SLVA_Val','M30RAP_RCIRSET_LLBL_Val',
                                     'M30RAP_RCIRSET_LLBD_Val','M30RAP_RCIRSET_LLDY_Val',
                                     'M30RAP_RCIRSET_LLEN_btn_click','M30RAP_RCIRSET_LLEN_Yes_click',
                                     'M30RAP_RCIRSET_LLEN_No','M30RAP_RCIRSET_MSSL_btn_click',
                                     'M30RAP_RCIRSET_MSSL_Yes_click',
                                     'M30RAP_RCIRSET_MSSL_No','M30RAP_RCIRSET_PARA_btn_click',
                                     'M30RAP_RCIRSET_PARA_Yes_click','M30RAP_RCIRSET_PARA_No']

        self.M30RAP_RCISLCT_swrite = []
        self.M30RAP_RCISLCT_tog = []
        self.M30RAP_RCISLCT_write = ['M30RAP_RCISLCT_CLSP_Val','M30RAP_RCISLCT_CRMP_Val',
                                     'M30RAP_RCISLCT_SCHD_Val','M30RAP_RCISLCT_ZGN_Val',
                                     'M30RAP_RCISLCT_RLS_btn_click','M30RAP_RCISLCT_RLS_Yes_click',
                                     'M30RAP_RCISLCT_RLS_No']

        self.M30RAP_RCISPT_swrite = []
        self.M30RAP_RCISPT_tog = []
        self.M30RAP_RCISPT_write = ['M30RAP_RCISPT_CSP1_Val','M30RAP_RCISPT_CSP2_Val','M30RAP_RCISPT_CSP3_Val','M30RAP_RCISPT_HDP_Val','M30RAP_RCISPT_FON_Val','M30RAP_RCISPT_FOFF_Val','M30RAP_RCISPT_BOFF_Val','M30RAP_RCISPT_FDLT_Val','M30RAP_RCISPT_BRFZ_Val']

        self.M30RAP_CTMST_swrite = []
        self.M30RAP_CTMST_tog = []
        self.M30RAP_CTMST_write = ["M30RAP_SERVICETEST_EXVA_btn_click ","M30RAP_SERVICETEST_EXVA_Yes_click",
                                   "M30RAP_SERVICETEST_EXVA_No","M30RAP_SERVICETEST_EXVA_Val",
                                   "M30RAP_SERVICETEST_EXVB_btn_click","M30RAP_SERVICETEST_EXVB_Yes_click",
                                   "M30RAP_SERVICETEST_EXVB_No","M30RAP_SERVICETEST_EXVB_Val",
                                   "M30RAP_SERVICETEST_FAN1_btn_click","M30RAP_SERVICETEST_FAN1_Yes_click",
                                   "M30RAP_SERVICETEST_FAN1_No","M30RAP_SERVICETEST_FAN2_btn_click",
                                   "M30RAP_SERVICETEST_FAN2_Yes_click","M30RAP_SERVICETEST_FAN3_btn_click",
                                   "M30RAP_SERVICETEST_FAN3_Yes_click","M30RAP_SERVICETEST_FAN3_No",
                                   "M30RAP_SERVICETEST_FAN4_btn_click","M30RAP_SERVICETEST_FAN4_Yes_click",
                                   "M30RAP_SERVICETEST_FAN4_No","M30RAP_SERVICETEST_FAN5_btn_click","M30RAP_SERVICETEST_FAN5_Yes_click","M30RAP_SERVICETEST_FAN5_No","M30RAP_SERVICETEST_FAN6_btn_click","M30RAP_SERVICETEST_FAN6_Yes_click","M30RAP_SERVICETEST_FAN7_btn_click","M30RAP_SERVICETEST_FAN7_Yes_click","M30RAP_SERVICETEST_FAN7_No","M30RAP_SERVICETEST_FAN8_btn_click","M30RAP_SERVICETEST_FAN8_Yes_click","M30RAP_SERVICETEST_FAN8_No","M30RAP_SERVICETEST_VHPA_btn_click","M30RAP_SERVICETEST_VHPA_Yes_click","M30RAP_SERVICETEST_VHPA_No","M30RAP_SERVICETEST_VHPA_Val","M30RAP_SERVICETEST_VHPB_btn_click","M30RAP_SERVICETEST_VHPB_Yes_click","M30RAP_SERVICETEST_VHPB_No","M30RAP_SERVICETEST_VHPB_Val","M30RAP_SERVICETEST_CLP1_btn_click","M30RAP_SERVICETEST_CLP1_On_click","M30RAP_SERVICETEST_CLP1_Off","M30RAP_SERVICETEST_CLP12_btn_click","M30RAP_SERVICETEST_CLP1_Yes_click","M30RAP_SERVICETEST_CLP1_No","M30RAP_SERVICETEST_CLP2_btn_click","M30RAP_SERVICETEST_CLP2_On_click","M30RAP_SERVICETEST_CLP2_Off","M30RAP_SERVICETEST_CLP22_btn_click","M30RAP_SERVICETEST_CLP2_Yes_click","M30RAP_SERVICETEST_DIGP_btn_click","M30RAP_SERVICETEST_DIGP_Yes_click","M30RAP_SERVICETEST_DIGP_No","M30RAP_SERVICETEST_CLHT_btn_click","M30RAP_SERVICETEST_CLHT_Yes_click","M30RAP_SERVICETEST_CCHA_btn_click","M30RAP_SERVICETEST_CCHA_On_click","M30RAP_SERVICETEST_CCHA_Off","M30RAP_SERVICETEST_CCHA2_btn_click","M30RAP_SERVICETEST_CCHA_Yes_click","M30RAP_SERVICETEST_CCHB_btn_click","M30RAP_SERVICETEST_CCHB_On_click","M30RAP_SERVICETEST_CCHB_Off","M30RAP_SERVICETEST_CCHB2_btn_click","M30RAP_SERVICETEST_CCHB_Yes_click","M30RAP_SERVICETEST_CCHB_No","M30RAP_SERVICETEST_RMTA_btn_click","M30RAP_SERVICETEST_RMTA_On_click","M30RAP_SERVICETEST_RMTA_Off","M30RAP_SERVICETEST_RMTA2_btn_click","M30RAP_SERVICETEST_RMTA_Yes_click","M30RAP_SERVICETEST_RMTA_No","M30RAP_SERVICETEST_CCA1_btn_click","M30RAP_SERVICETEST_CCA1_On_click","M30RAP_SERVICETEST_CCA1_Off","M30RAP_SERVICETEST_CCA12_btn_click","M30RAP_SERVICETEST_CCA1_Yes_click","M30RAP_SERVICETEST_CCA1_No","M30RAP_SERVICETEST_DIGP2_btn_click","M30RAP_SERVICETEST_DIGP2_Yes_click","M30RAP_SERVICETEST_DIGP2_No","M30RAP_SERVICETEST_CCA2_btn_click","M30RAP_SERVICETEST_CCA2_On_click","M30RAP_SERVICETEST_CCA2_Off","M30RAP_SERVICETEST_CCA22_btn_click","M30RAP_SERVICETEST_CCA2_Yes_click","M30RAP_SERVICETEST_CCA2_No","M30RAP_SERVICETEST_CCA3_btn_click","M30RAP_SERVICETEST_CCA3_On_click","M30RAP_SERVICETEST_CCA3_Off","M30RAP_SERVICETEST_CCA32_btn_click","M30RAP_SERVICETEST_CCA3_Yes_click","M30RAP_SERVICETEST_CCA3_No","M30RAP_SERVICETEST_MLV_btn_click","M30RAP_SERVICETEST_MLV_On_click","M30RAP_SERVICETEST_MLV_Off","M30RAP_SERVICETEST_MLV2_btn_click","M30RAP_SERVICETEST_MLV_Yes_click","M30RAP_SERVICETEST_MLV_No","M30RAP_SERVICETEST_CCB1_btn_click","M30RAP_SERVICETEST_CCB1_Yes_click","M30RAP_SERVICETEST_CCB2_btn_click","M30RAP_SERVICETEST_CCB2_Yes_click","M30RAP_SERVICETEST_CCB2_No","M30RAP_SERVICETEST_CCB3_btn_click","M30RAP_SERVICETEST_CCB3_Yes_click","M30RAP_SERVICETEST_CCB3_No"]


        self.M30RAP_OPDATA_swrite = []
        self.M30RAP_OPDATA_tog = []
        self.M30RAP_OPDATA_write = ['M30RAP_OD_DISPREA_Val','M30RAP_OD_DISPREB_Val','M30RAP_OD_SUCPREA_Val','M30RAP_OD_SUCPREB_Val','M30RAP_OD_SCTA_Val','M30RAP_OD_SCTB_Val','M30RAP_OD_SSTA_Val','M30RAP_OD_SSTB_Val','M30RAP_OD_RGTA_Val','M30RAP_OD_RGTB_Val','M30RAP_OD_LLTA_Val','M30RAP_OD_LLTB_Val','M30RAP_OD_DLTA_Val','M30RAP_OD_DLTB_Val','M30RAP_OD_EWT_Val','M30RAP_OD_LWT_Val','M30RAP_OD_OAT_Val','M30RAP_OD_CP_Val','M30RAP_OD_PTC_Val','M30RAP_OD_LEADLAG_Val']
        self.M30RAP_CRCT_swrite = []
        self.M30RAP_CRCT_tog = []
        self.M30RAP_CRCT_write = [
'M30RAP_CRCT_A1_click','M30RAP_CRCT_A1L1_Val','M30RAP_CRCT_A1L2_Val','M30RAP_CRCT_A1L3_Val','M30RAP_CRCT_A2_click',
            'M30RAP_CRCT_A2L1_Val','M30RAP_CRCT_A2L2_Val','M30RAP_CRCT_A2L3_Val','M30RAP_CRCT_A3_click',
            'M30RAP_CRCT_A3L1_Val', 'M30RAP_CRCT_A3L2_Val','M30RAP_CRCT_A3L3_Val','M30RAP_CRCT_B1_click',
            'M30RAP_CRCT_B1L1_Val','M30RAP_CRCT_B1L2_Val','M30RAP_CRCT_B1L3_Val','M30RAP_CRCT_B2_click','M30RAP_CRCT_B2L1_Val','M30RAP_CRCT_B2L2_Val','M30RAP_CRCT_B2L3_Val','M30RAP_CRCT_B3_click','M30RAP_CRCT_B3L1_Val','M30RAP_CRCT_B3L2_Val','M30RAP_CRCT_B3L3_Val','M30RAP_CRCT_FM1_click','M30RAP_CRCT_FM1L1_Val','M30RAP_CRCT_FM1L2_Val','M30RAP_CRCT_FM1L3_Val','M30RAP_CRCT_FM2_click','M30RAP_CRCT_FM2L1_Val','M30RAP_CRCT_FM2L2_Val','M30RAP_CRCT_FM2L3_Val','M30RAP_CRCT_FM3_click','M30RAP_CRCT_FM3L1_Val','M30RAP_CRCT_FM3L2_Val','M30RAP_CRCT_FM3L3_Val','M30RAP_CRCT_FM4_click','M30RAP_CRCT_FM4L1_Val','M30RAP_CRCT_FM4L2_Val','M30RAP_CRCT_FM4L3_Val','M30RAP_CRCT_FM5_click','M30RAP_CRCT_FM5L1_Val','M30RAP_CRCT_FM5L2_Val','M30RAP_CRCT_FM5L3_Val','M30RAP_CRCT_FM6_click','M30RAP_CRCT_FM6L1_Val','M30RAP_CRCT_FM6L2_Val','M30RAP_CRCT_FM6L3_Val','M30RAP_CRCT_FM7_click','M30RAP_CRCT_FM7L1_Val','M30RAP_CRCT_FM7L2_Val','M30RAP_CRCT_FM7L3_Val','M30RAP_CRCT_FM8_click','M30RAP_CRCT_FM8L1_Val','M30RAP_CRCT_FM8L2_Val','M30RAP_CRCT_FM8L3_Val','M30RAP_CRCT_FM9_click','M30RAP_CRCT_FM9L1_Val','M30RAP_CRCT_FM9L2_Val','M30RAP_CRCT_FM9L3_Val','M30RAP_CRCT_FM10_click','M30RAP_CRCT_FM10L1_Val','M30RAP_CRCT_FM10L2_Val','M30RAP_CRCT_FM10L3_Val','M30RAP_CRCT_CP1_click','M30RAP_CRCT_CP1L1_Val','M30RAP_CRCT_CP1L2_Val','M30RAP_CRCT_CP1L3_Val','M30RAP_CRCT_CP2_click','M30RAP_CRCT_CP2L1_Val','M30RAP_CRCT_CP2L2_Val','M30RAP_CRCT_CP2L3_Val']
        self.prefix = {'initial': 'M30RAP_INIT', 'start': 'M30RAP_SOM', 'record1': 'M30RAP_RCISW',
                        'record2': 'M30RAP_RCIUNIT','record3':'M30RAP_RCIOP1','record4': 'M30RAP_RCIOP2', 'record5':
                           'M30RAP_RCICCN','record6':'M30RAP_RCIEXVA','record7':'M30RAP_RCIEXVB','record8':
                           'M30RAP_RCIMM','record9': 'M30RAP_RCIRSET','record10': 'M30RAP_RCISLCT',
                       'record11':'M30RAP_RCISPT', 'component': 'M30RAP_CTMST','operating': 'M30RAP_OPDATA',
                       'compressor':'M30RAP_CRCT'}
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
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),i, "Error: ", eval("self." +
                                                                                                  self.prefix[Data[
                                                                                                      'Model']] +
                                                                                                    "_write[i]"),"=",\
                        Data['testdata'])

            elif "click" in eval("self." + self.prefix[Data['Model']] + "_write[i]"):
                self.checklist.click(eval("self." + self.prefix[Data['Model']] + "_write[i]"), "UnitStartUp_locators")
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), i, 'Selected UnitStartUp data of ' \
                                                                                 + eval("self." + self.prefix[Data['Model']] + "_write[i]"))

            # elif "Loe" in eval("self." + self.prefix[Data['Model']] + "_write[i]"):
            #     xpath = eval("UnitStartUp_locators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
            #     self.checklist.set_dropdown(xpath, index=eval(
            #         "UnitStartUp_locators." + eval("self." + self.prefix[Data['Model']] + "_write[i]")))

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

        # DropDown
        # try:
        #     if eval('self.' + self.prefix[Data['Model']] + '_write')[0][-3:] == 'Loe':
        #         count = 0
        #         xpath = eval("UnitStartUp_locators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
        #         for i in range(len(eval("self."+self.prefix[Data["Model"]]+"_write"))):
        #             if eval('self.' + self.prefix[Data['Model']] + '_write')[i][-3:] == 'Loe':
        #                 self.checklist.set_dropdown(xpath, index= eval("UnitStartUp_locators." + eval("self."+self.prefix[Data['Model']]+"_write[i]")))
        #         # xpath = self.find_elements(*xpath)
        #         # for ele in range(len(xpath)):
        #         #     try:
        #         #         xpath[ele].click()
        #         #         print(xpath[ele].text)
        #         #         # xpath[ele].send_keys(Keys.ENTER)
        #         #         print eval("self." + self.prefix[Data['Model']] + "_write[count]"),'= ', ele
        #         #         count = count + 1
        #         #     except:
        #         #         pass
        # except IndexError:
        #     pass
        # same writables
        # count = 0
        # xpath = eval("UnitStartUp_locators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
        # xpath = self.find_elements(*xpath)
        # for ele in range(len(xpath)):
        #     try:
        #         xpath[ele].send_keys(Data['testdata'])
        #         xpath[ele].send_keys(Keys.ENTER)
        #         print eval("self." + self.prefix[Data['Model']] + "_write[count]"), ele
        #         count = count + 1
        #     except:
        #         pass

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
                        assertion.assertEqual(value == str(Data['testdata'][:eval(ele[-2:])]), True)
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