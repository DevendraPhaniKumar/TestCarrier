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

driver = object
delay = 75
assertion = unittest.TestCase('__init__')

class UnitStartUp_30HX(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(UnitStartUp_30HX, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()

    def locator_name(self):
        ##########################################################  30HX  ##########################################################
        self.M30HX_INIT_write = []
        self.M30HX_INIT_swrite = ["M30HXGX_INIT_Default", "M30HXGX_INIT_9vimb_AB_Val_05", "M30HXGX_INIT_9vimb_AC_Val_05", "M30HXGX_INIT_9vimb_BC_Val_05", "M30HXGX_INIT_9vimb_max_Val_05", "M30HXGX_INIT_14Vcfr_pres_entr_Val_05", "M30HXGX_INIT_14Vcfr_pres_leav_Val_05",
                                    "M30HXGX_INIT_14Vcfr_cool_pres_Val_05", "M30HXGX_INIT_15Vcndfr_max_cool_Val_05", "M30HXGX_INIT_15Vcndfr_min_cool_Val_05", "M30HXGX_INIT_15Vcndfr_pres_econ_Val_05", "M30HXGX_INIT_15Vcndfr_pres_lcon_Val_05",
                                    "M30HXGX_INIT_15Vcndfr_con_press_Val_05", "M30HXGX_INIT_15Vcndfr_con_psig_Val_05", "M30HXGX_INIT_15Vcndfr_con_kpa_Val_05", "M30HXGX_INIT_15Vcndfr_con_flow_Val_05", "M30HXGX_INIT_14Vcfr_psig_Val_05", "M30HXGX_INIT_14Vcfr_kpa_Val_05"]
        self.M30HX_INIT_tog = ["M30HXGX_INIT_1Allvao_yes", "M30HXGX_INIT_1Allvao_no", "M30HXGX_INIT_2Advao_yes", "M30HXGX_INIT_2Advao_no", "M30HXGX_INIT_3Assvao_yes", "M30HXGX_INIT_3Assvao_no", "M30HXGX_INIT_4Aolvao_yes", "M30HXGX_INIT_4Aolvao_no",
                                    "M30HXGX_INIT_5llsv_yes", "M30HXGX_INIT_5llsv_no", "M30HXGX_INIT_6cwf_yes", "M30HXGX_INIT_6cwf_no", "M30HXGX_INIT_7lcu_yes", "M30HXGX_INIT_7lcu_no", "M30HXGX_INIT_8Viwl_yes", "M30HXGX_INIT_8Viwl_no",
                                    "M30HXGX_INIT_10atat_yes", "M30HXGX_INIT_10atat_no", "M30HXGX_INIT_11apat_yes", "M30HXGX_INIT_11apat_no", "M30HXGX_INIT_12act_yes", "M30HXGX_INIT_12act_no", "M30HXGX_INIT_13atfi_yes", "M30HXGX_INIT_13atfi_no",
                                    "M30HXGX_INIT_14Vcfr_yes", "M30HXGX_INIT_14Vcfr_no", "M30HXGX_INIT_15Vcndfr_yes", "M30HXGX_INIT_15Vcndfr_no", "M30HXGX_INIT_9volts_yes", "M30HXGX_INIT_9volts_no"]

        self.M30HX_SOM_swrite = ["M30HXGX_SOM_Default", "M30HXGX_SOM_5poi_Val_05"]
        self.M30HX_SOM_write = []
        self.M30HX_SOM_tog = ["M30HXGX_SOM_1Cct_Desc", "M30HXGX_SOM_1Cct_yes", "M30HXGX_SOM_1Cct_no", "M30HXGX_SOM_2Crochng_Desc", "M30HXGX_SOM_2Crochng_yes", "M30HXGX_SOM_2Crochng_no",
                                "M30HXGX_SOM_3rcm_Desc", "M30HXGX_SOM_3rcm_yes", "M30HXGX_SOM_3rcm_no", "M30HXGX_SOM_4r2sol_Desc", "M30HXGX_SOM_4r2sol_yes", "M30HXGX_SOM_4r2sol_no", "M30HXGX_SOM_5poi_Desc",
                                "M30HXGX_SOM_RC_Desc", "M30HXGX_SOM_RC_CirA_yes", "M30HXGX_SOM_RC_CirA_no", "M30HXGX_SOM_RC_CirB_yes", "M30HXGX_SOM_RC_CirB_no", "M30HXGX_SOM_OC_Desc ", "M30HXGX_SOM_OC_CirA_yes",
                                "M30HXGX_SOM_OC_CirA_no", "M30HXGX_SOM_OC_CirB_yes", "M30HXGX_SOM_OC_CirB_no"]
        self.M30HX_SW_swrite = []
        self.M30HX_SW_tog = []
        self.M30HX_SW_write = ["M30HXGX_SW_MBB_Desc", "M30HXGX_SW_MBB_Disp_val_20", "M30HXGX_SW_MBB_Itm_val_20", "M30HXGX_SW_EXV_Desc", "M30HXGX_SW_EXV_Disp_val_20", "M30HXGX_SW_EXV_Itm_val_20", "M30HXGX_SW_EMM_Desc",
                            "M30HXGX_SW_EMM_Disp_val_20", "M30HXGX_SW_EMM_Itm_val_20", "M30HXGX_SW_CP1_Desc", "M30HXGX_SW_CP1_Disp_val_20", "M30HXGX_SW_CP1_Itm_val_20", "M30HXGX_SW_CP2_Desc", "M30HXGX_SW_CP2_Disp_val_20",
                            "M30HXGX_SW_CP2_Itm_val_20", "M30HXGX_SW_CP3_Desc", "M30HXGX_SW_CP3_Disp_val_20", "M30HXGX_SW_CP3_Itm_val_20", "M30HXGX_SW_AUX_Desc", "M30HXGX_SW_AUX_Disp_val_20", "M30HXGX_SW_AUX_Itm_val_20",
                            "M30HXGX_SW_NAVI_Desc", "M30HXGX_SW_NAVI_Disp_val_20", "M30HXGX_SW_NAVI_Itm_val_20"]
        self.M30HX_RCIMC_swrite = []
        self.M30HX_RCIMC_tog = []
        RCIMC_dropdown_samexpath = ["M30HXGX_RCIMC_METR_Loe", "M30HXGX_RCIMC_CNPI_Loe", "M30HXGX_RCIMC_EMM_Loe", "M30HXGX_RCIMC_NOFL_Loe", "M30HXGX_RCIMC_WMSG_Loe",  "M30HXGX_RCIMC_MSSL_Loe", "M30HXGX_RCIMC_ENA2_Loe", "M30HXGX_RCIMC_ENB2_Loe",
                 "M30HXGX_RCIMC_ECON_Loe", "M30HXGX_RCIMC_OATB_Loe", "M30HXGX_RCIMC_BCAK_Loe"]
        self.M30HX_RCIMC_write = ["M30HXGX_RCIMC_Loe", "M30HXGX_RCIMC_TEST_Loe", "M30HXGX_RCIMC_TEST_Desc", "M30HXGX_RCIMC_METR_Desc", "M30HXGX_RCIMC_LANG_Val_05", "M30HXGX_RCIMC_LANG_Desc", "M30HXGX_RCIMC_PASE_Loe", "M30HXGX_RCIMC_PASE_Desc",
                            "M30HXGX_RCIMC_PASS_Val_05", "M30HXGX_RCIMC_PASS_Desc", "M30HXGX_RCIMC_TYPE_Val_05", "M30HXGX_RCIMC_TYPE_Desc", "M30HXGX_RCIMC_TONS_Val_05", "M30HXGX_RCIMC_TONS_Desc", "M30HXGX_RCIMC_CAPA_Val_05", "M30HXGX_RCIMC_CAPA_Desc",
                            "M30HXGX_RCIMC_CMPA_Val_05", "M30HXGX_RCIMC_CMPA_Desc", "M30HXGX_RCIMC_CMPB_Val_05", "M30HXGX_RCIMC_CMPB_Desc", "M30HXGX_RCIMC_TCPM_Loe", "M30HXGX_RCIMC_TCPM_Desc", "M30HXGX_RCIMC_DISS_Val_05", "M30HXGX_RCIMC_DISS_Desc",
                            "M30HXGX_RCIMC_FANS_Val_05", "M30HXGX_RCIMC_FANS_Desc", "M30HXGX_RCIMC_CMA1_Val_05", "M30HXGX_RCIMC_CMA1_Desc", "M30HXGX_RCIMC_CRA1_Val_05", "M30HXGX_RCIMC_CRA1_Desc", "M30HXGX_RCIMC_S1A1_Val_05", "M30HXGX_RCIMC_S1A1_Desc",
                            "M30HXGX_RCIMC_SRA1_Val_05", "M30HXGX_RCIMC_SRA1_Desc", "M30HXGX_RCIMC_CMA2_Val_05", "M30HXGX_RCIMC_CMA2_Desc", "M30HXGX_RCIMC_CRA2_Val_05", "M30HXGX_RCIMC_CRA2_Desc", "M30HXGX_RCIMC_S1A2_Val_05", "M30HXGX_RCIMC_S1A2_Desc",
                            "M30HXGX_RCIMC_SRA2_Val_05", "M30HXGX_RCIMC_SRA2_Desc", "M30HXGX_RCIMC_CMB1_Val_05", "M30HXGX_RCIMC_CMB1_Desc", "M30HXGX_RCIMC_CRB1_Val_05", "M30HXGX_RCIMC_CRB1_Desc", "M30HXGX_RCIMC_S1B1_Val_05", "M30HXGX_RCIMC_S1B1_Desc",
                            "M30HXGX_RCIMC_SRB1_Val_05", "M30HXGX_RCIMC_SRB1_Desc", "M30HXGX_RCIMC_CMB2_Val_05", "M30HXGX_RCIMC_CMB2_Desc", "M30HXGX_RCIMC_CRB2_Val_05", "M30HXGX_RCIMC_CRB2_Desc", "M30HXGX_RCIMC_S1B2_Val_05", "M30HXGX_RCIMC_S1B2_Desc",
                            "M30HXGX_RCIMC_SRB2_Val_05", "M30HXGX_RCIMC_SRB2_Desc", "M30HXGX_RCIMC_FLUD_Val_05", "M30HXGX_RCIMC_FLUD_Desc", "M30HXGX_RCIMC_MLVS_Loe", "M30HXGX_RCIMC_MLVS_Desc", "M30HXGX_RCIMC_HPCT_Val_05", "M30HXGX_RCIMC_HPCT_Desc",
                            "M30HXGX_RCIMC_VHPT_Val_05", "M30HXGX_RCIMC_VHPT_Desc", "M30HXGX_RCIMC_PRTS_Loe", "M30HXGX_RCIMC_PRTS_Desc", "M30HXGX_RCIMC_CPC_Loe", "M30HXGX_RCIMC_CPC_Desc", "M30HXGX_RCIMC_CNPI_Desc",
                            "M30HXGX_RCIMC_CNPC_Val_05", "M30HXGX_RCIMC_CNPC_Desc", "M30HXGX_RCIMC_CWTS_Loe", "M30HXGX_RCIMC_CWTS_Desc", "M30HXGX_RCIMC_EMM_Desc", "M30HXGX_RCIMC_CTRL_Val_05", "M30HXGX_RCIMC_CTRL_Desc",
                            "M30HXGX_RCIMC_LOAD_Val_05", "M30HXGX_RCIMC_LOAD_Desc", "M30HXGX_RCIMC_LLCS_Val_05", "M30HXGX_RCIMC_LLCS_Desc", "M30HXGX_RCIMC_CPSQ_Val_05", "M30HXGX_RCIMC_CPSQ_Desc", "M30HXGX_RCIMC_LCWT_Val_05", "M30HXGX_RCIMC_LCWT_Desc",
                            "M30HXGX_RCIMC_DELY_Val_05", "M30HXGX_RCIMC_DELY_Desc", "M30HXGX_RCIMC_CLSC_Loe", "M30HXGX_RCIMC_CLSC_Desc", "M30HXGX_RCIMC_ICEM_Loe", "M30HXGX_RCIMC_ICEM_Desc", "M30HXGX_RCIMC_CUNB_Val_05", "M30HXGX_RCIMC_CUNB_Desc",
                            "M30HXGX_RCIMC_NOFL_Desc", "M30HXGX_RCIMC_WMSG_Desc", "M30HXGX_RCIMC_ALRC_Val_05", "M30HXGX_RCIMC_ALRC_Desc", "M30HXGX_RCIMC_CRST_Val_05", "M30HXGX_RCIMC_CRST_Desc",
                            "M30HXGX_RCIMC_CRT1_Val_05", "M30HXGX_RCIMC_CRT1_Desc", "M30HXGX_RCIMC_CRT2_Val_05", "M30HXGX_RCIMC_CRT2_Desc", "M30HXGX_RCIMC_DGRC_Val_05", "M30HXGX_RCIMC_DGRC_Desc", "M30HXGX_RCIMC_HRST_Val_05", "M30HXGX_RCIMC_HRST_Desc",
                            "M30HXGX_RCIMC_HRT1_Val_05", "M30HXGX_RCIMC_HRT1_Desc", "M30HXGX_RCIMC_HRT2_Val_05", "M30HXGX_RCIMC_HRT2_Desc", "M30HXGX_RCIMC_DGRH_Val_05", "M30HXGX_RCIMC_DGRH_Desc", "M30HXGX_RCIMC_DMDC_Val_05", "M30HXGX_RCIMC_DMDC_Desc",
                            "M30HXGX_RCIMC_DM20_Val_05", "M30HXGX_RCIMC_DM20_Desc", "M30HXGX_RCIMC_SHNM_Val_05", "M30HXGX_RCIMC_SHNM_Desc", "M30HXGX_RCIMC_SHDL_Val_05", "M30HXGX_RCIMC_SHDL_Desc", "M30HXGX_RCIMC_SHTM_Val_05", "M30HXGX_RCIMC_SHTM_Desc",
                            "M30HXGX_RCIMC_DLS1_Val_05", "M30HXGX_RCIMC_DLS1_Desc", "M30HXGX_RCIMC_DLS2_Val_05", "M30HXGX_RCIMC_DLS2_Desc", "M30HXGX_RCIMC_LLEN_Loe", "M30HXGX_RCIMC_LLEN_Desc", "M30HXGX_RCIMC_MSSL_Desc",
                            "M30HXGX_RCIMC_SLVA_Val_05", "M30HXGX_RCIMC_SLVA_Desc", "M30HXGX_RCIMC_LLBL_Val_05", "M30HXGX_RCIMC_LLBL_Desc", "M30HXGX_RCIMC_LLBD_Val_05", "M30HXGX_RCIMC_LLBD_Desc", "M30HXGX_RCIMC_LLDY_Val_05", "M30HXGX_RCIMC_LLDY_Desc",
                            "M30HXGX_RCIMC_PARA_Loe", "M30HXGX_RCIMC_PARA_Desc", "M30HXGX_RCIMC_CLSP_Val_05", "M30HXGX_RCIMC_CLSP_Desc", "M30HXGX_RCIMC_HTSP_Val_05", "M30HXGX_RCIMC_HTSP_Desc", "M30HXGX_RCIMC_RLS_Loe", "M30HXGX_RCIMC_RLS_Desc",
                            "M30HXGX_RCIMC_CRMP_Val_05", "M30HXGX_RCIMC_CRMP_Desc", "M30HXGX_RCIMC_HRMP_Val_05", "M30HXGX_RCIMC_HRMP_Desc", "M30HXGX_RCIMC_HCSW_Loe", "M30HXGX_RCIMC_HCSW_Desc", "M30HXGX_RCIMC_ZGN_Val_05", "M30HXGX_RCIMC_ZGN_Desc",
                            "M30HXGX_RCIMC_BRNL_Loe", "M30HXGX_RCIMC_BRNL_Desc", "M30HXGX_RCIMC_FPSP_Val_05", "M30HXGX_RCIMC_FPSP_Desc", "M30HXGX_RCIMC_CCNA_Val_05", "M30HXGX_RCIMC_CCNA_Desc", "M30HXGX_RCIMC_CCNB_Val_05", "M30HXGX_RCIMC_CCNB_Desc",
                            "M30HXGX_RCIMC_BAUD_Val_05", "M30HXGX_RCIMC_BAUD_Desc", "M30HXGX_RCIMC_HPGN_Val_05", "M30HXGX_RCIMC_HPGN_Desc", "M30HXGX_RCIMC_HIGN_Val_05", "M30HXGX_RCIMC_HIGN_Desc", "M30HXGX_RCIMC_HDGN_Val_05", "M30HXGX_RCIMC_HDGN_Desc",
                            "M30HXGX_RCIMC_HMIN_Val_05", "M30HXGX_RCIMC_HMIN_Desc", "M30HXGX_RCIMC_MTSP_Val_05", "M30HXGX_RCIMC_MTSP_Desc", "M30HXGX_RCIMC_BRFZ_Val_05", "M30HXGX_RCIMC_BRFZ_Desc", "M30HXGX_RCIMC_MCSP_Val_05", "M30HXGX_RCIMC_MCSP_Desc",
                            "M30HXGX_RCIMC_EXSA_Val_05", "M30HXGX_RCIMC_EXSA_Desc", "M30HXGX_RCIMC_EXSB_Val_05", "M30HXGX_RCIMC_EXSB_Desc", "M30HXGX_RCIMC_ENA1_Loe", "M30HXGX_RCIMC_ENA1_Desc", "M30HXGX_RCIMC_ENA2_Desc",
                            "M30HXGX_RCIMC_ENB1_Loe", "M30HXGX_RCIMC_ENB1_Desc", "M30HXGX_RCIMC_ENB2_Desc", "M30HXGX_RCIMC_WDNE_Loe", "M30HXGX_RCIMC_WDNE_Desc", "M30HXGX_RCIMC_ECON_Desc",
                            "M30HXGX_RCIMC_EVPS_Val_05", "M30HXGX_RCIMC_EVPS_Desc", "M30HXGX_RCIMC_LWTC_Loe", "M30HXGX_RCIMC_LWTC_Desc", "M30HXGX_RCIMC_APSP_Val_05", "M30HXGX_RCIMC_APSP_Desc", "M30HXGX_RCIMC_CNDT_Loe", "M30HXGX_RCIMC_CNDT_Desc",
                            "M30HXGX_RCIMC_TDBC_Loe", "M30HXGX_RCIMC_TDBC_Desc", "M30HXGX_RCIMC_OATB_Desc", "M30HXGX_RCIMC_GSBC_Loe", "M30HXGX_RCIMC_GSBC_Desc", "M30HXGX_RCIMC_BCAK_Desc"]

        self.M30HX_RCIMSP_swrite = []
        self.M30HX_RCIMSP_tog = []
        self.M30HX_RCIMSP_write = ["M30HXGX_RCIMSP_CSP1_Val_05", "M30HXGX_RCIMSP_CSP1_Desc", "M30HXGX_RCIMSP_CSP2_Val_05", "M30HXGX_RCIMSP_CSP2_Desc", "M30HXGX_RCIMSP_CSP3_Val_05", "M30HXGX_RCIMSP_CSP3_Desc", "M30HXGX_RCIMSP_HSP1_Val_05",
                            "M30HXGX_RCIMSP_HSP1_Desc", "M30HXGX_RCIMSP_HSP2_Val_05", "M30HXGX_RCIMSP_HSP2_Desc", "M30HXGX_RCIMSP_HDPA_Val_05", "M30HXGX_RCIMSP_HDPA_Desc", "M30HXGX_RCIMSP_HDPB_Val_05", "M30HXGX_RCIMSP_HDPB_Desc"]

        self.M30HX_CTMST_swrite = []
        self.M30HX_CTMST_tog = []
        CTMST_dropdown_samexpath = [ "M30HXGX_CTMST_CNDP_Loe", "M30HXGX_CTMST_CNDP_Desc", "M30HXGX_CTMST_RMTA_Loe", "M30HXGX_CTMST_RMTA_Desc", "M30HXGX_CTMST_CCA1_Loe", "M30HXGX_CTMST_CCA1_Desc",
                            "M30HXGX_CTMST_CCA2_Loe", "M30HXGX_CTMST_CCA2_Desc", "M30HXGX_CTMST_LDA1_Loe", "M30HXGX_CTMST_LDA1_Desc", "M30HXGX_CTMST_LDA2_Loe", "M30HXGX_CTMST_LDA2_Desc", "M30HXGX_CTMST_MLV_Loe", "M30HXGX_CTMST_MLV_Desc",
                            "M30HXGX_CTMST_OLHA_Loe", "M30HXGX_CTMST_OLHA_Desc", "M30HXGX_CTMST_CCB1_Loe", "M30HXGX_CTMST_CCB1_Desc", "M30HXGX_CTMST_CCB2_Loe", "M30HXGX_CTMST_CCB2_Desc", "M30HXGX_CTMST_LDB1_Loe", "M30HXGX_CTMST_LDB1_Desc",
                            "M30HXGX_CTMST_LDB2_Loe", "M30HXGX_CTMST_LDB2_Desc", "M30HXGX_CTMST_OLHB_Loe", "M30HXGX_CTMST_OLHB_Desc"]
        self.M30HX_CTMST_write = ["M30HXGX_CTMST_Default", "M30HXGX_CTMST_EMPTY_Loe", "M30HXGX_CTMST_EMPTY_Desc", "M30HXGX_CTMST_EXVA_Val_05", "M30HXGX_CTMST_EXVA_Desc", "M30HXGX_CTMST_VHPA_Val_05", "M30HXGX_CTMST_VHPA_Desc", "M30HXGX_CTMST_OLPA_Loe", "M30HXGX_CTMST_OLPA_Desc",
                            "M30HXGX_CTMST_MCA1_Loe", "M30HXGX_CTMST_MCA1_Desc", "M30HXGX_CTMST_MCA2_Loe", "M30HXGX_CTMST_MCA2_Desc", "M30HXGX_CTMST_OSA1_Loe", "M30HXGX_CTMST_OSA1_Desc", "M30HXGX_CTMST_OSA2_Loe", "M30HXGX_CTMST_OSA2_Desc",
                            "M30HXGX_CTMST_EXVB_Val_05", "M30HXGX_CTMST_EXVB_Desc", "M30HXGX_CTMST_VHPB_Val_05", "M30HXGX_CTMST_VHPB_Desc", "M30HXGX_CTMST_OLPB_Loe", "M30HXGX_CTMST_OLPB_Desc", "M30HXGX_CTMST_MCB1_Loe", "M30HXGX_CTMST_MCB1_Desc",
                            "M30HXGX_CTMST_MCB2_Loe", "M30HXGX_CTMST_MCB2_Desc", "M30HXGX_CTMST_OSB1_Loe", "M30HXGX_CTMST_OSB1_Desc", "M30HXGX_CTMST_OSB2_Loe", "M30HXGX_CTMST_OSB2_Desc", "M30HXGX_CTMST_FAN1_Loe", "M30HXGX_CTMST_FAN1_Desc",
                            "M30HXGX_CTMST_FAN2_Loe", "M30HXGX_CTMST_FAN2_Desc", "M30HXGX_CTMST_FAN3_Loe", "M30HXGX_CTMST_FAN3_Desc", "M30HXGX_CTMST_FAN4_Loe", "M30HXGX_CTMST_FAN4_Desc", "M30HXGX_CTMST_CLRP_Loe", "M30HXGX_CTMST_CLRP_Desc",
                            "M30HXGX_CTMST_CLRH_Loe", "M30HXGX_CTMST_CLRH_Desc"]

        self.M30HX_OPDATA_swrite = []
        self.M30HX_OPDATA_tog = []
        self.M30HX_OPDATA_write = ["M30HXGX_OPDATA_COOEF_Val_05", "M30HXGX_OPDATA_COOEF_Desc", "M30HXGX_OPDATA_COOLF_Val_05", "M30HXGX_OPDATA_COOLF_Desc", "M30HXGX_OPDATA_OAT_Val_05", "M30HXGX_OPDATA_OAT_Desc", "M30HXGX_OPDATA_ST_Val_05", "M30HXGX_OPDATA_ST_Desc",
                                    "M30HXGX_OPDATA_CONEF_Val_05", "M30HXGX_OPDATA_CONEF_Desc", "M30HXGX_OPDATA_CONLF_Val_05", "M30HXGX_OPDATA_CONLF_Desc", "M30HXGX_OPDATA_LLLF_Val_05", "M30HXGX_OPDATA_LLLF_Desc", "M30HXGX_OPDATA_SCTA_Val_05", "M30HXGX_OPDATA_SCTB_Val_05",
                                    "M30HXGX_OPDATA_SCT_Desc", "M30HXGX_OPDATA_SSTA_Val_05", "M30HXGX_OPDATA_SSTB_Val_05", "M30HXGX_OPDATA_SST_Desc", "M30HXGX_OPDATA_DSTA_Val_05", "M30HXGX_OPDATA_DSTB_Val_05", "M30HXGX_OPDATA_DST_Desc", "M30HXGX_OPDATA_MTEMPA_Val_05",
                                    "M30HXGX_OPDATA_MTEMPB_Val_05", "M30HXGX_OPDATA_MTEMP_Desc", "M30HXGX_OPDATA_DISPREA_Val_05", "M30HXGX_OPDATA_DISPREB_Val_05", "M30HXGX_OPDATA_DISPRE_Desc", "M30HXGX_OPDATA_SUCPREA_Val_05", "M30HXGX_OPDATA_SUCPREB_Val_05",
                                    "M30HXGX_OPDATA_SUCPRE_Desc", "M30HXGX_OPDATA_ECOPREA_Val_05", "M30HXGX_OPDATA_ECOPREB_Val_05", "M30HXGX_OPDATA_ECOPRE_Desc", "M30HXGX_OPDATA_OILPREA_Val_05", "M30HXGX_OPDATA_OILPREB_Val_05", "M30HXGX_OPDATA_OILPRE_Desc",
                                    "M30HXGX_OPDATA_OILPREDA_Val_05", "M30HXGX_OPDATA_OILPREDB_Val_05", "M30HXGX_OPDATA_OILPRED_Desc", "M30HXGX_OPDATA_OILFILDA_Val_05", "M30HXGX_OPDATA_OILFILDB_Val_05", "M30HXGX_OPDATA_OILFILD_Desc", "M30HXGX_OPDATA_OILFILDA1_Val_05",
                                    "M30HXGX_OPDATA_OILFILDB1_Val_05", "M30HXGX_OPDATA_OILFILD1_Desc", "M30HXGX_OPDATA_CALOPA_Val_05", "M30HXGX_OPDATA_CALOPB_Val_05", "M30HXGX_OPDATA_CALOP_Desc", "M30HXGX_OPDATA_A1_click", "M30HXGX_OPDATA_A1_L1_Val_05",
                                    "M30HXGX_OPDATA_A1_L2_Val_05", "M30HXGX_OPDATA_A1_L3_Val_05", "M30HXGX_OPDATA_A2_click", "M30HXGX_OPDATA_A2_L1_Val_05", "M30HXGX_OPDATA_A2_L2_Val_05", "M30HXGX_OPDATA_A2_L3_Val_05", "M30HXGX_OPDATA_B1_click",
                                    "M30HXGX_OPDATA_B1_L1_Val_05", "M30HXGX_OPDATA_B1_L2_Val_05", "M30HXGX_OPDATA_B1_L3_Val_05", "M30HXGX_OPDATA_B2_click", "M30HXGX_OPDATA_B2_L1_Val_05", "M30HXGX_OPDATA_B2_L2_Val_05", "M30HXGX_OPDATA_B2_L3_Val_05",
                                    "M30HXGX_OPDATA_FM1_click", "M30HXGX_OPDATA_FM1_L1_Val_05", "M30HXGX_OPDATA_FM1_L2_Val_05", "M30HXGX_OPDATA_FM1_L3_Val_05", "M30HXGX_OPDATA_FM2_click", "M30HXGX_OPDATA_FM2_L1_Val_05", "M30HXGX_OPDATA_FM2_L2_Val_05",
                                    "M30HXGX_OPDATA_FM2_L3_Val_05", "M30HXGX_OPDATA_FM3_click", "M30HXGX_OPDATA_FM3_L1_Val_05", "M30HXGX_OPDATA_FM3_L2_Val_05", "M30HXGX_OPDATA_FM3_L3_Val_05", "M30HXGX_OPDATA_FM4_click", "M30HXGX_OPDATA_FM4_L1_Val_05",
                                    "M30HXGX_OPDATA_FM4_L2_Val_05", "M30HXGX_OPDATA_FM4_L3_Val_05", "M30HXGX_OPDATA_FM5_click", "M30HXGX_OPDATA_FM5_L1_Val_05", "M30HXGX_OPDATA_FM5_L2_Val_05", "M30HXGX_OPDATA_FM5_L3_Val_05", "M30HXGX_OPDATA_FM6_click",
                                    "M30HXGX_OPDATA_FM6_L1_Val_05", "M30HXGX_OPDATA_FM6_L2_Val_05", "M30HXGX_OPDATA_FM6_L3_Val_05", "M30HXGX_OPDATA_FM7_click", "M30HXGX_OPDATA_FM7_L1_Val_05", "M30HXGX_OPDATA_FM7_L2_Val_05", "M30HXGX_OPDATA_FM7_L3_Val_05",
                                    "M30HXGX_OPDATA_FM8_click", "M30HXGX_OPDATA_FM8_L1_Val_05", "M30HXGX_OPDATA_FM8_L2_Val_05", "M30HXGX_OPDATA_FM8_L3_Val_05", "M30HXGX_OPDATA_FM9_click", "M30HXGX_OPDATA_FM9_L1_Val_05", "M30HXGX_OPDATA_FM9_L2_Val_05",
                                    "M30HXGX_OPDATA_FM9_L3_Val_05", "M30HXGX_OPDATA_FM10_click", "M30HXGX_OPDATA_FM10_L1_Val_05", "M30HXGX_OPDATA_FM10_L2_Val_05", "M30HXGX_OPDATA_FM10_L3_Val_05", "M30HXGX_OPDATA_FM11_click", "M30HXGX_OPDATA_FM11_L1_Val_05",
                                    "M30HXGX_OPDATA_FM11_L2_Val_05", "M30HXGX_OPDATA_FM11_L3_Val_05", "M30HXGX_OPDATA_FM12_click", "M30HXGX_OPDATA_FM12_L1_Val_05", "M30HXGX_OPDATA_FM12_L2_Val_05", "M30HXGX_OPDATA_FM12_L3_Val_05", "M30HXGX_OPDATA_FM13_click",
                                    "M30HXGX_OPDATA_FM13_L1_Val_05", "M30HXGX_OPDATA_FM13_L2_Val_05", "M30HXGX_OPDATA_FM13_L3_Val_05", "M30HXGX_OPDATA_FM14_click", "M30HXGX_OPDATA_FM14_L1_Val_05", "M30HXGX_OPDATA_FM14_L2_Val_05", "M30HXGX_OPDATA_FM14_L3_Val_05",
                                    "M30HXGX_OPDATA_FM15_click", "M30HXGX_OPDATA_FM15_L1_Val_05", "M30HXGX_OPDATA_FM15_L2_Val_05", "M30HXGX_OPDATA_FM15_L3_Val_05", "M30HXGX_OPDATA_FM16_click", "M30HXGX_OPDATA_FM16_L1_Val_05", "M30HXGX_OPDATA_FM16_L2_Val_05",
                                    "M30HXGX_OPDATA_FM16_L3_Val_05"]

    def write_data(self, Data):
        self.prefix = {'initial': 'M30HX_INIT', 'start': 'M30HX_SOM', 'record1':'M30HX_SW', 'record2': 'M30HX_RCIMC', 'record3': 'M30HX_RCIMSP', 'component': 'M30HX_CTMST', 'operating': 'M30HX_OPDATA'}

        for i in range(len(eval("self." + self.prefix[Data['Model']] + "_write"))):
            if "Val_" in eval("self." + self.prefix[Data['Model']] + "_write[i]") or "val_" in eval(
                    "self." + self.prefix[Data['Model']] + "_write[i]"):
                xpath = eval("UnitStartUp_locators." + eval("self." + self.prefix[Data['Model']] + "_write[i]"))
                try:
                    self.checklist.write(xpath, Data)
                except:
                    print("Error: ", eval("self." + self.prefix[Data['Model']] + "_write[i]"))
                print('Written UnitStartUp data of ' + eval("self." + self.prefix[Data['Model']] + "_write[i]") + ' =', \
                    Data['testdata'])
            elif "click" in eval("self." + self.prefix[Data['Model']] + "_write[i]"):
                self.checklist.click(eval("self." + self.prefix[Data['Model']] + "_write[i]"), "UnitStartUp_locators")

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
                    print('Written UnitStartUp data to ' + str(eval("self."+self.prefix[Data['Model']]+"_swrite[i]")) \
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
            if eval('self.' + self.prefix[Data['Model']] + '_tog')[y][-3:] == 'yes':
                xpath = eval('self.' + self.prefix[Data['Model']] + '_tog')[y]
                self.checklist.click(xpath, page_locators="UnitStartUp_locators")
                print('Written UnitStartUp data of ' + xpath + ' =', 'yes')

    def read_data(self, Data):
        for ele in eval("self." + self.prefix[Data['Model']] + "_write"):
            if ele != self.prefix[Data['Model']] + "_Default":
                common_xpath = eval(
                    "UnitStartUp_locators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read_normal',
                                            page_locators="UnitStartUp_locators")
                if 'Val_' in ele[-6:]:
                    try:
                        assertion.assertEqual(float(value) == float(
                            ''.join(filter(str.isdigit, str(Data['testdata'])))[:eval(ele[-2:])]), True)
                        print('Read UnitStartUP Data (' + ele + ')' + ' =', value)
                    except Exception as e:
                        print("********************************************************************************************************************************\n" \
                              "88888888888888888888888888888888888888888888888888888888888   ERROR   8888888888888888888888888888888888888888888888888888888888\n" \
                              "********************************************************************************************************************************")
                        print(e.message)
                        print('Read UnitStartUP Data (' + ele + ')' + ' =', value)
                elif 'val_' in ele[-6:]:
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
            if ele[-3:] == 'yes':
                assertion.assertEqual(value == 'true', True)
            elif ele[-2:] == 'no':
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
                elif 'Val_' in ele[-6:] or 'val_' in ele[-6:]:
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
            if ele[-3:] == 'yes':
                assertion.assertEqual(value == None, True)
            elif ele[-2:] == 'no':
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