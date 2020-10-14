from validations import get_validated_integer, get_validated_string
import math


def starline():
    print("*" * 50)


def dashline():
    print("-" * 50)

def dotline():
    print("." * 50)

def get_integer_conformation(m, min, max):
    run = True
    while True:
        try:
            number = input(m)
            number = number.replace(" ", "")
            number = int(number)
        except ValueError:
            print("This is not a valid entry.")
            continue
        if number < min:
            print("Your entry is too small")
            continue
        elif number > max:
            print("Are you sure you want {} pizza's".format(number))
            choice = get_validated_string("Press <enter> to confirm or any other key to re-enter", 0, 1).upper()
            if choice == "":
                return number
        else:
            return number


def main_function():
    starline()
    print("Main Menu")
    pizzas = [
        [18.50, "BBQ Chicken", "Description"],
        [18.50, "Hawaiian", "Description"],
        [18.50, "Cheese and Garlic", "Description"],
        [25.50, "Chicken and Brie", "Description"],
        [25.50, "Steak and Kumara", "Description"]
    ]

    customer_order = []

    my_menu = [
        ("M", "See Menu"),
        ("A", "Add to order"),
        ("Q", "Quit")
        ]
    run = True
    while run is True:
        for i in range(0, len(my_menu)):
                output = "{}: {}".format(my_menu[i][0], my_menu[i][1])
                print(output)
        choice = get_validated_string("Please choose an option: -> ", 1, 1).upper()
        if choice == "M":
            starline()
            print_pizzas(pizzas)
        elif choice == "Q":
            print("Thank you for choosing Pete's Pizza's! Have a nice evening :)")
        elif choice == "A":
            starline()
            add_to_order(pizzas, customer_order)
        else:
            print("Invalid entry, please try again.")




def print_menu(m):
    for i in range(0, len(m)):
        output = "{}: {}".format(m[i][0], m[i][1])
        print(output)


pizzas = [
        [18.50, "BBQ Chicken", "Pizza description"],
        [18.50, "Hawaiian", "Pizza description"],
        [18.50, "Cheese and Garlic", "Pizza description"],
        [25.50, "Chicken and Brie", "Pizza description"],
        [25.50, "Steak and Kumara", "Pizza description"]
    ]

def print_pizzas(p):
    print("Pizza Menu")
    for i in range(0,len(p)):
        output = ("${}0   {}".format(pizzas[i][0], pizzas[i][1]))
        print(output)


customer_order = []


def pizza_options(p):
    print("Pizza Menu")
    for i in range(0, len(p)):
        output = "{}:  ${}0 {} - {}".format(i, p[i][0], p[i][1], p[i][2])
        print(output)


def print_order(co):
    for i in range(0, len(co)):
        output = "x{} @${}0 {}".format(co[i][0], co[i][1], co[i][2])
        print(output)


def add_to_order(p, co):
    pizza_options(p)
    starline()
    print("Add to order: ")
    run = False
    while run == False:
        input_1 = get_validated_integer("Please enter an item number from the menu above: -> ", 0, 10)
        chosen_pizza = p[input_1][1]
        input_2 = get_validated_integer("How many {} pizza's would you like? -> ".format(chosen_pizza), 1, 10)
        temp_list = (input_2, p[input_1][0], chosen_pizza)
        co.append(temp_list)
        choice = get_validated_string("Add another pizza? y/n : ", 1, 1).upper()
        if choice == "Y":
            continue
        elif choice == "N":
            starline()
            print("Your order:")
            print_order(co)
            return None
        else:
            print("Your input is invalid please choose y/n.")

customer_order = [
    [18.50, 3, "BBQ Chicken", "Description"],
    [18.50, 3, "Hawaiian", "Description"],
    [18.50, 1, "Cheese and Garlic", "Description"],
    [25.50, 1, "Chicken and Brie", "Description"],
    [25.50, 2, "Steak and Kumara", "Description"]
]


def receipt_calc(co):
    total_cost = 0
    for i in range(0, len(co)):
        sum_row = co[i][0] * co[i][1]
        total_cost += sum_row
    print("${}".format(total_cost))


def print_order(co):
    if len(co) == 0:
        print("Your order is empty, start ordering!")
        return None
    print("Your order:")
    print("Name: {}".format(co[i][3]))
    dashline()
    titles = "{:<5}  {:<20}  {:12} {}".format("Qty", "Flavour", "Price", "SUBTOTAL")
    print(titles)
    for i in range(0, len(co)):
        sub_total = co[i][0] * co[i][1]
        output = "x{:<5} {:<20} @ ${:<10.2f} ${:3.2f}".format(co[i][0], co[i][2], co[i][1], sub_total)
        print(output)
    dashline()
    receipt_calc(co)

