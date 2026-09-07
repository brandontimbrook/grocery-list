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
        grocery = input("\nEnter an item: ")
        grocery_command = grocery.strip().lower()
        if grocery_command == "done":
            break
        if grocery_command == "show":
            show()
            continue
        for existing_grocery in groceries:
            if existing_grocery["item"] == grocery_command:
                print("Item already added to list.")
                break
        else:
            quantity = input("How many do you need? ")
            quantity_command = quantity.strip().lower()
            if quantity_command == "done":
                break
            groceries.append(
                {
                    "item": grocery_command,
                    "quantity": quantity,
                    "checked": False
                }
            )
            print(f"{grocery_command} added.")
            save()

def add():
    while True:
        grocery = input("\nEnter an item: ")
        grocery_command = grocery.strip().lower()
        if grocery_command == "done":
            break
        if grocery_command == "show":
            show()
            continue
        for existing_grocery in groceries:
            if existing_grocery["item"] == grocery_command:
                print(f"{grocery_command} already added to list.")
                break
        else:
            quantity = input("How many do you need? ")
            quantity_command = quantity.strip().lower()
            if quantity_command == "done":
                break
            groceries.append(
                {
                    "item": grocery_command,
                    "quantity": quantity,
                    "checked": False
                }
            )
            print(f"{grocery_command} added.")
            save()

def edit():
    while True:
        grocery_edit = input("\nWhat item would you like to update? ")
        grocery_edit_command = grocery_edit.strip().lower()
        if grocery_edit_command == "done":
            return
        found = False
        for grocery in groceries:
            if grocery_edit_command == grocery["item"]:
                found = True
                break
        if found:
            quantity = input("How many do you need? ")
            grocery["quantity"] = quantity
            print(f"{grocery['item']} updated.")
            save()
        if not found:
            print(f"{grocery_edit_command} not found.")

def show():
    for grocery in groceries:
        quantity = grocery["quantity"]
        if not grocery["checked"]:
            print(f"[ ] {grocery['item']} - {quantity}")
        else:
            print(f"[X] {grocery['item']} - {quantity}")


def check():
    while True:
        check = input("\nWhat would you like to check off? ")
        check_command = check.strip().lower()
        if check_command == "done":
            return
        found = False
        for grocery in groceries:
            if check_command == grocery["item"]:
                grocery["checked"] = True
                found = True
                print(f"{grocery['item']} checked.")
                save()
        if not found:
            print(f"{check_command} not found.")

def uncheck():
    
    while True:
        uncheck = input("\nWhat would you like to uncheck? ")
        uncheck_command = uncheck.strip().lower()
        if uncheck_command == "done":
            return
        found = False
        for grocery in groceries:
            if uncheck_command == grocery["item"]:
                grocery["checked"] = False
                found = True
                print(f"{grocery['item']} unchecked.")
                save()
        if not found:
            print(f"{uncheck_command} not found.")

def remove():
    while True:
        remove = input("\nWhat would you like to remove? ")
        remove_command = remove.strip().lower()
        if remove_command == "done":
            return
        found = False
        for grocery in groceries:
            if remove_command == grocery["item"]:
                groceries.remove(grocery)
                found = True
                print(f"{grocery['item']} removed.")
                save()
                break
        if not found:
            print(f"{remove_command} not found.")

def clear():
    groceries.clear()
    save()

while True:
    branch = input("\nWhat are we doing today?\n")
    branch_command = branch.strip().lower()

    if branch_command == "new":
        new()
    if branch_command == "add":
        add()
    if branch_command == "edit":
        edit()
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