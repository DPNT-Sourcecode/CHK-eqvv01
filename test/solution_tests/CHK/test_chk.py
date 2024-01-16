import unittest
from lib.solutions.CHK.checkout_solution import checkout

class MyTestCase(unittest.TestCase):
    def test_checkout(self):
        assert checkout("AAABD") == 175 and checkout("") == 0


if __name__ == '__main__':
    unittest.main()



