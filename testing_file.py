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
    titles = "{:5}    {:10} {:15}".format("Qty", "Price", "Flavour")
    print(titles)
    dashline()
    for i in range(0, len(co)):
        output = "x{:<5} @ ${:<10.2f} {:15}".format(co[i][0], co[i][1], co[i][2])
        print(output)

def change_quantity():
    co = [
        [18.50, 3, "BBQ Chicken", "Description"],
        [18.50, 3, "Hawaiian", "Description"],
        [18.50, 1, "Cheese and Garlic", "Description"],
        [25.50, 1, "Chicken and Brie", "Description"],
        [25.50, 2, "Steak and Kumara", "Description"]
    ]
    index = get_validated_integer("Please enter the index number of the pizza you would like to change the quantity of: -> ", 1, len(co)-1)
    print("Your currently have {} {} pizza/s in your order".format(co[index-1][1], co[index-1][2]))
    new_quan = get_integer_conformation("Please enter your updated quantity of {} pizza's: -> ".format(co[index-1][2]), 1, 25)
    print("Your order now has {} {} pizza's".format(new_quan, co[index-1][2]))
    co[index - 1][2] = new_quan


def update_menu(co):
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
            starline()
        elif choice == "R":
            starline()
        elif choice == "A":
            starline()
        elif choice == "Q":
            starline()
        else:
            return None




#print_pizzas(pizzas)
#main_function()
#pizza_options(pizzas)
#add_to_order()
#print_order(customer_order)
#receipt_calc(customer_order)
change_quantity()

