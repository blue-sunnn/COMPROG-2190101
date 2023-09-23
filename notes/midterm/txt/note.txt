# -*- coding: utf-8 -*-

# useful list
lowercase = list('abcdefghijklmnopqrstuvwxyz')
uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
digits = list('0123456789')
symbols = list('!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~')

# 2
# concatenation
_string = '' + ''
_list = [] + []
# length
x = len(_string or _list)
# indexing
_string or _list = s[0] # start from the front
_string or _list = s[-1] # start from the back
# slicing & slicing abbreviation
_string or _list = s[ start : stop : step ]
# inside modification
x = '---------'
x = s[:5] + 'X' + s[6:]
# repetition
x = _string or _list * 10
# .split() -> splits a string into a list
  # separator -> Optional. Specifies the separator to use when splitting the string
  # maxsplit -> Optional. Specifies how many splits to do
x = _string.split(separator, maxsplit)
# useful string method
# .upper(), .lower(), .strip(), .format()
x = _string.upper()
x = _string.lower()
  # characters -> Optional. A set of characters to remove as leading/trailing characters
x = _string.strip(characters)
  # value -> Required. One or more values that should be formatted and inserted in the string
x = '{} ... {} ...'.format(value1, value2...)

# 3
# boolean expression
  # == equal
  # != not equal
  # > greater than
  # < less than
  # >= greater than or equal to
  # <= less than or equal to
# boolean (True == 1, False == 0)
# rational operators (and, or, not)
# list comparison
  # compare the lists elementwise from left to right
# string comparison
  # compare each character from left to right
# 'in' can use in both string and list
if condition :
  do something when condition is True
elif condition1 :
  do something when condition1 is True
else :
  do something when condition is False

# 4
# while: need to repeat tasks until the condition for repeat is False
while condition :
  do something when condition is True
  repeatedly until condition is False
  if condition : break
# for i in range(n): need to repeat tasks for n times
for _ in range(start, stop, step) :
# for c in string:: get each charecter in string one by one
# for e in list:: get each element in list one by one
for _ in _string or _list:

# 5 -> some already mention in # 2
# .index()
  # returns the position at the first occurrence of the specified value
  # elmnt -> Required. The element to search for
x = _list.index(elmnt)
# .join()
  # takes all items in an iterable and joins them into one string
  # iterable -> Required. (ex. list)
x = ''.join(iterable)
# .append()
  # appends an element to the end of the list
  # elmnt -> Required.
x = _list.append(elmnt)
# .insert()
  # inserts the specified value at the specified position
  # pos	-> Required. number specifying which position to insert the value
  # elmnt -> Required.
x = _list.insert(pos, elmnt)
# .remove()
  # removes the specified item
  # elmnt -> Required. The element you want to remove
x = _list.remove(elmnt)
# .pop()
  # removes the specified index
  # pos	-> Optional. number specifying which position to remove the value, default value is last item
x = _list.pop(pos)
# list comprehension
newlist = [expression for item in iterable if condition == True]
# sum()
  # start	-> Optional. A value that is added to the return value
x = sum(iterable, start)
# .sort() vs sorted()
  # .sort()
  #  sort and change the original list
  # reverse	-> Optional. reverse = True will sort the list descending. Default is reverse = False
  # key	-> Optional. to specify the sorting criteria
x = _list.sort(reverse = True|False, key = myFunc)
  # sorted()
  #  return a new list and does not change order of elements in the list
  # iterable -> Required.
  # key	-> Optional. to decide the order. Default is None
  # reverse	-> Optional. False will sort ascending, True will sort descending. Default is False
x = sorted(iterable, key = key, reverse = reverse)

# FILE
# open()
  # opens a file, and returns it as a file object
  # file -> path and name of the file
  # mode -> define which mode you want to open the file in
    # "r" - Read - Default value.
    #     -> Opens a file for reading, error if the file does not exist
    # "a" - Append
    #     -> Opens a file for appending, creates the file if it does not exist
    # "w" - Write
    #     -> Opens a file for writing, creates the file if it does not exist
    # "x" - Create
    #     -> Creates the specified file, returns an error if the file exist
f = open(file, mode)
# .close()
  # closes an open file
f.close()
# .readlines()
  # returns a list containing each line in the file as a list item
  # hint -> Optional. If the number of bytes returned exceed the hint number, no more lines will be returned.
  #         Default value is  -1, all lines will be returned.
lines = f.readlines(hint)
# .write()
  # writes a specified text to the file
  # byte -> text or byte object that will be inserted
f.write(byte)

# 6
def function_name(parameters):
    function body
    ...
    return result [optional]

# 7
# escape chars
  # \\, \', \", \n, \t
# .find()
  # finds the first occurrence of the specified value - returns -1 if the value is not found
  # value	-> Required. The value to search for
  # start	-> Optional. Where to start the search. Default is 0
  # end	-> Optional. Where to end the search. Default is to the end of the string
x = _string.find(value, start, end)
# ord()
  # returns the number representing the unicode code of a specified character
  # character	-> String, any character
ord(character)
# chr()
  # returns the character that represents the specified unicode
  # number -> integer representing a valid Unicode code point
chr(number)