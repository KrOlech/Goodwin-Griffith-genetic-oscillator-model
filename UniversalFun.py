import numpy as np
from numba import jit
from scipy.integrate import odeint, solve_ivp

@jit(nopython=True)
def xDot(x, y, alfa):
    return - alfa * x + y


@jit(nopython=True)
def yDot(x, beta):
    x2 = x * x
    return x2 / (1 + x2) - beta


def dfun(r, t, alfa, beta):
    tab = np.zeros((2, 2))
    tab[0, 0] = - alfa
    tab[0, 1] = 1
    tab[1, 0] = 2 * r[0] / pow(r[0] * r[0] + 1, 2)
    tab[1, 1] = - beta

    return tab


def model(t, r, alfa, beta):
    return [xDot(*r, alfa), yDot(r[0], beta)]