# print name 5 times
# print linearly from 1 to N
# print from N to 1
# print linearly from 1 to N (But By BackTrack)
# print from N to 1 (By Backtrack)


def print_name_5_times(n):
    if n == 5:
        return
    else:
        n += 1
        print("Neha")
        return print_name_5_times(n)

# print(print_name_5_times(1))

def print_linearly_from_one_to_n(start, end):
    if start >= end:
        return
    else:
        print(start)
        start += 1
        return print_linearly_from_one_to_n(start, end)

# print( print_linearly_from_one_to_n(start=0, end=7))

def print_from_n_to_one(end):
    if end == 0:
        return
    else:
        print(end)
        end = end-1
        return print_from_n_to_one(end)

# print(print_from_n_to_one(7))

# print linearly from 1 to N (But By BackTrack)

def linearly_print_one_to_n_through_backtracking(start, end):
    if start< 1:
        return
    else:
        linearly_print_one_to_n_through_backtracking(start-1, end)
        print(start)

# linearly_print_one_to_n_through_backtracking(7, 7)

def linearly_print_n_to_one_through_backtracking(start, end):
    if end < 0:
        return
    else:
        linearly_print_n_to_one_through_backtracking(start, end-1)
        print(start-end)

print(linearly_print_n_to_one_through_backtracking(7, 7))
