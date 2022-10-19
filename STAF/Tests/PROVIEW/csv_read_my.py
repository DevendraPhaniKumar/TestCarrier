import os,sys
import pandas as pd
import time

class CCN_read1():
    def __init__(self):
        global file_data_path
        # self.chiller_file=chiller_file
        file_data_path= os.path.dirname(os.path.abspath(__file__)) + "\\TestData\\"

    def read_ccn_val(self,Index_Name,model):
        file1 = file_data_path + model +'_Autofill.csv'
        file2 = file_data_path + model+'_PIC_CCN.csv'
        df1 = pd.read_csv(file1, usecols=['Index Name', 'Table Name', 'CCN_Name'])
        # df2 = pd.read_csv(file2,  usecols=['Description', 'BUS', 'SerialNumber'])
        df2 = pd.read_csv(file2, skiprows=3, usecols=['Table Name', 'Point Name', 'Point Description'])
        for i in df1.itertuples():
            if i[1] == Index_Name:
                col1 = i[2]
                # print(col1)
                col2 = i[3]
                # print(col2)
                querystring = 'Table Name == "{col1}" and Point Name == "{col2}"'
                querystring = querystring.format(col1=col1, col2=col2)
                # print(querystring)
                # df2 = pd.read_csv(file2, usecols=['Description', 'BUS', 'SerialNumber'])
                df2 = pd.read_csv(file2, skiprows=3, usecols=['Table Name', 'Point Name', 'Point Description'])
                df2.columns = [column.replace(" ", "_") for column in df2.columns]
                df2.query(querystring, inplace = True)
                x= df2["SerialNumber"]
                time.sleep(2)
                try:
                    val = x.array[0]
                    # print(f"Row Table: {col1} Point:{col2} Value:{x.array[0]} for {Index_Name}")
                    return val
                except Exception as e:
                    print(f"FAILED --value not found error for CCN point '{col2}'\n",e)

        return

# if __name__ == "__main__":
#     ccn=CCN_read()
#     M30XV_RCI_write_auto = ["M30XV_RCI_SP_Val", "M30XV_RCI_CPS_Val", "M30XV_RCI_RLS_Val", "M30XV_RCI_UOT_Val",
#                                  "M30XV_RCI_DLT_Val", "M30XV_RCI_NMS_Val", "M30XV_RCI_NME_Val", "M30XV_RCI_NCL_Val",
#                                  "M30XV_RCI_IME_Val", "M30XV_RCI_CPS1_Val", "M30XV_RCI_PAR_Val", "M30XV_RCI_PSP_Val",
#                                  "M30XV_RCI_SPD_Val", "M30XV_RCI_FCI_Val", "M30XV_RCI_CPO_Val",
#                                  "M30XV_RCI_USERPASS_Val", "M30XV_RCI_ONRV_Val", "M30XV_RCI_OFRV_Val",
#                                  "M30XV_RCI_DNRV_Val", "M30XV_RCI_DFRV_Val", "M30XV_RCI_CNRV_Val", "M30XV_RCI_CFRV_Val",
#                                  "M30XV_RCI_SNRV_Val", "M30XV_RCI_SFRV_Val", "M30XV_RCI_CRDV_Val",
#                                  "M30XV_RCI_UNITTYPE_Val", "M30XV_RCI_UNITCAP_Val", "M30XV_RCI_PFS_Val",
#                                  "M30XV_RCI_PSV_Val", "M30XV_RCI_EMM_Val", "M30XV_RCI_MSL_Val", "M30XV_RCI_CPN_Val",
#                                  "M30XV_RCI_MES_Val", "M30XV_RCI_DCS_Val", "M30XV_RCI_EXVA_Val", "M30XV_RCI_EXVB_Val",
#                                  "M30XV_RCI_EASN_Val", "M30XV_RCI_EBSN_Val", "M30XV_RCI_NFDA_Val", "M30XV_RCI_NFDB_Val",
#                                  "M30XV_RCI_CFT_Val", "M30XV_RCI_FSS_Val", "M30XV_RCI_CONDFT_Val", "M30XV_RCI_EFC_Val",
#                                  "M30XV_RCI_BFS_Val", "M30XV_RCI_BMFT_Val", "M30XV_RCI_PPGV_Val", "M30XV_RCI_IPGV_Val",
#                                  "M30XV_RCI_DPGV_Val", "M30XV_RCI_EWT_Val", "M30XV_RCI_LCTIMER_Val",
#                                  "M30XV_RCI_RFI_Val", "M30XV_RCI_METRIC_Val", "M30XV_RCI_SFDC_Val",
#                                  "M30XV_RCI_SCDC_Val", "M30XV_RCI_CHDS_Val", "M30XV_RCI_FANOFFA_Val",
#                                  "M30XV_RCI_FANOFFB_Val", "M30XV_RCI_FOO_Val", "M30XV_RCI_QMC_Val", "M30XV_RCI_MSS_Val",
#                                  "M30XV_RCI_SLVADD_Val", "M30XV_RCI_LLS_Val", "M30XV_RCI_LLBD_Val",
#                                  "M30XV_RCI_LLST_Val", "M30XV_RCI_LPT_Val", "M30XV_RCI_SIEH_Val", "M30XV_RCI_LMRT_Val",
#                                  "M30XV_RCI_LUPC_Val", "M30XV_RCI_CIS_Val", "M30XV_RCI_CSP1_Val", "M30XV_RCI_CSP2_Val",
#                                  "M30XV_RCI_CISP_Val ", "M30XV_RCI_CRL_Val", "M30XV_RCI_SLS1_Val", "M30XV_RCI_SLS2_Val",
#                                  "M30XV_RCI_SLS3_Val"]
#
#     for ele in M30XV_RCI_write_auto:
#         print(ele,": \t",ccn.read_ccn_val(ele))
