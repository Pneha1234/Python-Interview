# [9, 7, 6, 4, 3, 2,1]----> [6] (the number that we want to look)
#[9,7,6,4,3,2,1]-----> [4] the number that we have picked---->[4<6]
#[9,7,6]-------[7>6]
#[6]--->6=6

#come up with a correct solution for the problem.state it in plain english
#1. Find the middle element
#2. If it matches the queried number, return the middle position as the answer
#3.If it is less than the queried number, then search the first half of the list
#4.If it is greater than the queried number, then search the second half of the list
#5.if no more element return -1

def locate_card_using_binary_search(cards, query):
    lo, hi = 0, len(cards)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid -1
        elif result == 'right':
            lo = mid + 1

    return -1

def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid_number:" ,mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

print(locate_card_using_binary_search([9, 7, 6, 4, 3, 2,1], 9))

# Analyze the algorithm's complexity and identify inefficiencies, if any
# O(log N), O(1).

# Binary Search vs. Linear Search
def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

# Generic Binary Search:
# 1. Come up with a condition to determine wheather the answer lies before, after or at a give position
# 2. retrieve the midpoint and the middle element of the list
#3. If it is the answer, return the middle position as the answer
#4. If the answer lies before it, repeat the search with the first half of the list
# 5. If the answer lies after it, repeat the search with the second half of the list

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = lo + hi //2
        result = condition[mid]
        if result == 'found':
            return result
        elif result == 'left':
            hi= mid -1
        else:
            lo = mid +1
    return -1

# question: Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number.

# Assignment_1




