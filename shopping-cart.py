cart = []

while True:
    print("\n1. Add item")
    print("2. View cart")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item: ")
        quantity = int(input("Enter number of items: "))
        price = float(input("Enter price of one item: "))

        cart.append({
            "name": item,
            "quantity": quantity,
            "price": price
        })

        print(quantity, item, "added to cart!")

    elif choice == "2":
        print("\nYour Cart:")

        if len(cart) == 0:
            print("Cart is empty!")

        else:
            total_bill = 0

            for item in cart:
                item_total = item["quantity"] * item["price"]
                total_bill += item_total

                print(
                    "-",
                    item["name"],
                    "x",
                    item["quantity"],
                    "= ₹",
                    item_total
                )

            print("----------------------")
            print("Total Bill: ₹", total_bill)

    elif choice == "3":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice!")
