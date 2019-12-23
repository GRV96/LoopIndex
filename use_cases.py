# -*- coding: utf-8 -*-

from copy import deepcopy
from loop_index import LoopIndex

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
LIST_LENGTH = len(num_list)

print("The use cases are based on this list:\n"
      + str(num_list))


print("\nUse case 1.1: Print all numbers")
output = str()
visited_indices = list()

index = LoopIndex(LIST_LENGTH)
print(repr(index))
while index.will_stay_within_bounds():
    i = index.get_value()
    visited_indices.append(i)
    output += str(num_list[i]) + " "
    index.increment()

print("Visited indices:", visited_indices)
print(output)

del index, output, visited_indices


print("\nUse case 1.2: Print all numbers with iterate")
output = str()
visited_indices = list()

index = LoopIndex(LIST_LENGTH)
print(repr(index))
# Method iterate makes iteration simpler.
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    output += str(num_list[i]) + " "

print("Visited indices:", visited_indices)
print(output)

del index, output, visited_indices


print("\nUse case 2.1: Print all odd numbers")
output = str()
visited_indices = list()

index = LoopIndex(LIST_LENGTH, 2)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    output += str(num_list[i]) + " "

print("Visited indices:", visited_indices)
# Warning! 11 is not printed.
print(output)

del index, output, visited_indices


print("\nUse case 2.2: Print all even numbers")
output = str()
visited_indices = list()

index = LoopIndex(LIST_LENGTH, 2, 1)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    output += str(num_list[i]) + " "

print("Visited indices:", visited_indices)
print(output)

del index, output, visited_indices


print("\nUse case 3.1: Delete all odd numbers fowrard")
list_copy = deepcopy(num_list)
visited_indices = list()

index = LoopIndex(LIST_LENGTH)
print(repr(index))
# Method iterate cannot be used here.
while index.will_stay_within_bounds():
    i = index.get_value()
    visited_indices.append(i)
    if list_copy[i] % 2: # Odd number
        del list_copy[i]
        index.set_limit(len(list_copy))
    else:
        # Incrementation is only required
        # if the number is not deleted.
        index.increment()

print("Visited indices:", visited_indices)
print(list_copy)

del index, list_copy, visited_indices


print("\nUse case 3.2: Delete all odd numbers backward")
list_copy = deepcopy(num_list)
visited_indices = list()

index = LoopIndex(0, -1, LIST_LENGTH-1)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    if list_copy[i] % 2: # Odd number
        del list_copy[i]

print("Visited indices:", visited_indices)
print(list_copy)

del index, list_copy, visited_indices


print("\nUse case 4.1: Make groups of three elements forward")
groups = list()
visited_indices = list()

index = LoopIndex(LIST_LENGTH, 3)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    group = list()
    jndex = LoopIndex(i+3, start=i)
    while jndex.iterate():
        j = jndex.get_value()
        group.append(num_list[j])
    groups.append(group)

# Index 9 is not visited.
print("Visited indices:", visited_indices)

for group in groups:
    print(group)

del groups, index, visited_indices


print("\nUse case 4.2: Make groups of three elements backward")
groups = list()
visited_indices = list()

index = LoopIndex(0, -3, LIST_LENGTH-1)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    group = list()
    jndex = LoopIndex(i-2, -1, i)
    while jndex.iterate():
        j = jndex.get_value()
        group.append(num_list[j])
    groups.append(group)

# Index 1 is not visited.
print("Visited indices:", visited_indices)

for group in groups:
    print(group)

del groups, index, visited_indices
