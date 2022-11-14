from math import sqrt

def dist_1(x, y):
    d = 0
    for i in range(len(x)):
        d += (x[i] - y[i]) ** 2
    return sqrt(d)

print(dist_1((1, 2), (3, 2)))