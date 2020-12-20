import socket
import configparser
import hashlibrary
import threading
import logging
import clientObject
from jsonTools import jsonPacketBuilder, jsonPacketReader
import database

class main:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    config = configparser.ConfigParser()

    logger = logging.Logger(consoleOutput=True)

    hash = hashlibrary.hash()

    host = socket.gethostbyname(socket.gethostname())

    sCThread = None
    dThread = None

    serverLive = False

    serverClients = []

    databaseManager = None

    def __init__(self):

        self.logger.setFile("log/"+self.logger.genConfigFileName())

        try:
            self.config.read("config.ini")
            self.logger.log("Successfully opened config file")
        except FileNotFoundError:
            self.logger.log("Could not find config file, exiting...",4)
            exit()

        self.logger.log("Opening database")
        self.databaseManager = database.Database("database/database.db","password",self.logger)


        self.logger.log("Binding host & port and opening server")
        self.s.bind((self.host,int(self.config["Server"]["port"])))

        self.logger.log("Assigned timerout to 10")
        self.s.settimeout(10)
        self.serverLive = True

        self.sCThread = threading.Thread(target=self.serverClientThread)
        self.dThread = threading.Thread(target=self.databaseThread)

    def serverClientThread(self):
        while self.serverLive:

            try:
                client, addr = self.s.accept()
            except TimeoutError:
                self.logger.log("No connections within accept time, retrying",1,"Client Connection Thread")
                continue

            self.serverClients.append(clientObject.Client(addr,client))

            # Create new thread to wait for authorisation from each client to prevent one client holding up new connections.
            authorisationThread = threading.Thread(target=self.clientAuthorisationThread,args=(client,addr))
            authorisationThread.start()

    def clientAuthorisationThread(self, client, addr):

        client.send(jsonPacketBuilder.packetBuilder.simpleCode(0, "Please Authorise").encode())
        returnedData = jsonPacketReader.packetReader.decode(client.recv(2048).decode())









    def databaseThread(self):
        pass



if __name__ == '__main__':
    main()
