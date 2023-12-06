import unittest

from src.main import search_string


class TestSearchStringFunction(unittest.TestCase):
    def test_search_string_found(self):
        haystack = 'abcabd'
        needle = 'abd'
        result = search_string(haystack, needle)
        self.assertEqual(result, 5)

    def test_search_string_not_found(self):
        haystack = 'abcabd'
        needle = 'xyz'
        result = search_string(haystack, needle)
        self.assertEqual(result, 0)

    def test_search_string_empty_needle(self):
        haystack = 'abcabd'
        needle = ''
        result = search_string(haystack, needle)
        self.assertEqual(result, -1)

    def test_search_string_empty_haystack(self):
        haystack = ''
        needle = 'abc'
        result = search_string(haystack, needle)
        self.assertEqual(result, -1)

    def test_search_string_empty_haystack_and_needle(self):
        haystack = ''
        needle = ''
        result = search_string(haystack, needle)
        self.assertEqual(result, -1)

    def test_search_string_needle_longer_than_haystack(self):
        haystack = 'abc'
        needle = 'abcdef'
        result = search_string(haystack, needle)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
