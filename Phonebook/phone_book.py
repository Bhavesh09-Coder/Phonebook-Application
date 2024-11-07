import pickle

phone_book = {}

def load_contacts():
    global phone_book
    try:
        with open('phone_book.pkl', 'rb') as file:
            phone_book = pickle.load(file)
        print("Contacts loaded successfully.")
    except FileNotFoundError:
        print("No saved contacts found. Starting with an empty phone book.")

def save_contacts():
    with open('phone_book.pkl', 'wb') as file:
        pickle.dump(phone_book, file)
    print("Contacts saved successfully.")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    phone_book[name] = phone
    print(f"Contact {name} added successfully.")

def search_contact():
    name = input("Enter the name of the contact to search: ")
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print(f"Contact {name} not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in phone_book:
        del phone_book[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

def edit_contact():
    name = input("Enter the name of the contact to edit: ")
    if name in phone_book:
        new_phone = input("Enter the new phone number: ")
        phone_book[name] = new_phone
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")

def display_contacts():
    if phone_book:
        print("All contacts:")
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts in phone book.")
