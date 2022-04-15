import http.client
import json
from datetime import date
from flask import Flask
from flask import render_template




app = Flask(__name__)



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
gamesString = ""
while i <= NBAGamesToday - 1:
    gamesString += ("Visitor: "+ teamLib["response"][gamesLib["response"][i]["teams"]["visitors"]["id"] - 1]["name"]
    + " |||| Home: " + teamLib["response"][gamesLib["response"][i]["teams"]["home"]["id"] - 1]["name"]) + "\n"
    i += 1

#print(gamesString)

#@app.route('/')
#@app.route('/NBAhomepage')
#def index():
#    #name = teamLib["response"][]
#    return render_template('NBAhomepage.html', title='NBA Games Today', games = gamesString)

#if __name__ == '__main__':
#   app.run()

dictNbaTeams = {}

 #   dictNbaTeams[a] = NBAteam(name)

#for z in dictNbaTeams:
#    print(z.getName())