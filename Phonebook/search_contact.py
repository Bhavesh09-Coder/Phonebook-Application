# phonebook/search_contact.py

def search_contact(phone_book):
    name = input("Enter the name of the contact to search: ")
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print(f"Contact {name} not found.")
