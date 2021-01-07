import json

def parseData(data):
    data = json.loads(data)
    if data["type"] == "data":
        print("----------------------")
        if "credentials" in data["data"]:
            print("Username = " + data["data"]["credentials"]["Username"])
            print("Password = " + data["data"]["credentials"]["Password"])
            if "Domain" in data["data"]["credentials"]:
                print("Domain: " + data["data"]["credentials"]["Domain"])
        if "otherData" in data["data"]:
            for key in data["data"]["otherData"]:
                print(str(key) + " = " + str(data["data"]["otherData"][key]))
        print("----------------------")

    if data["type"] == "log":
        print("[" + data["data"]["type"] + "] " + data["data"]["text"])