def mem_test():
    x = 300
    y = 300
    print(id(x))
    print(id(y))
    print(x is y)


mem_test()


# A way for a program to automatically release memory when the object taking up that space is no longer in use -GIL
# Two main types of memory management in Python:
# 1. Reference counting
# 2. Tracing garbage collection

# Reference counting:
# - Each object has a reference count that tracks how many references point to it.
# - When the reference count reaches zero, the object is deallocated.
# - Cascading deletion: If an object has references to other objects, those references are also decremented.
# - Circular references can cause memory leaks, as reference counts may not reach zero.
# - Python uses a cyclic garbage collector to handle circular references.
# - The cyclic garbage collector periodically checks for circular references and deallocates them.
# - Reference counting is efficient for most cases, but can be slow for circular references.
# - Example of circular reference:
#   class Node:
#       def __init__(self, value):
#           self.value = value
#           self.next = None
# a = Node(1)
# b = Node(2)
# a.next = b
# b.next = a
# - here, a and b reference each other, creating a circular reference.
# - This can lead to memory leaks if not handled properly.
# - Python's cyclic garbage collector works as follows to deallocate circular references:
#   - The cyclic garbage collector periodically checks for circular references.
#   - It uses a mark-and-sweep algorithm to identify and collect unreachable objects.
#   - The mark phase marks all reachable objects, while the sweep phase deallocates unmarked objects.
#   - The cyclic garbage collector is not perfect and may not catch all circular references.
#   - It is important to avoid circular references when possible.
# - Here in the above example, the cyclic garbage collector will identify that a and b are part of a circular
# reference and will deallocate them when they are no longer reachable.

# Reference counting is not usually thread safe, as multiple threads can modify the reference count of an object
# at the same time.
# to avoid this python uses a Global Interpreter Lock (GIL) to ensure that only one thread can execute Python bytecode
# at a time.


# Tracing garbage collection:# - Tracing garbage collection is a technique used to identify and collect
# unreachable objects in memory.
# Mark and sweep algorithm:
# - The mark phase marks all reachable objects, while the sweep phase deallocates unmarked objects.
# - The mark phase starts from a set of root objects and traverses the object graph, marking all reachable objects.
# - The sweep phase deallocates all unmarked objects.
# - The tracing garbage collector is more efficient than reference counting for circular references.

#- Generational garbage collection:
# - The generational garbage collector divides objects into generations based on their age.
# - New objects are allocated in the youngest generation, while older objects are promoted to older generations.
# - The garbage collector collects the youngest generation more frequently than older generations.
# - This is based on the observation that most objects are short-lived and can be collected quickly.
# - Only contaoiner objecrs with a refecount greater than 0 will be stored in a generational list
#- what happens during a generational garbage collection cycle?
# - Python makes a list of objects to discard
# - It runs an alogorithm to detetct references cycles
# - If an object has no outside referencesm add it to the discard list
# - when the cycle is done , free up the discard list
# - After a garbage collection cycle objects that survived will be promited to the next generation
# - The garbage collector uses a threshold to determine when to collect each generation.
# - objects in the last generation stay there as the program exectutes


# Python instances have a dict of values
class Dog():
    pass


buddy = Dog()
buddy.name = "Buddy"
buddy.age = 5
print(buddy.__dict__)


# Python uses a dictionary to store instance variables and their values.
# This allows for dynamic creation and modification of instance variables.
# To prevent this we use __slots__ to define a fixed set of instance variables.
class Dog():
    __slots__ = ('name', 'age')
    pass

print("____________________________")
buddy = Dog()
buddy.name = "Buddy"
buddy.age = 5
print(type(buddy.__slots__))
print(id(buddy.name))

buddy2 = Dog()
buddy2.name = "Buddy2"
print(type(buddy2.__slots__))
print(id(buddy2.name))
# __slots__ is a way to define a fixed set of instance variables for a class.
# This can help reduce memory usage and improve performance.
# Tuples are immutable, while lists are mutable.

import sys

sys.getsizeof(dict())
sys.getsizeof(tuple())

# when to use slots?
# - When you have a large number of instances of a class and want to reduce memory usage.
# - When you want to prevent dynamic creation of instance variables.

# weak references:
# - A weak reference is a reference to an object that does not increase its reference count.
# - This allows the object to be garbage collected even if there are weak references to it.
# - Weak references are useful for caching and avoiding memory leaks.
# - Weak references are created using the weakref module.
import weakref


class Dog():
    pass


buddy = Dog()
buddy.name = "Buddy"
buddy.age = 5
print(buddy.__dict__)
# Create a weak reference to the buddy object
weak_buddy = weakref.ref(buddy)
print(weak_buddy())

# what a GIL is?
# - The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects,
# preventing multiple threads from executing Python bytecodes at once.
# - This means that only one thread can execute Python bytecode at a time, even on multi-core systems.
# - The GIL is necessary because Python's memory management is not thread-safe.
# - The GIL can be a bottleneck for CPU-bound programs, as it prevents true parallelism.
# - The GIL can be released during I/O operations, allowing other threads to run.



