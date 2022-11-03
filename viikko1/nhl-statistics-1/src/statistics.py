class Statistics:
    def __init__(self, PlayerReader):
        reader = PlayerReader
        
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort=1):

        sort_key = lambda player: player.points

        if sort == 2:
            sort_key = lambda player: player.goals
        
        if sort == 3:
            sort_key = lambda player: player.assists

        sorted_players = sorted(
            self._players,
            key=sort_key,
            reverse=True
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
