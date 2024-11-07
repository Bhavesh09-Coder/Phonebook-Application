# phonebook/delete_contact.py

def delete_contact(phone_book):
    name = input("Enter the name of the contact to delete: ")
    if name in phone_book:
        del phone_book[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")
