"""
simple grocery management using python

Understanding of lists and it's method, utilised conditional statements and loops concepts.
"""

basket = []

"""
defining functions over here...

# view basket - display_basket()

# add to basket - add_to_basket()

# remove from basket - remove_from_basket()

"""

# view basket

def display_basket():
    if(len(basket)):
        print("Available Groceries...")
        for item in basket:
            print(f"• {item}")
    else:
        print("basket is empty, add some groceries...")
        
# add to basket

def add_to_basket():
    available_products="""
1. apple
2. orange
3. mango
4. return
"""
    while True:
        print("Add Groceries to Basket")
        print(available_products)
        
        choice = input("choose item :")
        
        if choice.isalpha():
            print("kindly choose given choices")
            continue
        if choice == '1':
            basket.insert(0,"apple")
            print("apple added in basket")
        elif choice == '2':
            basket.insert(0,"orange")
            print("orange added in basket")
        elif choice == '3':
            basket.insert(0,"mango")
            print("mango added in basket")
        elif choice == '4':
            print("returned back...")
            break
        else:
            print("Invalid choice selection")
            continue

# remove from basket

def remove_from_basket():
    print("Available Groceries...")
    for item in basket:
        print(f"• {item}")
    
    while True:
        choice = input("name of an item to remove : ").lower()
        if choice.isnumeric():
            print(f"{choice} Numbers are restricted")
            continue
        if choice not in basket:
            print(f"{choice} is not in basket")
            continue
        basket.remove(choice)
        print(f"{choice} is removed from basket")
        break
    
     

print("••• GROCERY MANAGEMENT •••")

while True:
    
    operations = """
1. view basket
2. add to basket
3. remove from basket
4. exit
"""
    print(operations)
    
    choice = input("enter choice : ")
    if choice.isalpha():
        print("kindly choose given choices")
        continue
    
    if choice == '1':
        display_basket()
    elif choice == '2':
        add_to_basket()
    elif choice == '3':
        remove_from_basket()
    elif choice == '4':
        print('Happy Shopping...')
        break
    else:
        print("Invalid choice selection")
        continue
