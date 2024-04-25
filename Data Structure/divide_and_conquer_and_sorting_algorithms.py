# in this assigment, you will apply the concepts learned in the first two lessons to:
# Implement hash tables from scratch in Python
# Handle hasing collsions using linear probing
# Replicate the functionality of Python dictionaries

# Dictinaries in Python are implemented using a data structure called hash table. A hash table uses a list/array to
# store the key-value pairs, and uses a hashing function to determine the index for storing or retrieving the data
# associated with the given key

# question: 1. Insert : Insert a new key-value pair
# 2: Find: Find the value associated with a key
# 3. Update the value associated with a key
# 4. List: List all the keys stored in the has table
MAX_HASH_TABLE_SIZE = 4096


class HashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size

    def insert(self, key, value):
        """Insert a new key-value pair"""
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Store the key-value pair at the right index
        self.data_list[idx] = (key, value)

    def find(self, key):
        """ Find the value associated with a key"""
        #1. Find the index of the key using get_index
        idx = get_index(self.data_list, key)
        #2. Retrieve the data stored in the index
        kv = self.data_list[idx]
        # 3. Return the value if found else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return key, value

    def update(self, key, value):
        """Change the value associated with a key"""
        #1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        #2. STore the new key-value pair at the right index
        self.data_list[idx] = key, value

    def list_all(self):
        """List all the keys"""
        return [kv[0] for kv in self.data_list if kv is not None]


# create a list of fix size
data_list = [None] * 4096


# create a hashing function
# A hashing function is used to convert strings and other non-numeric data types into numbers,
# which can then be used as list indicies. For instance, if a hashing function converts the string "Neha" into the
# number 4 then the key-value pair("Neha", "1027366712") will be stored at the position 4 within the data list

# simple algorithm for hashing, which can convert strings into numeric list indicies
# 1. Iterate over the string, character by character
# 2. Convert each character to a number using Python's built-in ord function
# 3. Add the number for each character to obtain he hash for the entire string
# 4. Take the remainder of the list with the size of the data list

def get_index(data_list, a_string):
    # Variable to store the result (updated after each iteration)
    result = 0
    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number

    list_index = result % len(data_list)
    return list_index


key, value = 'CNeha', '125678321'
idx = get_index(data_list, key)
data_list[idx] = (key, value)

# to get the key_value_pair
id = get_index(data_list, 'CNeha')
key, value = data_list[id]
print(key, value)

keys = [kv[0] for kv in data_list if kv is not None]
print(keys)

# linear probing:
def get_valid_index(data_list, key):
    # start with the index returned by get_index
    idx = get_index(data_list, key)
    while True:
        # get the key-value pair store at idx
        kv = data_list[idx]

        # If it is None, return the index
        if kv is None:
            return idx

        # if the stored key matches the given key, return index
        k, v = kv
        if k == key:
            return idx
        # move to the next index
        idx +=1

        # go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0


