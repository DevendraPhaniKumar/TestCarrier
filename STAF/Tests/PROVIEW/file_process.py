import glob
import os

import datetime
import time
import shutil

os.getcwd()

class CCN_file():
    #this function gets the latest .csv exported file
    def get_ccn_file(self,chiller_model,dir_path):
        path = dir_path
        new_file = ""
        chiller_model = chiller_model.split(":")[0].strip(" ") + "_CCN"
        date= (datetime.datetime.now().strftime("%d%m")).replace('0',"",2)+(datetime.datetime.now().strftime("%Y"))+(datetime.datetime.now().strftime("_%H")).replace('0',"")
        print(date)
        try:
            list_of_files=glob.glob(path+'/ControllerPoints_'+date+'*.csv')
            latest_file = max(list_of_files, key=os.path.getctime)
            print (latest_file)
            new_file=(path+"\\"+str(chiller_model)+'.csv')
            if os.path.exists(new_file):
                print(f"{new_file} already exist. Deleting the file...")
                os.remove(new_file)
            os.rename(latest_file,new_file)
            time.sleep(2)
            dst = os.getcwd()+r'\TestData'
            shutil.copy(new_file,dst)

        except Exception as error:
            print("file processing error: ",error)
            return -1
        chng_file = glob.glob(new_file)
        print (f"New CCN file {chng_file}")
        return chng_file
        # for name in glob.glob(path+'/ControllerPoints_'+date+'_*.csv'):
    #     print (name)
if __name__ == "__main__":
    dwn_path = r"C:\Users\challau\Downloads"
    # controller_name = '30XV_PIC: 30XAXW PIC6 Ctrl - 0, 6'
    controller_name = '19XRPIC2 : 19XR Centrifugal Chiller - 0, 3'
    file_obj = CCN_file()
    file_obj.get_ccn_file(controller_name, dwn_path)
