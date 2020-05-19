#!/usr/bin/python
# coding=utf-8

"""

"""
import time
from src.lib.phone_control import PhoneControl
from src.lib.logger import Logger
import src.lib.utils as utils
import os


def run(number=None, stf_info=None, name="", filename="log_dialer.txt"):
    stf = False
    device_params = {}
    # path to save logs
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, "..", "..", "qa", "reports", "")
    logger = Logger(filename, path, name)

    controller = PhoneControl()

    if stf_info is not None:
        serials = [stf_info['remote_serial']]
        device_params = utils.get_device_data(stf_info['device'])
        stf = True
    else:
        serials = controller.read_serials()
    for i in range(len(serials)):
        logger.write_log(" Device {} = {}".format(i + 1, serials))

        controller.init_device(serials[i])

        if not stf:
            device_params = utils.get_device_data(serials[i])

        logger.write_log("Script Dial Number---------")
        if number is None:
            n = raw_input("Enter the number to dial : ")
        else:
            n = number
        try:
            dialable, parsedNumber, msg = utils.validate_number(n)
            if dialable:
                logger.write_log(msg + " " + str(parsedNumber))
                action(logger, controller, parsedNumber, device_params)
            else:
                logger.end_log("Invalid phone number")
        except Exception as ex:
            logger.error_log(ex.message)


def action(logger, controller, number, params):
    controller.unlock_phone()
    controller.click_home()
    controller.click_button(params["phone"]["text"], params["phone"]["className"])
    if controller.detailed_button_exists(params['key-pad']['className'], params['key-pad']['packageName'], params['key-pad']['description']):
        controller.click_detailed_button(params['key-pad']['className'], params['key-pad']['packageName'], params['key-pad']['description'])
    controller.longclick_detailed_button(params['backspace']['className'], params['backspace']['packageName'], params['backspace']['description'])
    controller.call_adb(number)
    time.sleep(3)
    if controller.check_call_adb():
        controller.end_call_adb()
        logger.end_log("SUCCESSFUL CALL")
    else:
        logger.error_log("CALL FAILED")
    controller.click_home()


if __name__ == "__main__":
    run(number="001 956 778 5720")
