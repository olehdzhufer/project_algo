import unittest

from level1.main import func


class TestFunc(unittest.TestCase):

    def test_sorting(self):
        input_array = [1, 7, 3, 10, 9, -2]
        expected_result = [1, 4, 9, 49, 81, 100]
        result = func(input_array)
        self.assertEqual(result, expected_result)

    def test_empty_input(self):
        input_array = []
        expected_result = []
        result = func(input_array)
        self.assertEqual(result, expected_result)

    def test_negative_numbers(self):
        input_array = [-5, -2, -1, -10]
        expected_result = [1, 4, 25, 100]
        result = func(input_array)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()