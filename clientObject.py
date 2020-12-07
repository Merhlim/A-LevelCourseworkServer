
class Client(object):

    address = None
    serverClientObject = None

    hasAuthorised = False

    authToken = None

    def __init__(self,address:str,serverConnectionObject):
        self.address = address
        self.serverClientObject = serverConnectionObject

    def authorise(self):
        pass