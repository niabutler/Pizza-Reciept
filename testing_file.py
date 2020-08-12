from validations import get_validated_integer, get_validated_string
import math


def starline():
    print("*" * 50)


def dashline():
    print("-" * 50)

def dotline():
    print("." * 50)


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



#print_pizzas(pizzas)
main_function()
#pizza_options(pizzas)
#add_to_order()

