from numpy import sqrt, arange
import matplotlib.pyplot as plt
from numba import jit


@jit(nopython=True)
def pkt1X(m4ab, a, b):
    return - (m4ab - 1) / (a * b)


@jit(nopython=True)
def pkt1Y(m4ab, a, b):
    return - (m4ab - 1) / b


@jit(nopython=True)
def pkt2X(m4ab, a, b):
    return (m4ab + 1) / (a * b)


@jit(nopython=True)
def pkt2Y(m4ab, a, b):
    return (m4ab + 1) / b


def wykres(f1, f2, name):
    for a in arange(0.01, 10, 0.01):
        for b in arange(0.01, 10, 0.01):
            m4ab = sqrt(1 - 4 * a * a * b * b)
            b2 = 2 * b
            plt.plot(f1(m4ab, a, b2), f2(m4ab, a, b2), marker='.', c='r')

    plt.savefig(name + '.png')
    plt.cla()
    plt.close()


def main():
    wykres(pkt1X, pkt1Y, 'ujemne')
    wykres(pkt2X, pkt2Y, 'dodatnie')


if __name__ == "__main__":
    main()
