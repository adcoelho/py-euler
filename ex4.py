def calculate_3digit_palindrome():
    res = 0
    for i in xrange(999, 100, -1):
        for j in xrange(999, 100, -1):
            if i*j > res:
                my_string = str(i*j)
                if my_string == my_string[::-1]:
                    res = i*j
    return res
        
print calculate_3digit_palindrome()
