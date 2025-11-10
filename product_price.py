 # 2) DISPLAY DATA IN GIVEN FORMAT (25 LETTERS)
        # Product Name........Price 
        # Kathi role............100    
 
Product_name = input("Enter Product name : ")  
Price = input('Enter Price : ') 
 
total_len = len(Product_name) + len(Price)
left_space = 25 - total_len
dots = '.' * left_space

print(f'{Product_name}{dots}{Price}')
