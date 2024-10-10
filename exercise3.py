# Koun Banega Karodpati
import time 

name = input('Enter Your Name : ')
print('Hello',name,'Welcome... in KBC :-) \n')

print(name,'Are you ready for KBC ? \n')
answer = input('Give your Answer Yes or No : ')
 
if (answer == 'yes'):
    print('\nStart Now... \nYour First Question is front of you ...\n')
    time.sleep(4) 
    list1 = 'Question 1) Which function used for taking input from user ? '# first question
    print(list1)
    time.sleep(4)  

    items = ['(a) print', '(b) input', '(c) index', '(d) append']

    for item in items : 
       print(item)
       time.sleep(1)

    ans = input('Enter your answer : ')
    print("\nWait For Result...\n")
    time.sleep(4) 

    if (ans == 'input'):
        print('Congratulations(^▽^)\n This is right answer you earnt 10,000 (^∇^)')
        time.sleep(4)

        print('\nYour Second question is front of you ... ,\n')
        time.sleep(3)
        list1 ='Question 2) Which function is used for Displaying the output ? '#2nd question
        print(list1)
        time.sleep(4)

        for item in items : 
           print(item)
           time.sleep(1)

        ans = input('Enter your answer : ')
        print("\nWait For Result...\n")
        time.sleep(4)    
   
        if (ans == 'print'):
            print('Congratulations(^▽^) \n This is right answer you earnt 20,000 (^∇^)')
            time.sleep(4)

            print('\nYour Third question is front of you ... ,\n')
            time.sleep(3)
            list1 ='Question 3) Any one of these function that is used for adding element at the end of the Data Item ?'#3ndquestion
            print(list1)
            time.sleep(4)

            for item in items : 
                print(item)
                time.sleep(1)

            ans = input('Enter your answer : ')
            print("\nWait For Result...\n")
            time.sleep(4)    
   
            if (ans == 'append'):
               print('Congratulations(^▽^) \n This is right answer you earnt 30,000 (^∇^)')
        else:
            print('(╥_╥) Sorry...This is Wrong Answer\n')  
            print('You will try next time (^_^)\nThankyou for coming here')  
    else:
        print('(╥_╥) Sorry...This is Wrong Answer\n')  
        print('You will try next time (^_^)\nThankyou for coming here')
else :
    print('\nT H A N K  Y O U ( ͡❛ ͜ʖ ͡❛)╭∩╮ for coming here\n\n')    
