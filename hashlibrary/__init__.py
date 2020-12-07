import math
import random
import string

class hash(object):
    """This is a self coded hashing function, do NOT use this in the real world, it has not been security tested and
    reviewed, it may not be secure, it is a proof of concept.

    The objective of this class is to hash any value put into it, this obfuscates users passwords when in transmission
    and when being stored in the database."""


    #roundDown = lambda number, divisor : number - (number % divisor)
    #Leftover lambda I wanted to save for use later.

    # This creates a list of all hashable characters, each is assigned a value based on its index in the list.
    table = list("." + string.ascii_lowercase + string.ascii_uppercase + string.digits + '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~')

    # This plaintext value is used to store the plaintext version of what is being hashed, it is cleared after use
    plainText = None

    def __init__(self):
        print("Hashlib C Jessica Ampstead 2020, this is for demonstration purposes only do not use in production")

    def genSalt(self,length:int):
        """genSalt is a function that generates a salt value, this is a random string consisting of some of the possible
        hashing values, the salt is added to the plaintext before it is hashed, the salt is stored in the database
        alongside the hashed value, this obfuscates the hash and prevents attackers from being able to work out
        two of the same plaintext values as without the salt they would have identical hashes."""

        salt = ""
        # Repeat for the amount in length.
        for i in range(length):
            # Add a random value from the value table to the salt string
            salt = salt + self.table[random.randint(1,len(self.table)-1)]

        return salt

    def update(self, string:str, salt:str=None):
        """This function sets the plaintext value and salt within the object to ready it for hashing"""

        if salt != None:
            self.plainText = string + salt
        else:
            self.plainText = string


    def recurse(self,string:str,depth:int,salt:str=None):
        """Recursive hashing is where the output of a hash is put back into the hash x amount of times, this creates
        security as it slows down an attacker from being able to break the hash back into its original text as they need
        to calculate through each recursive step of hashing."""

        self.update(string, salt)
        hashtext = self.digest()

        for i in range(0,depth-1):
            self.update(hashtext)
            hashtext = self.digest()

        return hashtext

    def digest(self):
        """This performs the action of the hash and returns a string. it does this by turning each character into an
        integer based on its index in self.table and then proceeds to multiply each number together and then store
        this value in a variable called "numbers", starting with the base value of 2, the final value is exponentiated
        by the "numbers" variable, this creates a very large number, this is then converted into a string and broken
        into a list by every 10th character, the list is named "mathTable". The first index in math table is then
        stored, and the math table is incremented through, every """

        hashText = ""

        lPlainText = list(self.plainText)
        numbers = 2

        for i in range(0,len(self.plainText)):
            for j in range(1,len(self.table)):
                if lPlainText[i] == self.table[j]:
                    if i == len(self.plainText)-1:
                        numbers = numbers ** j
                    else:
                        numbers = numbers * j

        mathTable = []
        numbersString = str(numbers)

        hold = ""
        i = 0
        for char in numbersString:

            if i == 10:
                i = 0
                mathTable.append(hold)
                hold = ""

            hold = hold + char
            i += 1

        if not hold == "":
            mathTable.append(hold)

        #print(mathTable)

        currNumber = list(mathTable[0])
        for i in range(1,len(mathTable)):
            workingValue = list(mathTable[i])

            for j in range(0,len(workingValue)):
                newValue = int(currNumber[j]) + int(workingValue[j])
                currNumber[j] = newValue

        #print(currNumber)

        for number in currNumber:
            hashText = hashText + hex(int(number)) + "/"

        self.plainText = None
        return hashText


