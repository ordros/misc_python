from math import sqrt


def g_pi(n):
    a = [1]
    b = [1 / sqrt(2)]
    t = [0.25]
    p = [1]
    i = 0
    while i < n:
        a.append((a[i] + b[i]) / 2)
        b.append(sqrt(a[i] * b[i]))
        t.append(t[i] - p[i] * (a[i] - a[i + 1]) ** 2)
        p.append(2 * p[i])
        i += 1
    f = lambda x: x[len(x) - 1]
    print f(a), f(b), f(t), f(p)
    print((f(a) + f(b)) ** 2) / (4 * f(t))

g_pi(input())
