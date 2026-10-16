#Q7. Format prices Format each price as a dollar string with exactly two decimals.
prices = [5, 12.5, 100]

def convert(n):
    return f"${n:.2f}"
    
res = list(map(convert, prices))
print(res)

#Q8. Two lists at once map() can take more than one iterable. Add the matching items of the two lists together
a = [1, 2, 3]
b = [10,20,30]

def matcher(element1, element2):
    return element1 + element2

res = list(map(matcher, a, b))
print(res)
