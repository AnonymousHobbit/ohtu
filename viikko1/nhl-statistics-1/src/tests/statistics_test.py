import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search(self):
        # etsitään pelaaja, joka löytyy
        player = self.statistics.search("Kurri")
        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 37)
        self.assertEqual(player.assists, 53)
        self.assertEqual(player.points, 90)

        # etsitään pelaaja, joka ei löydy
        player = self.statistics.search("adam kurri")
        self.assertEqual(player, None)

    def test_team(self):

        # etsitään joukkue, joka löytyy
        players = self.statistics.team("EDM")
        self.assertEqual(len(players), 3)

        # etsitään joukkue, joka ei löydy
        players = self.statistics.team("EDMM")
        self.assertEqual(len(players), 0)

    def test_top(self):
        players = self.statistics.top(3)
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Gretzky")
        
        players = self.statistics.top(3, 2)
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Lemieux")

        players = self.statistics.top(3, 3)
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Gretzky")




    