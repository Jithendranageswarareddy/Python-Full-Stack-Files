contacts = []

#for adding contacts
def add_contact(**kwargs):
    contacts.append(kwargs)
    print("contact added successfully!\n")

#for viewing contacts
def view_contacts():
    if not contacts:
        print("no contacts found!\n")
        return
    print("\n -- All Contacts ---")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. Name:{contact['name']}, Phone:{contact['phone']}, Email:{contact['email']}")
        print()

#for searching contacts
def search_contact(name):
    found=list(filter(lambda c:c['name'].lower() ==name.lower(), contacts))
    if found:
        print("\n Contact Found:")
        for contact in found:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email:{contact['email']}")
    else:
        print("No ontacts found with that name")
    print()

#for deleting
def delete_contact(name):
    global contacts
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("contact deleted successfully!\n")
            return
    print("no contacts found.\n")

#task executin start from here
def menu():
    while True:
        print("=== Contact Book ====")
        print("1. Add contact")
        print("2. View Contact")
        print("3. Search contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = (input("Enter the choice from (1-5): ")).strip()

        if choice == '1':
            name=str(input("enter Name to add: "))
            phone = int(input("Enter Phone number: "))
            email = input("enter email: ")
            add_contact(name=name, phone=phone, email=email)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            name = input("enter name to search:")
            search_contact(name)

        elif choice == '4':
            name = input("enter contact to delete :")
            delete_contact(name)

        elif choice == '5':
            print("EXiting from search")
            break
        else:
            print("Invalid Choice. Try again.\n")

menu()
