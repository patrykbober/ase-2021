from .. import calculator as c
import unittest


class TestGcd(unittest.TestCase):

    def test_gcd_nonzero_integers(self):
        result = c.gcd(270, 192)
        self.assertEqual(result, 6)

    def test_gcd_zero1(self):
        result = c.gcd(0, 6)
        self.assertEqual(result, 6)

    def test_gcd_zero2(self):
        result = c.gcd(4, 0)
        self.assertEqual(result, 4)

    def test_gcd_integers_negative(self):
        result = c.gcd(-270, -192)
        self.assertEqual(result, 6)

    def test_gcd_integers_pos_neg(self):
        result = c.gcd(270, -192)
        self.assertEqual(result, 6)

    def test_gcd_integers_neg_pos(self):
        result = c.gcd(-270, 192)
        self.assertEqual(result, 6)
