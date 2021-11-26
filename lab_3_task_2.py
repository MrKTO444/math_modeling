import numpy as np

H = 100
a = np.pi / 3
b = np.radians(30)
from const import g

V = np.sqrt(g * H * (np.tan(b) ** 2)) / (2 * (np.cos(a) **2) * (1 - (np.tan(b)) * (np.tan(a))))
print(V)

T = 200
E = 300
from const import k, h, e

N = (2 / (np.pi) ** 0.5) * (h / ((k*T) ** (3/2))) * (e ** (-E / (k*T))) * (E ** (T/2))
print(N)