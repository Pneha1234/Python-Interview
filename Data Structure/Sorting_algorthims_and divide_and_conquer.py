# you're working on a new feature on jovian called "Top Notebooks of the week". Write a function to sort a list of
# notebooks in decreasing order of likes. Keep in mind that up to millions of notebools can be created every week so
# your function needs to be as effcient as possible

# Write a program to sort a list of numbers

# 1. we need to write a function to sort a list of numbers in increasing order

# input= [6,4,2,1,5], output = [1,2,4,5,6]

#Solution
# iterate through the list
# compare it with all the remaining number of the list
# condition: check if the next item is smaller than the current number
# if true: set a temp variable with smaller number and check with the next occuring item, once the smallest is found
# append it to the new list

def sort_v2(numbers):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[j] < numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers

# print(sort_v2([4, 6,2,1,5]))

def bubble_sort(nums):
    nums = list(nums)

    for _ in range(len(nums)-1):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1] :
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

# print(bubble_sort([4, 6,2,1,5]))

def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >=0 and nums[j] > cur:
            j -=1
        nums.insert(j+1, cur)
    return nums

# print(insertion_sort([4, 6,2,1,5]))


# divide and conquer
# 1. Divide the inputs into two roughly equal parts
# 2. Recursively solve the problem individually for each of the two parts
# 3. Combine the results to solve the problem for the original inputs
# 4. Include terminating conditions for small or indivisible inputs


# state the problem:
#1. If the input list is empty or contains just one element, it is already sorted. Return it
#2. If not, divide the list of numbers into two roughly equal parts
# 3. Sort each part recursively using the merge sort algorithm. You'll get back two sorted lists
#4. Merge the two sorted lists to get a single sorted list

# [2,4,8] [3,5,7]
# i       j
# [2, 3, ]
def merge_sort(nums):
    if len(nums) <=1:
        return nums
    mid = len(nums) //2
    left_list = nums[:mid]
    right_list = nums[mid:]
    left_sorted, right_sorted = merge_sort(left_list), merge_sort(right_list)
    sorted_nums = merge(left_sorted,right_sorted)
    print("sorted_nums", sorted_nums)
    print("left_sorted", left_sorted)
    print("right_sorted", right_sorted)
    return sorted_nums

def merge(left_sorted, right_sorted):
    sorted = []
    i = 0
    j = 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            sorted.append(left_sorted[i])
            i += 1
        else:
            sorted.append(right_sorted[j])
            j+=1


    return sorted + left_sorted[i:] + right_sorted[j:]




print("result",merge_sort([1,5,3,6,8,2]))
# time_complexity: O(nlogn)
# space_complexity : O(n)

# QuickSort
# To overcome the space inefficiencies of merge sort, we'll study another divide-and-conquer based algorithm called
# quick sort
# 1. If the list is empty or has just one element, return it, it's already sorted.
#2. Pick a random element from the list. This element is called a pivot
#3. Reorder the list so that all elements with values less than or equal to the pivot come before the pivot, while all
# elements with values greater than the pivot come after it. This operation is called partitioning
#4. The pivot element divides the array into two parts which can be sorted independently by making a recursive call to
# quicksort

def quicksort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums)-1
    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums


def partition(nums, start, end):
    if end is None:
        end = len(nums)-1
    left_pointer, right_pointer = start, end - 1
    while right_pointer > left_pointer:
        if nums[left_pointer] <= nums[end]:
            left_pointer += 1
        elif nums[right_pointer] > nums[end]:
            right_pointer -= 1
        else:
            nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]

    if nums[left_pointer] > nums[end]:
        nums[left_pointer], nums[end] = nums[end], nums[left_pointer]
        return left_pointer
    else:
        return end

# time_complexity: O(n logn)
#







