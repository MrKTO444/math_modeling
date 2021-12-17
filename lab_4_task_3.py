g = 9.8
def enrg(m , h , v):
  E = ((m * (v**2)) / 2) + (m * g * h)
  return E

print(enrg(3,5,6))
