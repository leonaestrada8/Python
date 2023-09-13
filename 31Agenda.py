# 3.1 - AGENDA
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def find_contact_by_name(self, name):
        return next((contact for contact in self.contacts if contact.name == name), None)

    def update_contact(self, name, new_contact):
        index = next((i for i, contact in enumerate(self.contacts) if contact.name == name), None)
        if index is not None:
            self.contacts[index] = new_contact

    def delete_contact(self, name):
        index = next((i for i, contact in enumerate(self.contacts) if contact.name == name), None)
        if index is not None:
            self.contacts.pop(index)

    def print_contacts(self):
        print("Contatos:")
        for contact in self.contacts:
            print(f"Nome: {contact.name}, Telefone: {contact.phone}, Email: {contact.email}")

contact1 = Contact("Alice", "123-456", "alice@example.com")
contact2 = Contact("Bob", "789-123", "bob@example.com")

manager = ContactManager()
manager.add_contact(contact1)
manager.add_contact(contact2)
manager.print_contacts()

alice = manager.find_contact_by_name("Alice")
print("Encontrou:", alice.name, alice.phone, alice.email)

manager.update_contact("Alice", Contact("Alice", "111-222", "alice@new.com"))
manager.print_contacts()

manager.delete_contact("Alice")
manager.print_contacts()
