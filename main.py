from phone_book import add_contact, search_contact, delete_contact, edit_contact, display_contacts, load_contacts, save_contacts

def phone_book_app():
    load_contacts()  # Load contacts at the start of the application
    
    while True:
        print("\nPhone Book Menu:")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. Edit contact")
        print("5. Display all contacts")
        print("6. Save contacts")
        print("7. Exit")
        
        choice = input("Choose an option (1/2/3/4/5/6/7): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            save_contacts()
        elif choice == '7':
            save_contacts()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    phone_book_app()
