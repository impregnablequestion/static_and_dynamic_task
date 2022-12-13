import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.cardgame = CardGame()
        self.card1 = Card("Hearts", 10)
        self.card2 = Card("Clubs", 1)
        self.card3 = Card("Diamonds", 4)
        self.card4 = Card("Diamonds", 8)

        self.cards = [self.card1, self.card2, self.card3, self.card4]

    def test_check_for_ace_if_true(self):
        result = self.cardgame.check_for_ace(self.card2)
        self.assertEqual(result, True)

    def test_check_for_ace_if_false(self):
        result = self.cardgame.check_for_ace(self.card1)
        self.assertEqual(result, False)

    def test_check_highest_card_when_card1_higher(self):
        result = self.cardgame.highest_card(self.card1, self.card2)
        self.assertEqual(result, self.card1)

    def test_check_highest_card_when_card2_higher(self):
        result = self.cardgame.highest_card(self.card2, self.card3)
        self.assertEqual(result, self.card3)
        
    def test_check_cards_total(self):
        result = self.cardgame.cards_total(self.cards)
        self.assertEqual(result, "You have a total of 23")
    

    