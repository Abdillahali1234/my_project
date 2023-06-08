# A dictionary of available items
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


# greeting message
print("Welcome to Codezilla Store!")

# initialize the cart to an empty dictionary
cart = {}

# menu message
menu_message = """
What would you like to do?
1. View Available Items
2. View Cart
3. Total Cart Price
4. Clear Cart
5. Quit"""

# make a while loop to allow the user to continue shopping
while True:

    # print the menu message
    print(menu_message)

    # get the user's choice
    user_choice = input("Enter the number of your choice: ")

    # 1. if the user chose to view available items
    if user_choice == "1":
        # print the available items for the user to buy
        print("Available items:")
        # loop through avaialble items with enumerate and print them
        for i, item in enumerate(available_items):
            # get the price of the item
            item_price = available_items[item]['price']

            # get the quantity of the item
            item_quantity = available_items[item]['quantity']

            # check if the item is NOT Available
            if item_quantity != 0:
                # print the item and its price
                print(f"{i+1}. {item}: ${item_price}")
            else:
                # print the item and its price and that it is not available
                print(f"{i+1}. {item}: ${item_price} (Not Available)")
            

        # get the item the user wants to purchase
        item_number = int(input("Enter the number of the item you want to purchase \
(Enter 0 to return to previous menu): "))

        # if the user entered 0, return to the previous menu
        if item_number == 0:
            continue

        # get the order name from the item number
        order_name = list(available_items.keys())[item_number-1]
       
       
        # if the item is not available, print a message, and do not add to the cart 
        available_quantity = available_items[order_name]['quantity']
        if available_quantity == 0:
            print("Sorry, This Item is Not Available Now.")
            continue

        # get the desired quantity from the user
        desired_quantity = int(input("Please, Enter the quantity: "))

        # if the desired quantity is not available, print a message, and do not add to the cart
        if desired_quantity > available_quantity:
            print(f"Sorry, we only have {available_quantity} of this item.")
            continue

        # get the price of the item
        order_price = available_items[order_name]['price']
        
        # get the quantity of the item
        order_quantity = cart.get(order_name, {}).get('quantity', 0) + desired_quantity

        # create a dictionary for the order info
        order_info = {order_name: {'price': order_price, 'quantity': order_quantity}}

        # add the order info to the cart
        cart.update(order_info)

        # Confirm that the item has been added to the cart
        print(f"{order_name} has been added to cart successfully.")        

        # subtract desired quantity from the store's quantity
        available_items[order_name]['quantity'] -= desired_quantity

 
    # 2. if the user chose to view cart
    elif user_choice == "2":
        # print the cart
        # print the cart else print no items have been bought
        if cart:
            # format >>> iPhone 13: $1000 x 2 = $2000
            print("Cart:")
            print("-"*20)
            for item_name in cart:
                item_price = cart[item_name]['price']
                item_quantity = cart[item_name]['quantity']

                # total price of the item
                total_item_price = item_price * item_quantity
                print(f"{item_name}: ${item_price:,.2f} x {item_quantity} = ${total_item_price:,.2f}")

        else:
            print("No items have been bought.")

        # a list to store the total price of each item in the cart
        lst_total_item_price = [cart[item_name]['price'] * cart[item_name]['quantity'] for item_name in cart]

        # sum all items in the cart to get the total price of the cart
        total_price_of_cart = sum(lst_total_item_price)
        print("-"*20)
        print(f"Total Cart Price: ${total_price_of_cart:,.2f}")

    # 3. if the user chose to view total price of cart 
    elif user_choice == "3":
        # print the total price of the cart
        # a list to store the total price of each item in the cart
        lst_total_item_price = [cart[item_name]['price'] * cart[item_name]['quantity'] for item_name in cart]

        # sum all items in the cart to get the total price of the cart
        total_price_of_cart = sum(lst_total_item_price)
        print("-"*20)
        print(f"Total Cart Price: ${total_price_of_cart:,.2f}")


    # 4. if the user chose to clear cart
    elif user_choice == "4":
        # a confirmation message
        confirmation = input("Are you sure you want to clear the cart? (y/n): ").lower()

        # if the user did not confirm, return to the previous menu
        if confirmation != "y":
            continue

        # make the items available again 
        # by adding the quantity of the items in the cart to the available items
        for item_name in cart:
            available_items[item_name]['quantity'] += cart[item_name]['quantity']

        # clear the cart
        cart.clear()

        # print the cart is cleared
        print("Cart has been cleared successfully.")


    # 5. if the user chose to quit
    elif user_choice == "5":
        print("Thanks for choosing Codezilla!")
        break  


    # 6. if the user chose an invalid option
    else:
        print("Please enter a number between 1 and 5.")



# print the cart else print no items have been bought
if cart:
    # format >>> iPhone 13: $1000 x 2 = $2000
    print("Cart:")
    print("-"*20)
    for item_name in cart:
        item_price = cart[item_name]['price']
        item_quantity = cart[item_name]['quantity']

        # total price of the item
        total_item_price = item_price * item_quantity
        print(f"{item_name}: ${item_price:,.2f} x {item_quantity} = ${total_item_price:,.2f}")

else:
    print("No items have been bought.")
    


# a list to store the total price of each item in the cart
lst_total_item_price = [cart[item_name]['price'] * cart[item_name]['quantity'] for item_name in cart]

# sum all items in the cart to get the total price of the cart
total_price_of_cart = sum(lst_total_item_price)

# print the total price of the cart
print("-"*20)
print(f"Total Cart Price: ${total_price_of_cart:,.2f}")