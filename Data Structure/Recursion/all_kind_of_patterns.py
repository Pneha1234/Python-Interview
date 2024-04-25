# printing subsequences whose sum is k (take/not take)
# array = [1,2,1]----> [1,1], [2]---> sum=2

def printing_subsequences_whose_sum_is_k(start_index, sub_array, original_list, sum_value, k):
    if start_index >= len(original_list):
        if(sum_value == k):
            print(sub_array)
            return True
        return False
    sum_value += original_list[start_index]
    sub_array.append(original_list[start_index])

    if(printing_subsequences_whose_sum_is_k(start_index+1, sub_array,original_list, sum_value, k) == True):
        return True

    sum_value -= original_list[start_index]
    sub_array.remove(original_list[start_index])
    if(printing_subsequences_whose_sum_is_k(start_index + 1, sub_array, original_list, sum_value,k)== True):
        return True


print(printing_subsequences_whose_sum_is_k(0, [], [1,2,1], 0, 2))

# find the subsequences whose sum is sum:
# count the subsequence with sum is sum:
def printing_subsequences_whose_sum_is_k(start_index, sub_array, original_list, sum_value, k):
    if start_index >= len(original_list):
        if(sum_value == k):
            print(sub_array)
            return 1
        return 0
    sum_value += original_list[start_index]
    sub_array.append(original_list[start_index])

    left = printing_subsequences_whose_sum_is_k(start_index+1, sub_array,original_list, sum_value, k)


    sum_value -= original_list[start_index]
    sub_array.remove(original_list[start_index])
    right = printing_subsequences_whose_sum_is_k(start_index + 1, sub_array, original_list, sum_value,k)
    return left+right






