# STRING IN PYTHON
s1 = 'HELLO'
s2 = "hello"
s3 = '''Hello
       How are you'''

print(s1,s2,s3)
print(type(s3))
print(len(s2))
# STRING SLICING 
# POSITIVE INDEXING
print(s1[0])
print(s1[4])
print(s1[0:])
print(s1[:len(s1)])
# NEGATIVE INDEXING
print(s3[-3:])
print(s1[:])
print(len(s3))
print(s3[-8:-1])

# ACCESSING EACH ELEMENT THROUGH FOR LOOP
for char in s1:
    print(char)

# CONCATENATION THE STRING
s1 = 'MY'
s2 = 'BOY'
s3 = s1 + s2
print(s3)
s4 = 75
# s3 = s1 + s4 # TypeError: can only concatenate str (not "int") to str
s3 = s1 + str(s4) # TYPECAST INTO STR
print(s3)

# REPETITION OF STRING
R = ' '.join([s1] * 3)
print(R)
# R2 = s1 * 3.1
# print(R2) #TypeError: can't multiply sequence by non-int of type 'float'

# INDEXIMG 
a = 'KAJU LAL'

for i in range(0,len(a)):
       print(a[i])

for i in range(len(a)-1,-1,-1):
       print(a[i])

for i in range(0,len(a),2):
       print(a[i])