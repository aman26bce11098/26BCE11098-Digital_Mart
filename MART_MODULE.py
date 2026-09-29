def menu():
    print('''                                                                               
    \tItems\t\tQty.\tPrice\n
    1:\tPotatoes\t1kg\t80rs
    2:\tTomatoes\t1kg\t67rs
    3:\tBananas\t\t1doz.\t100rs
    4:\tAvacado\t\t1kg\t500rs
    5:\tCauliflower\t1kg\t40rs\n
    Spend-Based Discounts:- Spendings greater than 500 or 1000 will get '5%' - '10%', Extra discount
    ''')



def add(cart,list_of_items):
    print("_"*60)
    edit_add = input("Do you want to add any food items? (y/n): ")
    print("_"*60)

    if edit_add == "y":
        print("_"*60)
        new_add = int(input("Enter what you want to order: "))
        print("_"*60)

        if new_add in (1,2,3,4,5):
            print("_"*60)
            print(f"{list_of_items[new_add-1]} has been added to cart.")
            print("_"*60)
            cart.append(list_of_items[new_add-1])
        else:
            print("_"*60)
            print("Number should be in range 1 to 5")
            print("_"*60)

def remove(cart,list_of_items):
        print("_"*60)
        edit_remove = input("Do you want to remove any food items? (y/n): ")
        print("_"*60)
        if edit_remove =="y": 
            print("_"*60)
            new_remove = int(input("Enter what you want to remove : "))
            print("_"*60)
            if new_remove in (1,2,3,4,5):
                print("_"*60)
                print(f"{list_of_items[new_remove-1]} has been removed from cart.")
                print("_"*60)
                cart.remove(list_of_items[new_remove-1])
            else:
                print("_"*60)
                print("Number should be in range 1 to 5")
                print("_"*60)

def bill_and_discount(list_of_items,list_of_price,cart):

    y = []

    print("============= Bill ==============\n")
    print("Items\t\tQty.\n")
    print("_"*60)
    for i in cart :
        if i not in y :
            print(f"{i} \tx{cart.count(i)}")
            y.append(i)

    expense= 0

    for i in y:
        expense += cart.count(i) * list_of_price[list_of_items.index(i)]
    print("_"*60)
    print("Your total expense is :",expense)
    print("_"*60)
    if expense >= 500 and expense < 1000:
        print("_"*60)
        print("Congratulations! for getting 5%, Extra discount on your purchase")
        print("Discounted total expense: ", expense - (expense * 5/100))
        print("_"*60)
    elif expense >= 1000:
        print("_"*60)
        print("Congratulations!!! for getting 10%, Extra discount on your purchase")
        print("Discounted total expense: ", expense - (expense * 10/100))
        print("_"*60)