# -*- coding: utf-8 -*-

from copy import deepcopy
from loop_index import LoopIndex
from sys import stderr


NUM_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
LIST_LENGTH = len(NUM_LIST)

print("The use cases are based on this list:\n" + str(NUM_LIST))


print("\nUse case 1.1: Print all numbers")
output = str()
visited_indices = list()

index = LoopIndex(LIST_LENGTH)
print(repr(index))
while index.check_bounds():
    i = index.get_value()
    visited_indices.append(i)
    try:
        output += str(NUM_LIST[i]) + " "
    except IndexError:
        print("INDEX ERROR! i = " + str(i), file=stderr)
    index.increment()

print("Visited indices: " + str(visited_indices))
print(output)

del index, i, output, visited_indices


print("\nUse case 1.2: Print all numbers with iterate")
output = str()
visited_indices = list()

index = LoopIndex(LIST_LENGTH)
print(repr(index))
# Method iterate makes iteration simpler.
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    try:
        output += str(NUM_LIST[i]) + " "
    except IndexError:
        print("INDEX ERROR! i = " + str(i), file=stderr)

print("Visited indices: " + str(visited_indices))
print(output)

del index, i, output, visited_indices


print("\nUse case 1.3: Print all numbers in descending order")
output = str()
visited_indices = list()

index = LoopIndex(0, -1, LIST_LENGTH-1)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    try:
        output += str(NUM_LIST[i]) + " "
    except IndexError:
        print("INDEX ERROR! i = " + str(i), file=stderr)

print("Visited indices: " + str(visited_indices))
print(output)

del index, i, output, visited_indices


print("\nUse case 1.4: Print all numbers in descending order with negative indices")
output = str()
visited_indices = list()

index = LoopIndex(-LIST_LENGTH, -1, -1)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    try:
        output += str(NUM_LIST[i]) + " "
    except IndexError:
        print("INDEX ERROR! i = " + str(i), file=stderr)

print("Visited indices: " + str(visited_indices))
print(output)

del index, i, output, visited_indices


print("\nUse case 2.1: Print all odd numbers in ascending order")
output = str()
visited_indices = list()

index = LoopIndex(LIST_LENGTH, 2)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    try:
        output += str(NUM_LIST[i]) + " "
    except IndexError:
        print("INDEX ERROR! i = " + str(i), file=stderr)

print("Visited indices: " + str(visited_indices))
print(output)

del index, i, output, visited_indices


print("\nUse case 2.2: Print all odd numbers in descending order")
output = str()
visited_indices = list()

index = LoopIndex(0, -2, LIST_LENGTH-1)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    try:
        output += str(NUM_LIST[i]) + " "
    except IndexError:
        print("INDEX ERROR! i = " + str(i), file=stderr)

print("Visited indices: " + str(visited_indices))
print(output)

del index, i, output, visited_indices


print("\nUse case 3.1: Print all even numbers in ascending order")
output = str()
visited_indices = list()

index = LoopIndex(LIST_LENGTH, 2, 1)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    try:
        output += str(NUM_LIST[i]) + " "
    except IndexError:
        print("INDEX ERROR! i = " + str(i), file=stderr)

print("Visited indices: " + str(visited_indices))
print(output)

del index, i, output, visited_indices


print("\nUse case 3.2: Print all even numbers in descending order")
output = str()
visited_indices = list()

index = LoopIndex(0, -2, LIST_LENGTH-2)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    try:
        output += str(NUM_LIST[i]) + " "
    except IndexError:
        print("INDEX ERROR! i = " + str(i), file=stderr)

print("Visited indices: " + str(visited_indices))
print(output)

del index, i, output, visited_indices


print("\nUse case 4.1: Delete all odd numbers in ascending order")
list_copy = deepcopy(NUM_LIST)
visited_indices = list()

index = LoopIndex(LIST_LENGTH)
print(repr(index))
# Method iterate cannot be used here.
while index.check_bounds():
    i = index.get_value()
    visited_indices.append(i)
    try:
        number = list_copy[i]
    except IndexError:
        print("INDEX ERROR! i = " + str(i), file=stderr)
        continue
    if number % 2: # Odd number
        del list_copy[i]
        # The limit must be updated when an element is deleted.
        index.set_limit(len(list_copy))
    else:
        # Incrementation is only required
        # if the number is not deleted.
        index.increment()

print("Visited indices: " + str(visited_indices))
print(list_copy)

del index, i, list_copy, visited_indices


print("\nUse case 4.2: Delete all odd numbers in descending order")
list_copy = deepcopy(NUM_LIST)
visited_indices = list()

index = LoopIndex(0, -1, LIST_LENGTH-1)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    try:
        number = list_copy[i]
    except IndexError:
        print("INDEX ERROR! i = " + str(i), file=stderr)
        continue
    if number % 2: # Odd number
        del list_copy[i]

print("Visited indices: " + str(visited_indices))
print(list_copy)

del index, i, list_copy, visited_indices


print("\nUse case 5.1: Delete all even numbers in ascending order")
list_copy = deepcopy(NUM_LIST)
visited_indices = list()

