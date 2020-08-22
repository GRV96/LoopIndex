# -*- coding: utf-8 -*-

from loop_index import LoopIndex
from os import system


def backward_iter_console_test(num_list, jump, start=None, skip_last=False):
    test_announcement = "Backward iteration by " + str(jump)
    
    if start == None:
        start = len(num_list)-1
    else:
        test_announcement += " from " + str(start)

    print(test_announcement)
    
    index = LoopIndex(0, -jump, start, skip_last)
    print(repr(index))
    
    while index.check_bounds():
        i = index.get_value()
        print(str(i) + ": " + str(num_list[i]))
        index.increment()
        print("Next index: " + str(index._index))


def forward_iter_console_test(num_list, jump, start=0, skip_last=False):
    test_announcement = "Forward iteration by " + str(jump)
    if start != 0:
        test_announcement += " from " + str(start)
    print(test_announcement)
    
    index = LoopIndex(len(num_list), jump, start, skip_last)
    print(repr(index))
    
    while index.check_bounds():
        i = index.get_value()
        print("Value at " + str(i) + ": " + str(num_list[i]))
        index.increment()
        print("Next index: " + str(index._index))


def generate_range_list(length):
    return [n for n in range(length)]


def test_backward_iteration(num_list, jump, start=None, skip_last=False):
    if start == None:
        start = len(num_list)-1
    
    visited_items = list()
    
    index = LoopIndex(0, -jump, start, skip_last)
    while index.iterate():
        i = index.get_value()
        visited_items.append(num_list[i])

    return visited_items


def test_forward_iteration(num_list, jump, start=0, skip_last=False):
    visited_items = list()
    
    index = LoopIndex(len(num_list), jump, start, skip_last)
    while index.iterate():
        i = index.get_value()
        visited_items.append(num_list[i])

    return visited_items


def generate_range_list(length):
    return [n for n in range(length)]


# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list10 = generate_range_list(11)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list11 = generate_range_list(12)

