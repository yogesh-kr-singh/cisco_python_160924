# def find_diff(a=1, b= 0):
def find_diff(a:int=1, b:int= 0)-> int:
    return a-b

print(find_diff (20,10))#10
print(find_diff (b=10,a=20))#10
print(find_diff (b=10))#-9
print(find_diff ())#1
print('==========================================================')

# ===================================================================================

def change_name(names, index, name):
    names [index] = name
    
names = ['rahul', 'modi']
print (names)

change_name (names,1,'modiji')
print(names)
print('==========================================================')

# ===================================================================================

def find_sum(first, second, *others):
    s = first + second
    if(len(others) > 0):
        for num in others:
            s += num
        # end for
    # end if
    return s
print(find_sum (20,10))#30
print(find_sum (first=50,second=40,))#90
print(find_sum (10,20,30,))#60
print('==========================================================')

# ===================================================================================

def find_sum(a,b, **others):
    s = a+b
    if(len(others) > 0):
        for key in others:
            s += others[key]
        # end for
    # end if
    # print (type(others))
    return s
print(find_sum (a=10,b=20))#30
print(find_sum (a=50,b=40,c=50))#90
print(find_sum (a=50,b=40,c=50, d=10))#60
print('==========================================================')

# ===================================================================================

def fact (N):
    if N <= 1:
        return 1
    # end if
    return N * fact(N-1)

print(fact(5))
print(fact(4))
print('==========================================================')

# ===================================================================================

import math
def is_prime(n):
    n_sqrt = int (math.sqrt(n))
    for I in range (2,n_sqrt+1):
        if n % I == 0:
            return False
        # end if
    # end for
    return True

print(is_prime(5))
print(is_prime(51))
print(is_prime(60))
print(is_prime(25))
print('==========================================================')
    
# ===================================================================================