index = LoopIndex(LIST_LENGTH)
print(repr(index))
# Method iterate cannot be used here.
while index.check_bounds():
    i = index.get_value()
    visited_indices.append(i)
    try:
        number = list_copy[i]
    except IndexError:
        print("INDEX ERROR! i = " + str(i), file=stderr)
        continue
    if number%2 == 0: # Even number
        del list_copy[i]
        # The limit must be updated when an element is deleted.
        index.set_limit(len(list_copy))
    else:
        # Incrementation is only required
        # if the number is not deleted.
        index.increment()

print("Visited indices: " + str(visited_indices))
print(list_copy)

del index, i, list_copy, visited_indices


print("\nUse case 5.2: Delete all even numbers in descending order")
list_copy = deepcopy(NUM_LIST)
visited_indices = list()

index = LoopIndex(0, -1, LIST_LENGTH-1)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    try:
        number = list_copy[i]
    except IndexError:
        print("INDEX ERROR! i = " + str(i), file=stderr)
        continue
    if number%2 == 0: # Even number
        del list_copy[i]

print("Visited indices: " + str(visited_indices))
print(list_copy)

del index, i, list_copy, visited_indices


# When performing a task on groups of consecutive elements, it can be necessary
# to set a limit lesser than the sequence's length or greater than 0.
print("\nUse case 6.1: Make groups of three elements in ascending order")
GROUP_SIZE = 3
groups = list()
visited_indices = list()

index = LoopIndex(LIST_LENGTH-(LIST_LENGTH%GROUP_SIZE), GROUP_SIZE)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    group = list()
    jndex = LoopIndex(i+GROUP_SIZE, start=i)
    print("\t" + repr(jndex))
    while jndex.iterate():
        j = jndex.get_value()
        try:
            group.append(NUM_LIST[j])
        except IndexError:
            print("INDEX ERROR! j = " + str(j), file=stderr)
    groups.append(group)

# Index 9 is not visited.
print("Visited indices: " + str(visited_indices))

for group in groups:
    print(group)

del GROUP_SIZE, groups, group, index, i, jndex, j, visited_indices


print("\nUse case 6.2: Make groups of three elements in descending order")
GROUP_SIZE = 3
groups = list()
visited_indices = list()

index = LoopIndex(LIST_LENGTH%GROUP_SIZE, -GROUP_SIZE, LIST_LENGTH-1)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    group = list()
    jndex = LoopIndex(i-(GROUP_SIZE-1), -1, i)
    print("\t" + repr(jndex))
    while jndex.iterate():
        j = jndex.get_value()
        try:
            group.append(NUM_LIST[j])
        except IndexError:
            print("INDEX ERROR! j = " + str(j), file=stderr)
    groups.append(group)

# Index 1 is not visited.
print("Visited indices: " + str(visited_indices))

for group in groups:
    print(group)

del GROUP_SIZE, groups, group, index, i, jndex, j, visited_indices


print("\nUse case 7.1: Make groups of three elements from a list\n"
      + "              of nine elements in ascending order")
NUM_LIST_7_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
LIST_LENGTH_7_1 = len(NUM_LIST_7_1)
GROUP_SIZE = 3
groups = list()
visited_indices = list()

print("List for this use case: " + str(NUM_LIST_7_1))

index = LoopIndex(LIST_LENGTH_7_1-(LIST_LENGTH_7_1%GROUP_SIZE), GROUP_SIZE)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    group = list()
    jndex = LoopIndex(i+GROUP_SIZE, start=i)
    print("\t" + repr(jndex))
    while jndex.iterate():
        j = jndex.get_value()
        try:
            group.append(NUM_LIST_7_1[j])
        except IndexError:
            print("INDEX ERROR! j = " + str(j), file=stderr)
    groups.append(group)

print("Visited indices: " + str(visited_indices))

for group in groups:
    print(group)

del NUM_LIST_7_1, LIST_LENGTH_7_1, GROUP_SIZE,\
    groups, group, index, i, jndex, j, visited_indices


print("\nUse case 7.2: Make groups of three elements from a list\n"
      + "              of nine elements in descending order")
NUM_LIST_7_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
LIST_LENGTH_7_2 = len(NUM_LIST_7_2)
GROUP_SIZE = 3
groups = list()
visited_indices = list()

print("List for this use case: " + str(NUM_LIST_7_2))

index = LoopIndex(LIST_LENGTH_7_2%GROUP_SIZE, -GROUP_SIZE, LIST_LENGTH_7_2-1)
print(repr(index))
while index.iterate():
    i = index.get_value()
    visited_indices.append(i)
    group = list()
    jndex = LoopIndex(i-(GROUP_SIZE-1), -1, i)
    print("\t" + repr(jndex))
    while jndex.iterate():
        j = jndex.get_value()
        try:
            group.append(NUM_LIST_7_2[j])
        except IndexError:
            print("INDEX ERROR! j = " + str(j), file=stderr)
    groups.append(group)

print("Visited indices: " + str(visited_indices))

for group in groups:
    print(group)

del NUM_LIST_7_2, LIST_LENGTH_7_2, GROUP_SIZE,\
    groups, group, index, i, jndex, j, visited_indices
