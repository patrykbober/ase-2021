from .. import calculator as c
import unittest


class TestSubtract(unittest.TestCase):

    def test_subtract_integers_positive(self):
        result = c.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_subtract_integers_positive2(self):
        result = c.subtract(3, 5)
        self.assertEqual(result, -2)

    def test_subtract_integers_negative(self):
        result = c.subtract(-5, -3)
        self.assertEqual(result, -2)

    def test_subtract_integers_negative2(self):
        result = c.subtract(-3, -5)
        self.assertEqual(result, 2)

    def test_subtract_integers_pos_neg(self):
        result = c.subtract(5, -3)
        self.assertEqual(result, 8)

    def test_subtract_integers_neg_pos(self):
        result = c.subtract(-3, 5)
        self.assertEqual(result, -8)

        
if __name__ == '__main__':
    unittest.main()

