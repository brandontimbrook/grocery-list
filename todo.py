groceries = []

def new():
    while True:
        grocery = input("Enter an item: ")
        grocery_command = grocery.strip().lower()
        if grocery_command == "done":
            break
        groceries.append(
            {
                "item": grocery,
                "checked": False
            }
        )
    show()
    return

def show():
    for grocery in groceries:
        if not grocery["checked"]:
            print(f"[ ] {grocery['item']}")
        else:
            print(f"[X] {grocery['item']}")


def check():
    while True:
        check = input("What would you like to check off? ")
        if check.strip().lower() == "done":
            return
        for grocery in groceries:
            if check == grocery["item"]:
                grocery["checked"] = True

def uncheck():
    while True:
            uncheck = input("What would you like to check off? ")
            if uncheck.strip().lower() == "done":
                return
            for grocery in groceries:
                if uncheck == grocery["item"]:
                    grocery["checked"] = False

def remove():
    while True:
        remove = input("What would you like to remove? ")
        if remove.strip().lower() == "done":
            return
        for grocery in groceries:
            if remove == grocery["item"]:
                groceries.remove(grocery)

while True:
    branch = input("What are we doing today? ")
    branch_command = branch.strip().lower()

    if branch_command == "new":
        new()       
    if branch_command == "show":
        show()        
    if branch_command == "check":
        check()
    if branch_command == "uncheck":
        uncheck()
    if branch_command == "remove":
        remove()
    if branch_command == "exit":
        break