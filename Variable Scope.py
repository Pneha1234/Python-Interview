'''
LEGB
local, enclosing, global, built-in
'''

#local is which are defined inside a function
#enclosing is which are defined inside a function but are enclosed in a function
#global is which are defined at the top level of a module or declared global in a def within the module
#built-in are the names preassigned in Python

import builtins

# print(dir(builtins))

def my_min():
    pass

m = min([5, 1, 4, 2, 3])
print(m)
# x = 'global x'


def test(z):
    x = 'local x'
    # print(y)
    print(z)

test('local z')
# print(z)

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()