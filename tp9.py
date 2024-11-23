import unittest
from tp7 import Fraction

class testFraction(unittest.TestCase):
    def test_Init_valid(self):
        """Vérifie si les args sont valides dans l'initialisation d'une fraction"""
        f = Fraction(1,2)
        self.assertEqual(f.numerator,1,'num incorrect')
        self.assertEqual(f.denominator,2,'den incorrect')

    def test_Init_raises(self):
        """Vérifie le type des arguments"""
        with self.assertRaises(TypeError):
            Fraction(1.5, 2)
        with self.assertRaises(TypeError):
            Fraction(1, "2")

    def test_Init_den(self):
        """vérifie si le dénominateur est bien != 0"""
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_Str(self):
        """Vérification de la représentation du str"""
        self.assertEqual(str(Fraction(1,2)),"1/2","représentation réduire non correcte")
        self.assertEqual(str(Fraction(400,200)),"2","représentation réduire non correcte")
        self.assertEqual(str(Fraction(0,2)),"0","représentation réduire non correcte")

    def test_as_mixed_number(self):
        """Vérification de la représentation en entier et reste"""
        self.assertEqual(Fraction(7,3).as_mixed_number(),"2 1/3","représentation de l'entier et du reste incorrecte")
        self.assertEqual(Fraction(4,2).as_mixed_number(),"2","représentation de l'entier et du reste incorrecte")
        self.assertEqual(Fraction(30,40).as_mixed_number(),"3/4","représentation de l'entier et du reste incorrecte")

    def test_add(self):
        """vérifie l'addition"""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(f1 + f2, Fraction(5, 6), "Somme incorrecte")

    def test_sub(self):
        """Vérification du moins"""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(f1 - f2, Fraction(1, 6), "Différence incorrecte")

    def test_mul(self):
        """Vérification de la multiplication"""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertEqual(f1 * f2, Fraction(1, 2), "Produit incorrect")

    def test_division(self):
        """Vérification de la divisioin"""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertEqual(f1 / f2, Fraction(8, 9), "Quotient incorrect")

    def test_division_par_zero(self):
        """Vérification de l'exception ZeroDivisionError"""
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2) / Fraction(0, 1)

    def test_puissance(self):
        """Vérification de la puissance sur les fractions"""
        f = Fraction(1, 3)
        self.assertEqual(f ** 2, Fraction(1, 9), "Puissance incorrecte")
        self.assertEqual(f ** 0, Fraction(1, 1), "Puissance incorrecte")

    def test_equal(self):
        """Vérification de l'equal"""
        self.assertTrue(Fraction(2, 3) == Fraction(4, 6), "Égalité incorrecte")
        self.assertFalse(Fraction(2, 3) == Fraction(3, 4), "Égalité incorrecte")

    def test_float(self):
        """vérifie si le float retourné est correct"""
        self.assertEqual(float(Fraction(1,2)),0.5,"le float n'est pas correct")

    def test_is_zero(self):
        """Vérifie si une fraction est = à 0"""
        self.assertTrue(Fraction(0, 3).is_zero(), "la détection de 0 est incorrecte")
        self.assertFalse(Fraction(3, 4).is_zero(), "la détection de 0 est incorrecte")

    def test_is_integer(self):
        """Vérifie si la fraction est bien un entier"""
        self.assertTrue(Fraction(2, 1).is_integer(), "détection d'entier incorrecte")
        self.assertFalse(Fraction(3, 4).is_integer(), "détection d'entier incorrecte")

    def test_is_proper(self):
        """Vérification de la méthode is_proper"""
        self.assertTrue(Fraction(3, 4).is_proper(), "Détection de fraction propre incorrecte")
        self.assertFalse(Fraction(4, 2).is_proper(), "Détection de fraction propre incorrecte")

    def test_is_unit(self):
        """Vérification de la méthode is_unit"""
        self.assertTrue(Fraction(1, 4).is_unit(), "Détection d'unité incorrecte")
        self.assertFalse(Fraction(3, 4).is_unit(), "Détection d'unité incorrecte")

    def test_is_adjacent_to(self):
        """Vérification de la méthode is_adjacent_to"""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertTrue(f1.is_adjacent_to(f2), "Détection d'adjacence incorrecte")
        self.assertFalse(f1.is_adjacent_to(Fraction(1, 4)), "Détection d'adjacence incorrecte")



        

if __name__ == '__main__':
    unittest.main(argv=['firest-arg-is-ignored'], exit = False)
