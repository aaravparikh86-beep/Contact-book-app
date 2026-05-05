my_dict = {"Police" : [100] , "Ambulance" : [108], "Fire" : [101]}
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
                            my_dict[contacts] = [contact_no_1]
                            pass
                        else:
                            contact_no_3 = input("Do you want to update the contact: ")
                            contact_no_3_1 = contact_no_3.lower().strip()
                            if contact_no_3_1 == "yes":
                                update_contact()
                            else:
                                print("Failed to add contact")
                    else:
                        print("You already have saved a contact by this name")
                        contacts_1 = input("Do you want to change the name: ")
                        contacts_1_1 = contacts_1.lower().strip()
                        if contacts_1_1 == "yes":
                            contacts_2 = input("Enter the correct name: ")
                            if contacts_2 not in my_dict.keys():
                                my_dict[contacts_2] = [contact_no_1]
                                pass
                            else:
                                print("You already have saved a contact by this name")
                                print("Failed to add the contact")
                                break
                        elif contacts_1_1 == "no":
                            multiple_contacts = input("Do you want to add multiple phone number for this contact: ")
                            multiple_contacts_1 = multiple_contacts.lower().strip()
                            if multiple_contacts_1 == "yes":
                                for keys, value in my_dict.items():
                                    if value == contact_no_1:
                                        break
                                my_dict[contacts].append(contact_no_1)
                                print("Contact added successfully")
                            else:
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
            print()
            print()


    def update_contact():
        update = input("Whose contact do you want to update: ")
        update_1 = update.lower().strip()
        if update_1.isalpha():
            update_5 = str(update_1)
            key = my_dict[update_5]
        elif update_1.isnumeric():
            update_5 = int(update_1)
            for key, value in my_dict.items():
                if value == update_5:
                    pass
                    break

        if update_5 in my_dict or update_5 in my_dict.values():
            update_2 = input("Do you want to update the contact or the contact number: ")
            update_2_1 = update_2.lower().strip()
            if "contact" in update_2_1:
                update_3 = input("Enter the contact name: ")
                if update_3 not in my_dict.keys():
                    my_dict[update_3] = my_dict.pop(key,None)
                    print("Contact updated successfully")
                else:
                    print("You already have saved a contact by this name")
                    print("Update failed")
            elif "number" in update_2_1:
                update_4 = int(input("Enter the contact number: "))
                if len(str(update_4)) == 10:
                    if str(update_4).isnumeric():
                        if update_4 not in my_dict.values():
                            my_dict[key] = update_4
                            print("Contact updated successfully")
                        else:
                            print("You already have saved a contact by this number")
                            print("Update failed")
                            pass
                    else:
                        print("Enter an appropriate contact number")
                        print("Update failed")
                        pass
                else:
                    print("Enter a 10 digit number")
                    print("Update failed")
                    pass
            else:
                print("Update failed")
                pass
        else:
            print("Enter an appropriate contact name or number")
            print("Update failed")
            print()
            print()


    def delete_contact():
        delete = input("Enter name or number to delete: ").strip()

        if delete in my_dict:
            del my_dict[delete]
            print("Contact deleted successfully")
            return

        if delete.isdigit():
            delete_1 = int(delete)

            for name, numbers in my_dict.items():
                if delete_1 in numbers:
                    numbers.remove(delete_1)

                    if not numbers:
                        del my_dict[name]

                    print("Number deleted successfully")
                    return

        print("There is no such contact in the contact book")

        print()
        print()

    
    def view_contact():
        print()
        e = 0
        keys = list(my_dict.keys())
        values = list(my_dict.values())

        while e < 3:
            print(keys[e])
            print(*values[e])
            print()
            e += 1

        new_dict_1 = my_dict.copy()
        new_dict_2 = {"Police" : [100] , "Ambulance" : [108], "Fire" : [101]}
        for key2 in new_dict_2:
            new_dict_1.pop(key2, None)


        sorted_dict = dict(sorted(new_dict_1.items()))

        repeated_letter = set()

        for bb, cc in sorted_dict.items():
            print()
            pass

            first_letter = bb[0]
            if first_letter not in repeated_letter:
                print(first_letter)
                repeated_letter.add(first_letter)

            print()
            print(bb)

            for value in cc:
                print(f"- {value}")

        print()
        print()

        search = input("Do you want to search for contacts: ").strip().lower()

        if "yes" in search:
            search_2 = input("Enter the contact name or number: ").strip()


            if search_2 in my_dict:
                print(f"Contact: {search_2}")
                print("Numbers:", *my_dict[search_2])

            else:
                search_3 = False
                for name, numbers in my_dict.items():
                    if search_2 in numbers:
                        print(f"Number {search_2} belongs to {name}")
                        search_3 = True

                if not search_3:
                    print("There is no contact saved as", search_2)

        elif "no" in search:
            print("Search cancelled.")

        print()
        print()

        

    def Exit_app():
        print()
        print()
        print("Thank you for using Contact book app ")

    if Input_1 in add_contacts:
        add_contact()
    if Input_1 in update_contacts:
        update_contact()
    if Input_1 in delete_contacts:
        delete_contact()
    if Input_1 in view_contacts:
        view_contact()
    if Input_1 in exit_app:
        Exit_app()
        break