def change_quantity():
    co = [
        [18.50, 3, "BBQ Chicken", "Description"],
        [18.50, 3, "Hawaiian", "Description"],
        [18.50, 1, "Cheese and Garlic", "Description"],
        [25.50, 1, "Chicken and Brie", "Description"],
        [25.50, 2, "Steak and Kumara", "Description"]
    ]
    index = get_validated_integer(
        "Please enter the index number of the pizza you would like to change the quantity of: -> ", 1, len(co)-1)
    print("Your currently have {} {} pizza/s in your order".format( co[index-1][1], co[index-1][2]))
    new_quan = get_integer_conformation(
        "Please enter your updated quantity of {} pizza's: -> ".format(co[index-1][1]), 1, 25)
    print("Your order now has {} {} pizza's".format(new_quan, co[index-1][1]))
    co[index - 1][1] = new_quan
    return None

def remove_pizza():
    co = [
        [3, 18.50, "BBQ Chicken", "Description"],
        [2, 18.50, "Hawaiian", "Description"],
        [3, 18.50, "Cheese and Garlic", "Description"],
        [1, 25.50, "Chicken and Brie", "Description"],
        [2, 25.50, "Steak and Kumara", "Description"]
    ]
    index = get_validated_integer(
        "Please enter the index number of the pizza flavour you would like to remove from your order: -> ", 1, len(co) - 1)
    print("Your currently have {} {} pizza/s in your order".format(co[index - 1][2], co[index - 1][1]))
    choice = get_validated_string(
        "Are you sure you would like to remove all {} pizza's from your order? Y/N -> ".format(co[index - 1][1]), 1, 1).upper()
    if choice == "Y":
        co.pop(index - 1)
        print_order(co)
    elif choice == "N":
        return None
    else:
        print("Please enter Y yes or N no: -> ")


def update_menu(p, co):
    my_menu = [
        ("C", "Change a quantity"),
        ("R", "Remove a Pizza"),
        ("A", "Add a pizza"),
        ("Q", "Main Menu")
    ]

    run = True
    while run is True:
        print("Review Order")
        dotline()
        print_order(co)
        # print main menu
        for i in range(0, len(my_menu)):
            output = "{}: {}".format(my_menu[i][0], my_menu[i][1])
            print(output)
        # ask for user's choice as input
        choice = get_validated_string("Please choose an option: -> ", 1, 1).upper()
        if choice == "C":
            starline()
            change_quantity()
            starline()
        elif choice == "R":
            starline()
            remove_pizza()
        elif choice == "A":
            starline()
            add_to_order(p, co)
        elif choice == "Q":
            starline()
        else:
            return None


def print_order_with_indexes(co):
    if len(co) == 0:
        print("Your order is empty, start ordering!")
        return None
    dotline()
    print("Your order:")
    dashline()
    titles = "{:3} {:<5}  {:<20}  {:12} {}".format("Index", "Qty", "Flavour", "Price", "SUBTOTAL")
    print(titles)
    for i in range(0, len(co)):
        sub_total = co[i][0] * co[i][1]
        output = "{:3} x{:<5} {:<20} @ ${:<10.2f} ${:3.2f}".format(co[i], co[i][0], co[i][2], co[i][1], sub_total)
        print(output)
    dashline()
    receipt_calc(co)


def update_menu(p, co):
    my_menu = [
        ("C", "Change a quantity"),
        ("R", "Remove a Pizza"),
        ("A", "Add a pizza"),
        ("Q", "Main Menu")
    ]
    run = True
    while run is True:
        print("Review Order")
        print_order_with_indexes(co)
        # print main menu
        for i in range(0, len(my_menu)):
            output = "{}: {}".format(my_menu[i][0], my_menu[i][1])
            print(output)
        # ask for user's choice as input
        choice = get_validated_string("Please choose an option: -> ", 1, 1).upper()
        if choice == "C":
            starline()
            change_quantity(co)
            starline()
        elif choice == "R":
            starline()
            remove_pizza(co)
        elif choice == "A":
            starline()
            add_to_order(p, co)
        elif choice == "Q":
            starline()
        else:
            return None

def checkout():
    my_menu = [
        ("P", "Pick up"),
        ("D", "Delivery")
        ]
    run = True
    while run is True:
        for i in range(0, len(my_menu)):
            output = "{}: {}".format(my_menu[i][0], my_menu[i][1])
            print(output)
        choice = get_validated_string("Please choose an option: -> ", 1, 1).upper()
        if choice == "P":
            name = get_validated_string("Please enter your name: -> ", 1, 15).upper()
            number = get_validated_string("Please enter a contact number (mobile): -> ", 1, 15)
            cd1 = [name, number]
            print(cd1)
        elif choice == "D":
            name = get_validated_string("Please enter your name: -> ", 1, 15).upper()
            mobile = get_validated_string("Please enter a contact number (mobile): -> ", 1, 12)
            number = get_validated_string("Please enter your street number: ", 1, 3)
            street = get_validated_string("Please enter your street name: ", 3, 15)
            suburb = get_validated_string("Please enter your suburb: ", 3, 15)
            postcode = get_validated_string("Please enter your postcode: ", 4, 4)
            cd2 = [name, mobile, number, street, suburb, postcode]
            print(cd2)
        else:
            print("Please enter P or D")





#print_pizzas(pizzas)
#main_function()
#pizza_options(pizzas)
#add_to_order()
#print_order(customer_order)
#receipt_calc(customer_order)
#change_quantity()
#remove_pizza()
#update_menu(pizzas, customer_order)
checkout()

