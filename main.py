import src.suites.dialer as DialerSuite
import src.suites.wifi as WifiSuite
import src.suites.calculatorapp as CalculatorSuite
from src.lib.stf import Stf
import json


def run_framework(stf_info=None):
    # # here all the suites specified will be ran, to execute all test cases
    # # Wifi Suite
    WifiSuite.run_suite(stf_info)
    # # Dialer Suite
    # DialerSuite.run_suite()
    # # Calculator Suite
    # CalculatorSuite.run_suite()


if __name__ == "__main__":
    try:
        with open("stf_config.json", 'r') as json_file:
            config = json.load(json_file)
        StfInstance = Stf(config)
        devices = StfInstance.get_all_stf_devices()
        for device in devices:
            remote_serial = StfInstance.stf_connect(device)
            stf_info = {"remote_serial": remote_serial, "device": device}
            run_framework(stf_info)
            StfInstance.stf_disconnect(device, remote_serial)
    except Exception as ex:
        print ex.message

