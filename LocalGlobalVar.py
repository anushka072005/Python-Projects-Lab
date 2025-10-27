# x = 4
# print(x)

# def hello():
#     x = 5
#     y = 9
#     print(f"the local x is {x}")
#     print("hello harry")

# print(f"the global x is {x}")
# hello()
# x = 5
# print(f"the global x is {x}")
# # print(y)  # this will cause an error because y is a local variable and is not accessible outside of the function

x = 10
def my_func():
    global x
    x = 99
    y = 5
    print(y)

my_func()
print(x)
# print(y)