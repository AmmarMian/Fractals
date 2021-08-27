import sys
sys.path.append('../src')
sys.path.append('./src')
from math import sqrt 
from main import NombreComplexe
import unittest


class Test_NombreComplexe(unittest.TestCase):
    def test_creation(self):
        """Teste bonne création nombre complexe
        """
        z = NombreComplexe(5, 7)
        assert z.real == 5
        assert z.imag == 7

        z = NombreComplexe(0, -5)
        assert z.real == 0
        assert z.imag == -5


    def test_module(self):
        """Teste du module du nombre complexe.
        """

        list_numbers = [NombreComplexe(x, y) 
                for x, y in zip(range(-50, 150, 10),
                                range(-10,10,1))]
        list_numbers += [NombreComplexe(x, y) 
                for x, y in zip(range(-10,10,1),
                                range(-50, 150, 10))]

        for z in list_numbers:
            assert z.module() >= 0
            assert z.module() == sqrt(
                z.real**2 + z.imag**2)

    def test_somme1(self):
        """Teste la somme de deux nombres complexes (1/2).
        """
        z1 = NombreComplexe(5, 7)
        z2 = NombreComplexe(-1, 7)
        z = z1 + z2
        assert z.real == 4
        assert z.imag == 14

    def test_somme2(self):
        """Teste la somme de deux nombres complexes (2/2).
        """
        z1 = NombreComplexe(-5, 117)
        z2 = NombreComplexe(-10, 7)
        z = z1 + z2
        assert z.real == -15
        assert z.imag == 124

    def test_sub1(self):
        """Teste la soustraction de deux nombres complexes (1/2).
        """
        z1 = NombreComplexe(5, 7)
        z2 = NombreComplexe(-1, 7)
        z = z1 - z2
        assert z.real == 6
        assert z.imag == 0

    def test_sub2(self):
        """Teste la soustraction de deux nombres complexes (2/2).
        """
        z1 = NombreComplexe(0, 4)
        z2 = NombreComplexe(3, 7)
        z = z1 - z2
        assert z.real == -3
        assert z.imag == -3

    def test_prod1(self):
        """Teste le produit de deux nombres complexes (1/2).
        """
        z1 = NombreComplexe(0, 4)
        z2 = NombreComplexe(3, 7)
        z = z1 * z2
        assert z.real == -28
        assert z.imag == 12

    def test_prod2(self):
        """Teste le produit de deux nombres complexes (2/2).
        """
        z1 = NombreComplexe(117, 4)
        z2 = NombreComplexe(3, -70)
        z = z1 * z2
        assert z.real == 631
        assert z.imag == -8178

    def test_power0(self):
        """Teste la puissance d'un nombre complexe (1/2).
        """
        z1 = NombreComplexe(0, 4)
        z = z1**0
        assert z.real == 1
        assert z.imag == 0

    def test_power2(self):
        """Teste la puissance d'un nombre complexe (2/2).
        """
        z1 = NombreComplexe(117, 4)
        z = z1**2
        assert z.real == 13673
        assert z.imag == 936

    def test_str0(self):
        """Teste si l'impression d'un nombre complexe se fait bien (1/3).
        """
        z = NombreComplexe(1,5)
        assert z.__str__() == "1 + 5i"
    
    def test_str1(self):
        """Teste si l'impression d'un nombre complexe se fait bien (2/3).
        """
        z = NombreComplexe(-1,-555)
        assert z.__str__() == "-1 - 555i"

    def test_str2(self):
        """Teste si l'impression d'un nombre complexe se fait bien (3/3).
        """
        z = NombreComplexe(77,0)
        assert z.__str__() == "77"

if __name__ == '__main__':
    import nose2
    nose2.main()