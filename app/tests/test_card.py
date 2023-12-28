import unittest
from service.card import Card


class TestCard(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.card = Card()

    def test_create_card(self):
        self.assertIsInstance(self.card._all_numbers, set, '_all_numbers wrong type')
        self.assertIsInstance(self.card._card_numbers, list, '_card_numbers wrong type')
        self.assertTrue(self.card._all_numbers, '_all_numbers is empty')
        self.assertTrue(self.card._card_numbers, '_card_numbers is empty')

    def test__str__(self):
        self.assertIsInstance(self.card.__str__(), str, '__str__ returns not str')

    def test_cross_out_number(self):
        self.card._all_numbers = {1, 2, 3, 4, 5}
        number = 10
        self.assertEqual(self.card.cross_out_number(number), 'not number in card', \
                         f"the number {number} cannot not be found in card")

        number = 1
        self.assertEqual(self.card.cross_out_number(number), 'continue play', \
                         f"the number {number}  must be found in card")
