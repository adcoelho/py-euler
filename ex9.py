a = 0
b = 0
c = 0

for a in xrange(0, 999):
    for b in xrange(a, 999):
        c = 1000 - a - b
        if a*a + b*b == c*c and c > b:
            print a*b*c