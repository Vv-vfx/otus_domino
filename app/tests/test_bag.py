import unittest
from service.bag import Bag

class TestBag(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        
        cls.bag = Bag()


    def test_get_barrel(self):

        self.assertIsInstance(self.bag.get_barrel(), int, 'instance is not "int"')
