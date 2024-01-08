def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

def list_fibonacci(n):
    fib_list = []
    for i in range(n):
        fib_list.append(fibonacci(i))
    return fib_list
print(list_fibonacci(10))