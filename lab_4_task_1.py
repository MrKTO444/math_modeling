import numpy as np
a = [1,2,3,8]
def avrg(a):
  s = 0
  for i in range(len(a)):
    s = s + a[i]
  return s / len(a)

print(avrg(a))

  