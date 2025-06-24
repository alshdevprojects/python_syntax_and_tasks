# clear()
# task. Clear the dictionary values.
dict_for_clear = {'a':1, 'b':2, 'c':3, 'd':4}
print('Сleared dictionary:', dict_for_clear.clear())

# copy()
# task1. Copy the dictionary dict_for_copy.
dict_for_copy = {'a':7, 'k':5, 'f':5, 'c':4, 'x':3}
dict_for_copy_new = dict_for_copy.copy()
print('Copied dict_for_copy: ', dict_for_copy_new)

# task2. Copy the dictionary and add to the list of key 'b' value 10.
dict_for_copy_with_list = {'a': [1, 2, 3], 'b': [2, 1, 1]}
dict_for_copy_with_list_new = dict_for_copy_with_list.copy()
dict_for_copy_with_list_new['b'].append(10)
print('New dictionary with new values: ', dict_for_copy_with_list_new)
