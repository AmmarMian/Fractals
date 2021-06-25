# Visulisation de fractales : set de Mandelbrot

Le but de ce TP est de d'obtenir une visualisation du set de Mandelbrot qui est une fractale bien connue:

<figure>
<img src="https://upload.wikimedia.org/wikipedia/commons/2/21/Mandel_zoom_00_mandelbrot_set.jpg">
<figcaption>@Wikipedia</figcaption>
</figure>


La fractale est définie comme l'ensemble des points $c$ du plan complexe pour lesquels la suite de nombres complexes définie par récurrence par :
$$
\left \{\begin{array}{rcr} z_0 &=& 0 \\ z_{n+1} &=& z_n^2 + c \end{array}\right.
$$
est bornée.

Elle peut être tracée plus simplement à l'aide du résultat suivant:
> Si la suite des modules des $z_n$ est strictement supérieure à 2 pour un certain indice alors, cette suite est croissante à partir de cet indice, et elle tend vers l'infini.

Pour chacune des questions suivantes, des tests sont disponibles dans le dossier *tests/* afin de valider vos fonctions. Pour ce faire utiliser la commande suivante

```bash
nose2 -TODO
```

Il est toutefois nécéssaire de les tester manuellement à chaque fois en faisant des exemples dans le main du programme.

### Préliminaires : les nombres complexes

Dans un premier temps, nous avons besoin d'avoir une représentation des nobmre complexes afin de pouvoir effectuer les calculs des itérations de la suite de Mandelbrot. Pour ce faire, nous allons définir une classe.

1. Définir une classe **NombreComplexe** qui permet de représenter un nombre complexe à l'aide de deux attributs **real** et **imag** correspondant à la partie réelle et imaginaire avec le prototype suivant:

	```python
	class NombreComplexe:
	    """Classe représentant un nombre complexe."""
	    def __init__(self, real, imag):
	        # A remplir
	```
	
2. Ajouter à la classe la méthode **module** qui renvoie le module du nombre complexe représenté par la classe. On aura besoin de la fonction **sqrt** de la librairie math qui s'importe comme suit en préambule du code:

	```python
	from math import sqrt
	```

	

3. Surcharger la méthode **__str__** afin de pouvoir afficher le nombre complexe à l'aide de la fonction **print**.

4. Surcharger les méthodes pertinentes pour pouvoir additioner et multiplier des nombres complexes à l'aide des symboles + et *.

5. Surcharger la méthode pertinente pour pouvoir utiliser le symbole ** afin de réaliser la puissance d'un nombre complexe.

### Le plan complexe comme une image

Dans un second temps, pour pouvoir afficher le résultat de la fractale, nous avons besoin de représenter le plan complexe sous la forme d'une image (tableau bidimensionnel) de la manière suivante:

<figure>
<img src="./assets/pavage_complex.svg" style="float: center">
<figcaption>Pavage du plan complexe</figcaption>
</figure>

On considére un pavage du plan complexe à l'aide d'une grille de pixels où chaque pixel représente le nombre complexe situé au centre de celui-ci. Étant donné une image de taille $n_{colonnes}\times n_{lignes}$, et une résolution donnée par deux pas $pas_x$ et $pas_y$, un nombre complexe représenté par le pixel à la ligne $k$, et colonne $l$ est le suivant:
$$
c_{kl} = \left(l-\lfloor\frac{n_{colonnes}}{2}\rfloor\right)\times \frac{pas_x}{2} + i\times\left(k-\lfloor\frac{n_{lignes}}{2}\rfloor\right)\times \frac{pas_y}{2}.
$$


1. Implémenter la fonction **nombre_complexe** qui renvoie le nombre complexe à partir de l'indice du pixel avec le prototype suivant:

	```python
	def nombre_complexe(k, l):
	    
	    return ...
	```

2. Faire une fonction **grille_complexe** qui prend en entrée les paramètres $n_{lignes}$, $n_{colonnes}$, $pas_x$, $pas_y$ et qui renvoie un tableau bidimensionnel (liste de liste) correspondant à la grille de nombres complexes. Le prototype sera le suivant:

	```python
	def grille_complexe(n_lignes, n_colonnes, pas_x, pas_y):
	    
	    return ...
	```

	

### Visualisation à l'aide de la librairie matplotlib

Pour pouvoir visualiser la factrale, nous nous aidosn de la librairie **matplotlib** qui permet de tracer facilement des courbes et graphiques. Pour ce faire il faut ajouter la ligne d'importation suivante au préambule du code:

```python
import matplotlib.pyplot as plt
```

1. Expliquer ce que fait cette ligne.

2. À partir d'une grille contruite par la fonction **grille_complexe**, construire un tableau dans une variable nommée **tableau_module** contenant le module de chaque nombre complexe.

3. Afficher le résultat comme une image à l'aide des commandes suivantes:

	```python
	plt.figure()
	plt.imshow(tableau_module)
	plt.show()
	```

### Algorithme de calcul de la fractale

On va maintenant s'intéresser au problème principal à savoir trouver pour chaque nombre complexe de la grille, trouver si la suite à l'équation (1) converge. Pour cela on va réaliser un algorithme itératif qui va calculer les termes de la suite jusqu'à ce que la valeur du module est supérieure à 2 (suite diverge) ou jusqu'à un certain nombre $N$ défini par l'utilisateur (suite ne diverge pas).

1. Écrire une fonction **est_divergente** qui prend en paramètre un nombre complexe $c$, un nombre $N$ et qui renvoie $True$ si la suite diverge ou $False$ sinon. Le prototype est le suivant:

	```python
	def est_divergente(c, N):
	    
	    return ...
	```

	

2. Écrire une fonction **image_mandelbrot** qui calcule pour une image de taille et résolution données, une image avec comme valeur de pixel  255 si la suite converge et 0 sinon. Le prototype de la fonction est le suivant:

	```python
	def image_mandelbrot(n_colonnes, n_lignes, pas_x, pas_y, N):
	
		return ...
	```

3. Visualiser l'image à l'aide de **matplotlib**. Essayer avec différentes valeurs de $N$ et observer les différences.

### Utilisation le la librairie numpy

TODO
