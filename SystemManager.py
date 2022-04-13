import http.client
import json
from datetime import date

today = date.today()

s =today.strftime('%Y-%m-%d')

#print(s)



with open('BasketballTeams.json', 'r') as fp:
    teamsjson = json.load(fp)

teamLib = json.loads(teamsjson)

#print(teamLib["response"][1]["id"])


conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")

#headers = {
#    'X-RapidAPI-Host': "api-nba-v1.p.rapidapi.com",
#    'X-RapidAPI-Key': ""
#    }

#conn.request("GET", "/games?date="+s, headers=headers)

#res = conn.getresponse()
#data = res.read()

#jsongames = data.decode("utf-8")



#with open('Games.json', 'w') as f:
#    json.dump(jsongames, f, ensure_ascii=False, indent=4)
#
with open('Games.json', 'r') as fp:
    gamesjson = json.load(fp)

gamesLib = json.loads(gamesjson)
NBAGamesToday = len(gamesLib["response"])



#print("Visitor: "+ teamLib["response"][gamesLib["response"][0]["teams"]["visitors"]["id"] - 1]["name"]
#    + " |||| Home: " + teamLib["response"][gamesLib["response"][0]["teams"]["home"]["id"] - 1]["name"])

i = 0

while i <= NBAGamesToday - 1:
    print("Visitor: "+ teamLib["response"][gamesLib["response"][i]["teams"]["visitors"]["id"] - 1]["name"]
    + " |||| Home: " + teamLib["response"][gamesLib["response"][i]["teams"]["home"]["id"] - 1]["name"])
    i += 1