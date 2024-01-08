# "==" checks for equality of value
# "is" checks for equality of object


l1 = [1, 2, 3, 4, 5]
l2 = l1

l1[0] = 10
print(id(l1))
print(id(l2))

print(id(l1) == id(l2))
print(l1 is l2)

# if l1 is l2:
#     print("equal")
# else:
#     print("not equal")
