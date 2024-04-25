# write fibinacci number using recursion

def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(4))
# time complexity: O(2n)