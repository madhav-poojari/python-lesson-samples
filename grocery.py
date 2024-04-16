# Grocery

print("Welcome to your Grocery List!")

grocery_list = []

while True:
    print("\nMenu:")
    print("1. View Grocery List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        if grocery_list:
            print("Grocery List:")
            for item in grocery_list:
                print("-", item)
        else:
            print("Grocery List is empty!")
    elif choice == '2':
        item = input("Enter item to add: ")
        grocery_list.append(item)
        print("Item added to Grocery List.")
    elif choice == '3':
        item = input("Enter item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print("Item removed from Grocery List.")
        else:
            print("Item not found in Grocery List.")
    elif choice == '4':
        print("Thank you for using your Grocery List!")
        break
    else:
        print("Invalid choice!")
