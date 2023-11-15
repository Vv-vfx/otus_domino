import unittest
from service.bag import Bag

class TestBag(unittest.TestCase):

    def setUp(self) -> None:
        
        self.bag = Bag()
        self.assertIsInstance(self.bag, Bag, 'Bag instance not create')


    def test_get_barrel(self):

        self.assertIsInstance(self.bag.get_barrel(), int, 'instance is not "int"')
