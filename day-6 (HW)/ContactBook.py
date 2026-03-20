contacts = {
    "alice": {"phone":"9876543210","email":"alice@example.com"},
    "bob":   {"phone":"9123456789","email":"bob@example.com"},
}

def find_contact(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found"

print(find_contact(contacts, "alice"))
print(find_contact(contacts, "charlie"))  # not found