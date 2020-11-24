import datetime

class Logger(object):

    logFile = None
    consoleOut = False

    def __init__(self, fileName:str=None, consoleOutput:bool=False):
        if fileName != None:
            self.logFile = open(fileName, "w")

        self.consoleOut = consoleOutput

    def setFile(self, fileName:str):
        self.logFile = open(fileName, "w")

    def genConfigFileName(self):
        date = datetime.datetime.now()
        return date.strftime("%d.%m.%Y.%H.%M.%S") + ".log"

    def closeFile(self):
        self.logFile.close()

    def log(self,message:str,level:int=None, thread:str=None):
        if self.logFile != None:

            output = ""

            if level == None or level == 1:
                output = output + "[INFO]"

            elif level == 2:
                output = output + "[WARN]"

            elif level == 3:
                output = output + "[ERROR]"

            elif level == 4:
                output = output + "[FATAL]"

            elif level == 5:
                output = output + "[DEBUG]"

            output = output + "[" + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "]"

            if thread != None:
                output = output + "[" + thread + "]"

            output = output + " " + message + "\n"

            if self.consoleOut == True:
                print(output)

            self.logFile.write(output)
            return True
        else:
            print("Logfile not open or prepared to take log")
            return False


