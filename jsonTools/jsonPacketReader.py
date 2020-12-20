import json

class packetReader:

    def decode(self,data):
        packetType = data["packetType"]
        code = data["code"]

        if packetType == "simple":
            return {"code":code,"data":data["data"]}


