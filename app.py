add_contacts = "add contacts"
search_contacts = "search contacts"
delete_contacts = "delete contacts"
view_contacts = "view contacts"
exit_app = "exit app"

a = 1
while a > 0:
    print("Welcome to contact book app")
    print("what do you want to do:-")
    print("add contacts")
    print("search contacts")
    print("delete contacts")
    print("view contacts")
    print("exit app")
    print()
    Input = input("")
    Input_1 = Input.strip()
    Input_1 = Input_1.lower()
    if Input_1 in add_contacts:
        add = int(input("How many contacts do you want to add: "))
        add +=1
        b = 1
        while b < add:
            contacts = input(f"Contact {b}: ")
            contact_no = input(f"Contact number {b}: ")
            contact_no_1 = contact_no.strip()
            contact_no_2 = len(contact_no_1)
            if contact_no_2 == 10:
                pass
            else:
                print("Enter a proper contact number")
            if contact_no_1.isdigit():
                pass
            else:
                print("Enter a 10-digit number")
            b+=1