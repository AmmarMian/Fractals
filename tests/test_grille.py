import sys
sys.path.append('./src')
from math import sqrt 
from main import NombreComplexe
import unittest


class Test_grille(unittest.TestCase):
    def test_nombre_complexe(self):
        assert 1 == 2

if __name__ == '__main__':
    unittest.main()