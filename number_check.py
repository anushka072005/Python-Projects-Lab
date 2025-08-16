a = int(input("Enter the num : "))
if a < 0:
    print("It is Negative!")
elif a > 0:
    print("It is Positive!") 
    if a <= 10:
        print("It is Between 0-10!")
    elif a <= 100:
        print("It is Between 11-100!")
    elif a <= 500:
        print("It is Between 101-500!")
    else:
        print("It is Out of 500!")
else:
    print("It is Zero!")
