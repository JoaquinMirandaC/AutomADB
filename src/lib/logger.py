import datetime
import pytz


class Logger:
    def __init__(self, filename, path, name, verbose=True):
        self.filename = filename
        self.path = path
        self.verbose = verbose
        self.name = name
        self.start = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

        self.begin_log()

    def begin_log(self):
        f = open(self.path + self.filename, "a")
        text = self.name + "\n" + 'test start:  %s ' % self.start
        f.write(text + "\n")
        if self.verbose:
            print str(text)
        f.close()

    def write_log(self, text):
        f = open(self.path + self.filename, "a")
        f.write(str(text) + "\n")
        if self.verbose:
            print str(text)
        f.close()

    def end_log(self, message=""):
        f = open(self.path + self.filename, "a")
        stop = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))
        start = 'test start:  %s' % self.start
        end = 'test end  :  %s' % stop
        if message == "":
            mess_variant = "Test Pass \n"
        else:
            mess_variant = message + "\n" "Test Pass \n"
        text = "-------------RESULTS  ------------------------------------------- \n" + mess_variant + start + "\n" + end + "\n" + "--------------------------------------------------------------- \n \n"
        f.write(text + "\n")
        if self.verbose:
            print str(text)
        f.close()

    def error_log(self, error):
        f = open(self.path + self.filename, "a")
        stop = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))
        start = 'test start:  %s' % self.start
        end = 'test end  :  %s' % stop
        text = "-------------ERROR  ------------------------------------------- \n" + "Test Failed \n" + error + "\n" + start + "\n" + end + "\n" + "--------------------------------------------------------------- \n \n"
        f.write(text + "\n")
        if self.verbose:
            print str(text)
        f.close()