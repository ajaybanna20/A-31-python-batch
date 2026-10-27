# Generator and yield function in python

def value():
 yield 95
 yield 85
 yield 75

g = value()
print(next(g))
print(next(g))
print(next(g))

# Q1 need to know basic of generator and yield function

marks =[95,89,90,76,64,54,34]

def values(marks):
    for mark in marks:
        yield str(mark)+"%"
        
g = values(marks)
print(next(g))
print(next(g))
print(next(g))

# Q2 one at a time we can get the value from generator function

data = ["yash", "yogesh", "naveen", "rishi", "pranav"]

def greet(data):
    for name in data:
        yield "Hello "+name

g = greet(data)
print(next(g))
print(next(g))
print(next(g))

# Q3 find prime number using generator function

ranges = [100000, 679890809111, 127823888893733672632 ]

def prime_number(ranges):
    for top in ranges:
        primes = []
        counter = 0
        for x in range(2,int((top)**0.5)):
            
            if top%x == 0:
                counter+= 1
                break
            if counter == 0:
                primes.append(top)
            yield primes
gre