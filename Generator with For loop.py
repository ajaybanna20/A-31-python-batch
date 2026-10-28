# Q1. Write one_two_three() that yields 1, 2, 3 using three separate yield statements.
def one_two_three():
    yield 1
    yield 2
    yield 3

gen = one_two_three()
print(next(gen), next(gen), next(gen))

# Q2. Write count_down(n) that yields n down to 1. Print the values with a for loop.
def count_down(n):
    while n >= 1:
        yield n
        n -= 1

for x in count_down(3):
    print(x)
 

# Q3. Write multiples(k, count) that yields the first count multiples of k.
def multiples(k, count):
    for i in range(1, count + 1):
        yield k * i

for x in multiples(3, 4):
    print(x)
 
# Q4. Write repeat(value, times) that yields value exactly times times.
def repeat(value, times):
    for i in range(times):
        yield value

for x in repeat("hi", 3):
    print(x)
 
# Q5. Write chars(text) that yields each character of a string one at a time.
def chars(text):
    for char in text:
        yield char

gen = chars("abc")
print(next(gen), next(gen), next(gen))

# Q6. Write odds(limit) that yields all odd numbers from 1 up to and including limit.
def odds(limit):
    for n in range(1, limit + 1):
        if n % 2 == 1:
            yield n

for x in odds(7):
    print(x)
    
# Q7. Write long_words(words, min_len) that yields only the words with at least min_len characters.
def long_words(words, min_len):
    for word in words:
        if len(word) >= min_len:
            yield word

for w in long_words(["cat", "elephant", "dog", "giraffe"], 4):
    print(w) # elephant giraffe
    
# Q8. Write doubled(numbers) that yields each number multiplied by 2
def doubled(numbers):
    for number in numbers:
        yield number * 2
        
for x in doubled([1, 2, 3]):
    print(x) # 2 4 6    
    

