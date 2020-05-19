import src.scripts.dial_number as DialNumber
import src.scripts.dial_number_ui as DialNumberUI


def run_suite(stf_info=None):
    # here all the test cases are specified
    # you can run specific scripts if you want to input manual numbers
    # TC-005
    DialNumber.run("77236019", stf_info=stf_info, name="TC-005")
    # TC-006
    DialNumber.run("591 2 2794948", stf_info=stf_info, name="TC-006")
    # TC-007
    DialNumber.run("+591 77236019", stf_info=stf_info, name="TC-007")
    # TC-008
    DialNumber.run("+52 55 9045 8901", stf_info=stf_info, name="TC-008")
    # TC-009
    DialNumber.run("*666", stf_info=stf_info, name="TC-009")
    # TC-010
    DialNumber.run("  449@bc12839", stf_info=stf_info, name="TC-010")
    # TC-011
    DialNumber.run("SDJBFGALSJHKFGB", stf_info=stf_info, name="TC-011")
    # TC-012
    DialNumber.run("1234567890123456", stf_info=stf_info, name="TC-012")
    # TC-013
    DialNumber.run("911", stf_info=stf_info, name="TC-013")
    # TC-014
    DialNumber.run("9$1", stf_info=stf_info, name="TC-014")
    # TC-015
    DialNumber.run("+52845102+0232", stf_info=stf_info, name="TC-015")
    # TC-016
    DialNumber.run("1", stf_info=stf_info, name="TC-016")
    # TC-017
    DialNumber.run("$", stf_info=stf_info, name="TC-017")
    # TC-018
    DialNumber.run("", stf_info=stf_info, name="TC-018")
    # TC-019
    DialNumberUI.run("77236019", stf_info=stf_info, name="TC-019")
    # TC-020
    DialNumberUI.run("591 2 2794948", stf_info=stf_info, name="TC-020")
    # TC-021
    DialNumberUI.run("+591 77236019", stf_info=stf_info, name="TC-021")
    # TC-022
    DialNumberUI.run("+52 55 9045 8901", stf_info=stf_info, name="TC-022")
    # TC-023
    DialNumberUI.run("*666", stf_info=stf_info, name="TC-023")
    # TC-024
    DialNumberUI.run("449@bc12839", stf_info=stf_info, name="TC-024")
    # TC-025
    DialNumberUI.run("SDJBFGALSJHKFGB", stf_info=stf_info, name="TC-025")
    # TC-026
    DialNumberUI.run("1234567890123456", stf_info=stf_info, name="TC-026")
    # TC-027
    DialNumberUI.run("911", stf_info=stf_info, name="TC-027")
    # TC-028
    DialNumberUI.run("9$1", stf_info=stf_info, name="TC-028")
    # TC-029
    DialNumberUI.run("+52845102+0232", stf_info=stf_info, name="TC-029")
    # TC-030
    DialNumberUI.run("1", stf_info=stf_info, name="TC-030")
    # TC-031
    DialNumberUI.run("+", stf_info=stf_info, name="TC-031")
    # TC-032
    DialNumberUI.run("", stf_info=stf_info, name="TC-032")


if __name__ == "__main__":
    run_suite()
