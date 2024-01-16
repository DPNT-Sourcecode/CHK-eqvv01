import unittest
from lib.solutions.CHK.checkout_solution import checkout

class MyTestCase(unittest.TestCase):
    def test_something(self):
        # self.assertEqual(True, False)  # add assertion here
        assert checkout("AAABD") == 175


if __name__ == '__main__':
    unittest.main()


