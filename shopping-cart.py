cart = []

while True:
    print("\n1. Add item")
    print("2. View cart")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item: ")
        cart.append(item)
        print(item, "added to cart!")

    elif choice == "2":
        print("\nYour Cart:")
        for item in cart:
            print("-", item)

    elif choice == "3":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice!")
