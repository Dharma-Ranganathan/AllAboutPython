
'''
Updating our grocery management using 
list of disctionaries.

'''

# declared as global variable to have access anywhere.
basket = []

"""
declaring functions over here for convenience...

needed functions are,
# display basket
# add to basket
# remove from basket
# say message
# check basket
"""

# say message to user

def say_message(message):
    print(message)
    
# check basket

def check_basket(key):
    keys = []
    for item in basket:
        for k in item.keys():
            keys.append(k)
    
    if key in keys:
        for item in basket:
            for k in item.keys():
                if k == key:
                    item[k] += 1
                    say_message(f"{key} added again")
                    return
    
    if key not in keys:
        json = {}
        json[key] = 1
        basket.append(json)
        say_message(f"{key} added to basket")
        
# display basket

def display_basket():
    if not basket:
        say_message("basket is empty, you can add one")
    else:
        for item in basket:
            for k,v in item.items():
                print(f"• {k} = {v}")
    

# add to basket

def add_to_basket():
    groceries = """
Available Groceries to buy
1. apple
2. orange
3. mango
4. return
"""
    while True: 
        print(groceries)
        choice = input("enter choice : ")
        if choice.isalpha():
            say_message("Kindly choose given choices")
            continue
        
        if choice == '1':
            if not basket:
                new = {}
                new['apple'] = 1
                basket.append(new)
                say_message("apple added to basket")
                continue
            
            check_basket("apple")
                    
        elif choice == '2':
            if not basket:
                new = {}
                new['orange'] = 1
                basket.append(new)
                say_message("orange added to basket")
                continue
            
            check_basket("orange")
            
        elif choice == '3':
            if not basket:
                new = {}
                new['mango'] = 1
                basket.append(new)
                say_message("mango added to basket")
                continue
            
            check_basket("mango")
            
        elif choice == '4':
            say_message("Returned Back...")
            break
        else:
            say_message("Invalid choice selection")
            continue
    
# remove from basket

def remove(key):
    for item in basket:
        for k in item.keys():
            if k== key:
                if item[k]==1:
                    basket.remove(item)
                    say_message(f"{key} removed")
                    continue
                item[k]-=1
                say_message(f"{key} removed")
                
def remove_from_basket():
    print("Available Groceries...")
    for item in basket:
        for k,v in item.items():
            print(f"• {k} = {v}")
            
    while True:
        print("print x to exit...")
        
        choice = input("item name to remove : ").lower()
        if choice.isnumeric():
            say_message("item name cannot be numbers")
            continue
        if choice == "apple":
            remove("apple")
        elif choice == "orange":
            remove("orange")
        elif choice == "mango":
            remove("mango")
        elif choice == "x":
            say_message("Exited...")
            break
        else:
            say_message("Invalid choice selection")
            continue

print("GROCERY MANAGEMENT")

while True:
    choices = """
1. view basket
2. add to basket
3. remove from basket
4. exit
"""
    print(choices)
    choice = input("enter choice : ")
    if choice.isalpha():
        say_message("Kindly choose given choices")
        continue
    if choice == '1':
        display_basket()
    elif choice == '2':
        add_to_basket()
    elif choice == '3':  
        if basket:
            remove_from_basket()
            continue
        say_message("Nothing in basket to remove, you can add one")
    elif choice == '4':
        say_message("Happy Shopping")
        break
    else:
        say_message("Invalid choice selection")
        continue
