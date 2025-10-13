# try:
#     a = int(input("Enter the number : "))
#     print(f"Multiplication table of {a} is ")

#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print(e)

# print("Some imp lines of code")        
# print("End of program")


try:
    num = int(input("Enter an index : "))
    a = [6,3,5,8]
    print(a[num])
except ValueError:
    print("Value Error")
except IndexError:
    print("Index Error")

print("End of program")