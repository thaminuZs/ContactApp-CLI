contact_list = []


# Get Index
def get_index(key, value):
    for item in contact_list:
        if item[key] == value:
            return contact_list.index(item)
    return None


# Search Availability of a Value
def search_availability(key, value):
    for item in contact_list:
        if item[key] == value:
            return True
    return False


# Add Contact
def add_contact():
    name = input("\nEnter Contact Name : ")
    if search_availability("name", name):
        print("Already Saved !")
        menu()
        return

    company = input("Enter Company : ")

    phone_no = input("Enter Phone No : ")
    if search_availability("phone_no", phone_no):
        print("Already Saved !")
        menu()
        return

    email = input("Enter E-Mail : ")

    contact_list.append(
        {"name": name, "company": company, "phone_no": phone_no, "email": email}
    )

    print("\nSaved Successfully")
    menu()


# Search Contact
def search_contact():
    name = input("\nEnter Name For Search : ")
    if search_availability("name", name):
        print(
            "\nName : ",
            contact_list[get_index("name", name)]["name"],
            "\nCompany : ",
            contact_list[get_index("name", name)]["company"],
            "\nPhone No : ",
            contact_list[get_index("name", name)]["phone_no"],
            "\nEmail : ",
            contact_list[get_index("name", name)]["email"],
        )
        menu()
    else:
        print("Contact Not Found !")
        menu()


# Edit Contacts
def edit_contact():
    name = input("\nEnter Name For Edit : ")
    if search_availability("name", name):
        print(
            "\nWhat Do You Want To Edit\n1 - Name\n2 - Company\n3 - Phone No\n4 - Email\n"
        )
        option = input("Enter Option To Continue : ")
        if option == "1":
            contact_list[get_index("name", name)]["name"] = input("\nEnter New Name : ")
            print("\nUpdated Successfully")
        elif option == "2":
            contact_list[get_index("name", name)]["company"] = input(
                "\nEnter New Company : "
            )
            print("\nUpdated Successfully")
        elif option == "3":
            contact_list[get_index("name", name)]["phone_no"] = input(
                "\nEnter New Phone No : "
            )
            print("\nUpdated Successfully")
        elif option == "4":
            contact_list[get_index("name", name)]["email"] = input(
                "\nEnter New Email : "
            )
            print("\nUpdated Successfully")
        else:
            print("\nInvalid Option !")
        menu()
    else:
        print("\nContact Not Found !")
        menu()


# Delete Contact
def delete_contact():
    name = input("Enter Name For Delete : ")
    if search_availability("name", name):
        del contact_list[get_index("name", name)]
        print("\nDeleted Successfully")
        menu()
    else:
        print("\nContact Not Found")
        menu()


# View Book
def view_book():
    if len(contact_list) == 0:
        print("\nBook Is Empty !")
        menu()
    else:
        print()
        print(f"{'Name': <10}{'Company': <10}{'Phone No': <15}{'Email': <20}")
        print("-" * 55)

        for item in contact_list:
            print(
                f"{item['name']: <10}{item['company']: <10}{item['phone_no']: <15}{item['email']: <20}"
            )
        menu()


def menu():
    print(
        "\n1 - Add Contact\n2 - Search Contact\n3 - Edit Contact\n4 - Delete Contact\n5 - View Book\n6 - Exit\n"
    )

    option = input("Enter Option To Continue : ")
    if option == "1":
        add_contact()
    elif option == "2":
        search_contact()
    elif option == "3":
        edit_contact()
    elif option == "4":
        delete_contact()
    elif option == "5":
        view_book()
    elif option == "6":
        return
    else:
        print("\nInvalid Option !")
        menu()


print("====CONTACT APP====")
menu()
exit()
