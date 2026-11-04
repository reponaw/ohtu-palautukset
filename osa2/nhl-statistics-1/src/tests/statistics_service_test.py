import unittest
from statistics_service import StatisticsService
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


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_loytaa_olemassa_olevan_pelaajan(self):
        pelaaja = self.stats.search("Kurri")

        self.assertEqual(pelaaja.name, "Kurri")

    def test_search_palauttaa_none_jos_pelaajaa_ei_ole(self):
        pelaaja = self.stats.search("Selanne")

        self.assertIsNone(pelaaja)

    def test_team_palauttaa_joukkueen_pelaajat(self):
        pelaajat = self.stats.team("EDM")
        nimet = [pelaaja.name for pelaaja in pelaajat]

        self.assertEqual(nimet, ["Semenko", "Kurri", "Gretzky"])

    def test_top_palauttaa_parhaat_pistejarjestyksessa(self):
        parhaat = self.stats.top(2)

        self.assertEqual(parhaat[0].name, "Gretzky")
        self.assertEqual(parhaat[1].name, "Lemieux")