import requests
from subprocess import check_output

class Stf:
    def __init__(self, config, verbose=True):
        self.url = config['stf-url']
        self.verbose = verbose
        self.header = ""
        if config['auth-token'] is None or self.url is None:
            raise KeyError("Invalid stf_config")
        else:
            self.header = {'Authorization': 'Bearer ' + config['auth-token']}

    def get_all_stf_devices(self):
        path = '/api/v1/devices'
        serials = []
        res = requests.get(self.url + path, headers=self.header)
        response = res.json()
        print("There are " + str(len(response['devices'])) + " devices in the STF farm")
        for devices in response['devices']:
            serials.append(devices['serial'])
        return serials

    def stf_connect(self, device_serial):
        connection = self.stf_individual_connection(device_serial)
        if connection:
            print "Remote device activated in STF"
            return self.get_remote_serial(device_serial)
        else:
            raise SystemError("Connection to STF Failed")

    def stf_individual_connection(self, device_serial):
        path = '/api/v1/user/devices'
        data = {'serial': device_serial, 'timeout': 900000}
        res = requests.post(self.url + path, headers=self.header, json=data)
        response = res.json()
        return response['success']

    def get_remote_serial(self, device_serial):
        path = '/api/v1/user/devices/' + device_serial + '/remoteConnect'
        res = requests.post(self.url + path, headers=self.header)
        response = res.json()
        if response['success']:
            adb_ready = self.connect_remote(response['remoteConnectUrl'])
            if adb_ready:
                print "Remote device connected to local adb"
                return response['remoteConnectUrl']
            else:
                raise SystemError("Local adb refused connection to remote device")
        else:
            raise SystemError("Device is currently busy")

    def connect_remote(self, url):
        output = check_output(['adb', 'connect', url])
        return output

    def disconnect_remote(self, url):
        output = check_output(['adb', 'disconnect', url])
        return output

    def stf_disconnect(self, device_serial, device_remote_serial):
        status = self.remove_remote_serial(device_serial, device_remote_serial)
        if status:
            self.stf_individual_disconnection(device_serial)
        else:
            raise SystemError("Could not disconnect remote device")

    def stf_individual_disconnection(self, device_serial):
        path = '/api/v1/user/devices/' + device_serial
        res = requests.delete(self.url + path, headers=self.header)
        response = res.json()
        if response['success']:
            print 'Remote device deactivated in STF'
        else:
            raise SystemError("Failed to deactivate device from STF")

    def remove_remote_serial(self, device_serial, device_remote_serial):
        path = '/api/v1/user/devices/' + device_serial + '/remoteConnect'
        res = requests.delete(self.url + path, headers=self.header)
        response = res.json()
        if response['success']:
            adb_ready = self.disconnect_remote(device_remote_serial)
            if adb_ready:
                print "Remote device disconnected from local adb"
                return True
            else:
                raise SystemError("Failed disconnection from local adb")
        else:
            raise SystemError("Could not disconnect remote")


