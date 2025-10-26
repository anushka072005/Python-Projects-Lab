# MATCH CASE IS THE TYPE OF SWICH CASE
'''
lottry_num = int(input("Enter Number : "))
match lottry_num :
    case 13:
        print("Num is 13 you can get 300000 Congratulation !")
    case 19 :
        print("Num is 19 you can get 30000 Congratulation !")
    case 7 :
        print("Num is 7 you can get 3000 Congratulation !")   
    case _:
        print("Sorry",lottry_num, "Is Not a Lottry Ticket Be Try Thankyou !")
     '''



'''
x = int(input("Enter the number : "))

match x:
    case 0:
        print("Num is 0")
    case 4:
        print("Num is 4")   

    case _ if x!=90:     # It is a else part of match case
        print(x,"is not 90")     
    case _ if x!=80:
        print(x,"is not 80")
    case _:
        print(x)
'''


x = int(input("Enter : "))
match x :
    case 7 :
        print("Num is 7 you resive Lottry at First Position Congratulation !")
    case 67 :
        print("Num is 67 you resive Lottry at Second Position Congratulation !")
    case 46 :
        print("Num is 46 you resive Lottry at Third Position Congratulation !") 
    case _ :
        print("Thankyou")