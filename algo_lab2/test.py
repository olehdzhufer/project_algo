import unittest

from main import func


class TestFunc(unittest.TestCase):
  def testfunc1(self):
    piles = [3,6,7,11]
    h = 8
    result = func(piles, h)
    expected_result = 4
    self.assertEqual(expected_result, result)

  def testfunc2(self):
    piles = [30,11,23,4,20]
    h = 5
    result = func(piles, h)
    expected_result = 30
    self.assertEqual(expected_result, result)

  def testfunc3(self):
    piles = [30,11,23,4,20]
    h = 6
    result = func(piles, h)
    expected_result = 23
    self.assertEqual(expected_result, result)