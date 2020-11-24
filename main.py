import socket
import configparser
import hashlibrary
import threading
import logging

class main:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    config = configparser.ConfigParser()

    logger = logging.Logger(consoleOutput=True)

    hash = hashlibrary.hash()

    host = socket.gethostbyname(socket.gethostname())

    sCThread = None
    dThread = None

    serverLive = False

    def __init__(self):

        self.logger.setFile("log/"+self.logger.genConfigFileName())

        try:
            self.config.read("config.ini")
        except FileNotFoundError:
            print("Could not find configuration file, exiting")
            exit()

        self.s.bind((self.host,int(self.config["Server"]["port"])))
        self.serverLive = True

        self.sCThread = threading.Thread(target=self.serverClientThread)
        self.dThread = threading.Thread(target=self.databaseThread)

    def serverClientThread(self):
        while self.serverLive:
            pass


    def databaseThread(self):
        pass



if __name__ == '__main__':
    main()
