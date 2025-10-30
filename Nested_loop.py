# PRACTICE
 
# for i in range(0,5):
#     for j in range(0,5):
#         print(i,j)

# for i in range(0,5):
#     for j in range(0,5):
#         print(i, j, end=" ")

# for i in range(0,5):
#     for j in range(0,5):
#         print(i, j, end= " ")  # end= using for space  
#     print(" ")  # for next line 


# PRINT i AND j WITH BRACKETS
# for i in range(0,5):
#     for j in range(0,5):
#         print('(',i, j,')', end=" ")
#     print(" ")


# ADD (i+j) MATRIX
# for i in range(0,5):
#     for j in range(0,5):
#         print('(', i+j ,')', end=" ")
#     print(" ")


""" PRINT THIS PETTERN
* * * * *  
* * * * *
* * * * *
* * * * *
* * * * *
"""
# SQUARE PATTERN (5x5)
# for i in range(0,5):
#     for j in range(0,5):
#         print('*', end=" ")
#     print(' ')

# DRAW PATTERNS USING SINGLE LOOP
# for i in range(0,5):
#     print('* ' * 5)


""" PRINT THIS PETTERN
*  *  *  *  *  
*  *  *  *  
*  *  *  
*  *  
*
"""
# for i in range(0,5):
#     for j in range(0,5):
#         if i <= j:
#             print('*', end=' ')
#     print('')

# DRAW PATTERNS USING SINGLE LOOP
# for i in range(5,0,-1):
#     print('* ' * i)

# Method-2
# for i in range(1,6):
#     for j in range(1,6-(i-1)):
#         print('*' , end=' ')
#     print(' ')    


""" PRINT THIS PETTERN
*
* * 
* * *
* * * *
* * * * *
"""
# for i in range(0,5):
#     for j in range(0,5):
#         if i >= j:
#             print('*', end=" ")
#     print('')

# DRAW PATTERNS USING SINGLE LOOP
# for i in range(1,6):
#     print('* ' * i)


# PRINT PATTERN USING STRING
# s1 = 'abc'
# s2 = 'xyz'

# for i in s1:
#     for j in s2:
#         print('[',i,',',j,']', end=' ')
#     print('')


# PRINT PRIME NUMBER FROM 1-100
# for n in range(1,100+1):
#     count = 0
#     for i in range(1,n+1):
#         if n % i == 0:
#             count += 1
#             if count == 2:
#                 print(n)

# DRAW PATTERNS USING SINGLE LOOP

# for i in range(0,5):
#     print('* ' * 5)

# for i in range(1,6):
#     print('* ' * i)

# for i in range(5,0,-1):
#     print('* ' * i)


for i in range(0,5):
    for j in range(0,5):
        if i > j:
            print('_')
        else:
            print('*')    

    print(' ')        
