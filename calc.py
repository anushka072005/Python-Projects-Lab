# a = int(input ("Enter your fdigit : "))
# b = int(input ("Enter your ldigit : "))

# print( ' add   is = ' , a , "+",   b , ' = ' , a+b)
# print( ' sub   is = ' , a , "-",   b , ' = ' , a-b)
# print( ' mul   is = ' , a , "*"  , b , ' = ' , a*b)
# print( ' div   is = ' , a , "/"  , b , ' = ' , a/b)
# print( ' mod   is = ' , a , "%"  , b , ' = ' , a%b)

# print('foold  is = ' , a , "//"  , b , " = " , a//b)
# print('expon  is = ' , a , "**"  , b , " = " , a**b)

a = int(input("Enter your first digit: "))
b = int(input("Enter your second digit: "))

print("\n--- Results ---\n")
print(f"➕ Addition      : {a} + {b} = {a + b}")
print(f"➖ Subtraction   : {a} - {b} = {a - b}")
print(f"✖️ Multiplication: {a} * {b} = {a * b}")
print(f"➗ Division      : {a} / {b} = {a / b:.2f}")
print(f"🔢 Modulus       : {a} % {b} = {a % b}")
print(f"〽️ Floor Division: {a} // {b} = {a // b}")
print(f"✨ Exponent      : {a} ** {b} = {a ** b}")

print("\n----------------\n")
