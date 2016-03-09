primes = [2]

def check_and_add(p, primes):
    is_prime = 1
    for i in primes:
        if p == i or p % i == 0:
            is_prime = 0
    
    if is_prime:
        primes.append(p)


def get_primes(primes):
    p = 2
    while p < 2000000:
        check_and_add(p, primes)
        p += 1


get_primes(primes)
print sum(primes)