import unittest
from lib.solutions.CHK.checkout_solution import checkout

class MyTestCase(unittest.TestCase):
    def test_regular(self):
        assert checkout("ABCD") == 115

    def test_empty(self):
        assert checkout("") == 0

    def test_invalid(self):
        assert checkout("AbCx") == -1

    def test_multiple(self):
        assert checkout("AABCCDD") == 200

    def test_special1(self):
        assert checkout("AAABCD") == 195

    def test_special2(self):
        assert checkout("ABBCD") == 130

    def test_special3(self):
        assert checkout("AAAABBB") == 255

    def test_oneoff(self):
        assert checkout("E") == 255

if __name__ == '__main__':
    unittest.main()

