from concurrent.futures import ThreadPoolExecutor

import matplotlib.pyplot as plt
from numpy import linspace
from scipy.integrate import solve_ivp

from UniversalFun import model


def main(r):
    sol = solve_ivp(model, [0, 100], r[1], args=r[0], dense_output=True, method="BDF")

    return sol['t'], sol['y']


def multiThredFunInstaPlot(r):
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i, result in enumerate(executor.map(main, r)):
            plt.plot(result)
            plt.savefig(str(r[i]) + '.png')
            plt.cla()
            plt.close()


def multiThredFun(r, pltx, plty, pltxy):
    with ThreadPoolExecutor(max_workers=10) as executor:
        for result in executor.map(main, r):
            t, y = result
            pltx.plot(t, y[1])
            plty.plot(t, y[0])
            pltxy.plot(y[0], y[1])


def staticAB(a=1.0, b=1.0, n=linspace(0, 10, 20), l=linspace(0, 10, 20)):
    r = []

    for y in n:
        for x in l:
            r.append(((a, b), (x, y)))

    pltX, axX = plt.subplots()
    pltY, axY = plt.subplots()
    pltXY, azXY = plt.subplots()

    multiThredFun(r, axX, axY, azXY)

    axX.set_title(r"$\alpha$ = " + str(a) + r"; $\beta$ = " + str(b))
    pltX.savefig(f"DuzyZakres_2={a}_b={b}_X.png")

    axY.set_title(r"$\alpha$ = " + str(a) + r"; $\beta$ = " + str(b))
    pltY.savefig(f"DuzyZakres_2={a}_b={b}_Y.png")

    azXY.set_title(r"$\alpha$ = " + str(a) + r"; $\beta$ = " + str(b))
    pltXY.savefig(f"DuzyZakres_2={a}_b={b}_XY.png")


if __name__ == "__main__":
    a = float(input("podaj a: "))
    b = float(input("podaj b: "))
    x0 = float(input("podaj x0: "))
    x1 = float(input("podaj x1: "))
    nx = int(input("podaj ilosc pkt na x: "))
    y0 = float(input("podaj y0: "))
    y1 = float(input("podaj y1: "))
    ny = int(input("podaj ilosc pkt na y: "))

    n = linspace(x0, x1, nx)
    l = linspace(y0, y1, ny)
    staticAB(a, b, n, l)
