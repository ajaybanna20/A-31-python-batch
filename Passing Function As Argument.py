# Passing Functions as Arguments: 
    
Q1. 
def add(a, b):
 return a + b
def sub(a, b):
 return a - b
def mul(a, b):
 return a * b
def calc(f, x, y):
 return f(x, y)
print(calc(add, 12, 8))
print(calc(sub, 12, 8))
print(calc(mul, 12, 8))

Q2.
def add(a, b):
 return a + b
def sub(a, b):
 return a - b
def mul(a, b):
 return a * b
def calc(f, x, y):
 return f(x, y)
print(calc(add, calc(mul, 3, 4), calc(sub, 10, 6)))
print(calc(mul, calc(add, 2, 3), calc(add, 4, 5)))

Q3.
def square(n):
 return n * n
def double(n):
 return n * 2
def apply_twice(f, x):
 return f(f(x))
print(apply_twice(square, 2))
print(apply_twice(double, 7))
print(apply_twice(square, apply_twice(double, 1)))

Q4.
def square(n):
 return n * n
def double(n):
 return n * 2
def add_five(n):
 return n + 5
def apply_thrice(f, x):
 return f(f(f(x)))
print(apply_thrice(double, 3))
print(apply_thrice(add_five, 3))
print(apply_thrice(square, 2))

Q5.
def add_one(n):
 return n + 1
def double(n):
 return n * 2
def square(n):
 return n * n
def compose(f, g, x):
 return f(g(x))
print(compose(square, add_one, 4))
print(compose(add_one, square, 4))
print(compose(double, square, 3))
print(compose(square, double, 3))

Q6.
def double(n):
 return n * 2
def add_three(n):
 return n + 3
def repeat(f, x, times):
 for i in range(times):
  x = f(x)
 return x
print(repeat(double, 1, 6))
print(repeat(add_three, 10, 5))
print(repeat(double, 3, 0))

