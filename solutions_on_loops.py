# 1) Counting Positive Numbers
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# count = 0
# for i in numbers:
#     if i > 0:
#         count += 1
# print("positive numbers are : ", count)


# 2. Sum of Even Numbers
# number = int(input("Enter Number : "))
# sum_even = 0
# for i in range(1, number+1):
#     if i % 2 == 0:
#         # print(i)
#         sum_even += i
# print("Sum of even number is : ", sum_even)


# 3) Multiplication Table Printer
# num = int(input("Enter num : "))
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(f"{num} X {i} = {num*i}")


# 4) Reverse a String
# str = "Python"
# reversed_str = ""
# for char in str:
#     reversed_str = char + reversed_str 
# print(reversed_str)


# 5. Find the First Non-Repeated Character
# str = "anushka"
# for chr in str:
#     if str.count(chr) == 1:
#         print("char is :", chr)
#         break


# 6. Factorial Calculator
# num = 6
# count = 1
# fac = 1
# while count <= num:
#     fac = fac * count
#     count += 1
# print(fac)

# diff method (without count variable)
# num = 5
# fac = 1
# while num > 0:
#     fac = fac * num
#     num -= 1
# print(fac)    


# 7. Validate Input
# while True:
#     user_input = int(input("enter num : "))
#     if 1 <= user_input <= 10:
#     # if user_input >= 1 and user_input <= 10:
#         break
#     # print(user_input)

# 8) Prime Number Checker
# num = int(input("enter num : "))
# ans = True
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0 :
#             ans = False
#             break
# print(ans)           


# 9. List Uniqueness Checker
# items = ["apple", "banana", "apple", "orange", "mango"]
# unique_item = set()
# for item in items:
#     if item in unique_item:
#         print("Duplicate :", item)
#         break
#     unique_item.add(item)
# else:print("no duplicate")


# 10. Exponential Backoff
# import time
# wait_time = 1
# max_retries = 5
# attempts = 0
# while attempts < max_retries:
#     print("Attempts", attempts + 1, "- Wait time", wait_time)
#     time.sleep(wait_time)
#     wait_time *= 2
#     attempts += 1