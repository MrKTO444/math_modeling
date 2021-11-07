a = float(input('Введите коэффицент: '))
b = float(input('Введите коэффицент: '))
c = float(input('Введите коэффицент: ')) 

D = (b**2) - 4*a*c
print(f' Дискриминант: {D}')
if D < 0:
  print('Нет корней')
elif D == 0:
  x = -b // (2*a)
  print(f' Один корень: {x}')
elif D > 0:
  y = (-b + (D**0.5)) // (2*a)
  z = (-b - (D**0.5)) // (2*a)
  print(f'Два корня: {y,z}')