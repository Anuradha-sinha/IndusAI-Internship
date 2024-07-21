class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print("Contact added!")

    def delete(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted!")
                return
        print("Contact not found.")

    def search(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        print("Contact not found.")

    def show_all(self):
        if len(self.contacts) == 0:
            print("No contacts to show.")
        else:
            for contact in self.contacts:
                print(contact)

def menu():
    book = ContactBook()

    while True:
        print("\nMenu")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Show All Contacts")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            book.add(name, phone, email)
        elif choice == '2':
            name = input("Enter name to delete: ")
            book.delete(name)
        elif choice == '3':
            name = input("Enter name to search: ")
            book.search(name)
        elif choice == '4':
            book.show_all()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
