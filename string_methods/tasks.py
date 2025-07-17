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

# 8. find(sub[, start[, end]])
# task. Find 'cvh'
str_for_find = 'fcvhjkmnjygn'
print(str_for_find.find('cvh'))
print(str_for_find.find('cvh', 0, 10))

# 9. format(args, *kwargs)
# task. Return a formatted copy of the string
print('{}-{}-{}'.format(1, 2, 3))
print('{}-{}-{}'.format(*[1, 2, 3]))
print('{a}-{b}-{c}'.format(b=10, a=1, c=0))
import datetime
print('{a}-{b}-{c}'.format(b=10, a=1, c=datetime.datetime.now()))

# 10. index(sub[, start[, end]])
# task. Return index 'cvh'
str_for_index = 'fcvhjkmnjygn'
print(str_for_index.find('cvh'))
print(str_for_index.find('cvh', 0, 10))

# 11. isalnum()
# task. Return true 0r false
str1_for_isalnum = '12345'
str2_for_isalnum = 'qwertyu'
str3_for_isalnum = '$%^&'
str4_for_isalnum = '1'
print('first: ', str1_for_isalnum.isalnum(), 'second: ', str2_for_isalnum.isalnum(),
      'third:', str3_for_isalnum.isalnum(), 'fourth:', str4_for_isalnum.isalnum())

# 12. isalpha()
# task. Return true 0r false
str1_for_isalpha = ''
str2_for_isalpha = 'zxcvbn'
str3_for_isalpha = '456zxc'
str4_for_isalpha = '!!!!'
print('first: ', str1_for_isalpha.isalpha(), 'second: ', str2_for_isalpha.isalpha(),
      'third:', str3_for_isalpha.isalpha(), 'fourth:', str4_for_isalpha.isalpha()
      )

# 13. isascii()
# task. Check if there are strings with only ASCII.
str1_for_isascii = ''
str2_for_isascii = 'flower'
str3_for_isascii = 'цветок'
print("Check for ASCII in '':", str1_for_isascii.isascii(),
      "Check for ASCII in 'flower':", str2_for_isascii.isascii(),
      "Check for ASCII in 'цветок':", str3_for_isascii.isascii()
      )

# 14. isdigit()
# task.  Check if there are only numbers in a line
str1_for_isdigit = ''
str2_for_isdigit = 'flower'
str3_for_isdigit = '123'
str3_for_isdigit = '123flower'
print("Check the numbers in '':", str1_for_isdigit.isdigit(),
      "Check the numbers in 'flower':", str2_for_isdigit.isdigit(),
      "Check the numbers in '123':", str3_for_isdigit.isdigit(),
      )

# 15. isidentifier()
# task. Check if a string is an identifier
str1_for_isidentifier = 'cat'
str2_for_isidentifier = 'continue'
str3_for_isidentifier = ''
str4_for_isidentifier = '123'
print("Check isidentifier() in 'cat':", str1_for_isidentifier.isidentifier(),
      "Check isidentifier() in 'continue':", str2_for_isidentifier.isidentifier(),
      "Check isidentifier() in '':", str3_for_isidentifier.isidentifier(),
      "Check isidentifier() in '123':", str4_for_isidentifier.isidentifier()
      )

# 16. islower()
# task. Check whether a string contains only lowercase characters
str1_for_islower = 'DbNiuy'
str2_for_islower = '1234fghn'
str3_for_islower = 'uytgfdfghj'
print("Check islower in 'DbNiuy':", str1_for_islower.islower(),
      "Check islower in '1234fghn':", str2_for_islower.islower(),
      "Check islower in 'uytgfdfghj':", str3_for_islower.islower(),
      )
