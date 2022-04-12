import http.client
import json

conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Host': "api-nba-v1.p.rapidapi.com",
    'X-RapidAPI-Key': "b000ca23a4mshddcbd4524667073p1d4364jsnef1cddc8cc67"
    }

conn.request("GET", "/teams", headers=headers)

res = conn.getresponse()
data = res.read()

teams = data.decode("utf-8")


with open('BasketballTeams.json', 'w', encoding='utf-8') as f:
    json.dump(teams, f,sort_keys=True, indent=4)
