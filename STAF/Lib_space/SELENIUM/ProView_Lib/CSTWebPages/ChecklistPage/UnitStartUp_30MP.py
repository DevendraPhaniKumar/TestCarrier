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

class UnitStartUp_30MP(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(UnitStartUp_30MP, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()

    def locator_name(self):
        ##########################################################  30HX  ##########################################################
        self.M30MP_UNITSTATUP_INIT_swrite = ["M30MP_UNITSTATUP_INIT_Default", "M30MP_UNITSTATUP_INIT_6AB_Val_05", "M30MP_UNITSTATUP_INIT_6AB_Desc", "M30MP_UNITSTATUP_INIT_6AC_Val_05", "M30MP_UNITSTATUP_INIT_6AC_Desc",
                                        "M30MP_UNITSTATUP_INIT_6BC_Val_05", "M30MP_UNITSTATUP_INIT_6BC_Desc", "M30MP_UNITSTATUP_INIT_6AAVOLT_Val", "M30MP_UNITSTATUP_INIT_6AAVOLT_Desc", "M30MP_UNITSTATUP_INIT_6BMAXDEV_Val_05",
                                        "M30MP_UNITSTATUP_INIT_6BMAXDEV_Desc", "M30MP_UNITSTATUP_INIT_6CVOLIMB_Val", "M30MP_UNITSTATUP_INIT_6CVOLIMB_Desc"]
        self.M30MP_UNITSTATUP_INIT_write = []
        self.M30MP_UNITSTATUP_INIT_tog = ["M30MP_UNITSTATUP_INIT_1CG_yes", "M30MP_UNITSTATUP_INIT_1CG_no", "M30MP_UNITSTATUP_INIT_1C_Desc", "M30MP_UNITSTATUP_INIT_2CG_yes", "M30MP_UNITSTATUP_INIT_2CG_no", "M30MP_UNITSTATUP_INIT_2C_Desc",
                                          "M30MP_UNITSTATUP_INIT_3CG_yes", "M30MP_UNITSTATUP_INIT_3CG_no", "M30MP_UNITSTATUP_INIT_3CR_Desc", "M30MP_UNITSTATUP_INIT_4LG_yes", "M30MP_UNITSTATUP_INIT_4LG_no", "M30MP_UNITSTATUP_INIT_4L_Desc",
                                          "M30MP_UNITSTATUP_INIT_5SG_yes", "M30MP_UNITSTATUP_INIT_5SG_no", "M30MP_UNITSTATUP_INIT_5S_Desc", "M30MP_UNITSTATUP_INIT_7IG_yes", "M30MP_UNITSTATUP_INIT_7IG_no", "M30MP_UNITSTATUP_INIT_7I_Desc"]

        self.M30MP_UNITSTATUP_CPDAC_swrite = ["M30MP_UNITSTATUP_CPDAC_1FEC_Default ", "M30MP_UNITSTATUP_CPDAC_1FEC_Val_05", "M30MP_UNITSTATUP_CPDAC_1FEC_Desc", "M30MP_UNITSTATUP_CPDAC_2FLC_Val_05", "M30MP_UNITSTATUP_CPDAC_2FLC_Desc",
                                "M30MP_UNITSTATUP_CPDAC_3PSIG_Val_05", "M30MP_UNITSTATUP_CPDAC_3PSIG_Desc", "M30MP_UNITSTATUP_CPDAC_3A_Val_05", "M30MP_UNITSTATUP_CPDAC_3A_Desc", "M30MP_UNITSTATUP_CPDAC_3B_Val_05",
                                "M30MP_UNITSTATUP_CPDAC_3B_Desc", "M30MP_UNITSTATUP_CPDAC_3C_Val_05", "M30MP_UNITSTATUP_CPDAC_3C_Desc"]
        self.M30MP_UNITSTATUP_CPDAC_write = []
        self.M30MP_UNITSTATUP_CPDAC_tog = []

        self.M30MP_UNITSTATUP_SOM_swrite = []
        self.M30MP_UNITSTATUP_SOM_tog = ["M30MP_UNITSTATUP_SOM_C1G_yes", "M30MP_UNITSTATUP_SOM_C1G_no", "M30MP_UNITSTATUP_SOM_C1_Desc", "M30MP_UNITSTATUP_SOM_C2G_yes", "M30MP_UNITSTATUP_SOM_C2G_no",
                                "M30MP_UNITSTATUP_SOM_C2_Desc", "M30MP_UNITSTATUP_SOM_S1G_yes", "M30MP_UNITSTATUP_SOM_S1G_no", "M30MP_UNITSTATUP_SOM_S1_Desc", "M30MP_UNITSTATUP_SOM_S2G_yes",
                                "M30MP_UNITSTATUP_SOM_S2G_no", "M30MP_UNITSTATUP_SOM_S2_Desc", "M30MP_UNITSTATUP_SOM_S3G_yes", "M30MP_UNITSTATUP_SOM_S3G_no", "M30MP_UNITSTATUP_SOM_S3_Desc",
                                "M30MP_UNITSTATUP_SOM_S4G_yes", "M30MP_UNITSTATUP_SOM_S4G_no", "M30MP_UNITSTATUP_SOM_S4_Desc"]
        self.M30MP_UNITSTATUP_SOM_write = []

        self.M30MP_UNITSTATUP_RSVM_swrite = []
        self.M30MP_UNITSTATUP_RSVM_tog = []
        self.M30MP_UNITSTATUP_RSVM_write = ["M30MP_UNITSTATUP_RSVM_MBB1_val_20", "M30MP_UNITSTATUP_RSVM_MBB3_val_20", "M30MP_UNITSTATUP_RSVM_MBB_Desc", "M30MP_UNITSTATUP_RSVM_EXV1_val_20", "M30MP_UNITSTATUP_RSVM_EXV3_val_20",
                                    "M30MP_UNITSTATUP_RSVM_EXV123_Desc", "M30MP_UNITSTATUP_RSVM_EMM1_val_20", "M30MP_UNITSTATUP_RSVM_EMM3_val_20", "M30MP_UNITSTATUP_RSVM_EMM_Desc", "M30MP_UNITSTATUP_RSVM_AUX1_val_20",
                                    "M30MP_UNITSTATUP_RSVM_AUX3_val_20", "M30MP_UNITSTATUP_RSVM_AUX_Desc", "M30MP_UNITSTATUP_RSVM_MARQ1_val_20", "M30MP_UNITSTATUP_RSVM_MARQ3_val_20", "M30MP_UNITSTATUP_RSVM_MARQ_Desc",
                                    "M30MP_UNITSTATUP_RSVM_NAVI1_val_20", "M30MP_UNITSTATUP_RSVM_NAVI3_val_20", "M30MP_UNITSTATUP_RSVM_NAVI_Desc"]

        self.M30MP_UNITSTATUP_RCISP_swrite = []
        self.M30MP_UNITSTATUP_RCISP_tog = []
        self.M30MP_UNITSTATUP_RCISP_write = ["M30MP_UNITSTATUP_RCISP_CSP1_Val_05", "M30MP_UNITSTATUP_RCISP_CSP1_Desc", "M30MP_UNITSTATUP_RCISP_CSP2_Val_05", "M30MP_UNITSTATUP_RCISP_CSP2_Desc", "M30MP_UNITSTATUP_RCISP_CSP3_Val_05",
                                              "M30MP_UNITSTATUP_RCISP_CSP3_Desc", "M30MP_UNITSTATUP_RCISP_HSP1_Val_05", "M30MP_UNITSTATUP_RCISP_HSP1_Desc", "M30MP_UNITSTATUP_RCISP_HSP2_Val_05", "M30MP_UNITSTATUP_RCISP_HSP2_Desc",
                                              "M30MP_UNITSTATUP_RCISP_HDPA_Val_05", "M30MP_UNITSTATUP_RCISP_HDPA_Desc", "M30MP_UNITSTATUP_RCISP_HDPB_Val_05", "M30MP_UNITSTATUP_RCISP_HDPB_Desc"]

        self.M30MP_UNITSTATUP_RCIUC_swrite = []
        self.M30MP_UNITSTATUP_RCIUC_tog = []
        self.M30MP_UNITSTATUP_RCIUC_write = ["M30MP_UNITSTATUP_RCIUC_TYPE_Val_05", "M30MP_UNITSTATUP_RCIUC_TYPE_Desc", "M30MP_UNITSTATUP_RCIUC_SIZE_Val_05", "M30MP_UNITSTATUP_RCIUC_SIZE_Desc", "M30MP_UNITSTATUP_RCIUC_SZA1_Val_05",
                                    "M30MP_UNITSTATUP_RCIUC_SZA1_Desc", "M30MP_UNITSTATUP_RCIUC_SZA2_Val_05", "M30MP_UNITSTATUP_RCIUC_SZA2_Desc", "M30MP_UNITSTATUP_RCIUC_SZA3_Val_05", "M30MP_UNITSTATUP_RCIUC_SZA3_Desc",
                                    "M30MP_UNITSTATUP_RCIUC_A1TY_Loe", "M30MP_UNITSTATUP_RCIUC_A1TY_Desc", "M30MP_UNITSTATUP_RCIUC_MAXT_Val_05", "M30MP_UNITSTATUP_RCIUC_MAXT_Desc", "M30MP_UNITSTATUP_RCIUC_EXV_Loe",
                                    "M30MP_UNITSTATUP_RCIUC_EXV_Desc"]

        self.M30MP_UNITSTATUP_RCIOHC1_swrite = []
        self.M30MP_UNITSTATUP_RCIOHC1_tog = []
        self.M30MP_UNITSTATUP_RCIOHC1_write = ["M30MP_UNITSTATUP_RCIOHC1_FLUD_Val_05", "M30MP_UNITSTATUP_RCIOHC1_FLUD_Desc", "M30MP_UNITSTATUP_RCIOHC1_MLVS_Loe", "M30MP_UNITSTATUP_RCIOHC1_MLVS_Desc", "M30MP_UNITSTATUP_RCIOHC1_RGEN_Loe",
                                    "M30MP_UNITSTATUP_RCIOHC1_RGEN_Desc", "M30MP_UNITSTATUP_RCIOHC1_OATE_Loe", "M30MP_UNITSTATUP_RCIOHC1_OATE_Desc", "M30MP_UNITSTATUP_RCIOHC1_CSBE_Loe", "M30MP_UNITSTATUP_RCIOHC1_CSBE_Desc",
                                    "M30MP_UNITSTATUP_RCIOHC1_CPC_Loe", "M30MP_UNITSTATUP_RCIOHC1_CPC_Desc", "M30MP_UNITSTATUP_RCIOHC1_PMDY_Val_05", "M30MP_UNITSTATUP_RCIOHC1_PMDY_Desc", "M30MP_UNITSTATUP_RCIOHC1_DPME_Loe",
                                    "M30MP_UNITSTATUP_RCIOHC1_DPME_Desc", "M30MP_UNITSTATUP_RCIOHC1_DFLS_Loe", "M30MP_UNITSTATUP_RCIOHC1_DFLS_Desc", "M30MP_UNITSTATUP_RCIOHC1_CDWS_Loe", "M30MP_UNITSTATUP_RCIOHC1_CDWS_Desc"]

        self.M30MP_UNITSTATUP_RCIOHC2_swrite = []
        self.M30MP_UNITSTATUP_RCIOHC2_tog = []
        self.M30MP_UNITSTATUP_RCIOHC2_write = ["M30MP_UNITSTATUP_RCIOHC2_CTRL_Val_05", "M30MP_UNITSTATUP_RCIOHC2_CTRL_Desc", "M30MP_UNITSTATUP_RCIOHC2_LCWT_Val_05", "M30MP_UNITSTATUP_RCIOHC2_LCWT_Desc",
                                                "M30MP_UNITSTATUP_RCIOHC2_DELY1_Val_05", "M30MP_UNITSTATUP_RCIOHC2_DELY1_Desc", "M30MP_UNITSTATUP_RCIOHC2_ICEM_Loe", "M30MP_UNITSTATUP_RCIOHC2_ICEM_Desc"]

        self.M30MP_UNITSTATUP_RCICCN_swrite = []
        self.M30MP_UNITSTATUP_RCICCN_tog = []
        self.M30MP_UNITSTATUP_RCICCN_write = ["M30MP_UNITSTATUP_RCICCN_CCNA_Val_05", "M30MP_UNITSTATUP_RCICCN_CCNA_Desc", "M30MP_UNITSTATUP_RCICCN_CCNB_Val_05", "M30MP_UNITSTATUP_RCICCN_CCNB_Desc", "M30MP_UNITSTATUP_RCICCN_BAUD_Val_05",
                                              "M30MP_UNITSTATUP_RCICCN_BAUD_Desc"]

        self.M30MP_UNITSTATUP_RCIEXV_swrite = []
        self.M30MP_UNITSTATUP_RCIEXV_tog = []
        self.M30MP_UNITSTATUP_RCIEXV_write = ["M30MP_UNITSTATUP_RCIEXV_EXVL_Val_05", "M30MP_UNITSTATUP_RCIEXV_EXVL_Desc", "M30MP_UNITSTATUP_RCIEXV_LWTL_Val_05", "M30MP_UNITSTATUP_RCIEXV_LWTL_Desc", "M30MP_UNITSTATUP_RCIEXV_EXVH_Val_05",
                                                "M30MP_UNITSTATUP_RCIEXV_EXVH_Desc", "M30MP_UNITSTATUP_RCIEXV_LWTH_Val_05", "M30MP_UNITSTATUP_RCIEXV_LWTH_Desc", "M30MP_UNITSTATUP_RCIEXV_MINA1_Val_05", "M30MP_UNITSTATUP_RCIEXV_MINA1_Desc",
                                                "M30MP_UNITSTATUP_RCIEXV_RNGA_Val_05", "M30MP_UNITSTATUP_RCIEXV_RNGA_Desc", "M30MP_UNITSTATUP_RCIEXV_SPDA_Val_05", "M30MP_UNITSTATUP_RCIEXV_SPDA_Desc", "M30MP_UNITSTATUP_RCIEXV_POFA_Val_05",
                                                "M30MP_UNITSTATUP_RCIEXV_POFA_Desc", "M30MP_UNITSTATUP_RCIEXV_MINA2_Val_05", "M30MP_UNITSTATUP_RCIEXV_MINA2_Desc", "M30MP_UNITSTATUP_RCIEXV_MAXA_Val_05", "M30MP_UNITSTATUP_RCIEXV_MAXA_Desc",
                                                "M30MP_UNITSTATUP_RCIEXV_OVRA_Val_05", "M30MP_UNITSTATUP_RCIEXV_OVRA_Desc", "M30MP_UNITSTATUP_RCIEXV_TYPA_Val_05", "M30MP_UNITSTATUP_RCIEXV_TYPA_Desc", "M30MP_UNITSTATUP_RCIEXV_HSCT_Val_05",
                                                "M30MP_UNITSTATUP_RCIEXV_HSCT_Desc", "M30MP_UNITSTATUP_RCIEXV_XPCT_Val_05", "M30MP_UNITSTATUP_RCIEXV_XPCT_Desc", "M30MP_UNITSTATUP_RCIEXV_XPER_Val_05", "M30MP_UNITSTATUP_RCIEXV_XPER_Desc",
                                                "M30MP_UNITSTATUP_RCIEXV_APCT_Val_05", "M30MP_UNITSTATUP_RCIEXV_APCT_Desc", "M30MP_UNITSTATUP_RCIEXV_MPCT_Val_05", "M30MP_UNITSTATUP_RCIEXV_MPCT_Desc", "M30MP_UNITSTATUP_RCIEXV_SPCT_Val_05",
                                                "M30MP_UNITSTATUP_RCIEXV_SPCT_Desc", "M30MP_UNITSTATUP_RCIEXV_DELY2_Val_05", "M30MP_UNITSTATUP_RCIEXV_DELY2_Desc", "M30MP_UNITSTATUP_RCIEXV_LDLT_Val_05", "M30MP_UNITSTATUP_RCIEXV_LDLT_Desc",
                                                "M30MP_UNITSTATUP_RCIEXV_SHRT_Val_05", "M30MP_UNITSTATUP_RCIEXV_SHRT_Desc", "M30MP_UNITSTATUP_RCIEXV_LEXM_Val_05", "M30MP_UNITSTATUP_RCIEXV_LEXM_Desc"]

        self.M30MP_UNITSTATUP_RCISP_swrite = []
        self.M30MP_UNITSTATUP_RCISP_tog = []
        self.M30MP_UNITSTATUP_RCISP_write = ["M30MP_UNITSTATUP_RCISP_CSP1_Val_05", "M30MP_UNITSTATUP_RCISP_CSP1_Desc", "M30MP_UNITSTATUP_RCISP_CSP2_Val_05", "M30MP_UNITSTATUP_RCISP_CSP2_Desc", "M30MP_UNITSTATUP_RCISP_CSP3_Val_05",
                                                "M30MP_UNITSTATUP_RCISP_CSP3_Desc", "M30MP_UNITSTATUP_RCISP_HDP_Val_05", "M30MP_UNITSTATUP_RCISP_HDP_Desc", "M30MP_UNITSTATUP_RCISP_BRFZ_Val_05", "M30MP_UNITSTATUP_RCISP_BRFZ_Desc"]

        self.M30MP_UNITSTATUP_CTST_swrite = []
        self.M30MP_UNITSTATUP_CTST_tog = []
        self.M30MP_UNITSTATUP_CTST_write = ["M30MP_UNITSTATUP_CTST_CLRP1_Loe", "M30MP_UNITSTATUP_CTST_CLRP2_Loe", "M30MP_UNITSTATUP_CTST_CLRP1_Desc", "M30MP_UNITSTATUP_CTST_CNDP1_Loe", "M30MP_UNITSTATUP_CTST_CNDP2_Loe",
                                            "M30MP_UNITSTATUP_CTST_CLRP2_Desc", "M30MP_UNITSTATUP_CTST_ULTM11_Val_05", "M30MP_UNITSTATUP_CTST_ULTM21_Loe", "M30MP_UNITSTATUP_CTST_ULTM1_Desc", "M30MP_UNITSTATUP_CTST_CCH1_Loe",
                                            "M30MP_UNITSTATUP_CTST_CCH2_Loe", "M30MP_UNITSTATUP_CTST_CCH_Desc", "M30MP_UNITSTATUP_CTST_CWVO1_Loe", "M30MP_UNITSTATUP_CTST_CWVO2_Loe", "M30MP_UNITSTATUP_CTST_CWVO_Desc",
                                            "M30MP_UNITSTATUP_CTST_CWVC1_Loe", "M30MP_UNITSTATUP_CTST_CWVC2_Loe", "M30MP_UNITSTATUP_CTST_CWVC_Desc", "M30MP_UNITSTATUP_CTST_LLSV1_Loe", "M30MP_UNITSTATUP_CTST_LLSV2_Loe",
                                            "M30MP_UNITSTATUP_CTST_LLSV_Desc", "M30MP_UNITSTATUP_CTST_RMTA1_Loe", "M30MP_UNITSTATUP_CTST_RMTA2_Loe", "M30MP_UNITSTATUP_CTST_RMTA_Desc", "M30MP_UNITSTATUP_CTST_EXVA1_Val_05",
                                            "M30MP_UNITSTATUP_CTST_EXVA2_Loe", "M30MP_UNITSTATUP_CTST_EXFA_Desc", "M30MP_UNITSTATUP_CTST_CCA11_Loe", "M30MP_UNITSTATUP_CTST_CCA12_Loe", "M30MP_UNITSTATUP_CTST_CCA1_Desc",
                                            "M30MP_UNITSTATUP_CTST_ULTM12_Val_05", "M30MP_UNITSTATUP_CTST_ULTM22_Loe", "M30MP_UNITSTATUP_CTST_ULTM2_Desc", "M30MP_UNITSTATUP_CTST_CCA21_Loe", "M30MP_UNITSTATUP_CTST_CCA22_Loe",
                                            "M30MP_UNITSTATUP_CTST_CCA2_Desc", "M30MP_UNITSTATUP_CTST_CCA31_Loe", "M30MP_UNITSTATUP_CTST_CCA32_Loe", "M30MP_UNITSTATUP_CTST_CCA3_Desc", "M30MP_UNITSTATUP_CTST_MLV1_Loe",
                                            "M30MP_UNITSTATUP_CTST_MLV2_Loe", "M30MP_UNITSTATUP_CTST_MLV_Desc"]

        self.M30MP_UNITSTATUP_OP_swrite = ["M30MP_UNITSTATUP_OP_CLWT_Default", "M30MP_UNITSTATUP_OP_CLWT_Val_05", "M30MP_UNITSTATUP_OP_CLWT_Desc", "M30MP_UNITSTATUP_OP_CEWT_Val_05", "M30MP_UNITSTATUP_OP_CEWT_Desc",
                                            "M30MP_UNITSTATUP_OP_CDET_Val_05", "M30MP_UNITSTATUP_OP_CDET_Desc", "M30MP_UNITSTATUP_OP_CDLT_Val_05", "M30MP_UNITSTATUP_OP_CDLT_Desc", "M30MP_UNITSTATUP_OP_OAT_Val_05",
                                            "M30MP_UNITSTATUP_OP_OAT_Desc", "M30MP_UNITSTATUP_OP_SPT_Val_05", "M30MP_UNITSTATUP_OP_SPT_Desc", "M30MP_UNITSTATUP_OP_DISPRE_Val_05", "M30MP_UNITSTATUP_OP_DISPRE_Desc",
                                            "M30MP_UNITSTATUP_OP_SUCPRE_Val_05", "M30MP_UNITSTATUP_OP_SUCPRE_Desc", "M30MP_UNITSTATUP_OP_DLT_Val_05", "M30MP_UNITSTATUP_OP_DLT_Desc", "M30MP_UNITSTATUP_OP_SLT_Val_05",
                                            "M30MP_UNITSTATUP_OP_SLT_Desc", "M30MP_UNITSTATUP_OP_CEF_Val_05", "M30MP_UNITSTATUP_OP_CEF_Desc", "M30MP_UNITSTATUP_OP_CLF_Val_05", "M30MP_UNITSTATUP_OP_CLF_Desc",
                                            "M30MP_UNITSTATUP_OP_CONEF_Val_05", "M30MP_UNITSTATUP_OP_CONEF_Desc", "M30MP_UNITSTATUP_OP_CONLF_Val_05", "M30MP_UNITSTATUP_OP_CONLF_Desc", "M30MP_UNITSTATUP_OP_EXVP_Val_05",
                                            "M30MP_UNITSTATUP_OP_EXVP_Desc"]
        self.M30MP_UNITSTATUP_OP_tog = []
        self.M30MP_UNITSTATUP_OP_write = []

    def write_data(self, Data):
        self.prefix = {'initial': 'M30MP_UNITSTATUP_INIT', 'check_press': 'M30MP_UNITSTATUP_CPDAC', 'start': 'M30MP_UNITSTATUP_SOM', 'record1':'M30MP_UNITSTATUP_RSVM', 'record7': 'M30MP_UNITSTATUP_RCISP', 'record2': 'M30MP_UNITSTATUP_RCIUC',
                       'record3':'M30MP_UNITSTATUP_RCIOHC1', 'record4':'M30MP_UNITSTATUP_RCIOHC2', 'record5':'M30MP_UNITSTATUP_RCICCN', 'record6':'M30MP_UNITSTATUP_RCIEXV', 'component': 'M30MP_UNITSTATUP_CTST', 'operating': 'M30MP_UNITSTATUP_OP'}

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
                if "_Default" not in eval("self."+self.prefix[Data['Model']]+"_swrite[i]") and "_Desc" not in eval("self."+self.prefix[Data['Model']]+"_swrite[i]"):
                    self.checklist.write_similar_element(xpath= xpath, index= eval("UnitStartUp_locators." + eval("self."+self.prefix[Data['Model']]+"_swrite[i]")), Data= Data)
                    print('Written UnitStartUp data to ' + str(eval("self."+self.prefix[Data['Model']]+"_swrite[i]")) \
                           + ' =', Data['testdata'])
        except IndexError as e:
            pass

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
        # xpath = eval("UnitStartUp_locators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
        # xpath = self.find_elements(*xpath)
        # for ele in range(len(xpath)):
        #     try:
        #         xpath[ele].send_keys(Data['testdata'])
        #         xpath[ele].send_keys(Keys.ENTER)
        #         print eval("self." + self.prefix[Data['Model']] + "_swrite[count]"), ele
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

        try:
            common_xpath = eval("UnitStartUp_locators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
            common_xpath = self.find_elements(*common_xpath)
            for ele in eval("self."+self.prefix[Data['Model']]+"_swrite"):
                if '_Default' not in ele and '_Desc' not in ele:
                    value = self.checklist.read(ele, common_xpath, Data, 'read', page_locators="UnitStartUp_locators")
                    assertion.assertEqual(float(value) == float(
                            ''.join(filter(str.isdigit, str(Data['testdata'])))[:eval(ele[-2:])]), True)
                    print('Read Chiller Name Plate Data Information(' + ele + ')' + ' =', value)
        except:
            pass

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

        try:
            common_xpath = eval("UnitStartUp_locators." + eval("self." + self.prefix[Data['Model']] + "_swrite[0]"))
            common_xpath = self.find_elements(*common_xpath)
            for ele in eval("self."+self.prefix[Data['Model']]+"_swrite"):
                if '_Default' not in ele and '_Desc' not in ele:
                    value = self.checklist.read(ele, common_xpath, Data, 'read', page_locators="UnitStartUp_locators")
                    assertion.assertEqual(value == '', True)
                    print('Read Chiller Name Plate Data Information(' + ele + ')' + ' =', 'Null')
        except:
            pass

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