from tp7 import Fraction


fraction1 = Fraction(3, 4)
fraction2 = Fraction(5, 4)
fraction3 = Fraction(7, 4)
fraction4 = Fraction(3, 4)  # meme que 1, pour tester le equal


fraction_sum = fraction1 + fraction2
print(f"fraction1 + fraction2 = {fraction_sum._num}/{fraction_sum._den}")  # Attendu: (3/4) + (5/4) = 8/4 (ou 2)


print(f"fraction1 == fraction2: {fraction1 == fraction2}")  # Attendu: False
print(f"fraction1 == fraction4: {fraction1 == fraction4}")  # Attendu: True


fraction1_as_float = float(fraction1)
print(f"fraction1 en float: {fraction1_as_float}")  # Attendu: 0.75


print(f"fraction1 est adjacente à fraction2: {fraction1.is_adjacent_to(fraction2)}")  # Attendu: True, car |(5/4) - (3/4)| = 1/4
print(f"fraction1 est adjacente à fraction3: {fraction1.is_adjacent_to(fraction3)}")  # Attendu: False, car différence n'est pas ±1/d

# test pour le den nul
try:
    fraction_invalid = Fraction(1, 0)
except ValueError as e:
    print(f"Erreur de création de fraction: {e}")  # Attendu den put pas etrr nhul 
