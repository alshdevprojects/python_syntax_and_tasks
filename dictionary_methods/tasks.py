# clear()
# task. Clear the dictionary.
dict_for_clear = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print('Cleared dictionary: ', dict_for_clear.clear())

# copy()
# task1. Copy the dictionary.
dict_for_copy = {'a': 1, 'k': 3, 'f': 8, 'e': 7}
dict_for_copy_new = dict_for_copy.copy()
print('New dictionary with new values: ', dict_for_copy_new)

# task2. Copy the dictionary and add the value 10 to the list of key 'b'.
dict_for_copy_with_list = {'a': [1, 2, 3], 'b': [3, 8]}
dict_for_copy_with_list_new = dict_for_copy_with_list.copy()
dict_for_copy_with_list_new['b'].append(10)
print('New dictionary with a new value for the sheet at key "b": ', dict_for_copy_with_list_new)