# Forward tests from index 0 with an even length
assert(test_forward_iteration(list11, 1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
assert(test_forward_iteration(list11, 2) == [0, 2, 4, 6, 8, 10])
assert(test_forward_iteration(list11, 3) == [0, 3, 6, 9])
assert(test_forward_iteration(list11, 4) == [0, 4, 8])
assert(test_forward_iteration(list11, 5) == [0, 5, 10])
assert(test_forward_iteration(list11, 6) == [0, 6])
assert(test_forward_iteration(list11, 7) == [0, 7])
assert(test_forward_iteration(list11, 11) == [0, 11])
assert(test_forward_iteration(list11, 12) == [0])
assert(test_forward_iteration(list11, 13) == [0])

# Forward tests from index 0 with an even length and skip_last=True
assert(test_forward_iteration(list11, 1, skip_last=True) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
assert(test_forward_iteration(list11, 2, skip_last=True) == [0, 2, 4, 6, 8, 10])
assert(test_forward_iteration(list11, 3, skip_last=True) == [0, 3, 6, 9])
assert(test_forward_iteration(list11, 4, skip_last=True) == [0, 4, 8])
assert(test_forward_iteration(list11, 5, skip_last=True) == [0, 5])
assert(test_forward_iteration(list11, 6, skip_last=True) == [0, 6])
assert(test_forward_iteration(list11, 7, skip_last=True) == [0])
assert(test_forward_iteration(list11, 11, skip_last=True) == [0])
assert(test_forward_iteration(list11, 12, skip_last=True) == [0])
assert(test_forward_iteration(list11, 13, skip_last=True) == [])

# Forward tests from index 0 with an odd length
assert(test_forward_iteration(list10, 1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
assert(test_forward_iteration(list10, 2) == [0, 2, 4, 6, 8, 10])
assert(test_forward_iteration(list10, 3) == [0, 3, 6, 9])
assert(test_forward_iteration(list10, 4) == [0, 4, 8])
assert(test_forward_iteration(list10, 5) == [0, 5, 10])
assert(test_forward_iteration(list10, 6) == [0, 6])
assert(test_forward_iteration(list10, 7) == [0, 7])
assert(test_forward_iteration(list10, 11) == [0])
assert(test_forward_iteration(list10, 12) == [0])

# Forward tests from index 0 with an odd length and skip_last=True
assert(test_forward_iteration(list10, 1, skip_last=True) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
assert(test_forward_iteration(list10, 2, skip_last=True) == [0, 2, 4, 6, 8])
assert(test_forward_iteration(list10, 3, skip_last=True) == [0, 3, 6])
assert(test_forward_iteration(list10, 4, skip_last=True) == [0, 4])
assert(test_forward_iteration(list10, 5, skip_last=True) == [0, 5])
assert(test_forward_iteration(list10, 6, skip_last=True) == [0])
assert(test_forward_iteration(list10, 7, skip_last=True) == [0])
assert(test_forward_iteration(list10, 11, skip_last=True) == [0])
assert(test_forward_iteration(list10, 12, skip_last=True) == [])

# Forward tests from other indices
# Iterate by 3 from 2
assert(test_forward_iteration(list11, 3, 2) == [2, 5, 8, 11])
# Iterate by 5 from 1
assert(test_forward_iteration(list11, 5, 1) == [1, 6, 11])
# Iterate by 4 from 5
assert(test_forward_iteration(list11, 4, 5) == [5, 9])
# Iterate by 8 from 7
assert(test_forward_iteration(list11, 8, 7) == [7])

# Forward tests from other indices and skip_last=True
# Iterate by 3 from 2
assert(test_forward_iteration(list11, 3, 2, True) == [2, 5, 8])
# Iterate by 5 from 1
assert(test_forward_iteration(list11, 5, 1, True) == [1, 6])
# Iterate by 4 from 5
assert(test_forward_iteration(list11, 4, 5, True) == [5])
# Iterate by 8 from 7
assert(test_forward_iteration(list11, 8, 7, True) == [])

# Backward tests from last index with an even length
assert(test_backward_iteration(list11, 1) == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
assert(test_backward_iteration(list11, 2) == [11, 9, 7, 5, 3, 1])
assert(test_backward_iteration(list11, 3) == [11, 8, 5, 2])
assert(test_backward_iteration(list11, 4) == [11, 7, 3])
assert(test_backward_iteration(list11, 5) == [11, 6, 1])
assert(test_backward_iteration(list11, 6) == [11, 5])
assert(test_backward_iteration(list11, 7) == [11, 4])
assert(test_backward_iteration(list11, 11) == [11, 0])
assert(test_backward_iteration(list11, 12) == [11])
assert(test_backward_iteration(list11, 13) == [11])

# Backward tests from last index with an even length and skip_last=True
assert(test_backward_iteration(list11, 1, skip_last=True) == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
assert(test_backward_iteration(list11, 2, skip_last=True) == [11, 9, 7, 5, 3, 1])
assert(test_backward_iteration(list11, 3, skip_last=True) == [11, 8, 5, 2])
assert(test_backward_iteration(list11, 4, skip_last=True) == [11, 7, 3])
assert(test_backward_iteration(list11, 5, skip_last=True) == [11, 6])
assert(test_backward_iteration(list11, 6, skip_last=True) == [11, 5])
assert(test_backward_iteration(list11, 7, skip_last=True) == [11])
assert(test_backward_iteration(list11, 11, skip_last=True) == [11])
assert(test_backward_iteration(list11, 12, skip_last=True) == [11])
assert(test_backward_iteration(list11, 13, skip_last=True) == [])

# Backward tests from last index with an odd length
assert(test_backward_iteration(list10, 1) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
assert(test_backward_iteration(list10, 2) == [10, 8, 6, 4, 2, 0])
assert(test_backward_iteration(list10, 3) == [10, 7, 4, 1])
assert(test_backward_iteration(list10, 4) == [10, 6, 2])
assert(test_backward_iteration(list10, 5) == [10, 5, 0])
assert(test_backward_iteration(list10, 6) == [10, 4])
assert(test_backward_iteration(list10, 7) == [10, 3])
assert(test_backward_iteration(list10, 10) == [10, 0])
assert(test_backward_iteration(list10, 11) == [10])
assert(test_backward_iteration(list10, 12) == [10])

# Backward tests from last index with an odd length and skip_last=True
assert(test_backward_iteration(list10, 1, skip_last=True) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
assert(test_backward_iteration(list10, 2, skip_last=True) == [10, 8, 6, 4, 2])
assert(test_backward_iteration(list10, 3, skip_last=True) == [10, 7, 4])
assert(test_backward_iteration(list10, 4, skip_last=True) == [10, 6])
assert(test_backward_iteration(list10, 5, skip_last=True) == [10, 5])
assert(test_backward_iteration(list10, 6, skip_last=True) == [10])
assert(test_backward_iteration(list10, 7, skip_last=True) == [10])
assert(test_backward_iteration(list10, 10, skip_last=True) == [10])
assert(test_backward_iteration(list10, 11, skip_last=True) == [10])
assert(test_backward_iteration(list10, 12, skip_last=True) == [])

# Backward tests from other indices
# Iterate by -3 from 10
assert(test_backward_iteration(list11, 3, 10) == [10, 7, 4, 1])
# Iterate by -4 from 9
assert(test_backward_iteration(list11, 4, 9) == [9, 5, 1])
# Iterate by -5 from 7
assert(test_backward_iteration(list11, 5, 7) == [7, 2])
# Iterate by -6 from 4
assert(test_backward_iteration(list11, 6, 4) == [4])

# Backward tests from other indices and skip_last=True
# Iterate by -3 from 10
assert(test_backward_iteration(list11, 3, 10, True) == [10, 7, 4])
# Iterate by -4 from 9
assert(test_backward_iteration(list11, 4, 9, True) == [9, 5])
# Iterate by -5 from 7
assert(test_backward_iteration(list11, 5, 7, True) == [7])
# Iterate by -6 from 4
assert(test_backward_iteration(list11, 6, 4, True) == [])

if __name__ == "__main__":
    print("Testing with the following list: " + str(list11) + "\n")
    forward_iter_console_test(list11, 3, 2)
    print()
    forward_iter_console_test(list11, 2)
    print()
    backward_iter_console_test(list11, 2)
    print()
    backward_iter_console_test(list11, 4, 10)
    system("pause")
