# 3) CHECK IF THE PASSWORD AND CONFIRM PASSWORD ARE SAME
password = input('Enter password : ')   
confirm_password = input('Enter confirm password : ')
 
if password == confirm_password: 
    print('Yes, they are matching') 
 
else:
    if password.casefold() == confirm_password.casefold():
        print('Please check for the cases and try again')
    else:
        print('No they are not matching try again')
         
