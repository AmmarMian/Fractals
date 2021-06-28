import sys
sys.path.append('./src')
from math import sqrt 
from main import NombreComplexe
import unittest


class Test_nombrecomplexe(unittest.TestCase):
    def test_creation(self):
        z = NombreComplexe(5, 7)
        assert z.real == 5
        assert z.imag == 7

        z = NombreComplexe(0, -5)
        assert z.real == 0
        assert z.imag == -5


    def test_module(self):

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


if __name__ == '__main__':
    unittest.main()