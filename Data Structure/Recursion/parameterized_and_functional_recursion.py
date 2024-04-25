# sum of first N numbers-solve using parameterized and functional recursion

# [1,2,3,4,5,6,7]->[n+n+1]

#parameterized way
def sum(i, result):
    if i < 1 :
        print(result)
        return
    else:
        sum(i-1, result+i)

# print(sum(3,0))

#functional way
def functional_sum(n):
    if n==0:
        return 0
    else:
        return n + functional_sum(n-1)

# print( functional_sum(3))

# factorial of n; n = 3 [1*2*3] =6

def factorial_functional_way(n):
    if n == 1:
        return 1
    else:
        return n * factorial_functional_way(n-1)

print(factorial_functional_way(3))
