# a = int(input("Enter any Value between 5 and 9 : "))

# if(a<5 or a>9):
#     raise ValueError("Value Should be between 5 and 9")
# else:
#     print(a)    


try:
    a = input("Enter any Value between 5 and 9 : ")
    if (a == 'quit'):
        print("you write Quit Thankyou")
    elif(int(a)<5 or int(a)>9):
        raise ValueError("Value Should be between 5 and 9...")
        print("Good : ",a)

except ValueError as e:
    print("Error :", e)        
