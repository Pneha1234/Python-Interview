# data structures are containers storing data in a specific memory layout
# Array -> [298, 305,320, 301, 292]
# Big O notation is used to measure how running time or space requirements for your program grows as input size grows
# def foo(arr): size(arr)->100-> 0.22 milliseconds
#               size(arr)-> 1000 -> 2.310 milliseconds
# time = a*n+b-> 1. keep fastest growing term-> time= a*n-> 2. drop constants -> time =O(n)

def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n * n)
    return squared_numbers


numbers = [2, 5, 8, 9]
get_squared_numbers(numbers)


# def foo(a): size(arr) -> 100-> 0.22 milliseconds
#             size(arr) -> 1000 -> 0.23 milliseconds
# time =a ->1.keep fastest growing term,2. Drop Constants-> time =O(1)

def find_first_pe(prices, eps, index):
    pe = prices[index] / eps[index]
    return pe

# O(n2) -> a*n2 +b
numbers1 = [3,6,2,4,3,6,8,9]
for i in range(len(numbers1)):
    for j in range(i+1 ,len(numbers1)):
        if numbers1[i] == numbers1[j]:
            print(numbers1[i] + "is a duplicate")
            break


# time = a*n2 +b*n +c ->O(n2)

numbers2 = [3,6,2,4,3,6,8,9]
duplicate = None
for i in range(len(numbers2)):
    for j in range(i+1, len(numbers2)):
        if numbers2[i] == numbers2[j]:
            duplicate = numbers2[i]
            break

for i in range(len(numbers2)):
    if numbers2[i] == duplicate:
        print(i)

# space complexity
# a = [4,9,15,21,34,57,68,91] ---> search for 68
a = [4, 9, 15, 21, 34, 57, 68, 91]
for i in range(len(a)):
    if a[i] == 68:
        print(i)
# solving it using binary search
#[4,9,15,21,34,57,68,91] --> search for 68
# [4,9,15,21,34,57,68,91]--> 21 --> iteration 1 = n/2
# [34,57,68,91]---> 57 ---> iteration 2 = (n/2)/2 =n/2^2
# [68,91]--->68---> iteration 3 = (n/2^2)/2 = n/2^3
# iteration k =n/2^k----> 1 =n/2^k ----> n = 2^k---> log2n = log2 2^k---> log2n = k log2 2-->k =logn-->O(n)

# k = O(logn)-> log2 8 ---> log2 2^3 -> 3*log2 2---> 3 iteration
# Space Complexity:
# SC is also calculated in BigO notation itslef
#
# There are two spaces.
# 1.Auxilalry Space:The space taken to solve problem.
# 2.Input Space:The space taken to store the solution.
#
#
# C=a+b
#
# Where C is auxillary Space.
# a and b are input space.
#
# While coding, tampering the input for SC is wrong practice.



