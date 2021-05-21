# %% 
from time import time


print('Hello World')
# %%
n = 5
a = 100000000
print(a)
# %%
inp = input("Europea Floor?")
usf = int(inp)+1
print('US Floor',usf)
# %%
#hello World
print('Hello World')
# %%
width = 15
height = 12.0
print(height/3)
# %%
x = 2
if x < 2:
  print('Below 2')
elif x >= 2:
  print('Two or more')
else:
  print('Something else')

# %%
inp = input('Enter a number')
try:
  ival = int(inp)
except:
  ival = -1

if ival>0:
  print(ival)
else:
  print('Not a number')

# %%
def things():
  print('Things Function')
  print('2nd Line in Things Function')
things()
# %%
def poster(ads):
  print(ads)
poster('Zomato - Get Food at your doorsteps')
poster('OLA - Ride care free even if you drunk')
poster('Apple - Buy good built quality products')
# %%
big = max([1,2,3,4,5])
print(big)
# %%
def greet(lang):
  if lang == 'en':
    print('Hello')
  elif lang == 'es':
    print('Hola')
  elif lang == 'fr':
    print('Bonjour')
inp = input('lang>>')
greet(inp)
# %%
### find biggest number in list


a = [1,2,3,4,5,6,7,8,1,10]
def big(li):
  largest_so_far = -1
  for i in a:
    if i > largest_so_far:
      largest_so_far=i
  print(largest_so_far)

  
# %%
print('Hello WOrld')