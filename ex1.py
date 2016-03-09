# Find the sum of all the multiples of 3 or 5 below 1000.

def printer():
    for i in xrange(1000):
        if not i % 3 or not i % 5:
            yield i
            
            
print sum(printer())