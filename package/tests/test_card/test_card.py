import unittest
from service.card import Card

class TestCard(unittest.TestCase):

    def setUp(self) -> None:
        self.card = Card()

    def test_create_card(self):

        self.assertFalse(hasattr(self.card, '_card_numbers'))


