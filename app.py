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
                            contact_no_3_1 = contact_no_3.lower().strip()
                            if contact_no_3 == "yes":
                                update_contact()
                            else:
                                print("Failed to add the contact")
                                break
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
                                print("Failed to add the contact")
                                break
                        else:
                            print("Failed to add the contact")
                            break
                else:
                    print("Enter a 10-digit number")
                    print("Failed to add the contact")
                    break
            else:
                print("Enter a proper contact number")
                print("Failed to add the contact")
                break
            b+=1
            print("Contact added successfully")
    def update_contact():
        if Input_1 in update_contacts:
            update = input("Whose contact do you want to update: ")
            update_1 = update.lower().strip()
            if update_1 in my_dict.keys():
                update_2 = input("Do you want to update the contact or the contact number: ")
                update_2_1 = update_2.lower().strip()
                if "contact" in update_2_1:
                    update_3 = input("Enter the contact name: ")
                    if update_3 not in my_dict.keys():
                        my_dict[update_3] = my_dict.pop(update_1)
                        print("Contact updated successfully")
                    else:
                        print("You already have saved a contact by this name")
                        print("Update failed")
                else:
                    pass
                if "number" in update_2_1:
                    update_4 = input("Enter the contact number")
                    if update_4 not in my_dict.values():
                        my_dict[update_1] = update_4
                        print("Contact updated successfully")
                    else:
                        print("You already have saved a contact by this number")
                        print("Update failed")
                else:
                    pass
            else:
                print("Enter an appropriate contact name")
                print("Update failed")
        else:
            print("Enter an appropriate contact number")
            print("update failed")

    if Input_1 in add_contacts:
        add_contact()
    if Input_1 in update_contacts:
        update_contact()