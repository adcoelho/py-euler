def fib(i):
    if i <= 1:
        return i
    return fib(i-1) + fib(i-2)

i = 0
result = 0
while fib(i) <= 4000000:
    if not fib(i) % 2:
        result = result + fib(i)
    i = i + 1
    
print result