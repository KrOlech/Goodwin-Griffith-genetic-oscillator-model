from scipy.optimize import root


def fun1(a,b):

    ab = a * b
    a2 = a * a
    b2 = b * b
    a3 = a2 * a
    b3 = b2 * b
    a5 = a2 * a3
    b5 = b2 * b3
    ab55 = a5 * b5
    ab32 = a3 * b2
    ab33 = a3 * b3
    a8 = 8 * a
    b8 = 8 * b
    a2_16 = 16 * a2
    ab128 = 128 * ab
    ab32_16 = 16 * ab32
    pierwiastek = pow(1 - 4 * a2 * b2, 1 / 2)
    iner = (-ab32_16 - a2_16 * b3 - a8 * pierwiastek - b8 * pierwiastek + a8 + b8)
    return (ab32_16
            + a2_16 * b3
            + a8 * pierwiastek
            + b8 * pierwiastek +
            pow(iner * iner
                - 4 * (1024 * ab55
                       - 768 * ab33
                       - ab128 * pierwiastek
                       - 256 * ab55 * pierwiastek
                       + 512 * ab33 * pierwiastek
                       + ab128)
                - a8 - b8
                , 1 / 2)
            / (2 * pow(2 - 2 * pierwiastek, 1 / 2)))


def main():
    print(root(fun1, 10, 10))


if __name__ == "__main__":
    main()
