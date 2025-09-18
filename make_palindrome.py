# 6) CONVERT STRING TO PALINDROME. 

string = input("enter string : ") 

reverseString = string[::-1]

if string == reverseString:
    print("palindrom")

else:
    convert = string + reverseString
    print("converted palindrom : " , convert) 
