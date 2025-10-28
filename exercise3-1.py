questions = [
    ["What is the correct file extension for Python files?", ".py", ".pt", ".pyt", ".pyth", 1],
    ["Which keyword is used to define a function in Python?", "def", "func", "define", "function", 1],
    ["Which of the following is used to display output in Python?", "echo()", "print()", "display()", "write()", 2],
    ["What is the correct way to start a comment in Python?", "// comment", "/* comment */", "# comment", "-- comment", 3],
    ["What data type is the result of this expression: 3 + 4.0 ?", "int", "float", "str", "bool", 2],
    ["Which of the following is NOT a Python data type?", "int", "float", "double", "str", 3],
    ["What is the output of: print(2 * 3 ** 2) ?", "36", "18", "12", "9", 2],
    ["Which of these is used to take input from user in Python?", "input()", "scan()", "get()", "enter()", 1],
    ["Which operator is used for exponentiation in Python?", "^", "**", "//", "%%", 2],
    ["What will be the output of: print(len('Python')) ?", "5", "6", "7", "8", 2],
    ["What will be the output of print(type([])) ?", "<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>", 1],
    ["Which of these is an immutable data type in Python?", "list", "set", "tuple", "dictionary", 3],
    ["What is the output of print(10 // 3) ?", "3.33", "3", "3.0", "Error", 2],
    ["Which keyword is used to handle exceptions in Python?", "try", "except", "catch", "handle", 2],
    ["What is the correct syntax to import the math module?", "import.math", "math.import", "from math import", "import math", 4],
    ["Which function converts a string into an integer in Python?", "int()", "str()", "float()", "input()", 1]
]    
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 30000000, 50000000, 70000000]

money = 0
safe_money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nQuestion {i+1} for Rs. {levels[i]}")
    print(question[0])
    print(f"1. {question[1]}         2. {question[2]}" )
    print(f"3. {question[3]}         4. {question[4]}" )
    try:
        reply = int(input("Enter your answer (1-4) or 0 to quit! : "))
    except ValueError:
        print("Invalid input! Please enter a number between 0 and 4.")
        continue

    if(reply == 0):
        money = levels[i-1]
        break

    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}\n\n")
        money = levels[i]

        if(i==4):
            safe_money = 10000
        elif(i==9):
            safe_money = 320000
        elif(i==14):
            safe_money = 1000000
        elif(i==16):
            safe_money = 7000000        
    else:
        print("Wrong answer!")
        money = safe_money
        break

print(f"\n Your take home money is {money}")


