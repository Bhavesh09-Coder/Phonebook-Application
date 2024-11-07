# main.py

from Phonebook.add_contact import add_contact
from Phonebook.search_contact import search_contact
from Phonebook.delete_contact import delete_contact
from Phonebook.edit_contact import edit_contact
from Phonebook.display_contacts import display_contacts


def phone_book_app():
    phone_book = {}

    while True:
        print("\nPhone Book Menu:")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. Edit contact")
        print("5. Display all contacts")
        print("6. Exit")
        
        choice = input("Choose an option (1/2/3/4/5/6): ")
        
        if choice == '1':
            add_contact(phone_book)
        elif choice == '2':
            search_contact(phone_book)
        elif choice == '3':
            delete_contact(phone_book)
        elif choice == '4':
            edit_contact(phone_book)
        elif choice == '5':
            display_contacts(phone_book)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    phone_book_app()
