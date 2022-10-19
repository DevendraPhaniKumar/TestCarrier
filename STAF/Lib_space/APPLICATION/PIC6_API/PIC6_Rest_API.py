import requests
import urllib3
import urllib3.exceptions
import threading
import time
# import pycurl
from tkinter.filedialog import askopenfilename, Tk
from urllib.parse import urlencode

global session, server, token, user_type, read_data, stop_keep_alive
import json


class Rest_API():

    def init(self, _server='https://169.254.1.1'):
        global session, server
        session = requests.Session()
        session.verify = False
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        server = str(_server)

    def login(self, _user='user', _password='0'):
        global session, server, token, user_type
        self.init_check_server()
        _payload = {'username': _user, 'password': _password}
        try:
            _resp = session.post(server + '/PIC6/api/auth/login', json=_payload)
        except:
            return "setup Fail"
        if not _resp:
            return False
        _data = _resp.json()
        token = str(_data[0]['token'])
        user_type = str(_data[0]['usertype'])
        return "setup success"

    def logout(self):
        global token
        global session
        self.init_check()
        _payload = {'token': token}
        try:
            _resp = session.post(server + '/PIC6/api/auth/logout', json=_payload)
            session.close()
        except:
            session.close()
            return False
        if _resp:
            return True
        else:
            return False

    def get_upgrade_status(self):
        global token, read_data, session
        self.init_check()
        _payload = {'token': token}
        try:
            _resp = session.post(server + '/PIC6/api/upgrade/get_upgrade_status', json=_payload)
        except:
            return False
        if not _resp:
            return False
        read_data = _resp.json()
        return read_data

    def get_version_info(self):
        global token, read_data
        self.init_check()
        _payload = {'token': token}
        try:
            _resp = session.post(server + '/PIC6/api/upgrade/get_version_info', json=_payload)
        except:
            return False
        if not _resp:
            return False
        read_data = _resp.json()
        return read_data

    def get_monitor_task(self):
        global token, read_data
        self.init_check()
        _payload = {'token': token}
        try:
            _resp = session.post(server + '/PIC6/api/monitor_tasks/getmonitoringtaskupdates', json=_payload)
        except:
            return False
        if not _resp:
            return False
        read_data = _resp.json()
        return read_data

    def keep_alive(self):
        global stop_keep_alive
        stop_keep_alive = False
        while not stop_keep_alive:
            self.read('PLTSPRT_eth0_mac', 'present-value', False)
            time.sleep(20)

    def initiate_upgrade(self, _upgrade_file='', _keep_config=1):
        global session, server, token, read_data, stop_keep_alive
        self.init_check()
        self.get_upgrade_status()
        if read_data['download_status'] == 'Y' or read_data['upgrade_status'] == 'Y':
            return False
        download_thread = threading.Thread(target=self.keep_alive)
        download_thread.start()
        if _upgrade_file == '':
            Tk().withdraw()
            _upgrade_file = askopenfilename()
        headers = {
            'Expect': '',
        }
        files = {
            'token': (None, token),
            'options': (None, '{"keep_config" : 0 }'),
            'filename': (_upgrade_file, open(_upgrade_file, 'rb'), 'application/octet-stream'),
        }
        try:
            _resp = requests.post(server + '/PIC6/api/test/initiate_upgrade', files=files, verify=False, timeout=20)
        except requests.exceptions.Timeout:
            success = True
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        finally:
            stop_keep_alive = True
            download_thread.join()

    def read(self, _point_name, _field='present-value', _return_data=True):
        global session, server, token, read_data

        self.init_check()
        _payload = {'pathlist': [{'widgetType': 'PointValue', 'path': 'db/' + _point_name + '/' + _field}],
                    'token': token}
        try:
            _resp = session.post(server + '/PIC6/api/point_value/getpointvalue', json=_payload)
        except:
            return "Error: Error in read action"
        if not _resp:
            return "Error: Error in read action"
        read_data = _resp.json()['pathlist']
        # print(read_data)
        # print(type(read_data))
        # print(_resp.json)
        if not read_data[0]["valid"]:
            pntVal = "Error: Database point not valid"
        else:
            pntVal = read_data[0]['value']
        return pntVal

        # if not response["pathlist"][0]["valid"]:
        # print("pic6_REST_api: [ERROR] Database point not valid.")

    def read_list(self, _point_names):
        global session, server, token, read_data
        self.init_check()
        _payload = {'pathlist': [], 'token': token}
        for _point_name in _point_names:
            _payload['pathlist'].append({'widgetType': 'PointValue', 'path': 'db/' + _point_name + '/present-value'})
        _resp = session.post(server + '/PIC6/api/point_value/getpointvalue', json=_payload)
        if not _resp:
            return False
        read_data = _resp.json()['pathlist']
        return read_data

    def write(self, _point_name, _value):
        global session, server, token, read_data
        self.init_check()

        if ';' in _value:
            x = _value.split(";")
            _value = x[0]
            _payload = {'pathlist': [], 'token': token}
            _payload['pathlist'].append({'value': _value, 'path': 'db/' + str(_point_name) + '/present-value'})
            _resp = session.post(server + '/PIC6/api/point_value/savepointvalue', json=_payload)
            response_data = json.loads(_resp.text)
            print(_resp.text)
            try:
                if response_data[0]["status"] == "0":
                    return _value + ";" + "500"
                else:
                    # print("enter else")
                    return _value + ";" + "200"
            except:
                return _value + ";" + "500"
            # return _value + ";" + str(_resp.status_code)
        else:
            _payload = {'pathlist': [], 'token': token}
            if not str.isdigit(_value):
                # print("string case")
                _payload["pathlist"].append({"value": str(_value), "path": "db/" + _point_name + "/active-text"})
            else:
                _payload["pathlist"].append({"value": str(_value), "path": "db/" + _point_name + "/present-value"})
            try:
                _resp = session.post(server + '/PIC6/api/point_value/savepointvalue', json=_payload)
                # print("post sent")
            except:
                return "Error: Error in write action ErrorCode = " + str(_resp.status_code)
            # if not _resp:
            # return "Error: Error in write action ErrorCode = " + str(_resp.status_code)

            response_data = json.loads(_resp.text)
            # print(type(response_data))
            # print(_resp.text)
            # print(response_data[0]["status"])
            try:
                if response_data[0]["status"] == "0":
                    return "Error: Error in write"
                else:
                    # print("enter else")
                    return _value
            except:
                return "Error: Error in write"

    '''
        response_data = json.loads(_resp.text)
        if isinstance(response_data, dict):
            if response_data["status"] == "0":
                print("pic6_REST_api.write: [ERROR] " + response_data["error"])
        elif isinstance(response_data, list):
            if response_data[0]["status"] == "0":
                print("pic6_REST_api.write: [ERROR] " + response_data[0]["error"])
    '''

    def write_list(self, _point_names_and_values):
        global session, server, token, read_data
        self.init_check()
        _payload = {'pathlist': [], 'token': token}
        for _point_name, _value in _point_names_and_values:
            _payload['pathlist'].append({'value': str(_value), 'path': 'db/' + _point_name + '/present-value'})
        try:
            _resp = session.post(server + '/PIC6/api/point_value/savepointvalue', json=_payload)
        except:
            return False
        if not _resp:
            return False
        return True

    def init_check_server(self):
        try:
            server
        except NameError:
            # init('https://169.254.1.1')
            # login('user', '113')
            # print("login in init_check_server")
            raise NameError('run init() function to provide server address')

    def init_check(self):
        self.init_check_server()
        try:
            token
        except NameError:
            # init('https://169.254.1.1')
            # login('user', '113')
            # print("login in init_check")
            raise NameError(
                'No PIC connection initiated, please check connection and make sure login is occurring successfully')
