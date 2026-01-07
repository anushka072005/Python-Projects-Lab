import math
import random

print(math.pi)
print(random.random())

print(random.choice([1,2,3,4,5]))

# String 
username = "chaiaurcode"
print(username)
print(username[0])
print(username[-1])
print(username[-2])
print(username[1:3])

# List 
mylist = [123, 'hii', 'chai']
print(mylist)
print(mylist[0])

# Dictionary
dict = {'key1': 'lock', 'key2': 'home'}
print(dict['key1'])
# print(dict['key3'])

print(dir(username))

# Tuple
mytuple = (123, 'chai', 'code')
print(mytuple)
print(len(mytuple))
print(mytuple[2])
# print(mytuple[3])

# Set
myset = {1,2,3,3,4,5,2,1}
print(myset)
# print(myset[2])