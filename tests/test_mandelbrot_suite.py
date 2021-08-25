import sys
sys.path.append('./src')
from math import sqrt 
from main import NombreComplexe, est_divergente, nombre_iterations,\
    image_mandelbrot, image_mandelbrot_couleur, image_mandelbrot_numpy_couleur
import numpy as np
from numpy.testing import assert_almost_equal
import unittest

class test_est_divergente(unittest.TestCase):
    def test_convergence_small_c(self):
        """Teste si est_divergente renvoie faux pour un petit nombre.
        """
        N = 50

        c = NombreComplexe(0, 0)
        assert not est_divergente(c, N)

        c = NombreComplexe(-0.001, 0.001)
        assert not est_divergente(c, N)

    def test_divergence_big_c(self):
        """Teste si est_divergente renvoie vrai pour un grand nombre.
        """
        N = 500

        c = NombreComplexe(10, 10)
        assert est_divergente(c, N)

        c = NombreComplexe(-10, 10)
        assert est_divergente(c, N)


class test_nombre_iterations(unittest.TestCase):
    def test_iterations_zero(self):
        """Teste nombre_iterations pour un cas avec N iterations.
        """
        N = 500
        c = NombreComplexe(0, 0)
        assert_almost_equal(nombre_iterations(c,N), N, decimal=0)

    def test_iterations_big(self):
        """Teste nombre_iterations pour un cas avec 0 iterations.
        """
        N = 500
        c = NombreComplexe(10,-0.5)
        assert_almost_equal(nombre_iterations(c,N), 0, decimal=0)

    def test_iterations_medium(self):
        """Teste nombre_iterations pour un cas avec 342 iterations.
        """
        N = 500
        c = c = NombreComplexe(0.37,-0.3)
        assert_almost_equal(nombre_iterations(c,N), 342, decimal=0)


class test_image_mandelbrot(unittest.TestCase):
    def test_image_mandelbrot(self):
        """Teste si l'image mandebrot est bien créee.
        """
        ny, nx = 100, 200
        N = 30
        image = image_mandelbrot(ny, nx, N)
        assert type(image) is list
        assert len(image) == ny
        assert len(image[0]) == nx

    def test_image_mandelbrot_couleur(self):
        """Teste si l'image mandebrot couleur est bien créee.
        """
        ny, nx = 100, 200
        N = 30
        image = image_mandelbrot_couleur(ny, nx, N)
        assert type(image) is list
        assert len(image) == ny
        assert len(image[0]) == nx

    def test_image_mandelbrot_numpy_couleur(self):
        """Teste si l'image mandebrot numpy couleur est bien créee.
        """
        ny, nx = 100, 200
        N = 30
        image = image_mandelbrot_numpy_couleur(ny, nx, N)
        assert type(image) is np.ndarray
        assert image.shape == (ny, nx)

if __name__ == '__main__':
    import nose2
    nose2.main()