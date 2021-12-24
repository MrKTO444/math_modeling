a = float(input("Введите положительное число - "))
n = int(input("Введите целое число - "))

def stpn(a,n) :
  if n < 0 :
    a = 1.0 / a
    n = -n
    print(a)
  x = 1
  while n > 0 :
    x = x*a
    n = n - 1
  return(x)
  
print(stpn(a,n))