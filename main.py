from tinydb import TinyDB, Query
from datetime import date
import qrcode
import pandas as pd
from PIL import Image
import uuid
import csv
import json


db = TinyDB('db.json')
user = Query()

# Creating an instance of QRCode class
qr = qrcode.QRCode(version=1, box_size=10, border=5)


def menu():  # Main Menu
    print("Welcome to the Base Data of XYZ Company")
    print("[1] New Product")
    print("[2] Search")
    print("[3] Global Product Update")
    print("[4] Delete")
    print("[5] Update By ID")
    print("[6] All Data")
    print("[7] Export to Excel")
    print("[8] Exit")


def opt_search():  # Search Menu
    print("Function Search")
    print("[1] Search by Name")
    print("[2] Search by Year")
    print("[3] Material")
    print("[4] Back to Main Menu")


def opt_update():  # Global Update Menu
    print("Function Update")
    print("[1] Update Year")
    print("[2] Update Month")
    print("[3] Update Day")
    print("[3] Update Description")
    print("[4] Update Material")
    print("[5] Back to Main Menu")


def opt_byID():  # Global Update Menu
    print("Function Update by ID")
    print("[1] Update Name")
    print("[2] Update Year")
    print("[3] Update Month")
    print("[4] Update Day")
    print("[5] Update Description")
    print("[6] Update Material")
    print("[7] Back to Main Menu")


def opt_delete():  # Delete By Name
    print("Function Delete")
    print("[1] Delete by Name")
    print("[2] Back to Main Menu")


def insert():  # Function to insert New Data
    id = str(uuid.uuid4())
    name = str(input("Name of the Product: "))
    try:
        date_components = input('Enter a date formatted as YYYY-MM-DD: ').split('-')
        year, month, day = [int(item) for item in date_components]
        date(year, month, day)
    except:
        print("Please Enter a Vaild Date, Try Again!")
        return insert()
    description = str(input("Description of The Product: "))
    material = str(input("Material of the Product(Metal, Flammable, ect.): "))
    db.insert(
        {'ID': str(id),'Name': str(name), 'Year': str(year), 'Month': str(month), 'Day': str(day), 'Description': str(description),
         'Material': str(material)})
    save = (name, year, month, day, description, material)
    print("The Product " + str(name) + " has been Added")
    qr.add_data(save)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(name + '.png')



def search():  # Search Data by different Ways
    opt_search()
    opt = int(input("By which method do you want to search?: "))
    while opt != 0:
        if opt == 1:
            se_user = str(input("Name: "))
            results = db.search(Query()['Name'] == se_user)
            print(results)
            print()
            opt_search()
        if opt == 2:
            se_user = str(input("Year: "))
            results = db.search(Query()['Year'] == se_user)
            print(results)
            print()
            opt_search()
        if opt == 3:
            se_user = str(input("Material: "))
            results = db.search(Query()['Material'] == se_user)
            print(results)
            print()
            opt_search()
        if opt == 4:
            break
        else:
            print("Please Select a Valid Option")


def update():  # Update one by one Different Data
    opt_update()
    opt = int(input("What Element do you want to Update?: "))
    while opt != 0:
        if opt == 1:
            up_user = str(input("Name of the Product: "))
            dt_user = int(input("New Date Year: "))
            db.update({'Year': dt_user}, Query()['Name'] == up_user)
            results = db.search(Query()['Name'] == up_user)
            print(results)
            print("The Product has been Updated")
            opt_update()
        if opt == 2:
            up_user = str(input("Name of the Product: "))
            dt_user = str(input("New Date Month: "))
            db.update({'Month': dt_user}, Query()['Name'] == up_user)
            results = db.search(Query()['Name'] == up_user)
            print(results)
            print("The Product has been Updated")
            opt_update()
        if opt == 3:
            up_user = str(input("Name of the Product: "))
            dt_user = str(input("New Date Day: "))
            db.update({'Day': dt_user}, Query()['Name'] == up_user)
            results = db.search(Query()['Name'] == up_user)
            print(results)
            print("The Product has been Updated")
            opt_update()
        if opt == 4:
            up_user = str(input("Name of the Product: "))
            dt_user = str(input("New Description: "))
            db.update({'Description': dt_user}, Query()['Name'] == up_user)
            results = db.search(Query()['Name'] == up_user)
            print(results)
            print("The Product has been Updated")
            opt_update()
        if opt == 5:
            up_user = str(input("Name of the Product: "))
            dt_user = str(input("New Material: "))
            db.update({'Material': dt_user}, Query()['name'] == up_user)
            results = db.search(Query()['Name'] == up_user)
            print(results)
            print("The Product has been Updated")
            opt_update()
        if opt == 6:
            break
        else:
            print("Please Select a Valid Option")


