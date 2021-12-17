import numpy as np
a=np.zeros((1 , 5 ))
for i in range(5):
  a[0,i] = int(input())

def mult(a):
  s = 1
  for t in range(5):
    s = s * a[0,t]
  return s

print(mult(a))
  
  
