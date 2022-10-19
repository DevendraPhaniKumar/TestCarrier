import os
import psutil
import time

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                print(f'Process {processName} is running ')
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            print(f'{processName} has an exception: \n',psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess)

    return False

# Check if ProView services  was running or not.
# stop_process stops the specific process
def stop_process(process_name):
    os.system(f'taskkill /F /im {process_name}')
    time.sleep(2)

# Start process or an application from specific path
def start_process(app_path,app_exe):
    os.chdir(app_path)
    os.system(f'start {app_exe}')
    time.sleep(10)
    checkIfProcessRunning(app_exe)

#running ProView app
def proviewservices():
    start_process('C:\Program Files (x86)\Carrier\ProView\CST\ClientApp','CSTAppLauncher.exe')

#stopping proview app and its services
def stop_proview():
    stop_process('CSTAppLauncher.exe')
    time.sleep(5)
    stop_process('ProView.Client.Services.exe')
    time.sleep(5)
    stop_process('ProView.Communication.Devices.exe')

if __name__ == "__main__":
    proviewservices()
    time.sleep(20)
    stop_proview()

