
def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)

    return inner_func

my_func = outer_func()
print(my_func.__name__)
my_func()

# a closure is an inner function that remembers and has access to variables in the local scope in which it was created
# even after the outer function has finished executing

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

my_func = outer_func('Hi')
hello_func = outer_func('Hello')

my_func()
hello_func()

# a closure closes over the free variables from their environment