# print all subsequence -> a contigous/non-contigious sequences, which follows the order
# Pow sets
# recursive way
# array = [3,1,2] -> [3,2] -> take/not take

def find_subsequences(start_index, num, original_array):
    if(start_index >= len(original_array)):
        print(num)
        return
    num.append(original_array[start_index])
    find_subsequences(start_index+1, num, original_array)
    num.remove(original_array[start_index])
    find_subsequences(start_index + 1, num, original_array)

print(find_subsequences(0,[], [3,1,2]))

#time complexity :O(2n)