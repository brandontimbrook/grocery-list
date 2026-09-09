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
    grocery_entry()

def add():
    grocery_entry()

def edit():
    while True:
        command = input("\nWhat item would you like to update? ")
        command = command.strip().lower()
        if command == "":
            return
        elif command == "show":
            show()
            continue
        grocery = find_grocery(command)
        if grocery is not None:
            quantity = input("How many do you need? ")
            if quantity.strip() == "":
                break
            grocery["quantity"] = quantity
            print(f"{grocery['item']} updated.")
            save()
        else:
            print(f"{command} not found.")

def show():
    for grocery in groceries:
        quantity = grocery["quantity"]
        if not grocery["checked"]:
            print(f"[ ] {grocery['item']} - {quantity}")
        else:
            print(f"[X] {grocery['item']} - {quantity}")


def check():
    while True:
        command = input("\nWhat would you like to check off? ")
        command = command.strip().lower()
        if command == "":
            return
        elif command == "show":
            show()
            continue
        grocery = find_grocery(command)
        if grocery is not None:
            grocery["checked"] = True
            print(f"{grocery['item']} checked.")
            save()
        else:
            print(f"{command} not found.")

def uncheck():
    while True:
        command = input("\nWhat would you like to uncheck? ")
        command = command.strip().lower()
        if command == "":
            return
        elif command == "show":
            show()
            continue
        grocery = find_grocery(command)
        if grocery is not None:
            grocery["checked"] = False
            print(f"{grocery['item']} unchecked.")
            save()
        else:
            print(f"{command} not found.")

def remove():
    while True:
        command = input("\nWhat would you like to remove? ")
        command = command.strip().lower()
        if command == "":
            return
        elif command == "show":
            show()
            continue
        grocery = find_grocery(command)
        if grocery is not None:
            groceries.remove(grocery)
            print(f"{grocery['item']} removed.")
            save()
        else:
            print(f"{command} not found.")

def clear():
    groceries.clear()
    save()

def grocery_entry():
    while True:
        grocery = input("\nEnter an item: ")
        command = grocery.strip().lower()
        if command == "":
            break
        elif command == "show":
            show()
            continue
        grocery = find_grocery(command)
        if grocery is not None:
            print(f"{command} already added to list.")
            continue
        else:
            quantity = input("How many do you need? ")
            if quantity.strip() == "":
                break
            groceries.append(
                {
                    "item": command,
                    "quantity": quantity,
                    "checked": False
                }
            )
            print(f"{command} added.")
            save()

def find_grocery(command):
    for grocery in groceries:
        if command == grocery["item"]:
            return grocery
    return None

while True:
    command = input("\nWhat are we doing today?\n")
    command = command.strip().lower()

    if command == "new":
        new()
    elif command == "add":
        add()
    elif command == "edit":
        edit()
    elif command == "show":
        show()        
    elif command == "check":
        check()
    elif command == "uncheck":
        uncheck()
    elif command == "remove":
        remove()
    elif command == "clear":
        clear()
    elif command == "quit":
        break
    else:
        print("""
        Not a valid command.
        
        The currently available list of commands are:
        
        new - clears existing list and creates a new list
        
        add - adds new entries to current list
        
        edit - update the quantity of an item on the current list
        
        show - shows the current list and item statuses
        
        check - changes state of an item to checked off
        
        uncheck - changes state of an item to not checked off
        
        remove - deletes an item's entry from the current list
        
        clear - clears all entries on current list
        
        quit - closes program and exits to shell""")