primes = [2]

def is_prime(num):
    for p in primes:
        if p == num or num % p == 0:
            return 0
    return 1

def calc_prime_number(nth):
    num = 2
    count = 0
    while count < nth:
        if is_prime(num):
            primes.append(num)
            count += 1
        num += 1
    return primes[nth-1]
    
print calc_prime_number(10001)
