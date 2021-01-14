import requests
import json

username = input("Username of the individual: ")

IDRequest = requests.get('https://api.roblox.com/users/get-by-username?username=' + username)
RoID = ''.join(filter(lambda i: i.isdigit(), IDRequest.text))
print("ID: " + str(RoID))
Status = IDRequest.text.find('"IsOnline":True')

if Status < 0:
    print(username + " is currently offline.")
if Status > 0:
    print(username + " is currently online.")

rap = 0
hats = 0
rinv = requests.get('https://inventory.roblox.com/v1/users/' + RoID + '/assets/collectibles?assetType=Hat&sortOrder=Asc&limit=100')
invres = rinv.text
cinvres = json.loads(invres)
data = cinvres['data']
for key in data:
    hats += 1
    rap += key['recentAveragePrice']
if hats == 100:
    print("NOTICE: The RAP will be wrong, the player has over 100 hats and API does not support more requests than 100. He is most likely REALLY rich.")
print(username + "'s RAP based on hats is " + str(rap) + ' and has ' + str(hats) + ' hats')


