# phonebook/add_contact.py

def add_contact(phone_book):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    phone_book[name] = phone
    print(f"Contact {name} added successfully.")
