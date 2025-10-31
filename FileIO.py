# READING A FILE
# f = open('myfile.txt', 'r')
# f = open('myfile.txt', 'rb')
# f2 = open('myfile2.txt', 'w')
# print(f)
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE
# f = open('myfile2.txt', 'w')
# text = f.write("Hello World!")
# print(text)
# f.close()

# APPENDING A FILE
# f = open('myfile2.txt', 'a')
# text = f.write(" How are you!")
# print(text)
# f.close()

# CREATING A FILE
# f = open('myfile2.txt', 'x')
# text = f.write(" How are you!")
# print(text)
# f.close()

# "WITH" Statement (dont need to close file)
# with open('myfile.txt', 'a') as f:
#     f.write("\nHey i am inside with")

# READLINE() AND 
# f = open('myfile.txt', 'r')
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line, type(line))
#         break


# f = open('myfile.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# EXAMPLE
# f = open('myfile3.txt', 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1  = int(line.split(",")[0])
#     m2  = int(line.split(",")[1])
#     m3  = int(line.split(",")[2])
    
#     print(f"Marks of student {i} in Maths is {m1*2}")
#     print(f"Marks of student {i} in English is {m2*2}")
#     print(f"Marks of student {i} in Hindi is {m3*2}")
#     print(line)

# WRITELINES() METHOD - {writelines() method does'nt add newlines chr bet str in sequence if you want to add newlines bet the str, you can use loop to write each str separately}
# f = open('myfile2.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

# USING LOOP
# f = open('myfiles.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# for line in lines:
#     f.write(line + '\n')
# f.close()    


# SEEK() AND TELL() METHOD
with open('myfile.txt', 'rb') as f:
    print(type(f))

    # move to 10th byte in the file 
    # f.seek(10)
    # print(f.tell())
    
    f.seek(5)
    print("Position after seek(5):", f.tell())

    f.seek(-3, 1)
    print("Position after seek(-3, 1):", f.tell())

    # read the next 5 bytes
    # data = f.read(7)
    # print(data)


