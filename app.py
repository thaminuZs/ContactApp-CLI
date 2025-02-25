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
        return item[key] == value
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
    name = input("Enter Name For Search : ")
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
    name = input("Enter Name For Edit : ")
    if search_availability("name", name):
        # TODO: From Here
        menu()
    else:
        print("Contact Not Found !")
        menu()


def menu():
    print(
        "\n1 - Add Contact\n2 - Search Contact\n3 - Edit Contact\n4- Delete Contact\n5- View Book\n"
    )

    option = input("Enter Option To Continue : ")
    if option == "1":
        add_contact()
    elif option == "2":
        search_contact()
    elif option == "3":
        edit_contact()


print("====CONTACT APP====")
menu()