def delete():  # Delete Data
    opt_delete()
    opt = int(input("Please Select a Option: "))
    while opt != 0:
        if opt == 1:
            name = str(input("What Product do you Want to delete?: "))
            db.remove(Query()['Name'] == name)
        if opt == 2:
            break
        else:
            print("Please Select a Valid Option")


def update_by_document_id():  # Deep Update
    opt_byID()
    opt = int(input("What Element do you want to Update?: "))
    while opt != 0:
        if opt == 1:
            up_user = str(input("ID of the Product: "))
            dt_user = str(input("New name: "))
            db.update({'Name': dt_user}, Query()['ID'] == up_user)
            results = db.search(Query()['ID'] == up_user)
            print(results)
            print("The Product has been Updated")
            opt_byID()
        if opt == 2:
            up_user = str(input("ID of the Product: "))
            dt_user = int(input("New Date Year: "))
            db.update({'Year': dt_user}, Query()['ID'] == up_user)
            results = db.search(Query()['ID'] == up_user)
            print(results)
            print("The Product has been Updated")
            opt_byID()
        if opt == 3:
            up_user = str(input("ID of the Product: "))
            dt_user = str(input("New Date Month: "))
            db.update({'Month': dt_user}, Query()['ID'] == up_user)
            results = db.search(Query()['ID'] == up_user)
            print(results)
            print("The Product has been Updated")
            opt_byID()
        if opt == 4:
            up_user = str(input("ID of the Product: "))
            dt_user = str(input("New Date Day: "))
            db.update({'Day': dt_user}, Query()['ID'] == up_user)
            results = db.search(Query()['ID'] == up_user)
            print(results)
            print("The Product has been Updated")
            opt_byID()
        if opt == 5:
            up_user = str(input("ID of the Product: "))
            dt_user = str(input("New Description: "))
            db.update({'Description': dt_user}, Query()['ID'] == up_user)
            results = db.search(Query()['ID'] == up_user)
            print(results)
            print("The Product has been Updated")
            opt_byID()
        if opt == 6:
            up_user = str(input("ID of the Product: "))
            dt_user = str(input("New Material: "))
            db.update({'Material': dt_user}, Query()['ID'] == up_user)
            results = db.search(Query()['ID'] == up_user)
            print(results)
            print("The Product has been Updated")
            opt_byID()
        if opt == 7:
            break
        else:
            print("Please Select a Valid Option")


def print_all():  # Print All Data
    print(db.all())


def export(): # Export Data to Excel
    df = pd.read_json("db.json")
    df.to_excel("Data.xlsx", index=False)


# Here it's the Menu
menu()
selection = int(input("Enter Your Option: "))
while selection != 0:
    if selection == 1:
        insert()
    elif selection == 2:
        search()
    elif selection == 3:
        update()
    elif selection == 4:
        delete()
    elif selection == 5:
        update_by_document_id()
    elif selection == 6:
        print_all()
    if selection == 7:
        export()
    if selection == 8:
        break
    else:
        print()
    print()
    menu()
    selection = int(input("Enter Your Option: "))
