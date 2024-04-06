def add_item(shopping_list):
    added_item = input("Enter the item to add: ")
    shopping_list.append(added_item)
    print(shopping_list)
    print(f"{added_item} is added successfully to the shopping list")

def remove_item(shopping_list):
    remove_item = input("Enter the item to remove: ")
    if remove_item in shopping_list:
        shopping_list.remove(remove_item)
        print("Item removed successfully")
        print(shopping_list) 
    else:
        print(f"{remove_item} is not in the shopping list") 

def display_item(shopping_list):
    print("Items in the shopping list:")
    for item in shopping_list:
        print(item)

def checking_item(shopping_list): 
    item = input("Enter the item to check: ")                  
    if item in shopping_list:
        print(f"{item} is already in the shopping list")
    else:
        print(f"{item} is not in the shopping list")    

def main():
    shopping_list = []
    while True:
        print("------------ Shopping List ------------")
        print("1. Add item")
        print("2. Remove Item")
        print("3. Display items")
        print("4. Check list")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                add_item(shopping_list)
            elif choice == 2:
                remove_item(shopping_list)
            elif choice == 3:
                display_item(shopping_list)
            elif choice == 4:
                checking_item(shopping_list)
            elif choice == 5:
                print("\nHappy shopping!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
