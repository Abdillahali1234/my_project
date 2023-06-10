available_items = {
'iPhone 13': {'price': 1000, 'quantity': 10},
'MacBook Pro': {'price': 2000, 'quantity': 5},
'AirPods Pro': {'price': 250, 'quantity': 2},
'iPad Pro': {'price': 800, 'quantity': 15},
'Apple Watch Series 7': {'price': 600, 'quantity': 3},
}
print("Welcome to Codezilla Store!")
menu_message = """
What would you like to do?
1. View Available Items
2. View Cart
3. Total Cart Price
4. Clear Cart
5. Quit"""
cart={}
def print_fincation(available_items,qunitiy=False):
    if qunitiy==False:
        for i,iteam in enumerate(available_items):
            if available_items[iteam]["quantity"]==0: 
                print(f"{i+1}.{iteam}: ${available_items[iteam]['price']} (not Avalible)")
            else:
                print(f"{i+1}.{iteam}: ${available_items[iteam]['price']}")
    else:
        for i,iteam in enumerate(available_items): 
                print(f"{i+1}.{iteam}: ${available_items[iteam]['price']} quntity you buy from{iteam} is {available_items[iteam]['quantity']}")
              

def view_available_items(available_items,cart):
    print("Availaible iteam: ")
    print_fincation(available_items)
    try:    
        choice_iteam=int(input("number for the iteam purchase (enter 0 to return to preavus menu:  ) "))
    
        if choice_iteam==0:
            return
        elif choice_iteam >=1 and choice_iteam<=len(available_items):
            name_order=list(available_items.keys())[choice_iteam-1]
            available_quntity=available_items[name_order]['quantity']
            if available_quntity==0:
                print(f"sorry,{name_order} not avilable for now")
                return
            print(f"available quntity:{available_quntity} ")
            user_quntiity=int(input("please enter quntity you want: "))
            if user_quntiity>available_quntity:
                print(f"sorry,we only have {available_quntity} ")
                return
            else:
                info_iteam={name_order:{"price":available_items[name_order]["price"],"quantity":user_quntiity}}
                cart.update(info_iteam)
                available_items[name_order]["quantity"]-=user_quntiity
                print(f"{name_order} added successfuly to cart")
                # print(cart)
                # print(available_items[name_order])
        else:
            print(f"invalid number please enter number from 1 to {len(available_items)}")    
    except ValueError:
        print("enter the number for iteam integer not string")

def print_cart(cart,print_cart=False,re_total=False):
    total_price_for_cart=0
    for iteam in cart:
        salary=cart[iteam]["price"]
        quntity=cart[iteam]["quantity"]
        total_price_for_cart+=salary*quntity
        total_salary=salary*quntity
        if print_cart==True:
            print(f"{iteam}: ${salary} x {quntity} = ${total_salary:,.2f}")
            print("-"*20)
    if re_total==True:
        return total_price_for_cart
def View_Cart(cart):
    print("Cart: ")
    if not cart:
        print("no iteam in cart to view")
        return
    print_cart(cart,print_cart=True)
    total_cart_price=print_cart(cart,re_total=True)
    print(f"total price of cart: ${total_cart_price:,.2f}")

def view_total_cart_price(cart):
    print("-"*20)
    total_cart_price1=print_cart(cart,re_total=True)
    print(f"total cart price = ${ total_cart_price1:,.2f}")

def clear_cart(cart):
    masege="""1.enter to clear all cart
2.enter to clear specific iteam"""
    print(masege)
    choice=input("enter your chice please: ")
    if choice=="1":
        print("iteams in the cart before deleting: ")
        print_cart(cart,print_cart=True)
        total_price=print_cart(cart,re_total=True)
        print(f"total price of cart= ${total_price:,.2f}")
        question_to_confirm=input("are you sure you want to clear the cart? (y/n): ")
        if question_to_confirm=="y":
            cart.clear()
            print("card has been cleared successfuly")
        elif question_to_confirm=="n":
            print("card has not been cleared successfuly")
            return    
        else:
            print("invalid choice")
            clear_cart(cart)
    elif choice=="2":
        print_fincation(cart,qunitiy=True)
        number_iteam=int(input("enter number of iteam you want delete (enter 0 to return main menu): " ))


def main():
    while True:
        print(menu_message)
        user_choice=input("enter your choice please: ")
        if user_choice=="1":
            view_available_items(available_items,cart)
        elif user_choice=="2":
            View_Cart(cart)
        elif user_choice=="3":
            view_total_cart_price(cart)
        elif user_choice=="4":
            clear_cart(cart)
        elif user_choice=="5":
            break
        else:
            print("please enter number from 1 to 5 ")   


main()