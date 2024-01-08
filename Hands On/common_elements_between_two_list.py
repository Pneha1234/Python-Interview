def common_elements_between_two_list(list1, list2):
    return list(set(list1) & set(list2))

print(common_elements_between_two_list([1,2,3,4,5], [1,2,3,4,5,6,7,8,9,10]))