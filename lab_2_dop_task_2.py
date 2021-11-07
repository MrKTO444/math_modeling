a = float(input('Введите длину первого отрезка: '))
b = float(input('Введите длину второго отрезка: '))
c = float(input('Введите длину третьего отрезка: '))

if (a + b) < c or (a +c) < b or (b+c) < a:
  print('Треугольник не существует')
else:
  if a != b and a != c and b != c:
    print('Разносторонний')
  elif a == b and b == c and a == c:
    print('Равносторонний')
  elif a == b or b ==c or c == a:
    print('Равнобедеренный')
