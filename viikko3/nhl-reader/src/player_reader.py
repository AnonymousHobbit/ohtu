import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        players = []
        r = requests.get(self.url)

        for player in r.json():
            players.append(
                Player(player["name"], player["team"], player["goals"], player["assists"], player["nationality"])
                )
        
        return players