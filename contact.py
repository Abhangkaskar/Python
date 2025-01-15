import json

# Initialize contacts
contacts = {}

# Load contacts from a file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            global contacts
            contacts = json.load(file)
            print("Contacts loaded successfully!")
    except FileNotFoundError:
        print("No saved contacts found. Starting fresh.")

# Save contacts to a file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)
    print("Contacts saved successfully!")

# Add a contact
def add_contact(name, number):
    contacts[name] = number
    print(f"Contact {name} added.")

# View all contacts
def view_contacts():
    if not contacts:
        print("No contacts yet!")
    else:
        for name, number in contacts.items():
            print(f"{name}: {number}")

# Search for a contact
def search_contact(name):
    if name in contacts:
        print(f"{name}'s number is {contacts[name]}")
    else:
        print(f"{name} not found in contacts.")

# Edit a contact
def edit_contact(name):
    if name in contacts:
        new_name = input("Enter new name (or press Enter to keep current name): ")
        new_number = input("Enter new number (or press Enter to keep current number): ")
        
        if new_name:
            contacts[new_name] = contacts.pop(name)
            name = new_name  # Update name if changed
        
        if new_number:
            contacts[name] = new_number
        
        print(f"Contact {name} updated!")
    else:
        print(f"{name} not found in contacts.")

# Delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"{name} not found in contacts.")

# Main program loop
load_contacts()  # Load contacts at the start

while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Save Contacts")
    print("7. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        add_contact(name, number)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == "4":
        name = input("Enter name to edit: ")
        edit_contact(name)
    elif choice == "5":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "6":
        save_contacts()
    elif choice == "7":
        save_contacts()
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
