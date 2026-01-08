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

from decimal import Decimal
Var = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
print(Var)


# String in Detail
chai = "Masala Chai"
first_char = chai[0]
second_char = chai[3]
print(first_char)
print(second_char)

slice_char = chai[:]
slice_char = chai[:6]
slice_char = chai[7:]
print(slice_char)

num_list = "0123456789"
print(num_list[:])
print(num_list[3:])
print(num_list[:7])
print(num_list[0:7:2])
print(num_list[0:7:3])
print(num_list[::-1])

# methods
print(chai)
print(chai.lower())
print(chai.upper())

chai = "  Masala Chai  "
print(chai.strip())

chai = "Lemon Chai"
print(chai.replace("Lemon", "Ginger"))
print(chai) # chai will not change because strings are immutable

chai = "Lemon, Ginger, Masala, Mint"
print(chai.split())
print(chai.split(","))

chai = "Masala Chai"
print(chai.find("Chai"))
print(chai.find("s"))
print(chai.find("chai"))

chai = "Lemon, chai, chai, chai"
print(chai.count("chai"))

# String formating
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order)
print(order.format(quantity,chai_type))
print(f"I ordered {quantity} cups of {chai_type} chai")


chai_variety = ["Lemon", "Ginger", "Masala", "Mint"]
print(" ".join(chai_variety))
print("-".join(chai_variety))
print(", ".join(chai_variety))

chai = "Ginger Chai"
print(len(chai))
for letter in chai:
    # print(letter)
    print(letter, end=' ')
print("\n")    


chai = "He said, \"Masala chai is awesome\" "
print(chai)
chai = "Masala\nChai"
print(chai)

# row String
chai = r"c:\user\pwd"
print(chai)

chai = "c:\\user\\pwd"
print(chai)

# containing or not
chai = "Lemon", "Ginger", "Masala", "Mint"
print("Ginger" in chai)
print("Orange" in chai)


# List/Array Data Type
tea_varieties = ["Black", "Green", "Oolong", "White"]

# Indexing
print(tea_varities)
print(tea_varities[0])
print(tea_varities[-2])

# slicing
print(tea_varities[:])
print(tea_varities[1:3])
print(tea_varities[1:1])
print(tea_varities[2:])
print(tea_varities[:2])

tea_varities[3] = "Herbal"
print(tea_varities)
# tea_varities[2:2] = "Mint"
# print(tea_varities)
# ['Black', 'Green', 'M', 'i ', 'n', 't', 'Oolong', 'Herbal']
tea_varieties [2:2] = ["Mint"]
print(tea_varities)

# add/remove using slicing
tea_varieties [1:1] = ["test", "test"]
print(tea_varities)
print(tea_varities[1:3])

tea_varities[1:3] = []
print(tea_varities)

# condition/for loop with list
c = 1
for tea in tea_varieties:
    print(c, tea)
    c += 1 

if "Mint" in tea_varieties:
    print("Mint tea avilble")
else:
    print("Not availble")    

# Methods
tea_varities.append("Lemon")
print(tea_varities)

print("poped :-", tea_varities.pop())

tea_varities.remove("Mint")
print(tea_varities)

tea_varities.insert(1, "Ginger")
print(tea_varities)

# tea_varieties_copy and tea_varieties have different memory references 
tea_varities_copy = tea_varities.copy()

print(tea_varities_copy)
tea_varities_copy.append("Special")

print(tea_varities_copy)
print(tea_varities)

# List Compreihension
squared_nums = [x**2 for x in range(10)]
print(squared_nums)

cube_nums = [x**3 for x in range(5)]
print(cube_nums)

# Dictionary DataType

