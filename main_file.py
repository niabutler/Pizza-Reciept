"""Fruitbowl management programme."""
from validations import get_validated_integer, get_validated_string, get_integer_conformation
import math

def starline():
    print("*" * 50)


def dashline():
    print("-" * 50)


def dotline():
    print("." * 50)


def print_menu(m):
    for i in range(0, len(m)):
        output = "{}: {}".format(m[i][0], m[i][1])
        print(output)


def print_pizzas(p):
    print("Pizza Menu")
    dotline()
    for i in range (0,len(p)):
        output = ("${}0   {}".format(p[i][0], p[i][1]))
        print(output)


def pizza_options(p):
    print("Pizza Menu")
    dotline()
    for i in range(0, len(p)):
        output = "{}:  ${}0 {} - {}".format(i+1, p[i][0], p[i][1], p[i][2])
        print(output)


def print_order(co):
    if len(co) == 0:
        print("Your order is empty, start ordering!")
        return None
    print("Your order:")
    for i in range(0, len(co)):
        output = "x{} @${}0 {}".format(co[i][0], co[i][1], co[i][2])
        print(output)


def add_to_order(p, co):
    pizza_options(p)
    dotline()
    print("Add to order: ")
    dotline()
    run = False
    while run == False:
        input_1 = get_validated_integer("Please enter an item number from the menu above: -> ", 1, len(p))
        input_1 = input_1 - 1
        chosen_pizza = p[input_1][1]
        input_2 = get_integer_conformation("How many {} pizza's would you like? -> ".format(chosen_pizza), 1, 10)
        temp_list = (input_2, p[input_1][0], chosen_pizza)
        co.append(temp_list)
        choice = get_validated_string("Add another pizza? y/n : ", 1, 1).upper()
        if choice == "Y":
            continue
        elif choice == "N":
            starline()
            print_order(co)
            return None
        else:
            print("Your input is invalid please choose y/n.")


def main_function():
    starline()
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
        ("R", "Review Order"),
        ("Q", "Quit")
        ]
    run = True
    while run is True:
        print("Main Menu")
        dotline()
        for i in range(0, len(my_menu)):
                output = "{}: {}".format(my_menu[i][0], my_menu[i][1])
                print(output)
        choice = get_validated_string("Please choose an option: -> ", 1, 1).upper()
        if choice == "M":
            starline()
            print_pizzas(pizzas)
            starline()
        elif choice == "Q":
            print("Thank you for choosing Pete's Pizza's! Have a nice evening :)")
        elif choice == "A":
            starline()
            add_to_order(pizzas, customer_order)
            starline()
        elif choice == "R":
            starline()
            print_order(customer_order)
            starline()
        else:
            print("Invalid entry, please try again.")



if __name__ == '__main__':
    main_function()





