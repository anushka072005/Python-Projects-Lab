marks = [2, 12, 3, 99, 14, 53, 63]
for mark in marks:
    print(mark)
    if(mark == 3):
        print("Great Student")

# for index, mark in enumerate(marks):
#     print(index, mark)
#     if(index == 3):
        # print("Well Done roll number 3")

# You can give argument this enumerate(start = _ //i.e. 1,2 etc) func
for index, mark in enumerate(marks, start = 1):
    print(index, mark)
    if(index == 3):
        print("Well Done below")