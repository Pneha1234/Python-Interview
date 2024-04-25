# reverse an array [1,2,3,4,5] -> [5,4,3,2,1]

def reverse_an_array(n):
    left_cursor = 0
    right_cursor = len(n)-1
    for _ in range(len(n)-1):
        if left_cursor != right_cursor:
            n[left_cursor], n[right_cursor] = n[right_cursor], n[left_cursor]
            left_cursor +=1
            right_cursor -=1
    return n

# print(reverse_an_array([1,2,3]))

def recursive_call_to_reverse_an_array(left_index, right_index, num):
    if left_index > right_index:
        return num
    else:
        num[left_index], num[right_index] = num[right_index], num[left_index]
        return recursive_call_to_reverse_an_array(left_index+1, right_index-1, num)

num = [1,2,3,4,5,6]
# print(recursive_call_to_reverse_an_array(0, len(num)-1, num))

# check if the string is palindrome

def check_if_the_string_is_palindrome(left_index, string_to_check):
    if left_index >= len(string_to_check)//2:
        return
    elif string_to_check[left_index] == string_to_check[len(string_to_check)-left_index-1]:
        check_if_the_string_is_palindrome(left_index+1, string_to_check)
        return True
    else:
        return False

reversed_string =check_if_the_string_is_palindrome(0, 'hen')
print(reversed_string)




