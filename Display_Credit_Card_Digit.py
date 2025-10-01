# 4) DISPLAY CREDIT CARD NUMBER.

print('Please Credit Card Number In This Format i.e. 1111 2222 3333 4444')

user_input = input('Enter credit card number : ')

last_4_digit = user_input[15:]

four = '*' * 4 + ' '

display = four * 3 + last_4_digit

print('Your Credit Card Number is : ', display)
        