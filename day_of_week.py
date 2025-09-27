day = int(input('Enter day number : '))

match day: 
  
    case 1: 
        print('Sunday')
    case 2:
        print("Monday")
    case 3:    
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thusday")
    case 6:
        print("Friday")
    case 7:
        print("Saterday")
    case _ :
        print('holiday')
