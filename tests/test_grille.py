import sys
sys.path.append('../src')
sys.path.append('./src')
from math import sqrt 
from main import NombreComplexe, nombre_complexe, grille_complexe,\
     nombre_complexe_numpy, grille_complexe_numpy
import numpy as np
from numpy.testing import assert_almost_equal
import unittest
import numbers

def convert_NombreComplexePython(z):
    return z.real + 1j*z.imag

class Test_nombre_complexe(unittest.TestCase):
    def test_nombre_complexe_leftup(self):
        """Teste de nombre_complexe au point de la bordure gauche haute.
        """
        for n_y, n_x in zip(range(10,1000,100), range(50,1000,100)):
            a = nombre_complexe(0, 0, n_y, n_x)
            assert_almost_equal(a.real, -2)
            assert_almost_equal(a.imag, 1)

    def test_nombre_complexe_leftdown(self):
        """Teste de nombre_complexe au point de la bordure gauche basse.
        """
        for n_y, n_x in zip(range(10,1000,100), range(50,1000,100)):
            a = nombre_complexe(n_y-1, 0, n_y, n_x)
            assert_almost_equal(a.real, -2)
            assert_almost_equal(a.imag, -1)

    def test_nombre_complexe_rightdown(self):
        """Teste de nombre_complexe au point de la bordure droite basse.
        """
        for n_y, n_x in zip(range(10,1000,100), range(50,1000,100)):
            a = nombre_complexe(n_y-1, n_x-1, n_y, n_x)
            assert_almost_equal(a.real, 1)
            assert_almost_equal(a.imag, -1)

    def test_nombre_complexe_rightup(self):
        """Teste de nombre_complexe au point de la bordure droite haute.
        """
        for n_y, n_x in zip(range(10,1000,100), range(50,1000,100)):
            a = nombre_complexe(0, n_x-1, n_y, n_x)
            assert_almost_equal(a.real, 1)
            assert_almost_equal(a.imag, 1)

    
class Test_nombre_complexe_numpy(unittest.TestCase):
    def test_nombre_complexe_leftup(self):
        """Teste de nombre_complexe au point de la bordure gauche haute. Numpy.
        """
        for n_y, n_x in zip(range(10,1000,100), range(50,1000,100)):
            a = nombre_complexe_numpy(0, 0, n_y, n_x)
            assert_almost_equal(a.real, -2)
            assert_almost_equal(a.imag, 1)

    def test_nombre_complexe_leftdown(self):
        """Teste de nombre_complexe au point de la bordure gauche basse. Numpy.
        """
        for n_y, n_x in zip(range(10,1000,100), range(50,1000,100)):
            a = nombre_complexe_numpy(n_y-1, 0, n_y, n_x)
            assert_almost_equal(a.real, -2)
            assert_almost_equal(a.imag, -1)

    def test_nombre_complexe_rightdown(self):
        """Teste de nombre_complexe au point de la bordure droite basse. Numpy.
        """
        for n_y, n_x in zip(range(10,1000,100), range(50,1000,100)):
            a = nombre_complexe_numpy(n_y-1, n_x-1, n_y, n_x)
            assert_almost_equal(a.real, 1)
            assert_almost_equal(a.imag, -1)

    def test_nombre_complexe_rightup(self):
        """Teste de nombre_complexe au point de la bordure droite haute. Numpy.
        """
        for n_y, n_x in zip(range(10,1000,100), range(50,1000,100)):
            a = nombre_complexe_numpy(0, n_x-1, n_y, n_x)
            assert_almost_equal(a.real, 1)
            assert_almost_equal(a.imag, 1)


