# using Map find out the square of each element of tuple 
def square(t):
  return list(map(lambda x:x**2, t))
# using map find out the cube of each element of set
def cubde(s):
  return list(map(lambda x:x**3, s))
# using map increase each element by 50. element are in a list
def increase(l):
  return list(map(lambda x:x+50, l))
# using map floor divide each element by 4 in a tuple
def divide(t):
  return list(map(lambda x:x//4, t))
# using map decrease each number by half its value in a set
def decrease(s):
  return set(map(lambda x:x/2, s))
  # using map convert each sring to uppercase in a list
def uppearcase(1):
  return list(map(lambda x: x.upper(), 1))
# using map find the length of each string in a tuple
def length(t):
  return list(map(lambda x: len(x), t))
data = [5,4,2,1,7,8,9,10,11,12,15]

def is_even(n):
  if n%2==0:
    return True
  else:
    return False
res =list(filter(is_even, data))
print(res)