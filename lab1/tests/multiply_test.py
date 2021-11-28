from .. import calculator as c
import unittest


class TestMultiply(unittest.TestCase):

    def test_multiply_integers_positive(self):
        result = c.multiply(3, 6)
        self.assertEqual(result, 18)

    def test_multiply_integers_negative(self):
        result = c.multiply(-3, -6)
        self.assertEqual(result, 18)

    def test_multiply_integers_pos_neg(self):
        result = c.multiply(3, -6)
        self.assertEqual(result, -18)

    def test_multiply_integers_neg_pos(self):
        result = c.multiply(-3, 6)
        self.assertEqual(result, -18)

    def test_multiply_by_one1(self):
        result = c.multiply(1, 3)
        self.assertEqual(result, 3)

    def test_multiply_by_one2(self):
        result = c.multiply(3, 1)
        self.assertEqual(result, 3)

    def test_multiply_by_zero1(self):
        result = c.multiply(0, 3)
        self.assertEqual(result, 0)

    def test_multiply_by_zero2(self):
        result = c.multiply(3, 0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
