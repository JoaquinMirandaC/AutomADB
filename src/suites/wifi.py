import src.scripts.turn_wifi as TurnWifi
import os


def run_suite(stf_info=None):
    # here all the test cases are specified
    TurnWifi.run("OFF", stf_info=stf_info, name="TC-001")
    TurnWifi.run("OFF", stf_info=stf_info, name="TC-002")
    TurnWifi.run("ON", stf_info=stf_info, name="TC-003")
    TurnWifi.run("ON", stf_info=stf_info, name="TC-004")


if __name__ == "__main__":
    run_suite()
