import subprocess
from subprocess import check_output
import time
import datetime
import os
import sys
import shlex
import json


class IotModule:

    def __init__(self):

        #self.rawdt = "2018-04-02T19:17:00"
        #self.current_dt = (datetime.datetime.now().replace(microsecond=0))
        #self.connectionString = "HostName=rsa-hub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=tpMFSvuxNNSAzkiCCo4SzFtzh8GYmBuhH3G+t+aa/dQ="
        self.connectionString = "HostName=utc-testhub-1.azure-devices.net;SharedAccessKeyName=device;SharedAccessKey=n2yOWtXyRz3iXOn7yhhiiwsaMJl74E7emPjIYmgyfUs="
        #self.iot_Option = "monitor-events"
        #self.device_Name = "riot-rsa-pic6"
        #self.device_Name = "50:33:8B:45:AD:01"
        #self.start_Time = self.current_dt #+ ".000"
        self.in_json = []
        self.out_json = []

    def monitor_events(self, device_name, duration, time_taken):
        current_dt = (datetime.datetime.now().replace(microsecond=0))
        offset = datetime.timedelta(seconds=time_taken)
        modified_start_time = (current_dt - offset).isoformat()
        print("current time = ", current_dt)
        print("modified_start_time = ", modified_start_time)
        #print(modified_start_time)
        launch_iot_hub_explorer = "iothub-explorer" + " " + "monitor-events" + " " + device_name + " " + "-l" +\
                                  " " + self.connectionString + " " + " " + "-r" + " " + "-s" + " " + modified_start_time +\
                                  " " + "-d" + " " + duration
        print(launch_iot_hub_explorer)
        #start time
        #print(self.start_Time)
        #utc time
        #utc_time = datetime.datetime.utcnow()
        #print(utc_time)
        #epoch time
        #epoch_time = int(time.time())
        #print(epoch_time)
        json_data = []
        process = subprocess.Popen(launch_iot_hub_explorer, stdout=subprocess.PIPE, shell=True)
        while True:
            output = process.stdout.readline().decode()
            print(output)
            if output == '' and process.poll() is not None:
                print("NO VALUE FROM IOT HUB - Check max IOT users or DEVICE DID NOT SEND TELMETRY")
                break
            if output.strip() == '--------':
                print("output is removed = ", output)
                output = process.stdout.readline().decode()
                if output.strip() == 'DEPRECATION NOTICE: iothub-explorer will be retired on November 31st, 2018':
                    print("output is removed = ", output)
                    output = process.stdout.readline().decode()
                    if output.strip() =='It has been replaced by the Azure CLI IoT Extension (https://aka.ms/iotcli).':
                        print("output is removed = ", output)
                        output = process.stdout.readline().decode()
                        if output.strip() == '--------':
                            print("output is removed = ", output)
                            output = process.stdout.readline().decode()
                            if output.strip() == 'The equivalent command in the Azure CLI is: az iot hub monitor-events':
                                print("output is removed = ", output)
                                output = process.stdout.readline().decode()
                                if output.strip() == '--------':
                                    print("output is removed = ", output)
                                    output = process.stdout.readline().decode()
            if output:
                data = output.strip()
                print(data)
                json_data.append(json.loads(data))
        process.poll()
        mylist_lenght = len(json_data)
        print(mylist_lenght)
        final_list = []
        i = 0
        while i < int(mylist_lenght):
            z = {**json_data[i], **json_data[i + 1]}
            print(z)
            i = i + 2
            final_list.append(z)
        print("print final json = ", final_list)
        return final_list

    def compare_COV_json_data(self, in_put, out_put):
        self.in_json = in_put
        self.out_json = out_put
        print("input_json = ", self.in_json)
        print("output_json = ", self.out_json)

        #for out in self.out_json:
        #    if out["MT"] == "True":
        #        print("IoT message sent type is ALARM")
        #        del out["MT"]
        #    elif out["MT"] == "False":
        #        print("IoT message sent type is Telemetry")
        #        del out["MT"]
        #    else:
        #        print("Wrong:::**********Message Type")

        for out in self.out_json:
            del out["MT"]
        print("output_json after delete = ", self.out_json)

        tempflag = 0
        for i in self.in_json:
            for j in self.out_json:
                if abs(j["timestamp"] - i["timestamp"]) < 10:
                    print("time difference lesser than 10 seconds")
                    tempflag = 1

        if tempflag == 1:
            for ii in self.in_json:
                del ii["timestamp"]
            for jj in self.out_json:
                del jj["timestamp"]

        flag = 0
        i = 0
        for m in self.in_json:
            for dict_key, dict_value in m.items():
                i = i + 1
                for n in self.out_json:
                    for dict_key2, dict_value2 in n.items():
                        if dict_key == dict_key2 and dict_value == dict_value2:
                            data1 = data2 = {}
                            data1[dict_key] = dict_value
                            data2[dict_key2] = dict_value2
                            flag = flag + 1
                            print(data1)
                        else:
                            pass
        print("total no of matching points = ", flag)
        print("length of input json =", i)
        if flag == i:
            print("**************all data recieved at IoT****************")
        else:
            print("--------------data not recieved at IoT--------------")
            #exit()  # this is written in order to fail the test cases

    def compare_periodic_json_data(self, input, output):
        self.in_json = input
        self.out_json = output
        print("input_json = ", self.in_json)
        print("output_json = ", self.out_json)

        #for out in self.out_json:
        #    if out["MT"] == "True":
        #        print("IoT message sent type is ALARM")
        #        del out["MT"]
        #    elif out["MT"] == "False":
        #        print("IoT message sent type is Telemetry")
        #        del out["MT"]
        #    else:
        #        print("Wrong:::**********Message Type")

        for out in self.out_json:
            del out["MT"]
        print("output_json after delete = ", self.out_json)

        #tempflag = 0
        #for i in self.in_json:
        #    for j in self.out_json:
        #        if abs(j["timestamp"] - i["timestamp"]) < 10:
        #            print("time difference lesser than 10 seconds")
        #            tempflag = 1
        tempflag = 1
        if tempflag == 1:
            for ii in self.in_json:
                if "timestamp" in ii:
                    del ii["timestamp"]
                    break
            for jj in self.out_json:
                if "timestamp" in jj:
                    del jj["timestamp"]
                    break

        flag = 0
        i = 0
        for m in self.in_json:
            for dict_key, dict_value in m.items():
                i = i + 1
                for n in self.out_json:
                    for dict_key2, dict_value2 in n.items():
                        if dict_key == dict_key2 and dict_value == dict_value2:
                            data1 = data2 = {}
                            data1[dict_key] = dict_value
                            data2[dict_key2] = dict_value2
                            flag = flag + 1
                            print(data1)
                        else:
                            pass
        print("total no of matching points = ", flag)
        print("length of input json =", i)
        if flag == i:
            print("**************all data recieved at IoT****************")
        else:
            print("--------------data not recieved at IoT--------------")
            #exit()  # this is written in order to fail the test cases