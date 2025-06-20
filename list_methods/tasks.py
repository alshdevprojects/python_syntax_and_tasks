# append
# task. Insert an extra character into the list
a = ['a', 5, 'e', 'g', 8]
b = input('Insert an extra character into the list: ')
a.append(b)
print(a)

# clear
# task. Clear the list a and show what is returned
print(a.clear())

# copy
# task. Make a copy of the list d and append [1, 2]
d = ['list', 10, 'b', 'x', 3]
e = d.copy() # or e = d[:]
e.append([1, 2])
print(e)

# count
# task. Count the number of digits 10 in list e
print(e.count(10))

# extend(iterable)
# task. Add symbols to list
first_list = []
additional_symbol = input('Insert symbol: ')
first_list.extend(additional_symbol)
print(first_list)

# index(x[, start[, end]])
# task. Find element 'a' in list list_for_index
list_for_index = ['w', 'r', 3, 'a', 'd', 'v,', 9, 'e', 'x']
print(list_for_index.index('a'))

# insert(i, x)
# task. Insert 1 into list list_for_index at index 0
list_for_index.insert(0,1)
print(list_for_index)

# pop([i])
# task.
list_for_pop = ['r', 'c', 'e', 'f', 'y', 'r', 'sdf', 'zxc', 'cvb']
list_for_pop.pop(0)
print(list_for_pop)

# remove(x) - removes the specified element from the list
# task.
list_for_remove = ['t', 'f', 'z', 'g', 'e', 'v', 't', 'a']
list_for_remove.remove('t')
print(list_for_remove)
