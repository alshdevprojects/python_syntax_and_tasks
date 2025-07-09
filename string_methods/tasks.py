# 1. capitalize()
# task. Format user text
a = input('Enter your text: ')
print('Your formatted text: ', a.capitalize())

# 2. casefold()
# task. Format user text
b = input('Enter your text: ')
print('Your formatted text: ', b.casefold())

# 3. center(width[, fillchar])
# task.From the text entered by the user, make a resulting string of 10 characters. If the text is less than
#      10 characters, then add the characters 1 on both sides
c = input('Enter your text: ')
print(c.center(10, '1'))

# 4. count(sub[, start[, end]])
# task. Count the number of occurrences of a string
str_for_count = "Count the number of occurrences of a string"
print('Count the number of occurrences', str_for_count.count('number'))
print('Count the number of occurrences', str_for_count.count('number', 1, 20))

# 5. encode(encoding="utf-8", errors="strict")
# task. Encode a string
from sys import getdefaultencoding
getdefaultencoding()
str_for_encode = 'Secret information'
print('Encoded information', str_for_encode.encode())


# 6. endswith(suffix[, start[, end]])
# task. Find 'information'
str_for_endswith = 'Secret information'
print('Search result', str_for_endswith.endswith('information'))

# 7. expandtabs(tabsize)
# task. Return a copy of the string with tabs replaced with spaces
str_for_expandtabs = ('\tgh\tghj\tgyuik')
print(str_for_expandtabs.expandtabs(tabsize=8))
print(str_for_expandtabs.expandtabs(tabsize=3))

