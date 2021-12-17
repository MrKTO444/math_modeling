import numpy as np
a = int(input('выберите фигуру (1) Круг (2) Прямоугольник (3) Треугольник ' ))

def piska(a):
  if a==1:
    R = float(input('Введите радиус '))
    s = np.pi  * (R**2)
    print(s)
  
  elif a==2:
    a1 = float(input('введите длину первой стороны '))
    a2 = float(input('Введите длину второй стороны '))
    s = a1 * a2
    print(s)

  elif a==3:
    h = float(input('Введите длину высоты '))
    A = float(input('Введите длину основания '))
    s = (h * A) / 2 
    print(s)
  

piska(a)