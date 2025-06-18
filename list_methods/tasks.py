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
