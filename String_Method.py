# STRING METHODS

string = 'Hello, how are you'
s = type(string)
print(s)

s = dir(string) # using dir func you can know how many methods present for this class
print(s)

print(help(s.clear)) # using help function you can know what does this methods do?


# find() METHOD
# find method is used to find occerence of sub string in original string(from left to right).
print(string.find('o'))
print(string.find('o',4))
print(string.find('o',5))
print(string.find('c'))
print(string.find('how'))

# rfind() METHOD
# (Traversing from right to left)
print(string.rfind('o'))
print(string.rfind('o',15))
print(string.rfind('o',0,15))
print(string.rfind('k'))

# index() METHOD
#(it is similier to find() method but minor diff is that when any str not present then error occer instence of -1)
print(string.index('o'))
print(string.index('o',4))
print(string.index('o',5))
print(string.index('how'))
# print(string.index('c')) # ERROR

# rindex() METHOD
# (it is similer to rfind() method same minor diff as well as find() and rfind method)
print(string.rindex('o'))
print(string.rindex('o',15))
print(string.rindex('o',0,15))
# print(string.rindex('k')) # Error

