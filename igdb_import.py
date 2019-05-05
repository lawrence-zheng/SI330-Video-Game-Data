import requests
import json

def getIgdbData(name):
    headers = {
        # API key hidden for security purposes, can get one for free at https://api.igdb.com/
        "user-key": user_key,
        "user-agent": "Lawrence Zheng's personal project",
    }
    payload = "fields name,first_release_date, genres, rating; where name = \"" + name + "\";"
    url = "https://api-v3.igdb.com/games"
    response = requests.post(url, headers=headers, data=payload)
    results = json.loads(response.content)
    return results