available_items = {
    "Google Pixel 6a": {
        "price": 280,
        "quantity": 5
    },
    "SAMSUNG Galaxy S23 Ultra": {
        "price": 1200,
        "quantity": 3
    },
    "iPhone 13 Pro Max": {
        "price": 1300,
        "quantity": 2
    },
    "Xiaomi Redmi 9A": {
        "price": 100,
        "quantity": 4
    },
    "Huawei P50 Pro": {
        "price": 1000,
        "quantity": 1
    },
    "OnePlus 9 Pro": {
        "price": 800,
        "quantity": 1
    },
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
def print_fincation(available_items):
    for i,iteam in enumerate(available_items):
        print(f"{i+1}.{iteam}: ${available_items[iteam]['price']}")
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

def View_Cart():
     ...

def view_total_cart_price():
     ...

def clear_cart():
     ...


def main():
    while True:
        print(menu_message)
        user_choice=input("enter your choice please: ")
        if user_choice=="1":
            view_available_items(available_items,cart)
        elif user_choice=="2":
            View_Cart()
        elif user_choice=="3":
            view_total_cart_price()
        elif user_choice=="4":
            clear_cart()
        elif user_choice=="5":
            break
        else:
            print("please enter number from 1 to 5 ")   


main()