class test_grille_complexe(unittest.TestCase):
    def test_type(self):
        """Teste si le type de la grille est une liste.
        """
        n_y, n_x = 50, 50
        assert type(grille_complexe(n_y, n_x)) is list

    def test_size(self):
        """Teste si la taille de la grille est bonne.
        """
        for n_y, n_x in zip(range(10, 1000, 70), range(20, 1000, 70)):
            grille = grille_complexe(n_y, n_x)
            assert len(grille) == n_y
            assert len(grille[0]) == n_x

    def test_borders_equal_size(self):
        """Teste si les bordures de la grille sont bien les nombres qu'on cherche.
        """
        n_y, n_x = 100, 100
        grille = grille_complexe(n_y, n_x)
        grille_numpy = np.empty((n_y, n_x), dtype=complex)
        for k, ligne in enumerate(grille):
            for l, z in enumerate(ligne):
                grille_numpy[k, l] = convert_NombreComplexePython(z)

        assert_almost_equal(grille_numpy[0, 0], -2+1j)
        assert_almost_equal(grille_numpy[-1, 0], -2-1j)
        assert_almost_equal(grille_numpy[0, -1], 1+1j)
        assert_almost_equal(grille_numpy[-1, -1], 1-1j)

    def test_borders_different_size(self):
        """Teste si les bordures de la grille sont bien les nombres qu'on cherche.
        """
        n_y, n_x = 100, 200
        grille = grille_complexe(n_y, n_x)
        grille_numpy = np.empty((n_y, n_x), dtype=complex)
        for k, ligne in enumerate(grille):
            for l, z in enumerate(ligne):
                grille_numpy[k, l] = convert_NombreComplexePython(z)
        assert_almost_equal(grille_numpy[0, 0], -2+1j)
        assert_almost_equal(grille_numpy[-1, 0], -2-1j)
        assert_almost_equal(grille_numpy[0, -1], 1+1j)
        assert_almost_equal(grille_numpy[-1, -1], 1-1j)
    
    def test_increasing_realfromleft(self):
        """Teste si la partie réelle de la grille augmente bien de gauche à droite.
        """
        n_y, n_x = 100, 200
        grille = grille_complexe(n_y, n_x)
        grille_numpy = np.empty((n_y, n_x))
        for k, ligne in enumerate(grille):
            for l, z in enumerate(ligne):
                grille_numpy[k, l] = z.real
        
        for k, ligne in enumerate(grille_numpy):
            assert np.all(np.diff(ligne) > 0)

    def test_decreasing_imagfromup(self):
        """Teste si la partie imaginaire de la grille diminue bien de haut en bas.
        """
        n_y, n_x = 100, 200
        grille = grille_complexe(n_y, n_x)
        grille_numpy = np.empty((n_y, n_x))
        for k, ligne in enumerate(grille):
            for l, z in enumerate(ligne):
                grille_numpy[k, l] = z.imag

        for k, ligne in enumerate(grille_numpy.T):
            assert np.all(np.diff(ligne) < 0)


class test_grille_complexe_numpy(unittest.TestCase):
    def test_type(self):
        """Teste si le type de la grille est un tableau numpy.
        """
        n_y, n_x = 50, 50
        assert type(grille_complexe_numpy(n_y, n_x)) is np.ndarray

    def test_size(self):
        """Teste si la taille de la grille est bonne.
        """
        for n_y, n_x in zip(range(10, 1000, 70), range(20, 1000, 70)):
            grille = grille_complexe_numpy(n_y, n_x)
            assert grille.shape == (n_y, n_x)


    def test_borders_equal_size(self):
        """Teste si les bordures de la grille sont bien les nombres qu'on cherche. Numpy.
        """
        n_y, n_x = 100, 100
        grille_numpy = grille_complexe_numpy(n_y, n_x)
        assert_almost_equal(grille_numpy[0, 0], -2+1j)
        assert_almost_equal(grille_numpy[-1, 0], -2-1j)
        assert_almost_equal(grille_numpy[0, -1], 1+1j)
        assert_almost_equal(grille_numpy[-1, -1], 1-1j)

    def test_borders_different_size(self):
        """Teste si les bordures de la grille sont bien les nombres qu'on cherche.  Numpy.
        """
        n_y, n_x = 100, 200
        grille_numpy = grille_complexe_numpy(n_y, n_x)
        assert_almost_equal(grille_numpy[0, 0], -2+1j)
        assert_almost_equal(grille_numpy[-1, 0], -2-1j)
        assert_almost_equal(grille_numpy[0, -1], 1+1j)
        assert_almost_equal(grille_numpy[-1, -1], 1-1j)
    
    def test_increasing_realfromleft(self):
        """Teste si la partie réelle de la grille augmente bien de gauche à droite.  Numpy.
        """
        n_y, n_x = 100, 200
        grille_numpy = np.real(grille_complexe_numpy(n_y, n_x))
        
        for k, ligne in enumerate(grille_numpy):
            assert np.all(np.diff(ligne) > 0)

    def test_decreasing_imagfromup(self):
        """Teste si la partie imaginaire de la grille diminue bien de haut en bas. Numpy.
        """
        n_y, n_x = 100, 200
        grille_numpy = np.imag(grille_complexe_numpy(n_y, n_x))

        for k, ligne in enumerate(grille_numpy.T):
            assert np.all(np.diff(ligne) < 0)


if __name__ == '__main__':
    import nose2
    nose2.main()