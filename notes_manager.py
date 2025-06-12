import os

FILENAME = "notes.txt"

def show_menu():
    print("\n--- Notes Manager ---")
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Delete all notes")
    print("4. Exit")

def add_note():
    note = input("\nEnter your note: ")
    try:
        with open(FILENAME, "a") as file:
            file.write(note + "\n")
        print("Note saved successfully.")
    except Exception as e:
        print("An error occurred while saving the note:", e)

def view_notes():
    try:
        with open(FILENAME, "r") as file:
            content = file.read()
            if content.strip() == "":
                print("No notes available.")
            else:
                print("\n--- All Notes ---")
                print(content)
    except FileNotFoundError:
        print("No notes file found. Please add a note first.")

def delete_notes():
    confirm = input("Are you sure you want to delete all notes? (yes/no): ").lower()
    if confirm == "yes":
        try:
            os.remove(FILENAME)
            print("All notes deleted.")
        except FileNotFoundError:
            print("No notes file to delete.")
    else:
        print("Deletion cancelled.")

# Main program loop
while True:
    show_menu()
    choice = input("Select an option (1-4): ").strip()

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_notes()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please choose between 1 and 4.")
