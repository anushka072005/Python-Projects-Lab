def Restaurant():
    items = [] 
    for i in range(4):     
        item = input("Enter item name : ")  
        price = input("Enter item price : ")  

        totalLen = len(item) + len(price)
        desh = 20 - totalLen

        output = f"{item}{'-' * desh}${price}"
        items.append(output)

    print("\n----- MENU -----")

    for i in items:
        print(i)    

Restaurant()


