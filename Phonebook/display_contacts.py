# phonebook/display_contacts.py

def display_contacts(phone_book):
    if phone_book:
        print("All contacts:")
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts in phone book.")
