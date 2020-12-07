import sqlite3
import os
import hashlibrary
import logging

class Database(object):
    databaseFile = None
    database = None
    cursor = None
    hash = None
    log = None

    def __init__(self, databaseFile:str,defaultAdminPassword:str,log:logging.Logger):
        self.databaseFile = databaseFile

        self.hash = hashlibrary.hash()

        new = False
        if not os.path.isfile(databaseFile):
            new = True

        self.database = sqlite3.connect(databaseFile)
        self.cursor = self.database.cursor()

        print(new)

        if new:

            saltLength = 16
            recurse = 100
            adminSalt = hashlibrary.hash.genSalt(self.hash,saltLength)

            print(f"INSERT INTO users VALUES(admin, {self.hash.recurse(defaultAdminPassword,recurse,adminSalt)},{adminSalt},{recurse})")

            self.cursor.execute("PRAGMA foreign_keys = ON;")
            self.cursor.execute("CREATE TABLE users(username text NOT NULL PRIMARY KEY, password text NOT NULL, salt text NOT NULL, recursion int NOT NULL)")
            self.cursor.execute("CREATE TABLE userRights(username text NOT NULL, power int NOT NULL, FOREIGN KEY(username) REFERENCES users(username))")
            self.cursor.execute(f"INSERT INTO users VALUES('admin', '{self.hash.recurse(defaultAdminPassword,recurse,adminSalt)}','{adminSalt}','{recurse}')")
            self.cursor.execute(f"INSERT INTO userRights VALUES('admin','5')")
            self.cursor.execute("CREATE TABLE serverKeys(username text, ipAddress text, key text)")
            self.cursor.execute("CREATE TABLE book(id int, name text, author text, genres text, stock int, )")
            self.database.commit()