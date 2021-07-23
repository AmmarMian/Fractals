'''
TP1 - Fractals
Nom élève :
Groupe élève :
File: main.py
Created Date: Friday June 25th 2021 - 04:51pm
Author: Ammar Mian
Contact: ammar.mian@univ-smb.fr
-----
Last Modified: Fri Jul 23 2021
Modified By: Ammar Mian
-----
Copyright (c) 2021 Université Savoie Mont-Blanc
'''


class NombreComplexe:
    def __init__(self, real, imag):
        pass

    def __str__(self):
        pass

    def module(self):
        pass


def nombre_complexe(k, l, n_y, n_x):
    """Renvoie un nombre complexe de la grille pour afficher l'ensemble de Mandelbrot.

    Parameters
    ----------
    k : int
        indice ligne.
    l : int
        indice colonne.
    n_y : int
        nombre de points en ligne.
    n_x : int
        nombre de points en colonne.

    Returns
    -------
    NombreComplexe
        le nombre complexe correspondant.
    """
    pass


def grille_complexe(n_y, n_x):
    """Crée une grille de nombre complexes pour afficher l'ensemble de Mandelbrot.

    Parameters
    ----------
    n_y : int
        nombre de points en ligne.
    n_x : int
        nombre de points en colonne.

    Returns
    -------
    list
        la grille sous forme de liste de liste.
    """
    pass


def est_divergente(c, N):
    """Vérifie si la suite de Mandelbrot diverge ou non à l'aide d'un nombre
    d'itérations en vérifiant si le module dépasse 2.

    Parameters
    ----------
    c : NombreComplexe
        le nombre complexe de décalage.
    N : int
        le nombre d'itérations maximum à partir du quel on considère 
        que la suite converge.

    Returns
    -------
    bool
        True si suite diverge. False sinon.
    """
    pass


def nombre_iterations(c, N):
    """Nombre d'itérations de la suite de Mandelbrot que l'on calcule
    tant que le module ne dépasse pas 2.

    Parameters
    ----------
    c : NombreComplexe
        le nombre complexe de décalage.
    N : int
        le nombre d'itérations maximum à partir du quel on considère 
        que la suite converge.

    Returns
    -------
    int
        nombre d'itérations faites.
    """
    pass


def image_mandelbrot(n_y, n_x, N):
    """Crée une image de Mandelbrot binaire de taille définie par les entrées et
    paramétrée par un nombre d'itérations maximum.

    Parameters
    ----------
    n_y : int
        nombre de points en ligne.
    n_x : int
        nombre de points en colonne.
    N : int
        le nombre d'itérations maximum à partir du quel on considère 
        que la suite converge.

    Returns
    -------
    list
        l'image sous forme de liste de liste.
    """
    pass


def image_mandelbrot_couleur(n_y, n_x, N):
    """Crée une image de Mandelbrot en couleur de taille définie par les entrées et
    paramétrée par un nombre d'itérations maximum.

    Parameters
    ----------
    n_y : int
        nombre de points en ligne.
    n_x : int
        nombre de points en colonne.
    N : int
        le nombre d'itérations maximum à partir du quel on considère 
        que la suite converge.

    Returns
    -------
    list
        l'image sous forme de liste de liste.
    """
    pass


def nombre_complexe_numpy(k, l, n_y, n_x):
    """Renvoie un nombre complexe de la grille pour afficher l'ensemble de Mandelbrot.

    Parameters
    ----------
    k : int
        indice ligne.
    l : int
        indice colonne.
    n_y : int
        nombre de points en ligne.
    n_x : int
        nombre de points en colonne.

    Returns
    -------
    NombreComplexe
        le nombre complexe correspondant.
    """
    pass


def grille_complexe_numpy(n_y, n_x):
    """Crée une grille de nombre complexes pour afficher l'ensemble de Mandelbrot.
    Version à l'aide de numpy.

    Parameters
    ----------
    n_y : int
        nombre de points en ligne.
    n_x : int
        nombre de points en colonne.

    Returns
    -------
    array, de taille (n_y, n_x)
        la grille sous forme d'un array numpy.
    """
    pass


def image_mandelbrot_numpy_couleur(n_y, n_x, N):
    """Crée une image de Mandelbrot couleur de taille définie par les entrées et
    paramétrée par un nombre d'itérations maximum. Version avec numpy.

    Parameters
    ----------
    n_y : int
        nombre de points en ligne.
    n_x : int
        nombre de points en colonne.
    N : int
        le nombre d'itérations maximum à partir du quel on considère 
        que la suite converge.

    Returns
    -------
    array, de taille (n_y, n_x)
        la grille sous forme d'un array numpy.
    """
    c = grille_complexe_numpy(n_y, n_x)
    z = np.zeros((n_y, n_x), dtype=complex)
    masque_non_divergent = np.full((n_y, n_x), True, dtype=bool)
    image = np.zeros((n_y, n_x))
    for n in trange(N):
        z[masque_non_divergent] = z[masque_non_divergent]**2 +\
                                  c[masque_non_divergent]
        masque_nouveau_divergent = np.logical_and(
            masque_non_divergent, np.abs(z) > 2
        )
        image[masque_nouveau_divergent] = n
        masque_non_divergent = (np.abs(z) <= 2)
    return image


if __name__ == '__main__':
    pass
