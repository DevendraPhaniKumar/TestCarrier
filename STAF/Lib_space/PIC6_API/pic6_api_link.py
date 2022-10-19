
import time,os,sys
dirnameutils = (os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
#sys.path.append(dirnameutils + "\Selenium_POM")
#dirnameutils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dirnameutils)
from Lib_space.PIC6_API import rest_frame as PIC6
from Lib_space.Connectivity.Sierra_Router.Sierra_Router import *


class PIC_6():

    def __init__(self):
        """
        fx30 is used as router to get eth0 ip address
        """
        fx30_instance = Fx30()
        Fx30.login(self=fx30_instance)
        self.IPAddress, self.Subnet_Mask, self.Gateway_IP, self.Gateway_Mask, self.dns1, self.dns2 = Fx30.network_settings(self=fx30_instance)
        Fx30.close_browser(self=fx30_instance)

    def Eath0_IP(self):
        PIC6.ss_rest_write("PLTSP_set_eth0_ip","169.254.1.1")  # writing Eth0 IP Address
        PIC6.ss_rest_write("PLTSP_set_eth0_nmask","255.255.0.0")# Writing Eth0 Subnet Mask Address
        PIC6.ss_rest_write("PLT_set_eth0_aply_dn","1") # Click on Save Button
        Status = PIC6.ss_rest_read("PLTSP_set_eth0_stat") # Read the IP Status of IP and Subnet Mask Saving
        if Status == "0":

            print("ETH0 IP & Subnet Mask Address Updated Successfully(IP Address: 169.254.1.1  SubnetMask:255.255.0.0)")
        else:
            print("ETH0 IP & Subnet Mask Address Updating is Failed")
        # Gateway
        PIC6.ss_rest_write("PLTSP_set_gw1_aply_dn", "2")  # Click on Delete
        time.sleep(3)
        PIC6.ss_rest_write("PLTSP_set_gw1", "192.168.168.9") # Writing Gateway 1 IP 169.254.1.3
        PIC6.ss_rest_write("PLTSP_set_gw1_mask","0.0.0.0/0") #Writing GW 1 Dest/Mask Address
        PIC6.ss_rest_write("PLTSP_set_gw1_aply_dn","1") # Click on Apply
        Status = PIC6.ss_rest_read("PLTSP_set_gw1_stat")# Read the Status of Gateway
        if Status == "0":  # O for Applyed Successsfull 9 For Already Gateway Exists
            print("Eath0 Gateway Address Updated Successfully(Gateway: 192.168.168.9  Dest/Mask:0.0.0.0/0)")
        elif Status == "5":
            print("Invalid Gateway Mask")
            print("Eath0 Gateway Address Updating is Failed")
        elif Status == "9":
            print("Gateway Exists")
            print("Eath0 Gateway Address Updated Successfully")
        elif Status == "7":
            print("Invalid Argument To Route Command")
            print("Eath0 Gateway Address Updating is Failed")
        else:
            pass


    def Eath1_IP(self):
        # obj = SierraConfiguration()
        # data = obj.test_sierra_smart_configuration()
        # IPAddress = data[0]
        # Subnet_Mask = data[1]
        # Gateway_IP = data[2]
        # Gateway_Mask = data[3]
        # DNS1 = data[4]
        # DNS2 = data[5]

        PIC6.ss_rest_write("PLTSP_set_eth1_ip", self.IPAddress) # Writing Eth 1 IP Address 192.168.168.10
        PIC6.ss_rest_write("PLTSP_set_eth1_nmask", self.Subnet_Mask )# Writing Eth 1 Subnetmask Address 255.255.0.0
        PIC6.ss_rest_write("PLT_set_eth1_aply_dn", "1") # Click on Save Button
        Status = PIC6.ss_rest_read("PLTSP_set_eth1_stat")# Read the Status of IP Status
        if Status == "0":
            print("ETH1 IP & Subnet Mask Address Updated Successfully(IP Address:" + self.IPAddress +"  Subnet Mask:" + self.Subnet_Mask)
        else:
            print("ETH1 IP & Subnet Mask Address Updating is Failed")
        #

        PIC6.ss_rest_write("PLTSP_set_gw2_aply_dn", "2")  # Click on Delete
        time.sleep(3)
        PIC6.ss_rest_write("PLTSP_set_gw2",self.Gateway_IP)# Writing Gateway 2 IP 192.168.168.9
        PIC6.ss_rest_write("PLTSP_set_gw2_mask",self.Gateway_Mask)# Writing GW2 Dest/Mask Address 0.0.0.0/0
        PIC6.ss_rest_write("PLTSP_set_gw2_aply_dn","1")# Click on Apply
        Status = PIC6.ss_rest_read("PLTSP_set_gw2_stat")# Read The Status of Gateway
        PIC6.ss_rest_write("PLT_set_eth1_aply_dn", "1")  # Click on Save Button
        # print(Status)
        if Status == "0":#  O for Applyed Successsfull 9 For Already Gateway Exists
            print("Eath1 Gateway Address Updated Successfully(Gateway:"+ self.Gateway_IP + "Dest/Mask:" + self.Gateway_Mask)
        elif Status == "5":
            print("Invalid Gateway Mask")
            print("Eath1 Gateway Address Updating is Failed")
        elif Status == "9":
            print("Gateway Exists")
            print("Eath0 Gateway Address Updated Successfully")
        elif Status == "7":
            print("Invalid Argument To Route Command")
            print("Eath1 Gateway Address Updating is Failed")
        else:
            pass

    def DNS_Server(self):
        # DSN Server
        self.DNS1='192.168.168.9'
        self.DNS2='192.168.168.9'
        PIC6.ss_rest_write("PLTSP_set_dnsip1",self.DNS1) # 192.168.168.9
        PIC6.ss_rest_write("PLTSP_set_dnsip2",self.DNS2) # 192.168.168.9
        PIC6.ss_rest_write("PLTSP_dns_aply_dn","1")
        Status = PIC6.ss_rest_read("PLTSP_dns_stat")
        if Status == "0":
            print("DNS Server Address Updated Successfully(DNS1 :"+ self.DNS1  + " DNS2:" + self.DNS2)
        else:
            print("DNS Server Address Updating is Failed")

    def Network_Config(self):

        # Ping Test
        print("Performing Ping Test ********: ")
        PIC6.ss_rest_write("PLTSP_nw_png_tst_ip", "google.com")  # Write Server Address
        PIC6.ss_rest_write("PLTSP_nw_png_tst_if", "2")  # Select the Inter face  2 For Eath:1
        PIC6.ss_rest_write("PLTSP_nw_png_tst", "1")  # Click on Ping Test
        time.sleep(5)
        Status = PIC6.ss_rest_read("PLTSP_nw_png_tst_sts")  # Read the Status of Ping Test
        print(Status)
        if Status == "1":
            print("Ping Test is Passed")
        else:
            print("Ping Test Is Failed")

        # Cloud Test
        print("Performing Cloud Test ********:")
        PIC6.ss_rest_write("PLTSP_nw_cloud_tst_tout","5") # Writing Time out Time
        PIC6.ss_rest_write("PLTSP_nw_cloud_tst","1") # Click on Cloud Test
        time.sleep(15)
        Status = PIC6.ss_rest_read("PLTSP_nw_cloud_tst_sts")# Read the Status of Cloud Test
        print(Status)
        if Status == "1":
            print("Cloud Test is Passed")
        else:
            print("Cloud Test is Failed")

        # IOT Certificate Checking
        Status = PIC6.ss_rest_read("PLTSP_nw_iot_cert_exist")
        # print(Status)
        if Status != "0":
            print("IOT Certificate is Present")
        else:
            print("IOT Certificate is Not Present")

    def CCN_Config(self):
        PIC6.ss_rest_write("CTRLID_CCN_ADDRESS", "1")
        print("CCN Address is set as :"+PIC6.ss_rest_read("CTRLID_CCN_ADDRESS"))
        PIC6.ss_rest_write("CTRLID_CCN_BUS", "0")
        print("CCN BUS is set as :"+PIC6.ss_rest_read("CTRLID_CCN_BUS"))
        PIC6.ss_rest_write("CTRLID_CCN_BAUD_PRI", "38400")
        print("CCN Baudrate is set as :"+PIC6.ss_rest_read("CTRLID_CCN_BAUD_PRI"))
        print(" CCN Configuration Completed")


def Timer(A):
    t =int(A)
    while t:
        mins =t //60
        sec = t %60
        timer = '{:02d}:{:02d}'.format(mins,sec)
        print(f'\r{timer}', end='')
        time.sleep(1)
        t -=1
    print("Done!!!!!!")


# A = PIC_6()
# A.Network_Config()
#
# A = PIC_6()
# A.Timer(240)




