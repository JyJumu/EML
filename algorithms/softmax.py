"""
Module: algorithms/softmax.py
Description: Implementación del algoritmo ucb1 para el problema de los k-brazos.

Author: Jesús Verdú Chacón & Jorge López Abad
Email: jesus.v.c@um.es & jorge.lopeza@um.es
Date: 2025/01/29

This software is licensed under the GNU General Public License v3.0 (GPL-3.0),
with the additional restriction that it may not be used for commercial purposes.

For more details about GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.html
"""

import numpy as np
import math

from algorithms.algorithm import Algorithm

class Softmax(Algorithm):

    def __init__(self, k: int, tau: float = 1):
        """
        Inicializa el algoritmo UCB.

        :param k: Número de brazos.
        :param tau: Parámetro del algoritmo.
        :raises ValueError: Si tau no es mayor que 0.
        """
        assert 0 < tau, "El parámetro tau debe se mayor que 0."

        super().__init__(k)
        self.tau = tau

    def select_arm(self) -> int:
        """
        Selecciona un brazo basado en la política Softmax.
        :return: índice del brazo seleccionado.
        """

        prob = np.zeros(self.k, dtype=float)
        denominador = 0
        for i in range(self.k):
            denominador = math.e**( self.values[i] / self.tau)
            
        for i in range(self.k):
            prob[i] = (math.e **(self.values[i] / self.tau)) / denominador

        chosen_arm = np.random.choice(range(k), size=1, p=prob)
        chosen_arm = sum(chosen_arm)

        return chosen_arm
