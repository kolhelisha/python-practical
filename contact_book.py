contacts = {}
num = int(input("Enter the number of contacts you want to add:"))
for i in range(num):
    name = input("Enter the name of the contact:")
    phone = input("Enter the phone number of the contact: ")
    contacts[name] = phone

print("\n Contact List:")
print("----------------------")
for name, phone in contacts.items():
    print(name, ":", phone)

search_name = input("\n Enter the name of the contact you want to search for:")
if search_name in contacts:
    print("Phone number of", search_name, "is:", contacts[search_name])
else:
    print("Contact not found.")