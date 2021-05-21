# %%
#### Formating Output
print("""Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky. Twinkle, twinkle, little star,\n\t How I wonder what you are""")
# %%
#### Python Version
import os
import sys
from time import time
print(sys.version)
# %%
#### Current Time
import datetime as dt
print(dt.date.today())
print(dt.datetime.now( ))
# %%
#### Area of circle
import math
userInput = input('radius> ')
def areaOfCircle(radius):
    return math.pi*radius**2 
try:
    radius = float(userInput)
    print(areaOfCircle(radius))
except:
    print('Invalid Input')
# %%
#### Formating Output
first_name = input("First name")
last_name = input("Last name")
print(f'{last_name} {first_name}')
# %%
#### split() method is splits a string into List with user specified separator default separator is whitespace 
inp = input('Enter sequence of number')
list_output = inp.split(',')
tuple_output = tuple(list)
print(f'List: {list_output}')
print(f'Tuple: {tuple_output}')

# %%
#### spliting user input
inp = input('Enter Filename with extension:')
try:
    extension_name = inp.split('.')
    print(extension_name[1])
except:
    print('Invalid Input')
# %%
color_list = ["Red","Green","White" ,"Black"]
print(f'first: {color_list[0]}, last: {color_list[-1]}')
# %%
import re
delimiters = '/'
exam_st_date = (11,12,2014)
(day,month,year) = exam_st_date
print(f'The examination will start from : {day} / {month} / {year}')

# %%
def joinChar():
    num = input('Enter integer')
    times = input('How many tiems.')
    try:
        result = str(num)*int(times)
    except:
        print('Invalid Input')
    return int(result)

print(f'{joinChar()+joinChar()+joinChar()}')
# %%
### printing the documention of any bultin function
print(print.__doc__)
# %%
### output the calender for given month and year 
import calendar as cl
print(cl.month(2021,5))