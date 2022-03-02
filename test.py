from src.nf04 import *


def ex_1_3():
    initialize("A", "B", "C")
    a, b, c = '', '', ''
    trace(0, locals())
    A = "T"
    trace(1, locals())
    B = "A"
    trace(2, locals())
    C = "G"
    trace(3, locals())
    A = C
    trace(4, locals())
    print(A + B + C)


def ex_1_7():
    initialize("texas", "oregon", "alaska", "indice", "utah")
    texas, oregon, alaska, indice, utah = (0, 0, 0, 0, 0)
    trace(0, locals())
    print("Entrer un entier")
    trace(1, locals())
    alaska = int(input())
    trace(2, locals())
    print("Entrer un réel")
    trace(3, locals())
    oregon = float(input())
    trace(4, locals())
    utah = 0
    trace(5, locals())
    for indice in range(1, alaska + 1):
        trace(6, locals())
        print("Entrer un réel")
        trace(7, locals())
        texas = float(input())
        trace(8, locals())
        if texas > oregon:
            trace(9, locals())
            utah += 1
            trace(10, locals())
    print(utah)
    trace(11, locals())
    stop()
    display()


if __name__ == "__main__":
    ex_1_3()
    stop()
    display()
