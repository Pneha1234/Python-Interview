def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()
# decorators are functions that take another function as an argument, add some kind of functionality and
# then return another function
# decorators are used to add functionality to an existing function

def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('display function ran')

# decorated_display = decorator_function(display)
# decorated_display()

display()