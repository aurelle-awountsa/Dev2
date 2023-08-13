class Fraction:
    """Class representing a fraction and operations on it

    Author : Aurelle Awountsa
    Date : juillet 202"
    This class allows fraction manipulations through several operations.

    """
    def __init__(num, den):
        """This builds a fraction based on some numerator and denominator.
        PRE:num must be an integer
        POST: Return a fraction simplified if den != 0
        :raise return an error if denominator or numerator is not an integer
        :raise : Exception if den = 0 or ShouldbeAndIntegerException if num and den are not real number

        """
        pass

    @property
    def numerator(self):
        pass

    @property
    def denominator(self):
        pass

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

          PRE : receive a Fraction Object
        POST : returns a textual representation of the reduced from the fraction
        """
        pass

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : an Fraction object is a reduced form of a fraction
        POST : Return a fraction in reduced float! int (num) + num its own fraction
        """
        pass

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : Other is a parameter that point another object of the same class
         POST : return the addition of  self.num + other.num reduced with the same denominator
         """
        pass

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : Other is a parameter that point another object of the same class
        POST : return the substraction of  self.num - other.num reduced with the same denominator
        """
        pass

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE :  Other is a parameter that point another object of the same class
        POST :  return the multiplication of  self.num * other.num and self.__den * other.__den
        """
        pass

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : Other is a parameter that point another object of the same class
         POST : return the division of object 1 with object 2
        """
        pass

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : Other is a parameter that point another object of the same class
        POST : return the power of the first object with the second object
        """
        pass

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        RE : Receive two instances of the Fraction class
        POST : return a boolean true that if object 1 is equal to object 2

        """

    def __float__(self):
        """Returns the decimal value of the fraction

         PRE : Receive one object of the Fraction class
        POST : return a decimal number
        """
        pass

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

            PRE : receive a numerator of the fraction
            POST : return a boolean if the fraction is equal to zero or not

        """
        pass

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

            PRE : Receive one objet of the Fraction class
            POST : return a result of a boolean if a fraction is an integer or not
        """
        pass

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

             PRE : Receive one instance of the Fraction class
             POST : return a boolean if the fraction is less than 0

         """
    def test_sub(self):
        self.assertEqual(self.fraction1 - self.fraction2, "13/6", "Soustraction impossible")
        self.assertRaises(DenominatorNullException, lambda: self.fraction9 - Fraction(1, 0))
    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

                PRE : Receive one instance of the Fraction class
                POST : Return a boolean if the numerator is equal to 1 or not
        """
        pass

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

           Two fractions are adjacents if the absolute value of the difference them is a unit fraction

            PRE : Receive two ojects of Fraction class
            POST : return a boolean if the absolute value of the difference of 2 object is a unit

           """
        pass

