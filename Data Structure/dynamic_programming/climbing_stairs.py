# shortcuts to implement dp/recursion
# 1. Try to represent the problem in terms of index
# 2. Do all possible stuffs on that and index according to the problem statement
# 3. If the question says count all ways -> sum of all stuffs
#4. find minimum -> min(of all stuffs)


def fib(n):
    if n <= 3:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(3))

