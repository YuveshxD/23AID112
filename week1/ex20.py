#Program on Shopping list manager

shopping_list=[]

while True:
    #What Action needed
    print("Options: add,remove,show,quit")
    option=input("What You like to do in the shopping cart:").lower()

    #Add an item
    if option=="add":
        item=input("Enter the item name to add:").upper()
        shopping_list.append(item)
        print(item,"has been added.")
    
    #remove an item
    elif option=="remove":
        item=input("Enter the item name to remove:").upper()
        if item in shopping_list:
            shopping_list.remove(item)
            print(item,"has been removed.")
        else:
            print("Item not found in shopping cart")
    
    #show the list
    elif option=="show":
        if len(shopping_list)==0:
            print("shopping cart is empty.")
        else:
            print("---------Your Shopping Cart---------")
            print("Items:"+",".join(shopping_list))
    
    #quit.
    elif option=="quit":
        if len(shopping_list)==0:
            print("Thank You For Checking,Bye!!")
            break
        else:
            print("Thank You For Shopping,Bye!!")
            break

    #invalid option
    else:
        print("Invalid option,please try again.")
        