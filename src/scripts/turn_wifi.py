#!/usr/bin/python
# coding=utf-8

"""

"""

import time
from src.lib.phone_control import PhoneControl
from src.lib.logger import Logger
import src.lib.utils as utils
import os


def run(turn, stf_info=None, name="", filename="log_wifi.txt"):
    stf = False
    device_params = {}
    # path to save logs
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, "..", "..", "qa", "reports", "")
    # instantiate logger to save a report file
    logger = Logger(filename, path, name)
    # initiate connection to device(s)
    controller = PhoneControl()
    # if a serial was received, run test only for that single serial
    if stf_info is not None:
        serials = [stf_info['remote_serial']]
        device_params = utils.get_device_data(stf_info['device'])
        stf = True
    else:
        # read the serials
        serials = controller.read_serials()

    for i in range(len(serials)):
        logger.write_log(" Device {} = {}".format(i+1, serials))
        # init device with serial
        controller.init_device(serials[i])
        # get the device parameters from the device version json
        if not stf:
            device_params = utils.get_device_data(serials[i])
        logger.write_log("Script Turn Wifi " + turn + " ---------")
        try:
            action(turn, logger, controller, device_params)
            time.sleep(3)
        except Exception as ex:
            logger.error_log(ex.message)


def action(turn, logger, controller, params):
    controller.unlock_phone()
    controller.click_home()
    controller.click_button(params['settings']['text'], params['settings']['className'])
    controller.click_button(params['network']['text'], params['network']['className'])
    controller.click_button(params['wi-fi']['text'], params['wi-fi']['className'])
    if turn == "ON":
        if not controller.button_checked(params['ON']['packageName'], params['ON']['className'], params['ON']['resourceId']):
            logger.write_log("Status: Wifi Off")
            controller.click_detailed_button(params['ON']['className'], params['ON']['packageName'], "")
            if controller.button_checked(params['ON']['packageName'], params['ON']['className'], params['ON']['resourceId']):
                logger.write_log("WIFI TURNED ON")
        else:
            logger.write_log("WIFI ALREADY ON")
        controller.click_back()
        time.sleep(10)
        value = controller.info_detailed_select(params["connection"]["className"],
                                                params["connection"]["packageName"],
                                                params["connection"]["resourceId"])
        if value:
            logger.write_log("SUCCESSFUL CONNECTION TO: " + value)
            logger.end_log()

        else:
            logger.error__log("NOT CONNECTED TO A NETWORK")
        controller.click_home()
    elif turn == "OFF":
        if controller.button_checked(params['ON']['packageName'], params['ON']['className'], params['ON']['resourceId']):
            logger.write_log("Status: Wifi On")
            controller.click_detailed_button(params['ON']['className'], params['ON']['packageName'], "")
            if not controller.button_checked(params['OFF']['packageName'], params['ON']['className'], params['ON']['resourceId']):
                logger.write_log("WIFI TURNED OFF")
        else:
            logger.write_log("WIFI ALREADY OFF")
        logger.end_log()

    else:
        raise ValueError(
            'Invalid Input. Should only be ON or OFF')
    controller.click_home()


if __name__ == "__main__":
    run(turn="ON")

