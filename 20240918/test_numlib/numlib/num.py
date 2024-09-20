import math

def is_odd(n):
    return n % 2 ==1

def is_even(n):
    return n % 2 ==0

def is_prime(n):
    n_sqrt = int (math.sqrt(n))
    for I in range (2,n_sqrt+1):
        if n % I == 0:
            return False
        # end if
    # end for
    return True