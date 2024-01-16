import unittest
from lib.solutions.CHK.checkout_solution import checkout

class MyTestCase(unittest.TestCase):
    def test_regular1(self):
        assert checkout("ABCD") == 115

    def test_regular2(self):
        assert checkout("UVPK") == 220

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

    def test_special4(self):
        assert checkout("AAAAAA") == 250

    def test_special5(self):
        assert checkout("AAAAAAAA") == 330

    def test_special6(self):
        assert checkout("LMMNNN") == 225

    def test_special7(self):
        assert checkout("UUUUUU") == 200

    def test_oneoff1(self):
        assert checkout("EEBB") == 110

    def test_oneoff2(self):
        assert checkout("FFF") == 20

    def test_oneoff2(self):
        assert checkout("FFFFFF") == 40

if __name__ == '__main__':
    unittest.main()



