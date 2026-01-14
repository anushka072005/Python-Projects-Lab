import math
# 1) Basic Function Syntax
# def square(num):
#     return num ** 2

# result = square(5)
# print(result)


# 2) Function with Multiple Parameters
# def sum(num1, num2):
#     return num1 + num2

# print(sum(10, 10))


# 3) Polymorphism in Functions
# def multiply(num1, num2):
#     return num1 * num2

# print(multiply(2, 5))
# print(multiply('a', 5))
# print(multiply(5, 'a'))


# 4) Function Returning Multiple Values
# def circle_stats(radius):
#     area =  math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
#     return area, circumference

# a, c = circle_stats(3)
# print("Area : ", round(a, 2), "Circumference : ", round(c, 2))    


# 5) Default Parameter Value
# def greets(name="shivansh"):
#     return "Hello, " + name + " !"

# print(greets("anushka"))


# 6) Lambda Function ("A Lambda func used only once")
# cube = lambda x: x ** 3
# print("cube:- ", cube(3))
# print("cube:- ", cube(5))


# 7) Function with *args
# def sum_all(*args):
#     # print(*args)
#     return sum(args)

# print(sum_all(1, 2))
# print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5))

"""
def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print("sum:-", sum_all(1, 2, 3))
"""

# 8. Function with **kwargs
