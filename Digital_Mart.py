from MART_MODULE import *

##---------------------------Digital Mart-------------------------------##

print("============= Mart Items =============")

##--------------------------Lists of Items------------------------------##

menu()

list_of_items = ["Potatoes","Tomatoes","Bananas","Avacado","Cauliflower"]
list_of_price = [80,67,100,500,40]

cart = []                                                                                # Cart
print("_"*60)
n = int(input("Enter the number of items you want to purchase: "))
print("_"*60)
while n != 0:
    if n < 0:

        print("_"*60)
        print("The number of items cant be negative.")
        print("_"*60)
        n = int(input("Enter the number of items you want to purchase: "))
        print("_"*60)
        continue

    while n != 0:

        print("_"*60)
    
        a = int(input("Enter serial number of the item which you want to purchase: "))
        print("_"*60)

        if a >= 6 or a-1 < 0:                                                            # Here I converted my indexing as index[0] is the first item.
            print("_"*60)
            print("Please select items from the list only. ")
            print("_"*60)
            continue
        while a >= 6 or a-1 < 0:
            print("_"*60)
            a = int(input("Enter serial number of the item which you want to purchase: "))
            print("_"*60)
            continue
        if a >= 6 or a-1 < 0:
            print("_"*60)
            print("Please select items only from the list. ")
            print("_"*60)
            continue
        print("_"*60)
        print(list_of_items[a-1]," has been added to cart.")
        print("_"*60)

        cart.append(list_of_items[a-1])

        n -= 1

print("_"*60)
final = input("Before finalising your order , do you want to remove or add any food items?(y/n): ")
print("_"*60)
i = 1

while i == 1 :

    if final == "y":

        add(cart,list_of_items)
        remove(cart,list_of_items)
    print("_"*60)
    i = int(input("Before finalising your order, do you want to remove or add any food items again? ( Enter 1 to continue, 0 to exit): "))
    print("_"*60)
if cart == []:
    print("_"*60)
    print("Please enter a valid item number.")
    print("_"*60)
else:
    print("_"*60)
    print("Your final cart is :", cart,"\n")
    print("_"*60)

bill_and_discount(list_of_items,list_of_price,cart)