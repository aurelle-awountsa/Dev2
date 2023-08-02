# Python 3.10

class ComplexNumberException(Exception):
    pass


class DenominatorNullException(Exception):
    pass


class DivZero(Exception):
    pass


class ShoulBeAnInteger(Exception):
    pass

class Fraction:
    """Class representing a fraction and operations on it

    Author : Aurelle Awountsa
    Date : Juillet 2023
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This built a fraction based on numerator and denominator
        PRE:num must be an integer
        POST: Return a fraction simplified if den != 0
        :raise return an error if denominator or numerator is not an integer
        :raise : Exception if den = 0 or ShouldbeAndIntegerException if num and den are not real number


        """
        self.comp = 0
        self.__num = num
        self.__den = den

        if isinstance(self.__num, str) or isinstance(self.__den, str):
            raise ShoulBeAnInteger('Attention!!! les numerateurs et denominateurs doivent etre des nombres')

        if self.__den == 0 and (self.__num > 0 or self.__num < 0):
            raise DenominatorNullException("Vous avez entrer un dénominateur nul")

        if (self.__num and isinstance(self.__num, complex)) or isinstance(self.__den, complex):
            raise ComplexNumberException("Attention!!! Veuillez entrer des nombres réels")

    @staticmethod
    def reduce(num, den):
        """This built a fraction based on numerator and denominator
        PRE:num must be an integer
        POST: Return a fraction simplified
        :raise: return an error if den or num is not an integer

        """
        n = 1
        if type(num) != int:
            raise Exception("Attention!!! Le numérateur doit être un entier")
        elif type(den) != int:
            raise Exception("Attention!!! Le dénominateurdoit être un entier")
        if den > num:
            highest_number = den
        else:
            highest_number = num
        for i in range(1, highest_number):
            if (num % i == 0) and (den % i == 0):
                n = i
        num = num / n
        den = den / n
        return int(num), int(den)

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    @numerator.setter
    def numerator(self, num):
        self.__num = num

    @denominator.setter
    def denominator(self, den):
        self.__den = den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : receive a Fraction Object
        POST : returns a textual representation of the reduced from the fraction
        """
        self.__num, self.__den = self.reduce(self.__num, self.__den)
        result = '{}/{}'.format(self.__num, self.__den)
        return result

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction
        #Trouver une forme reduite

        PRE : an Fraction object is a reduced form of a fraction
        POST : Return a fraction in reduced float! int (num) + num its own fraction
        """
        m_num = self.__num // self.__den
        m_den = self.__num % self.__den
        return 'Mixed num is {} + {}/{}'.format(m_num, m_den, self.__den)

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : Other is a parameter that point another object of the same class
         POST : return the addition of  self.num + other.num reduced with the same denominator
         """
        num = self.__num * other.__den + other.__num * self.__den
        den = self.__den * other.__den

        num, den = self.reduce(num, den)

        return Fraction(num, den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : Other is a parameter that point another object of the same class
        POST : return the substraction of  self.num - other.num reduced with the same denominator
        """
        num = self.__num * other.__den - other.__num * self.__den
        den = self.__den * other.__den

        num, den = self.reduce(num, den)

        return Fraction(num, den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE :  Other is a parameter that point another object of the same class
        POST :  return the multiplication of  self.num * other.num and self.__den * other.__den
        """
        muln = self.__num * other.__num
        muld = self.__den * other.__den

        muln, muld = self.reduce(muln, muld)

        return Fraction(muln, muld)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

         PRE : Other is a parameter that point another object of the same class
         POST : return the division of object 1 with object 2
        """
        divnum = self.__num * other.__den
        divden = self.__den * other.__num

        divnum, divden = self.reduce(divnum, divden)

        return Fraction(divnum, divden)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : Other is a parameter that point another object of the same class
        POST : return the power of the first object with the second object
        """
        #Pow == exponsant d'une fraction par une autre fraction
        pown = (self.__num * other.__num) ** (self.__den * other.__den)
        powd = self.__den * other.__den
        pown, powd = self.reduce(pown, powd)

        return Fraction(pown, powd)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : Receive two instances of the Fraction class
        POST : return a boolean true that if object 1 is equal to object 2

        """
        fact1 = self.__num / self.__den
        fact2 = other.__num / other.__den
        if isinstance(other, str):
            return str(self.__num) + "/" + str(self.__den) == other

        return fact1 == fact2

    # Fraction(1 , 4 ).__eq__(Fraction(1,4))
    # Fraction(1 , 4 ).__eq__("1/4")

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : Receive one object of the Fraction class
        POST : return a decimal number
        """
        frac = float(self.__num / self.__den)
        return frac

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : receive a numerator of the fraction
        POST : return a boolean if the fraction is equal to zero or not
        """
        if self.__num == 0:
            return True
        else:
            return False

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : Receive one objet of the Fraction class
        POST : return a result of a boolean if a fraction is an integer or not
        """
        if self.__num % self.__den == 0:
            return True
        else:
            return False

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : Receive one instance of the Fraction class
        POST : return a boolean if the fraction is less than 0

        """
        if self.__num < 0 or self.__den < 0:
            return True
        return False

    def is_unit(self):

        """Check if a fraction's numerator is 1 in its reduced form

        PRE : Receive one instance of the Fraction class
        POST : Return a boolean if the numerator is equal to 1 or not

        """
        number = 1
        if self.__num >= self.__den:
            self.comp = self.__den
        else:
            self.comp = self.__num

        for i in range(1, self.comp + 1):
            if self.__num % i == 0 and self.__den % i == 0:
                number = i
        self.__num = self.__num // number
        self.__den = self.__den // number
        if self.__num == 1:
            return True
        else:
            return False

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : Receive two ojects of Fraction class
        POST : return a boolean if the absolute value of the difference of 2 object is a unit

        """
        num = self.__num * other.__den - other.__num * self.__den
        den = self.__den * other.__den
        n = self.reduce(num, den)
        return True if n[0] == 1 or n[0] == -1 else False


fract1 = Fraction(-4, -3)
fract2 = Fraction(10, 2)


# Truediv = simplifier 2 fraction
print(fract1.is_proper())

#pown = self.__num * other.__num ** self.__den * other.__den
