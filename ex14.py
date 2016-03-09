# Longest Collatz sequence

def collatz(i, chain_length):
    chain_length += 1
    if i == 1:
        return chain_length
    elif i % 2 == 0:
        return collatz(i/2, chain_length)
    else:
        return collatz(3 * i + 1, chain_length)
        
max = 0
starting_num = 0
for i in xrange(1, 1000000):
    curr_value = collatz(i, 0)
    if curr_value  > max:
        max = curr_value
        starting_num = i
        
print starting_num