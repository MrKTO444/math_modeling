x0 = 10

def move(t) :
  x = x0 * t
  return x

print(move(3))
print()
a = 'Good'

def my_func() :
  a = 'Bad'
  print(a)

my_func()
print(a)