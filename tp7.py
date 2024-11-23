from math import *

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self,num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : 
            * num doit etre un entier
            * den doit etre un entier non nul
        POST : 
            *un objet Fraction est créé
        RAISE :
            * TypeError si les arguments ne sont pas deux entiers
            * ValueError si le dénominateur est nul
        """
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError('Les arguments doivent tous les deux etres des entiers')
        if den == 0:
            raise ValueError("Le dénominateur ne pas peut etre nul")
        
        self._num = num
        self._den = den
        
    @property
    def numerator(self):
        """Retourne le numérateur de la fraction"""
        return self._num 

    @property
    def denominator(self):
        """Retourne le dénominateur de la fraction"""
        return self._den

# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : 
            * aucun
        POST : 
            * retourne la représentation textuelle de la fraction réduite au maximum
        """
        plusGrndDiviseurCmn =gcd(self._num, self._den)

        num = self._num//plusGrndDiviseurCmn
        den = self._den//plusGrndDiviseurCmn

        if den == 1:
            return f"{num}"
        else:
            return f"{num}/{den}"


    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : 
            *aucun
        POST : 
            * si le num > den, le résultat va inclure la partie entière et une fraction propre
            * si le num < den, le résultat sera le même que __str__
        """
        if abs(self._num) > abs(self._den): 
            entier = self._num // self._den
            reste = abs(self._num % self._den) 
            
            if reste != 0:
                return f"{entier} {reste}/{abs(self._den)}"
            else:
                return f"{entier}"

        elif abs(self._num) < abs(self._den):
            return str(self)

            

    
# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : 
            * other doit etre une instance de Fraction
         POST :
            * la sortie est une nouvelle fraction qui est équivalente à la somme de self et other
        RAISE : 
            * TypeError si other n'est pas une fraction
         """
        if not isinstance(other, Fraction):
            raise TypeError("les deux parametres doivent etre une fraction")
        num = self._num * other._den + other._num * self._den
        den = self._den * other._den

        return Fraction(num, den)


    def __sub__(self, other):
        """Overloading of the - operator for fractions

         PRE : 
            * other doit etre une instance de Fraction
         POST :
            * retourne une nouvelle fraction qui est équivalente à la différence
        RAISE : 
            * TypeError si other n'est pas une fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("les deux parametres doivent etre une fraction")
        return self + Fraction(-other._num, other._den)     #j'ajoute la fraction négative de other pour calculer la nouvelle


    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE :
            * other doit etre une instance de Fraction
        POST : 
            * retourne la multiplication des deux fractions, toujours sous forme de fraction
        RAISE : 
            * TypeError si other n'est pas une fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("les deux parametres doivent etre une fraction")
        num = self._num * other._num
        den = self._den * other._den

        return Fraction(num, den)


    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE :
            * other ne peut pas avoir un numérateur nul
        POST :
            * retourne une nouvelle fraction qui est le quotient des paramètres
         RAISE : 
            * TypeError si other n'est pas une fraction
            * ZeroDivisionError si le dénominateur est 0
        """
        if not isinstance(other, Fraction):
            raise TypeError("les deux parametres doivent etre une fraction")
        if other._num == 0:
            raise ZeroDivisionError("on ne poet pas diviser par 0")
        
        return self * Fraction(other._den, other._num)


    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE :
            *other doit etre un entier
        POST : 
            * élève le num et le den à une puissance et retourne cette nouvelle fraction
        RAISE : 
            * TypeError si other other n'est pas un entier
        """
        if not isinstance(other, int):
            raise TypeError("other doit etre un entier")
        
        return Fraction(self._num ** other, self._den ** other)
    
    
    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
        PRE :
            * other doit etre une instance de la classe fraction 

        POST : 
            * retourne true si les fractions sont équivelentes, sinon renvoie false
        RAISE : 
            * TypeError si other n'est pas une fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("La comparaison est définie uniquement entre deux fractions.")
        return self._num * other._den == self._den * other._num

    def __float__(self) :
        """Returns the decimal value of the fraction

        PRE :
            *aucun
        POST :
            * retourne la fraction en float
        """
        return self._num / self._den
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)



# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : 
            * aucun
        POST : 
            * retourne True si la fraction est égale à 0, return False sinon
        """
        return self._num == 0


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : aucun
        POST : 
            * Retourne True si la fraction est un entier, False sinon
        """
        return self._num % self._den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : RIENNNN
        POST : return true si la fraction est propre, false sinon
        """
        return abs(self._num) < abs(self._den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : aucun
        POST : 
            * Retourne True si la fraction est une unité, False sinon
        """
        plusGrndDiviseurCmn =gcd(self._num, self._den)
        return abs(self._num // plusGrndDiviseurCmn) == 1

    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE :
            * other est une sintance de Fraction
        POST : 
            * Retourne True si la différence est de la forme ±1/d, False sinon  (si c'est une fraction unitaire)
        RAISE : 
            * TypeError si other n'est pas une fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("other doit etre une fraction")
        
        diff = self - other
        isAdjacent = abs(diff._num) == 1
        isDenValid = abs(diff._den) > 0

        return isAdjacent and isDenValid
