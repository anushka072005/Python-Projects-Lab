# STRING METHODS

string = 'Hello, how are you'
s = type(string)
print(s)

s = dir(string) # using dir func you can know how many methods present for this class
print(s)

print(help(s.clear)) # Using help function you can know what does this methods do?


# find() METHOD
# find method is used to find occurrence of sub string in the original string(from left to right).
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
#(it is similier to find() method but the minor diff is that when any str is not present then error occer instence of -1)
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

# count() METHOD (used to total count occerence of char or sub)
print(string.count('o'))
print(string.count('dhor')) # return 0


"""    THESE METHOD GENRATING NEW STRING NOT MODIFY ORIGINAL STRING (BELLOW)  """
# ljust() METHOD (it is used to give space from the LEFT side)
s = 'python'
n = s.ljust(10,'-')
print(n)
n = s.ljust(15,'.')
print(n)

# rjust() METHOD (it is used to give space from the RIGHT side)
n = s.rjust(10,'-')
print(n)

# center() METHOD (used to come center)
n = s.center(20,'-')
print(n)

"""   strip() method remove space along with character    """
# lstrip() METHOD (lstrip()used to remove only leading spaces)
new ="   python   "
n = new.lstrip()
# print(f"'{n}'")
print(n)

# rstrip() METHOD (rstrip()used to remove only trailing spaces)
n = new.rstrip()
print(n)

# strip() METHOD (strip() used to remove leading and trailing spaces)
n = new.strip()
print(n)

s1 = '.... ... +++ kkkhajoor'
print(s1.lstrip())
print(s1.lstrip(".")) #it will remove only starting dots because sfter this sapce there which is diff
print(s1.lstrip('. +')) #it can remove multiple char
print(s1.strip('. +k'))

# capitalize() METHOD (it capitalize only first latter of string)
string2 = "tu jhooti mai makkar"
c = string2.capitalize()
print(c)

# title() METHOD (it capitalize first latter of each word in string)
c = string2.title()
print(c)

# lower() METHOD (it makes lower to each word in str)
c = string2.lower()
print(c)

# upper() METHOD (it makes each letter capital)
c = string2.upper()
print(c)

# swapcase() METHOD (used to swap each upper to lower vica versa)
swap = 'HEllo , SHivanANSH'
c = swap.swapcase()
print(c)

# casefold() METHOD (it do work same as lower but minor diff is-)
c = swap.casefold()
print(c)

# MINOR DIFFERENCE 
a1 = 'heLLO'
a2 = 'HELLO'
print(a1 == a2)


T = True
F = False
if a1.lower() == a2.lower():
    print(T)
else:
    print(F)

b1 = 'Bu\u00DF'
print(b1)  # o/p Buß

b2 = 'Buss'
print(b1 == b2)
print(b1.lower() == b2.lower()) # False
print(b1.casefold() == b2.casefold())  #True

t = '\u01C6'
print(t)
print(t.upper())
print(t.title())

# isupper() METHOD 
print(string.isupper())
print(string2.isupper())
print(swap.isupper())
b = 'HELLO'
print(b.isupper())

# islower() METHOD
print(string.islower())
print(string2.islower())
print(swap.islower())

# istitle() METHOD
print(string.istitle())
print(string2.istitle())
print(swap.istitle())
print(b2.istitle())


# isalnum() METHOD (not consider space or any special char)
d = 'hello 5435'
print(d.isalnum())
print(b.isalnum())

# isalpha() METHOD (not consider space any char only alpha)
print(d)
print(string.isalpha())
print(b.isalpha())

# isspace() METHOD (consider only space even not empty str)
f = '   '
print(f.isspace())
f = ''
print(f.isspace())
print(b.isspace())

# isascii() METHOD (ASCII char consider like abc #@ etc)
print(string.isascii())
v = '`@ 4 - + = etc'
print(v.isascii())

# UNICODE 
uni_code = '\u03b1\u03b2\u03b3'
print(uni_code)
print(uni_code.isalpha())
print(uni_code.isalnum())
print(uni_code.isascii())

# isidentifire() METHOD (it check if literls or user_input follow varialbe rules then return in bool)
x = 'length_01'
y = '07_lenght'
z = 'length@_01'
print(x.isidentifier())
print(y.isidentifier())
print(z.isidentifier())
