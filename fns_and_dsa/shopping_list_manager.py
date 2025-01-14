#### APPROACH 1
# add items to the list, remove items, and display the current list.

# shopping_list = []

# Use a loop to continuously display a menu with options to the user until they choose to exit. The menu should offer options to add an item, remove an item, view the list, and exit.

#-------------------------------------------------------------------------

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list
    while True:
        display_menu()  # Display the menu options
        choice = input("Enter your choice: ")  # Prompt the user for their choice

        if choice == '1':  # Add an item to the shopping list
            item = input("Enter the item to add: ").strip()
            if item:  # Check if the input is not empty
                shopping_list.append(item)  # Add the item to the list
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("You entered an empty item. Please try again.")
        
        elif choice == '2':  # Remove an item from the shopping list
            if shopping_list:  # Check if the list is not empty
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:  # Check if the item exists in the list
                    shopping_list.remove(item)  # Remove the item from the list
                    print(f"'{item}' has been removed from the shopping list.")
                else:
                    print(f"'{item}' is not in the shopping list.")
            else:
                print("The shopping list is empty. Nothing to remove.")
        
        elif choice == '3':  # Display the shopping list
            if shopping_list:  # Check if the list is not empty
                print("\nYour Shopping List:")
                for index, item in enumerate(shopping_list, start=1):  # Enumerate for a numbered list
                    print(f"{index}. {item}")
                print()  # Add a blank line for better readability
            else:
                print("Your shopping list is empty.")
        
        elif choice == '4':  # Exit the program
            print("Goodbye!")
            break  # Exit the loop and end the program
        
        else:  # Handle invalid input
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


