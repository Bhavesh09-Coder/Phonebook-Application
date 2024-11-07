# phonebook/edit_contact.py

def edit_contact(phone_book):
    name = input("Enter the name of the contact to edit: ")
    if name in phone_book:
        new_phone = input("Enter the new phone number: ")
        phone_book[name] = new_phone
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")
