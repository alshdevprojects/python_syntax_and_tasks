# clear()
# task. Clear the dictionary
dict_for_clear = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print('Cleared dictionary: ', dict_for_clear.clear())

# copy()
# task1. Copy the dictionary
dict_for_copy = {'a': 1, 'k': 3, 'f': 8, 'e': 7}
dict_for_copy_new = dict_for_copy.copy()
print('New dictionary with new values: ', dict_for_copy_new)

# task2. Copy the dictionary and add the value 10 to the list of key 'b'
dict_for_copy_with_list = {'a': [1, 2, 3], 'b': [3, 8]}
dict_for_copy_with_list_new = dict_for_copy_with_list.copy()
dict_for_copy_with_list_new['b'].append(10)
print('New dictionary with a new value for the sheet at key "b": ', dict_for_copy_with_list_new)

# get()
# task. Get the value of one of the dictionary keys
dict_for_get = {'a': 1, 'k': 3, 'f': 8, 'e': 7}
print('Value of key "a": ', dict_for_get.get('a'))

#items()
# task. Extract key value pairs from dictionary
dict_for_items = {'first': 4, 'second':1, 'third':3}

for i,j in dict_for_items.items():
    print('Key value: ', i,j)

# key()
# task. Output dictionary keys
dict_for_keys = {'first': 4, 'second':1, 'third':3}

for i in dict_for_keys.keys():
    print('Key: ', i)

# values()
# task. Output dictionary values
dict_for_values = {'first': 4, 'second':1, 'third':3}

for j in dict_for_values.values():
    print('Value: ', j)

# pop()
# task.Output the value of key 1. And try to output the non-existent value of key 4
# and write that the message does not exist.
dict_for_pop = {'first': 4, 'second':1, 'third':3}
print('Value of first', dict_for_pop.pop('first'), 'dict_for_pop after pop()', dict_for_pop)
print(dict_for_pop.pop('fourth', 'The value does not exist'))

# popitem()
# task. Delete the last pair of keys values.
dict_for_popitem = {'first': 4, 'second':1, 'third':3}
dict_for_popitem.popitem()
print('dict_for_popitem after popitem()', dict_for_popitem)

