# -*- coding: utf-8 -*-
import unittest

# Local
from core.utils import combine_players_moves, get_first_turn, kombat


class TestKombatGame(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            "player1": {"movimientos": ["DSD", "S"], "golpes": ["P", ""]},
            "player2": {
                "movimientos": ["", "ASA", "DA", "AAA", "", "SA"],
                "golpes": ["P", "", "P", "K", "K", "K"],
            },
        }

    def test_combine_players_moves(self):
        player1_moves = [
            {"text": "Tonyn conecta un Taladoken", "value": 3, "player": "player1"},
            {"text": "Tonyn usa un Remuyuken", "value": 2, "player": "player1"},
            {"text": "Tonyn le da un puñetazo", "value": 1, "player": "player1"},
        ]
        player2_moves = [
            {"text": "Arnaldor conecta un Remuyuken", "value": 3, "player": "player2"},
            {"text": "Arnaldor usa un Taladoken", "value": 2, "player": "player2"},
            {"text": "Arnaldor le da un puñetazo", "value": 1, "player": "player2"},
        ]
        combined_moves = combine_players_moves(
            player1_moves, "Tonyn", player2_moves, "Arnaldor"
        )
        expected_result = [
            {"text": "Tonyn conecta un Taladoken", "value": 3, "player": "player1"},
            {"text": "Arnaldor conecta un Remuyuken", "value": 3, "player": "player2"},
            {"text": "Tonyn usa un Remuyuken", "value": 2, "player": "player1"},
            {"text": "Arnaldor usa un Taladoken", "value": 2, "player": "player2"},
            {"text": "Tonyn le da un puñetazo", "value": 1, "player": "player1"},
            {"text": "Arnaldor le da un puñetazo", "value": 1, "player": "player2"},
        ]
        self.assertEqual(combined_moves, expected_result)

    def test_get_first_turn(self):
        player1 = {"movimientos": ["D", "S", "D", "P"], "golpes": ["P", "K", "W"]}
        player2 = {"movimientos": ["S", "A", "K"], "golpes": ["P", "K", "W"]}
        result = get_first_turn(player1, player2)
        self.assertEqual(result, "player2")

    def test_kombat(self):
        kombat_result = kombat(self.test_data)
        self.assertTrue(len(kombat_result) > 0)


if __name__ == "__main__":
    unittest.main()
