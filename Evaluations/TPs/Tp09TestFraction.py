import unittest

from Tp07fraction import Fraction


class TestFraction(unittest.TestCase):
    def test_init_fraction(self):
        self.assertRaises(Exception, "The parameter should be an Integer")
        self.assertRaises(TypeError, '"Denominator should be an integer"' )

    def test_reduce_fraction(self):
        self.assertEqual(Fraction(4, 8), Fraction(1, 2), "1/2")
        self.assertEqual(Fraction(3), Fraction(3, 1), "3/1")
        self.assertEqual(Fraction(0), Fraction(0), '0/1')
        self.assertEqual(Fraction(), Fraction(), '0/1')

    def test_str_fraction(self):
        fract = Fraction(2, 5)
        fract.numerator = 2
        fract.denominator = 5
        self.assertEqual(Fraction(2, 5).__str__(), "2/5")
        self.assertEqual(Fraction(4, 8).__str__(), "1/2")
        self.assertEqual(Fraction(0).__str__(),"0/1")

    def test_as_mixed_fraction(self):
        fract = Fraction(5, 2)
        self.assertEqual(fract.as_mixed_number(), 'Mixed num is 2 + 1/2')
        self.assertEqual(Fraction(3, 1).as_mixed_number(), "Mixed num is 3 + 0/1")
        self.assertEqual(Fraction(0).as_mixed_number(), "Mixed num is 0 + 0/1")
        self.assertEqual(Fraction().as_mixed_number(), "Mixed num is 0 + 0/1")

    def test_add_fraction(self):
        fract1 = Fraction(5, 2)
        fract2 = Fraction(3, 2)
        result = fract1 + fract2
        fract1 = Fraction(1, 4)
        fract2 = Fraction(2, 4)
        self.assertEqual(fract1 + fract2, Fraction(3, 4), 'The value will be 3/4')
        self.assertEqual(result.__str__(), "4/1")
        self.assertEqual((Fraction(-2,9) + Fraction(2,-6)).__str__(), "5/-9")
        self.assertEqual((Fraction(0) + Fraction(0)).__str__(), "0/1")
        self.assertEqual((Fraction() + Fraction()).__str__(), "0/1")


    def test_sub_fraction(self):
        fract1 = Fraction(6, 2)
        fract2 = Fraction(3, 2)
        result = fract1 - fract2
        self.assertEqual(str(result), '3/2')
        self.assertEqual(str(Fraction(-2, 4) - Fraction(-2, 3)), "1/6")
        self.assertEqual(str(Fraction(0) - Fraction(0)), "0/1")
        self.assertEqual(str(Fraction() - Fraction()), "0/1")

    def test_mul_fraction(self):
        fract1 = Fraction(2, 3)
        fract2 = Fraction(5, 3)
        result = fract1 * fract2
        self.assertEqual(str(result), '10/9')
        self.assertEqual(str(Fraction(-2, 4) * Fraction(-2, 3)), "1/3")
        self.assertEqual(str(Fraction(1) * Fraction(0)), "0/1")
        self.assertEqual(str(Fraction() * Fraction()), "0/1")

    def test_truediv_fraction(self):
        fract1 = Fraction(2, 4)
        fract2 = Fraction(5, 3)
        result = fract1 / fract2
        self.assertEqual(result.__str__(), '3/10')
        self.assertEqual((Fraction(-2, 4) - Fraction(-2, 3)).__str__(), "1/6")
        self.assertEqual((Fraction(0) / Fraction(0)).__str__(), "0/0")
        self.assertEqual((Fraction() / Fraction()).__str__(), "0/0")

    def test_pow_fraction(self):
        fract1 = Fraction(2, 1)
        fract2 = Fraction(3, 2)
        result = fract1 ** fract2
        self.assertEqual(result.__str__(), '18/1')

    def test_eq_farction(self):
        fract1 = Fraction(2, 1)
        fract2 = Fraction(3, 2)
        self.assertEqual(fract1.__eq__(fract2), False)
        self.assertEqual(fract1.__eq__(Fraction(4, 2)), True)

    def test_float_fraction(self):
        self.assertEqual(Fraction(4, 2).__float__(), 2.0)
        self.assertEqual(Fraction(2, 3).__float__(), 0.6666666666666666)
        self.assertEqual(Fraction(0, 3).__float__(), 0.0)

    def test_is_zero_fraction(self):
        self.assertTrue(Fraction(0, 3).is_zero(), "La valeur est egale à zero")
        self.assertFalse(Fraction(1, 4).is_zero(), "La valeur est fausse")

    def test_integer_fraction(self):
        self.assertTrue(Fraction(4, 2).is_integer(), "la value est vrai")
        self.assertFalse(Fraction(1, 5).is_integer(), 'La valeur est fausse')

    def test_proper_fraction(self):
        self.assertEqual(Fraction(1,4).is_proper(), False)
        self.assertFalse(Fraction(2,6).is_proper())

    def test_is_unit_fraction(self):
        self.assertTrue(Fraction(1, 6).is_unit(), 'il retourne True comme valeur')
        self.assertFalse(Fraction(3, 7).is_unit(), 'il retourne False comme valeur')

    def test_is_adjacent_fraction(self):
        fract1 = Fraction(3, 2)
        fract2 = Fraction(4, 2)
        self.assertEqual(fract1.is_adjacent_to(fract2), True)
        self.assertEqual(fract2.is_adjacent_to(fract1), True)
        self.assertEqual(Fraction(5, 6).is_adjacent_to(Fraction(-3, 7)), False)


if __name__ == '__main__':
    unittest.main()
