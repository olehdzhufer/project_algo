import unittest

from src.main import UnionFind


class TestUnionFind(unittest.TestCase):

    def test_union_find(self):
        union_find = UnionFind([1, 2, 3, 4, 5, 8, 10])
        pairs = []

        pair1 = union_find.union(1, 2)
        pair2 = union_find.union(2, 4)
        pair3 = union_find.union(1, 3)
        pair4 = union_find.union(3, 5)
        pair5 = union_find.union(8, 10)

        pairs.append(pair1)
        pairs.append(pair2)
        pairs.append(pair3)
        pairs.append(pair4)
        pairs.append(pair5)

        result = union_find.wedd(pairs)

        self.assertEqual(result, (6, [(8, 1), (8, 3), (8, 5), (10, 1), (10, 3), (10, 5)]))

    def test_union_find_empty(self):
        # Тест для порожнього списку
        union_find = UnionFind([])
        pairs = []
        result = union_find.wedd(pairs)
        self.assertEqual(result, (0, []))

    def test_union_find_no_pairs(self):
        # Тест для випадку, коли немає пар
        union_find = UnionFind([1, 2, 3, 4])
        pairs = []
        result = union_find.wedd(pairs)
        self.assertEqual(result, (0, []))

if __name__ == '__main__':
    unittest.main()
