# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import random
import matplotlib.pyplot as plt
import numpy as np


def show_plot(_f, ab, title_f, suptittle_f):
    x = np.linspace(ab[0] - 10, ab[len(ab) - 1] + 10)
    y = [_f(i) for i in x]
    plt.xlabel("x")
    plt.ylabel(title_f)
    plt.suptitle(suptittle_f)
    plt.plot(x, y)
    plt.show()


def show_hist(d, n):
    db = dict(zip(d, n))
    plt.bar(db.keys(), db.values(), color='g', alpha=0.5)
    plt.show()


def f(x):
    if 0 <= x <= 8:
        return x ** (1 / 3) / 12
    else:
        return 0


def F(x):
    if x < 0:
        return 0
    elif 0 <= x <= 8:
        return 1 / 12 * 3 / 4 * x ** (4 / 3)
    else:
        return 1


def invF(x):
    if x < 0:
        return 0
    if 0 <= x <= 8:
        return (16 * x) ** (3 / 4)
    else:
        return 1


def matv(x, n):
    S = 0
    for i in range(len(x)):
        S += x[i] * n[i]
    return S


def disp(x, n):
    S = 0
    for i in range(len(x)):
        S += (x[i] ** 2) * n[i]
    return S


def new_F(x, ab, w):
    for i in range(len(w)):
        if ab[i - 1] < x <= ab[i]:
            return w[i]


def new_db(f, n):
    dbi = []
    for i in range(len(f)):
        dbi.append(max(i / n - f[i], f[i] - (i - 1) / n))
    db = max(dbi)
    return db


def new_u():
    u = []
    for i in range(N):
        u.append(random.random())
    return u


def new_x(u):
    x = []
    for i in range(N):
        x.append(invF(u[i]))
    return x


def new_ab(k, h):
    ab = []
    for i in range(k + 1):
        ab.append(i * h)
    return ab


def new_n(k, N, ab, x):
    n = []
    for i in range(k):
        count = 0
        for j in range(N):
            if ab[i - 1] < x[j] <= ab[i]:
                count = count + 1
        n.append(count)  # кол-во значений случайной величины
    return n


def new_w(n, N):
    w = []
    for i in range(len(n)):
        w.append(n[i] / N)
    return w


def new_x_in_ab(ab):
    x = []
    for i in range(k):
        x.append((ab[i - 1] + ab[i]) / 2)
    return x


def new_f(x):
    f = []
    for i in range(1, len(x)):
        f.append(F(x[i]))
    return f


if __name__ == '__main__':
    epsi = []
    xi = []
    ui = []
    ni = []
    pi = []
    wi = []
    N = 90
    q = 12
    ab = []

    ui = new_u()
    xi = new_x(ui)
    max_xi = max(xi)
    min_xi = min(xi)

    k = round(1 + math.log2(N)) + 1  # Кол-во интервалов
    h = (max_xi - min_xi) / k  # Шаг
    ab = new_ab(k, h)

    xi.sort()
    ni = new_n(k, N, ab, xi)
    wi = new_w(ni, N)

    n_hist = ni
    for i in range(len(n_hist)):
        n_hist[i] *= 1 / (N * h)

    xi = new_x_in_ab(ab)
    x2b = matv(xi, ni) / N  # выборочная случайная величина
    dispb = (disp(xi, ni) - x2b ** 2) / N
    sigmb = dispb ** (1 / 2)
    fi = new_f(xi)
    db = new_db(fi, N)
    lambda_b = N ** (1 / 2) * db
    alpha = F(0.3)
    k = 1 - alpha

    show_hist(ab, n_hist)

    if lambda_b > k:
        print("Yes")
    else:
        print("No")

    show_plot(F, ab, "F(x)", "Функция распределения")
    show_plot(f, ab, "f(x)", "Функция плотности")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
