import json

class packetBuilder:

    def simpleCode(code:int,message=None):
        data = {}
        data["code"] = code
        data["message"] = message
        return json.dumps(data)


