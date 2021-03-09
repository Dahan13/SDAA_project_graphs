# -*- coding: utf-8 -*-
"""

.. moduleauthor:: Valentin Emiya
"""
import numpy as np
import line_profiler


# On crée 3 fonctions à chronométrer
def f(A, B):
    """ Produit de deux matrices avec np """
    return np.dot(A, B)


def g(A, B):
    """ Produit de deux matrices avec 3 boucles  """
    assert A.shape[1] == B.shape[0]

    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            for k in range(A.shape[1]):
                C[i, j] += A[i, k] * B[k, j]
    return C


def h(A, B):
    """ Produit de deux matrices avec 2 boucles  """
    assert A.shape[1] == B.shape[0]

    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            C[i, j] = np.vdot(A[i, :], B[:, j])
    return C


# Une classe dont on veut chronométrer une méthode
class MatMul:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def dot(self):
        A = self.A
        B = self.B
        x = f(A, B)
        y = g(A, B)
        z = h(A, B)
        print(np.max(np.abs(x - y)))
        print(np.max(np.abs(x - z)))


# La fonction principale à lancer
def main(params, n_runs=3):
    # On peut faire plusieurs appels (plusieurs runs) afin d'avoir des temps
    # moyens plus fiables
    n1, n2, n3 = params['dims']
    for i in range(n_runs):
        print('Run', i)
        A = np.random.randn(n1, n2)
        B = np.random.randn(n2, n3)
        Cf = f(A, B)
        Cg = g(A, B)
        Ch = h(A, B)
        m = MatMul(A, B)
        m.dot()


if __name__ == '__main__':
    # Les paramètres de la fonction principale
    my_params = {
        'dims': (100, 150, 150),
    }

    # Création d'un objet line_profiler
    lp = line_profiler.LineProfiler()
    # ajout des fonctions et méthodes à chronométrer
    lp.add_function(f)
    lp.add_function(g)
    lp.add_function(h)
    lp.add_function(MatMul.dot)
    # ajout de la fonction principale et de ses paramètres
    lp_wrapper = lp(main)
    lp_wrapper(my_params)

    # affichage des résultats en choisissant l'unité de temps (1e-3 = 1 ms)
    lp.print_stats(output_unit=1e-3)

    # sauvegarde des résultats dans un fichier pour un affichage ultérieur
    stats_file = 'profile_demo.lprof'
    lp.dump_stats(stats_file)
    print('Run the following command to display the results:')
    print('$ python -m line_profiler {}'.format(stats_file))

