nums = [1, 2, 3]
# for num in nums:
#     print(num)

print(dir(nums))

i_nums = iter(nums)
print(i_nums)
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))

# ITERATORS

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break


class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1



my_range = my_range(1, 5)
for num in my_range:
    print(num)
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))

# iterables
# Just how does for.... in work?
# what kinds of things can you iterate over?
# How does iteration operate?
# How can you write your own iterables?

# the iterator protocol is a loose definition of methods that an object must implement to be considered an iterable
# __iter__() and __next__()
# __iter__() returns an iterator object
# __next__() returns the next value from the iterator

# iterables and iterators
# iterables are objects that can be iterated over
# Commin built-in iterables are:
# lists, tuples, dictionaries, sets, strings

# how does for work?
# python's for command uses the iterator protocol to iterate over an iterable
# iterators are objects that implement the iterator protocol

#A for loop calls iter() on the iterable to create an iterator
# the iterator object is responsible for returning each item to the loop
# A for loop call next() on the iterator to get the next item
# the iterator returns the next item or raises StopIteration when there are no more items





