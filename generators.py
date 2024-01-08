# def square_number(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result
#
# my_nums = square_number([1,2,3,4,5])
#
# print(my_nums)

# generators
# doesn't hold all the values in the memory
def square_number(nums):
    for i in nums:
        yield (i*i)

my_nums = square_number([1,2,3,4,5])
print(my_nums)

for num in my_nums:
    print(num)