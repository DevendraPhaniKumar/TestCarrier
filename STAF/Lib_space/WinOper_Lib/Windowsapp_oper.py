import pygetwindow as gw
import time


class WindowApp:
    def __init__(self):
        pass

    def app_maximize(self, title=None):
        print(f"App {title} is about to maximze")
        file_exp = gw.getWindowsWithTitle(title)[0]
        file_exp.maximize()
        time.sleep(2)
        if file_exp.isMaximized:
            print(f"{title} is maximized ")
            return True
        else:
            print(f'{title} is failed maximize, status: ', file_exp.isMaximized)
            return False

    def app_minimize(self, title=None):
        print(f"App {title} is about to minimize")
        file_exp = gw.getWindowsWithTitle(title)[0]
        file_exp.minimize()
        time.sleep(2)
        if file_exp.isMinimized:
            print(f"{title} is minimized ")
            return True
        else:
            print(f'{title} is failed minimize, status: ', file_exp.isMinimized)
            return False

    def app_close(self, title=None):
        print(f"App {title} is about to close")
        if title in gw.getAllTitles():
            file_exp = gw.getWindowsWithTitle(title)[0]
            try:
                file_exp.close()
                time.sleep(2)
                if not file_exp.isActive:
                    print(f'{title} is  closed')
                    return True
                else:
                    print(f'{title} is not closed status:', file_exp.isActive)
                    return False
            except Exception as closeEr:
                print(f"{title} closing has exception:\n",closeEr)
        else:
            print(" Downloads not active or running")


    def app_activate(self, title=None):
        file_exp = gw.getWindowsWithTitle(title)[0]
        file_exp.activate()
        if file_exp.isActive:
            print(f'{title} is active')
            return True
        else:
            print(f'{title} activation failed, status:', file_exp.isActive)
            return False

if __name__ == "__main__":
    obj = WindowApp()
    obj.app_close('PIC6_data')
    # obj.app_maximize('Carrier ProView - Google Chrome')
    # file_exp_dwnld= gw.getWindowsWithTitle('Downloads')[0]
    # file_exp_dwnld.isMaximized
    # False
    # file_exp_dwnld.isActive
    #
    # file_exp_dwnld.minimize()
    # file_exp_dwnld.isMinimized
    #
    # app_chromedrv= gw.getWindowsWithTitle('Carrier ProView - Google Chrome')[0]
    # app_chromedrv.activate()
#
# app_chromedrv.maximize()
# app_chromedrv.isMaximized
# file_exp_dwnld.close()
