# Highly divisible triangular number

current = 1
triangular = 0

while True:
    triangular = current * (current + 1) / 2
        
    num_divisors = 0
    for i in xrange(1, triangular+1):
        if triangular % i == 0:
            num_divisors += 1
        
    if num_divisors > 500:
        print triangular
        break

    current += 1
        