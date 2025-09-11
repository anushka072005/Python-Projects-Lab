import time 

name = input('Enter Your Name: ')
print('Hello', name, 'Welcome to KBC :-) \n')

print(name, 'Are you ready for KBC?\n')
answer = input('Give your Answer Yes or No: ')
 
if answer.lower() == 'yes':
    print('\nStart Now...\nYour First Question is here...\n')
    time.sleep(2) 
    question = 'Question 1) Which function is used for taking input from user?'
    print(question)
    time.sleep(2)  

    options = ['(a) print', '(b) input', '(c) index', '(d) append']
    for opt in options: 
       print(opt)
       time.sleep(1)

    ans = input('Enter your answer: ')
    print("\nWait For Result...\n")
    time.sleep(2) 

    if ans.lower() == 'input':
        print('🎉 Congratulations! This is the right answer, you earned ₹10,000!')
        time.sleep(2)

        # Second question
        print('\nYour Second question is here...\n')
        question = 'Question 2) Which function is used for displaying the output?'
        print(question)
        time.sleep(2)

        for opt in options: 
           print(opt)
           time.sleep(1)

        ans = input('Enter your answer: ')
        print("\nWait For Result...\n")
        time.sleep(2)    
   
        if ans.lower() == 'print':
            print('🎉 Congratulations! This is the right answer, you earned ₹20,000!')
            time.sleep(2)

            # Third question
            print('\nYour Third question is here...\n')
            question = 'Question 3) Which function is used to add element at the end of a list?'
            print(question)
            time.sleep(2)

            for opt in options: 
                print(opt)
                time.sleep(1)

            ans = input('Enter your answer: ')
            print("\nWait For Result...\n")
            time.sleep(2)    
   
            if ans.lower() == 'append':
               print('🎉 Congratulations! This is the right answer, you earned ₹30,000!')
            else:
               print('❌ Wrong Answer! Better luck next time.')
        else:
            print('❌ Wrong Answer! Better luck next time.')
    else:
        print('❌ Wrong Answer! Better luck next time.')
else:
    print('\n🙏 Thank you for coming to KBC!')
