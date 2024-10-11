# FIND THE FACTORS OF A NUMBER.
n = int(input("enter the num : "))
for i in range(1,n+1):
    if n % i == 0:
        print(i)
