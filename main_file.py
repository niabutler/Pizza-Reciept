"""Fruitbowl management programme."""
from validations import get_validated_integer, get_validated_string
import math

def starline():
    print("*" * 50)


def dashline():
    print("-" * 50)


def print_menu(m):
    for i in range(0, len(m)):
        output = "{}: {}".format(m[i][0], m[i][1])
        print(output)


def print_pizzas(p):
    print("Pizza Menu")
    for i in range (0,len(p)):
        output = ("${}0   {}".format(p[i][0], p[i][1]))
        print(output)
    input = get_validated_string("Please press Q to quit to main menu: -> ", 1, 1).upper()
    if input == "Q":
        main_function()
    else:
        print("You have not entered a valid input")




def main_function():
    starline()
    print("Main Menu")
    pizzas = [
        [18.50, "BBQ Chicken"],
        [18.50, "Hawaiian"],
        [18.50, "Cheese and Garlic"],
        [25.50, "Chicken and Brie"],
        [25.50, "Steak and Kumara"]
    ]
    customer_order = []
    my_menu = [
        ("M", "See Menu"),
        ("Q", "Quit")
    ]
    print_menu(my_menu)
    choice = get_validated_string("Please choose an option: -> ", 1, 1).upper()

    if choice == "M":
        starline()
        print_pizzas(pizzas)
    elif choice == "Q":
        print("Thank you for choosing Pete's Pizza's! Have a nice evening :)")
    else:
        print("Invalid entry, please try again.")



if __name__ == '__main__':
    main_function()





