import json

def save():
    with open("groceries.json", "w") as file:
        json.dump(groceries, file)


def load():
    try:
        with open("groceries.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

groceries = load()

def new():
    clear()
    while True:
        grocery = input("Enter an item: ")
        grocery_command = grocery.strip().lower()
        if grocery_command == "done":
            break
        if grocery_command == "show":
            show()
            continue
        for existing_grocery in groceries:
            if existing_grocery["item"] == grocery:
                print("Item already added to list.")
                break
        else:
            quantity = input("How many do you need? ")
            quantity_command = quantity.strip().lower()
            if quantity_command == "done":
                break
            groceries.append(
                {
                    "item": grocery,
                    "quantity": quantity,
                    "checked": False
                }
            )
            save()

def add():
    while True:
        grocery = input("Enter an item: ")
        grocery_command = grocery.strip().lower()
        if grocery_command == "done":
            break
        if grocery_command == "show":
            show()
            continue
        for existing_grocery in groceries:
            if existing_grocery["item"] == grocery:
                print("Item already added to list.")
                break
        else:
            quantity = input("How many do you need? ")
            quantity_command = quantity.strip().lower()
            if quantity_command == "done":
                break
            groceries.append(
                {
                    "item": grocery,
                    "quantity": quantity,
                    "checked": False
                }
            )
            save()

def show():
    for grocery in groceries:
        quantity = grocery["quantity"]
        if not grocery["checked"]:
            print(f"[ ] {grocery['item']} - {quantity}")
        else:
            print(f"[X] {grocery['item']} - {quantity}")


def check():
    while True:
        check = input("What would you like to check off? ")
        if check.strip().lower() == "done":
            return
        found = False
        for grocery in groceries:
            if check == grocery["item"]:
                grocery["checked"] = True
                found = True
                print(f"{grocery['item']} has been checked.")
                save()
        if not found:
            print("Item not found")

def uncheck():
    
    while True:
        uncheck = input("What would you like to uncheck? ")
        if uncheck.strip().lower() == "done":
            return
        found = False
        for grocery in groceries:
            if uncheck == grocery["item"]:
                grocery["checked"] = False
                found = True
                print(f"{grocery['item']} has been unchecked.")
                save()
        if not found:
            print("Item not found")

def remove():
    while True:
        remove = input("What would you like to remove? ")
        if remove.strip().lower() == "done":
            return
        found = False
        for grocery in groceries:
            if remove == grocery["item"]:
                groceries.remove(grocery)
                found = True
                save()
                break
        if not found:
            print("Item not found")

def clear():
    groceries.clear()
    save()

while True:
    branch = input("What are we doing today? ")
    branch_command = branch.strip().lower()

    if branch_command == "new":
        new()
    if branch_command == "add":
        add()       
    if branch_command == "show":
        show()        
    if branch_command == "check":
        check()
    if branch_command == "uncheck":
        uncheck()
    if branch_command == "remove":
        remove()
    if branch_command == "clear":
        clear()
    if branch_command == "exit":
        break