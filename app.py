my_dict = {"Police" : 100 , "Ambulance" : 108, "Fire" : 101}
add_contacts = "add contacts"
search_contacts = "search contacts"
delete_contacts = "delete contacts"
view_contacts = "view contacts"
exit_app = "exit app"
update_contacts = "update conacts"

print("Welcome to contact book app")
a = 1
while a > 0:
    print("what do you want to do:-")
    print("add contacts")
    print("update contacts")
    print("search contacts")
    print("delete contacts")
    print("view contacts")
    print("exit app")
    print()
    Input = input("")
    Input_1 = Input.strip()
    Input_1 = Input_1.lower()
    def add_contact():    
        add = int(input("How many contacts do you want to add: "))
        add +=1
        b = 1
        while b < add:
            contacts = input(f"Contact {b}: ")
            contact_no = int(input(f"Contact number {b}: "))
            contact_no_1 = contact_no
            contact_no_2 = len(str(contact_no_1))
            if contact_no_2 == 10:
                if str(contact_no_1).isnumeric():
                    if contacts not in my_dict.keys():
                        if contact_no_1 not in my_dict.values():
                            my_dict[contacts] = contact_no_1
                            pass
                        else:
                            contact_no_3 = input("Do you want to update the contact")
                    else:
                        print("You already have saved a contact by this name")
                        contacts_1 = input("Do you want to change the name")
                        contacts_1_1 = contacts_1.lower().strip()
                        if contacts_1 == "yes":
                            contacts_2 = input("Enter the correct name")
                            if contacts_2 not in my_dict.keys():
                                my_dict[contacts_2] = contact_no_1
                                pass
                            else:
                                print("You already have saved a contact by this name")
                                break
                        else:
                            break
                else:
                    print("Enter a 10-digit number")
                    break
            else:
                print("Enter a proper contact number")
                break
            b+=1

    if Input_1 in add_contacts:
        add_contact()

