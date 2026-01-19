# username = "chaiorcode"    # global var

# def func():
#     # global username
#     # username = "chai"  #local var
#     print(username)
#     # global username
    
# print(username)
# func()    


x = 99
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# NOTE = AVOID OVER WRITE GLOBAL VARIABLE

# def func3():
#     global x
#     x = 88

# func3()
# print(x)    

# NOTE - f1 is inside the f2 so first it access the inner var but if inner var not present so it will print outer ko
# def f1():
#     x = 88
#     def f2():
#         print(x)    # 88
#         pass
#     f2()
# f1()     

# print(x)  # 99

# NOTE-  chaicoder(2) returns the inner function actual, The inner function remembers the value of num = 2, Even after chaicoder finishes execution, num is still accessible
# def chaicoder(num):
#     def actual(x):
#         return x ** num   # 3 ** 2
#     return actual

# f = chaicoder(2)
# g = chaicoder(3)

# print(f(3))  # x = 3
# print(g(3))  # x = 3