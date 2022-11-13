from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nat):
        players = self.reader.get_players()
        
        players = [p for p in players if p.nationality == nat]
        players.sort(key=lambda player: player.goals + player.assists, reverse=True)
        return players
