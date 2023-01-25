import matplotlib.pyplot as plt

from scipy.integrate import odeint, solve_ivp
from numpy import linspace
from concurrent.futures import ThreadPoolExecutor
from UniversalFun import model


def mainOneel(r):
    sol = solve_ivp(model, [0, 10], r[1], args=r[0], dense_output=True, method="BDF")

    return sol['y'], r[2]


def multiThredFunOneEl(r):
    x = []
    y = []
    t = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        for result in executor.map(mainOneel, r):
            x.append(result[0][0][-1])
            y.append(result[0][1][-1])
            t.append(result[1])

    return x, y, t


def bifurkacja(aw, bw, xw, yw, zmienna='a', offset=0.5, npkt=10000):
    A, B, X, Y = [aw], [bw], [xw], [yw]
    if zmienna == 'a':
        A = linspace(A[0] - offset, A[0] + offset, npkt)
        tabelka = [(A, "a")]
    elif zmienna == 'b':
        B = linspace(B[0] - offset, B[0] + offset, npkt)
        tabelka = [(B, "b")]
    elif zmienna == 'ab':
        A = linspace(A[0] - offset, A[0] + offset, npkt)
        B = linspace(B[0] - offset, B[0] + offset, npkt)
        tabelka = [(A, "a"), (B, "b")]
    else:
        print(f"Podano nie obslugiwany parametr {zmienna}, dopuscalne wartosci to: \"a\" \"b\"  \"ab\"")
        return

    z = []

    for i, a in enumerate(A):
        for j, b in enumerate(B):
            for k, x in enumerate(X):
                for l, y in enumerate(Y):
                    z.append(((a, b), (x, y), (i, j, k, l)))

    _x, y, time = multiThredFunOneEl(z)


    for w, name in zip([_x, y], ["x", "y"]):
        for t in tabelka:
            plt.plot(t[0], w, linewidth=0, markersize=1, marker='.')
            plt.savefig(f"a={aw}, b={bw}, x={xw}, y={yw}, z={zmienna}, i= {t[1]}, j= {name}.png")
            plt.cla()
            plt.close()


if __name__ == "__main__":
    a = float(input("podaj a0: "))
    b = float(input("podaj b0: "))
    x0 = float(input("podaj x0: "))
    y0 = float(input("podaj y0: "))

    zmienna = input("podaj woku ktorej zmiennej szukamy Bifurkacji\n Dopuszcalne wartosci \"a\" \"b\"  \"ab\": ")

    offset = float(input("podaj plus minus ile bedziemy zmieniac zakres parametru: "))

    n = int(input("podaj ile pktow w tym zakresie chcemy rozwazyc: "))

    bifurkacja(a, b, x0, y0, zmienna, offset, n)
