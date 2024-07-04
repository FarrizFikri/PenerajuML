class InventoryManager:
    def __init__(self, filename):
        self.filename = filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        try:
            open(self.filename, 'a').close()  # Create the file if it does not exist
        except Exception as e:
            print(f"An error occurred while ensuring the file exists: {e}")

    def add_item(self, item_name, quantity):
        try:
            with open(self.filename, 'a') as file:
                file.write(f"{item_name}|{quantity}\n")
        except Exception as e:
            print(f"An error occurred while adding the item: {e}")

    def list_items(self):
        try:
            with open(self.filename, 'r') as file:
                items = file.readlines()
            for item in items:
                item_name, quantity = item.strip().split('|')
                print(f"Item: {item_name}, Quantity: {quantity}")
        except Exception as e:
            print(f"An error occurred while listing the items: {e}")

    def update_item(self, item_name, new_quantity):
        try:
            with open(self.filename, 'r') as file:
                items = file.readlines()
            updated = False
            with open(self.filename, 'w') as file:
                for item in items:
                    name, quantity = item.strip().split('|')
                    if name == item_name:
                        file.write(f"{name}|{new_quantity}\n")
                        updated = True
                    else:
                        file.write(f"{name}|{quantity}\n")
            if not updated:
                print(f"Item '{item_name}' not found in inventory.")
        except Exception as e:
            print(f"An error occurred while updating the item: {e}")

    def menu(self):
        while True:
            print("\nInventory Menu")
            print("1. Add Item")
            print("2. List Items")
            print("3. Update Item")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                item_name = input("Enter item name: ")
                quantity = int(input("Enter quantity: "))
                self.add_item(item_name, quantity)
            elif choice == '2':
                self.list_items()
            elif choice == '3':
                item_name = input("Enter the name of the item to update: ")
                new_quantity = int(input("Enter the new quantity: "))
                self.update_item(item_name, new_quantity)
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

# Usage example
inventory_manager = InventoryManager('inventory.txt')
inventory_manager.menu()
