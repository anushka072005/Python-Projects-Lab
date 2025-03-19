# 5) FIND USER-ID AND DOMAIN NAME FROM EMAIL.
email = input('Enter your email : ')   
check = email.index('@')
print("User ID is :",email[0:check] )
print("Domain name is :",email[check+1:len(email)] )
 
