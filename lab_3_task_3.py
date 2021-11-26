import numpy as np
from const import g

a = np.zeros((6 , 3))

x0 = float(input('Введите начальное значение (X) '))
y0 = float(input('Введите начальное значение (Y) '))
v0 = float(input('Введите начальное значение скорости '))

for t in range(0 , 6):
  x = x0 + (v0 * t)
  y = y0 + (v0 * t) - (g * (t**2) / 2)
  a[t,0] = t
  a[t,1] = x
  a[t,2] = y

print('    t     x     y')
print(a)
