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
from Page_locators.ChecklistPagelocators.PrestartPage_locators import PreStartPageLocators
from Page_locators.ChecklistPagelocators.ConfigLog_locators import ConfigLogPageLocators
from Page_locators.ChecklistPagelocators.ChecklistPage_locators import ChecklistPageLocators
from . import Checklist
from selenium.webdriver.common.by import By
import unittest

driver = object
delay = 75
assertion = unittest.TestCase('__init__')


class ConfigLogSheet_19XRD(Page):
    def __init__(self, webdriver):
        global driver, delay
        super(ConfigLogSheet_19XRD, self).__init__(webdriver)
        driver = webdriver
        self.checklist = Checklist.ChecklistPage(webdriver)
        self.locator_name()

    def locator_name(self):
        ##########################################################  16JB  ##########################################################
        ##########################################################  SET Config table  ##########################################################
        self.M19XRD_set_write = ["M19XRD_SPT_BDL_Val_05", "M19XRD_SPT_BDL_Desc", "M19XRD_SPT_LCWS_Val_05", "M19XRD_SPT_LCWS_Desc", "M19XRD_SPT_ECWS_Val_05", "M19XRD_SPT_ECWS_Desc", "M19XRD_SPT_ICEBS_Val_05",
                                "M19XRD_SPT_ICEBS_Desc", "M19XRD_SPT_TFHS_Val_05", "M19XRD_SPT_TFHS_Desc", "M19XRD_SPT_ICVCSP_Val_21", "M19XRD_SPT_ICVCSP_Desc", "M19XRD_SPT_ICVCIB_Val_21", "M19XRD_SPT_ICVCIB_Desc",
                                "M19XRD_SPT_ICVCIA_Val_21", "M19XRD_SPT_ICVCIA_Desc"]

        self.M19XRD_set_click = ["M19XRD_SPT_ASS_Val_no", "M19XRD_SPT_ASS_Val_yes"]

        self.M19XRD_ismct_write = ["M19XRD_ISMCT_MRLV_Val_05", "M19XRD_ISMCT_MRLV_Desc", "M19XRD_ISMCT_VTR1_Val_05", "M19XRD_ISMCT_VTR1_Desc", "M19XRD_ISMCT_OT_Val_05", "M19XRD_ISMCT_OT_Desc", "M19XRD_ISMCT_UT_Val_05",
                                    "M19XRD_ISMCT_UT_Desc", "M19XRD_ISMCT_OUVT_Val_05", "M19XRD_ISMCT_OUVT_Desc", "M19XRD_ISMCT_VI_Val_05", "M19XRD_ISMCT_VI_Desc", "M19XRD_ISMCT_VIT_Val_05", "M19XRD_ISMCT_VIT_Desc",
                                    "M19XRD_ISMCT_MRLA_Val_05", "M19XRD_ISMCT_MRLA_Desc", "M19XRD_ISMCT_MLRT_Val_05", "M19XRD_ISMCT_MLRT_Desc", "M19XRD_ISMCT_LRSD_Val_05", "M19XRD_ISMCT_LRSD_Desc", "M19XRD_ISMCT_SLRAT_Val_05",
                                    "M19XRD_ISMCT_SLRAT_Desc", "M19XRD_ISMCT_MCCTR1_Val_05", "M19XRD_ISMCT_MCCTR1_Desc", "M19XRD_ISMCT_CIB_Val_05", "M19XRD_ISMCT_CIB_Desc", "M19XRD_ISMCT_CIBT_Val_05", "M19XRD_ISMCT_CIBT_Desc",
                                    "M19XRD_ISMCT_GFCT_Loe", "M19XRD_ISMCT_GFCT_Desc", "M19XRD_ISMCT_GFCTR_Val_05", "M19XRD_ISMCT_GFCTR_Desc", "M19XRD_ISMCT_GFC_Val_05", "M19XRD_ISMCT_GFC_Desc", "M19XRD_ISMCT_GFSD_Val_05",
                                    "M19XRD_ISMCT_GFSD_Desc", "M19XRD_ISMCT_GFP_Val_05", "M19XRD_ISMCT_GFP_Desc", "M19XRD_ISMCT_SCD_Val_Loe", "M19XRD_ISMCT_SCD_Desc", "M19XRD_ISMCT_FREQ_Loe", "M19XRD_ISMCT_FREQ_Desc", "M19XRD_ISMCT_LFF_Loe", "M19XRD_ISMCT_LFF_Desc"]

        self.M19XRD_opti_write = ["M19XRD_OPTIONSPRIOR_ARO_loe", "M19XRD_OPTIONSPRIOR_ARO_Desc", "M19XRD_OPTIONSPRIOR_RCO_Loe", "M19XRD_OPTIONSPRIOR_RCO_Desc", "M19XRD_OPTIONSPRIOR_SSAT_Val_05", "M19XRD_OPTIONSPRIOR_SSAT_Desc",
                                    "M19XRD_OPTIONSPRIOR_SURG_Val_05", "M19XRD_OPTIONSPRIOR_SURG_Desc", "M19XRD_OPTIONSPRIOR_SURGDEAD_Val_05", "M19XRD_OPTIONSPRIOR_SURGDEAD_Desc", "M19XRD_OPTIONSPRIOR_HGBPON_Val_05",
                                    "M19XRD_OPTIONSPRIOR_HGBPON_Desc", "M19XRD_OPTIONSPRIOR_HGBPOFF_Val_05", "M19XRD_OPTIONSPRIOR_HGBPOFF_Desc", "M19XRD_OPTIONSPRIOR_SURGEDELTA_Val_05", "M19XRD_OPTIONSPRIOR_SURGEDELTA_Desc",
                                    "M19XRD_OPTIONSPRIOR_STP_Val_05", "M19XRD_OPTIONSPRIOR_STP_Desc", "M19XRD_OPTIONSPRIOR_ICEBO_Loe", "M19XRD_OPTIONSPRIOR_ICEBO_Desc", "M19XRD_OPTIONSPRIOR_ICETERM_Val_05", "M19XRD_OPTIONSPRIOR_ICETERM_Desc",
                                    "M19XRD_OPTIONSPRIOR_ICEBR_Loe", "M19XRD_OPTIONSPRIOR_ICEBR_Desc", "M19XRD_OPTIONSPRIOR_REFLO_Loe", "M19XRD_OPTIONSPRIOR_REFLO_Desc", "M19XRD_OPTIONSPRIOR_REFLEAKA_Val_05", "M19XRD_OPTIONSPRIOR_REFLEAKA_Desc",
                                    "M19XRD_OPTIONSPRIOR_DELTAPAT4_Val_05", "M19XRD_OPTIONSPRIOR_DELTAPAT4_Desc", "M19XRD_OPTIONSPRIOR_DELTAPAT20_Val_05", "M19XRD_OPTIONSPRIOR_DELTAPAT20_Desc", "M19XRD_OPTIONSPRIOR_MINOUT_Val_05", "M19XRD_OPTIONSPRIOR_MINOUT_Desc"]

        self.M19XRD_opti2_write = ["M19XRD_OPTIONSLATER_ARO_loe", "M19XRD_OPTIONSLATER_ARO_Desc", "M19XRD_OPTIONSLATER_RCO_loe", "M19XRD_OPTIONSLATER_RCO_Desc", "M19XRD_OPTIONSLATER_SSAT_Val_05", "M19XRD_OPTIONSLATER_SSAT_Desc",
                                    "M19XRD_OPTIONSLATER_SURGEBYPA_Val_05", "M19XRD_OPTIONSLATER_SURGEBYPA_Desc", "M19XRD_OPTIONSLATER_SURGELIM_Val_05", "M19XRD_OPTIONSLATER_SURGELIM_Desc", "M19XRD_OPTIONSLATER_SURGEDEL_Val_05",
                                    "M19XRD_OPTIONSLATER_SURGEDEL_Desc", "M19XRD_OPTIONSLATER_SURGEIGV_Val_05", "M19XRD_OPTIONSLATER_SURGEIGV_Desc", "M19XRD_OPTIONSLATER_SURGETSMAX_Val_05", "M19XRD_OPTIONSLATER_SURGETSMAX_Desc",
                                    "M19XRD_OPTIONSLATER_SURGEIGVMAX_Val_05", "M19XRD_OPTIONSLATER_SURGEIGVMAX_Desc", "M19XRD_OPTIONSLATER_SLSF_Val_05", "M19XRD_OPTIONSLATER_SLSF_Desc", "M19XRD_OPTIONSLATER_SLSPF_Val_05",
                                    "M19XRD_OPTIONSLATER_SLSPF_Desc", "M19XRD_OPTIONSLATER_SLHOFF_Val_05", "M19XRD_OPTIONSLATER_SLHOFF_Desc", "M19XRD_OPTIONSLATER_SURGEDEAD_Val_05", "M19XRD_OPTIONSLATER_SURGEDEAD_Desc",
                                    "M19XRD_OPTIONSLATER_HGBPONDELTA_Val_05", "M19XRD_OPTIONSLATER_HGBPONDELTA_Desc", "M19XRD_OPTIONSLATER_HGBPOFFDELTA_Val_05", "M19XRD_OPTIONSLATER_HGBPOFFDELTA_Desc", "M19XRD_OPTIONSLATER_SURGEDELAMP_Val_05",
                                    "M19XRD_OPTIONSLATER_SURGEDELAMP_Desc", "M19XRD_OPTIONSLATER_SURGETP_Val_05", "M19XRD_OPTIONSLATER_SURGETP_Desc", "M19XRD_OPTIONSLATER_ICEBO_Loe", "M19XRD_OPTIONSLATER_ICEBO_Desc",
                                    "M19XRD_OPTIONSLATER_ICEBTERM_Val_05", "M19XRD_OPTIONSLATER_ICEBTERM_Desc", "M19XRD_OPTIONSLATER_ICEBR_Loe", "M19XRD_OPTIONSLATER_ICEBR_Desc", "M19XRD_OPTIONSLATER_REFLEAK_Loe",
                                    "M19XRD_OPTIONSLATER_REFLEAK_Desc", "M19XRD_OPTIONSLATER_REFLEAKA_Val_05", "M19XRD_OPTIONSLATER_REFLEAKA_Desc", "M19XRD_OPTIONSLATER_DELTAAT4_Val_05", "M19XRD_OPTIONSLATER_DELTAAT4_Desc",
                                    "M19XRD_OPTIONSLATER_DELTAAT20_Val_05", "M19XRD_OPTIONSLATER_DELTAAT20_Desc", "M19XRD_OPTIONSLATER_MINOUT_Val_05", "M19XRD_OPTIONSLATER_MINOUT_Desc"]

        self.M19XRD_setup1_write = ["M19XRD_SETUP1_CMTO_Val_05", "M19XRD_SETUP1_CMTO_Desc", "M19XRD_SETUP1_CONDPO_Val_05", "M19XRD_SETUP1_CONDPO_Desc", "M19XRD_SETUP1_COMPDISALE_Val_05", "M19XRD_SETUP1_COMPDISALE_Desc",
                                    "M19XRD_SETUP1_COMPTHRALE_Val_05", "M19XRD_SETUP1_COMPTHRALE_Desc", "M19XRD_SETUP1_CONDHFAO_Val_05", "M19XRD_SETUP1_CONDHFAO_Desc", "M19XRD_SETUP1_CONDHFDL_Val_05", "M19XRD_SETUP1_CONDHFDL_Desc",
                                    "M19XRD_SETUP1_TBRF_Val_05", "M19XRD_SETUP1_TBRF_Desc", "M19XRD_SETUP1_CHILLMED_Loe", "M19XRD_SETUP1_CHILLMED_Desc", "M19XRD_SETUP1_CHILLIQDEAD_Val_05", "M19XRD_SETUP1_CHILLIQDEAD_Desc",
                                    "M19XRD_SETUP1_EVAPREFTRIP_Val_05", "M19XRD_SETUP1_EVAPREFTRIP_Desc", "M19XRD_SETUP1_REFOVERDELTA_Val_05", "M19XRD_SETUP1_REFOVERDELTA_Desc", "M19XRD_SETUP1_EVAPAPPALE_Val_05", "M19XRD_SETUP1_EVAPAPPALE_Desc",
                                    "M19XRD_SETUP1_CONDAPPALE_Val_05", "M19XRD_SETUP1_CONDAPPALE_Desc", "M19XRD_SETUP1_CONDFREEP_Val_05", "M19XRD_SETUP1_CONDFREEP_Desc", "M19XRD_SETUP1_FLOWDELP_Loe", "M19XRD_SETUP1_FLOWDELP_Desc",
                                    "M19XRD_SETUP1_EVAPFLOWP_Val_05", "M19XRD_SETUP1_EVAPFLOWP_Desc", "M19XRD_SETUP1_CONDFLOWP_Val_05", "M19XRD_SETUP1_CONDFLOWP_Desc", "M19XRD_SETUP1_OILPVT_Val_05", "M19XRD_SETUP1_OILPVT_Desc",
                                    "M19XRD_SETUP1_LIQFVT_Val_05", "M19XRD_SETUP1_LIQFVT_Desc", "M19XRD_SETUP1_RESDEL_Val_05", "M19XRD_SETUP1_RESDEL_Desc", "M19XRD_SETUP1_SHUTDEL_Val_05", "M19XRD_SETUP1_SHUTDEL_Desc", "M19XRD_SETUP1_SPTEMP1E_Val_05",
                                    "M19XRD_SETUP1_SPTEMP1E_Desc", "M19XRD_SETUP1_SPTEMP1L_Val_05", "M19XRD_SETUP1_SPTEMP1L_Desc", "M19XRD_SETUP1_SPTEMP2E_Val_05", "M19XRD_SETUP1_SPTEMP2E_Desc", "M19XRD_SETUP1_SPTEMP2L_Val_05",
                                    "M19XRD_SETUP1_SPTEMP2L_Desc", "M19XRD_SETUP1_CANCEL_Btn", "M19XRD_SETUP1_SAVE_Btn"]

        self.M19XRD_setup2_write = ["M19XRD_SETUP2_PROINCB_Val_05", "M19XRD_SETUP2_PROINCB_Desc", "M19XRD_SETUP2_PRODECB_Val_05", "M19XRD_SETUP2_PRODECB_Desc", "M19XRD_SETUP2_PROECWG_Val_05", "M19XRD_SETUP2_PROECWG_Desc",
                                    "M19XRD_SETUP2_GVTL_Val_05", "M19XRD_SETUP2_GVTL_Desc", "M19XRD_SETUP2_VFDOPT_Loe", "M19XRD_SETUP2_VFDOPT_Desc", "M19XRD_SETUP2_VFDGAIN_Val_05", "M19XRD_SETUP2_VFDGAIN_Desc",
                                    "M19XRD_SETUP2_VFDINCST_Val_05", "M19XRD_SETUP2_VFDINCST_Desc", "M19XRD_SETUP2_VFDMINSPD_Val_05", "M19XRD_SETUP2_VFDMINSPD_Desc", "M19XRD_SETUP2_VFDMAXSPDT_Val_05", "M19XRD_SETUP2_VFDMAXSPD_Desc",
                                    "M19XRD_SETUP2_VFDSTATSPD_Val_05", "M19XRD_SETUP2_VFDSTATSPD_Desc", "M19XRD_SETUP2_VFDSURGLG_Val_05", "M19XRD_SETUP2_VFDSURGLG_Desc", "M19XRD_SETUP2_VFDCRNTLIM_Val_05", "M19XRD_SETUP2_VFDCRNTLIM_Desc"]

        self.M19XRD_vdosrd_write = ["M19XRD_VDOSRD_DIFFOPT_Val_05", "M19XRD_VDOSRD_DIFFOPT_Desc", "M19XRD_VDOSRD_DIFFFULLSP_Val_05", "M19XRD_VDOSRD_DIFFFULLSP_Desc", "M19XRD_VDOSRD_GUD25L_Val_05", "M19XRD_VDOSRD_GUD25L_Desc", "M19XRD_VDOSRD_GUD50L_Val_05",
                                    "M19XRD_VDOSRD_GUD50L_Desc", "M19XRD_VDOSRD_GUD75L_Val_05", "M19XRD_VDOSRD_GUD75L_Desc", "M19XRD_VDOSRD_SRD25L_Val_05", "M19XRD_VDOSRD_SRD25L_Desc", "M19XRD_VDOSRD_SRD50L_Val_05", "M19XRD_VDOSRD_SRD50L_Desc",
                                    "M19XRD_VDOSRD_SRD75L_Val_05", "M19XRD_VDOSRD_SRD75L_Desc", "M19XRD_VDOSRD_LIFT25L1_Val_05", "M19XRD_VDOSRD_LIFT25L1_Desc", "M19XRD_VDOSRD_LIFT100L_Val_05", "M19XRD_VDOSRD_LIFT100L_Desc", "M19XRD_VDOSRD_LIFT25L2_Val_05",
                                    "M19XRD_VDOSRD_LIFT25L2_Desc", "M19XRD_VDOSRD_SRDOFFSS_Val_05", "M19XRD_VDOSRD_SRDOFFSS_Desc", "M19XRD_VDOSRD_LLPS_Val_05", "M19XRD_VDOSRD_LLPS_Desc"]

        self.M19XRD_leadlag_write = ["M19XRD_LEADLAG_LLCONF_Val_05", "M19XRD_LEADLAG_LLCONF_Desc", "M19XRD_LEADLAG_LBO_Loe", "M19XRD_LEADLAG_LBO_Desc", "M19XRD_LEADLAG_CSO_Loe", "M19XRD_LEADLAG_CSO_Desc", "M19XRD_LEADLAG_LAGCAP_Val_05",
                                    "M19XRD_LEADLAG_LAGCAP_Desc", "M19XRD_LEADLAG_LAGADD_Val_05", "M19XRD_LEADLAG_LAGADD_Desc", "M19XRD_LEADLAG_LAGSTATTIM_Val_05", "M19XRD_LEADLAG_LAGSTATTIM_Desc", "M19XRD_LEADLAG_LAGSTOPTIM_Val_05",
                                    "M19XRD_LEADLAG_LAGSTOPTIM_Desc", "M19XRD_LEADLAG_PREFT_Val_05", "M19XRD_LEADLAG_PREFT_Desc", "M19XRD_LEADLAG_PULLDT_Val_05", "M19XRD_LEADLAG_PULLDT_Desc", "M19XRD_LEADLAG_STANDCO_Loe",
                                    "M19XRD_LEADLAG_STANDCO_Desc", "M19XRD_LEADLAG_STANDCAP_Val_05", "M19XRD_LEADLAG_STANDCAP_Desc", "M19XRD_LEADLAG_STANDADD_Val_05", "M19XRD_LEADLAG_STANDADD_Desc"]

        self.M19XRD_rampdem_write = ["M19XRD_RAMPDEM_PRTS_Val_05", "M19XRD_RAMPDEM_PRTS_Desc", "M19XRD_RAMPDEM_DLSS_Val_05", "M19XRD_RAMPDEM_DLSS_Desc", "M19XRD_RAMPDEM_MLRM_Val_05", "M19XRD_RAMPDEM_MLRM_Desc", "M19XRD_RAMPDEM_DLPB_Val_05",
                                    "M19XRD_RAMPDEM_DLPB_Desc", "M19XRD_RAMPDEM_DL20_Val_05", "M19XRD_RAMPDEM_DL20_Desc", "M19XRD_RAMPDEM_20DLO_Loe", "M19XRD_RAMPDEM_20DLO_Desc", "M19XRD_RAMPDEM_MRK_Val_05", "M19XRD_RAMPDEM_MRK_Desc",
                                    "M19XRD_RAMPDEM_DWL_Val_05", "M19XRD_RAMPDEM_DWL_Desc"]

        self.M19XRD_tempctl_write = ["M19XRD_TEMPCTL_ECWCO_Loe", "M19XRD_TEMPCTL_ECWCO_Desc", "M19XRD_TEMPCTL_TEMPPULL_Val_05", "M19XRD_TEMPCTL_TEMPPULL_Desc", "M19XRD_TEMPCTL_RESETTYP_Val_05", "M19XRD_TEMPCTL_RESETTYP_Desc", "M19XRD_TEMPCTL_DEGRESET20_Val_05",
                                    "M19XRD_TEMPCTL_DEGRESET20_Desc", "M19XRD_TEMPCTL_REMTEMPNR_Val_05", "M19XRD_TEMPCTL_REMTEMPNR_Desc", "M19XRD_TEMPCTL_REMTEMPFR_Val_05", "M19XRD_TEMPCTL_REMTEMPFR_Desc", "M19XRD_TEMPCTL_DEGRESET_Val_05",
                                    "M19XRD_TEMPCTL_DEGRESET_Desc", "M19XRD_TEMPCTL_CHWDELTANR_Val_05", "M19XRD_TEMPCTL_CHWDELTANR_Desc", "M19XRD_TEMPCTL_CHWDELTAFR_Val_05", "M19XRD_TEMPCTL_CHWDELTAFR_Desc", "M19XRD_TEMPCTL_DEGRES_Val_05",
                                    "M19XRD_TEMPCTL_DEGRES_Desc", "M19XRD_TEMPCTL_SERESETTYPE_Val_05", "M19XRD_TEMPCTL_SERESETTYPE_Desc"]

        self.M19XRD_brodef_write = ["M19XRD_BRODEF_TIMEBE_Loe", "M19XRD_BRODEF_TIMEBE_Desc", "M19XRD_BRODEF_STATMONT_Val_05", "M19XRD_BRODEF_STATMONT_Desc", "M19XRD_BRODEF_STATDAYWEEK_Val_05", "M19XRD_BRODEF_STATDAYWEEK_Desc", "M19XRD_BRODEF_STATWEEK_Val_05",
                                    "M19XRD_BRODEF_STATWEEK_Desc", "M19XRD_BRODEF_STATTIME_Val_05", "M19XRD_BRODEF_STATTIME_Desc", "M19XRD_BRODEF_STATADV_Val_05", "M19XRD_BRODEF_STATADV_Desc", "M19XRD_BRODEF_STOPMONT_Val_05", "M19XRD_BRODEF_STOPMONT_Desc",
                                    "M19XRD_BRODEF_STOPDAYWEEK_Val_05", "M19XRD_BRODEF_STOPDAYWEEK_Desc", "M19XRD_BRODEF_STOPWEEK_Val_05", "M19XRD_BRODEF_STOPWEEK_Desc", "M19XRD_BRODEF_STOPTIME_Val_05", "M19XRD_BRODEF_STOPTIME_Desc",
                                    "M19XRD_BRODEF_STOPBACK_Val_05", "M19XRD_BRODEF_STOPBACK_Desc"]

    def write_data(self, Data):
        self.prefix = {'set': 'M19XRD_set', 'ismct': 'M19XRD_ismct', 'opti':'M19XRD_opti',
                       'opti2': 'M19XRD_opti2', 'setup1': 'M19XRD_setup1', 'setup2': 'M19XRD_setup2', 'vdosrd': 'M19XRD_vdosrd',
                       'leadlag': 'M19XRD_leadlag', 'rampdem': 'M19XRD_rampdem', 'tempctl': 'M19XRD_tempctl', 'brodef': 'M19XRD_brodef'}

        for i in range(len(eval("self." + self.prefix[Data['Model']] + "_write"))):
            if "Val_" in eval("self." + self.prefix[Data['Model']] + "_write[i]") or "val_" in eval(
                    "self." + self.prefix[Data['Model']] + "_write[i]"):
                xpath = eval("ConfigLogPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[i]"))
                try:
                    self.checklist.write(xpath, Data)
                except:
                    print("Error: ", eval("self." + self.prefix[Data['Model']] + "_write[i]"))
                print('Written Prestart data of ' + eval("self." + self.prefix[Data['Model']] + "_write[i]") + ' =', \
                    Data['testdata'])

    def read_data(self, Data):
        for ele in eval("self." + self.prefix[Data['Model']] + "_write"):
            if ele != self.prefix[Data['Model']] + "_Default":
                common_xpath = eval(
                    "ConfigLogPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read_normal',
                                            page_locators="ConfigLogPageLocators")
                if 'Val_' in ele[-6:]:
                    try:
                        assertion.assertEqual(float(value) == float(
                            ''.join(filter(str.isdigit, str(Data['testdata'])))[:eval(ele[-2:])]), True)
                        print('Read Chiller Name Plate Data Information(' + ele + ')' + ' =', value)
                    except Exception as e:
                        print("********************************************************************************************************************************\n" \
                              "88888888888888888888888888888888888888888888888888888888888   ERROR   8888888888888888888888888888888888888888888888888888888888\n" \
                              "********************************************************************************************************************************")
                        print(e.message)
                        print('Read Chiller Name Plate Data Information(' + ele + ')' + ' =', value)
                elif 'val_' in ele[-6:]:
                    try:
                        assertion.assertEqual(value == str(Data['testdata'][:eval(ele[-2:])]), True)
                        print('Read Chiller Name Plate Data Information(' + ele + ')' + ' =', value)
                    except Exception as e:
                        print("********************************************************************************************************************************\n" \
                              "88888888888888888888888888888888888888888888888888888888888   ERROR   8888888888888888888888888888888888888888888888888888888888\n" \
                              "********************************************************************************************************************************")
                        print(e.message)
                        print('Read Chiller Name Plate Data Information(' + ele + ')' + ' =', value)
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

    def read_reset_data(self, Data):
        for ele in eval("self." + self.prefix[Data['Model']] + "_write"):
            if ele != self.prefix[Data['Model']] + "_Default":
                common_xpath = eval(
                    "ConfigLogPageLocators." + eval("self." + self.prefix[Data['Model']] + "_write[0]"))
                common_xpath = self.find_elements(*common_xpath)
                value = self.checklist.read(ele, common_xpath, Data, 'read_normal',
                                            page_locators="ConfigLogPageLocators", index_assert=5)
                if 'drop' in ele[-4:]:
                    pass
                elif 'CheckBox' in ele[-8:]:
                    pass
                elif 'Val_' in ele[-6:] or 'val_' in ele[-6:]:
                    try:
                        assertion.assertEqual(value == '', True)
                    except Exception as e:
                        print("********************************************************************************************************************************\n" \
                              "88888888888888888888888888888888888888888888888888888888888   ERROR   8888888888888888888888888888888888888888888888888888888888\n" \
                              "********************************************************************************************************************************")
                        print(e.message)

                print('Read Chiller Name Plate Data Information of ' + ele + ' = ', 'Null' if value == '' else value)

    def configlog_exit(self):
        self.find_element(*ConfigLogPageLocators.configlog_exit).click()

    def configlog_save_submenu(self):
        self.find_element(*ConfigLogPageLocators.configlog_savesubmenu).click()

    def configlog_save_mainmenu(self):
        self.find_element(*ConfigLogPageLocators.configlog_savemainmenu).click()

    def configlog_save(self):
        self.find_element(*ConfigLogPageLocators.configlog_save).click()

    def configlog_cancel(self):
        self.find_element(*ConfigLogPageLocators.configlog_cancel).click()

    def startup_form_cancle(self):
        self.find_element(*ChecklistPageLocators.startup_page_cancel).click()

    def startup_form_reset(self):
        self.find_element(*ChecklistPageLocators.startup_page_exit).click()

    def startup_form_exit(self):
        self.find_element(*ChecklistPageLocators.startup_page_exit).click()

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