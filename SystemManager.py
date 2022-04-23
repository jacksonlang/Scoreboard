import http.client
import json
from datetime import date
from flask import Flask
from flask import render_template, url_for
from NBA.NBATeamsDict import NBATeamDict as NBATeams
from NBA.NBAGame import NBAGame as NBAGameClass



app = Flask(__name__)



today = date.today()

s =today.strftime('%Y-%m-%d')

#print(s)



with open('BasketballTeams.json', 'r') as fp:
    teamsjson = json.load(fp)

teamLib = json.loads(teamsjson)

#print(teamLib["response"][1]["id"])


#conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")

#headers = {
 #   'X-RapidAPI-Host': "api-nba-v1.p.rapidapi.com",
  #  'X-RapidAPI-Key': "b000ca23a4mshddcbd4524667073p1d4364jsnef1cddc8cc67"
   # }

#conn.request("GET", "/games?date="+s, headers=headers)

#res = conn.getresponse()
#data = res.read()

#jsongames = data.decode("utf-8")



#with open('Games.json', 'w') as f:
#    json.dump(jsongames, f, ensure_ascii=False, indent=4)

with open('Games.json', 'r') as fp:
    gamesjson = json.load(fp)

gamesLib = json.loads(gamesjson)
NBAGamesToday = len(gamesLib["response"])



#print("Visitor: "+ teamLib["response"][gamesLib["response"][0]["teams"]["visitors"]["id"] - 1]["name"]
#    + " |||| Home: " + teamLib["response"][gamesLib["response"][0]["teams"]["home"]["id"] - 1]["name"])

i = 0
NBAGames = {}

while i <= NBAGamesToday - 1:
    NBAVisitor = NBATeams[gamesLib["response"][i]["teams"]["visitors"]["id"]]
    NBAHome = NBATeams[gamesLib["response"][i]["teams"]["home"]["id"]]
    GameId = gamesLib["response"][i]["id"]
    #time is like 1:30 ahead of est so need to make that change
    NBAgameStart = gamesLib["response"][i]["date"]["start"]
    g = NBAGameClass(NBAVisitor, NBAHome, NBAgameStart, GameId)
    NBAGames[i] = g
    i += 1

@app.route('/')
@app.route('/NBAhomepage')
def index():
    #name = teamLib["response"][]
    return render_template('NBAhomepage.html', len = NBAGamesToday - 1, NBAGames = NBAGames)

if __name__ == '__main__':
   app.run()
