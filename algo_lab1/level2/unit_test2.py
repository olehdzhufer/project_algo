import unittest
from level2.lev2 import func

class TestFunc(unittest.TestCase):
    def test_func(self):
        k = 1
        mas = [1, 2, 3]
        result = func(k, mas)
        actulal = (result, mas[result])
        expected_result = (2,3)
        self.assertEqual(expected_result, actulal)

    def test_func2(self):
        k = 2
        mas = [1, 2, 3]
        result = func(k, mas)
        actulal = (result, mas[result])
        expected_result = (1,2)
        self.assertEqual(expected_result, actulal)

    def test_func3(self):
        k = 3
        mas = [1, 2, 3]
        result = func(k, mas)
        actulal = (result, mas[result])
        expected_result = (0,1)
        self.assertEqual(expected_result, actulal)

if __name__ == '__main__':
    unittest.main()