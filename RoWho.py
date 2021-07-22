import requests
import json

# This is a useless tool, to be honest...

def obtainInformation(user):
    try:
        ReqResponse = requests.get('https://api.roblox.com/users/get-by-username?username=' + user)
        ResponseDict = json.loads(ReqResponse.text)
        ID = ResponseDict["Id"]
        print(user + "'s ID is: " + str(ID))
        checkStatus(ResponseDict)
    except Exception as err:
        print(err)


def checkStatus(ResponseDict):
    try:
        if ResponseDict["IsOnline"] == False:
            print(user + ' is offline')
        else:
            print(user + ' is online')
    except Exception as err:
        print(err)


if __name__ == "__main__":
    user = input("Please input the username of target: ")
    obtainInformation(user)
