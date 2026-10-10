
cart = []

while True:
    print("\n===== SHOPPING CART =====")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Generate Bill")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price of one item: "))

        cart.append({
            "name": name,
            "quantity": quantity,
            "price": price
        })

        print(name, "added to cart!")

    elif choice == "2":
        if len(cart) == 0:
            print("Cart is empty!")
        else:
            print("\nYour Cart:")
            for item in cart:
                print(
                    item["name"],
                    "x", item["quantity"],
                    "= Rs.", item["quantity"] * item["price"]
                )

    elif choice == "3":
        if len(cart) == 0:
            print("Cart is empty!")
        else:
            print("\nItems in Cart:")
            for item in cart:
                print("-", item["name"])

            remove_name = input("Enter item name to remove: ")
            found = False

            for item in cart:
                if item["name"].lower() == remove_name.lower():
                    cart.remove(item)
                    print(remove_name, "removed from cart!")
                    found = True
                    break

            if not found:
                print("Item not found!")

    elif choice == "4":
        if len(cart) == 0:
            print("Cart is empty! Cannot generate bill.")
        else:
            print("\n======= FINAL BILL =======")
            total_bill = 0

            for item in cart:
                item_total = item["quantity"] * item["price"]
                total_bill += item_total

                print(
                    item["name"],
                    "x", item["quantity"],
                    "Rs.", item["price"],
                    "=", "Rs.", round(item_total, 2)
                )

            print("Total Items:", len(cart))
            print("Final Bill: Rs.", round(total_bill, 2))

    elif choice == "5":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice! Try again.")
