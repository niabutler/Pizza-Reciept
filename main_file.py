"""Pizza Ordering programme."""
from validations import get_validated_integer, get_validated_string, get_integer_conformation


def starline():
    # print line of 50 stars
    print("*" * 70)


def dashline():
    # print line of 50 dashes
    print("-" * 70)


def dotline():
    # print line of 50 dots
    print("." * 70)


def print_menu(m):
    # print menu, formatted
    for i in range(0, len(m)):
        output = "{}: {}".format(m[i][0], m[i][1])
        print(output)


def print_pizzas(p):
    # print pizza menu with prices
    print("Pizza Menu")
    dotline()
    for i in range(0, len(p)):
        # print price and name of pizzas
        output = ("${}0   {}".format(p[i][0], p[i][1]))
        print(output)


def pizza_options(p):
    # print pizza menu with indexes
    print("Pizza Menu")
    dotline()
    # print headings above the information to make it easier to understand
    titles = "{:5}   {:22} {:14}  {}".format("Item no.", "Name", "Description", "Price")
    print(titles)
    # print in order: index number +1, space, name, space, description and price
    for i in range(0, len(p)):
        output = "{:3}: {:5} {:20} {} -{:15} ${}0".format(i+1, "", p[i][1], "", p[i][2], p[i][0])
        print(output)


def receipt_calc(co):
    total_cost = 0
    for i in range(0, len(co)):
        sub_total = co[i][0] * co[i][1]
        total_cost += sub_total
    print("{:29}Total Cost: ${:5.2f} ".format("", total_cost))
    print("{:36}GST: ${:5.2f} ".format("", total_cost*(3/23)))
    dashline()


def print_order(co):
    if len(co) == 0:
        print("Your order is empty, start ordering!")
        return None
    dotline()
    print("Your order:")
    dashline()
    titles = "{:<5}  {:<20}  {:12} {}".format("Qty", "Flavour", "Price", "SUBTOTAL")
    print(titles)
    for i in range(0, len(co)):
        sub_total = co[i][0] * co[i][1]
        output = "x{:<5} {:<20} @ ${:<10.2f} ${:3.2f}".format(co[i][0], co[i][2], co[i][1], sub_total)
        print(output)
    dashline()
    receipt_calc(co)


def print_order_with_indexes(co):
    if len(co) == 0:
        print("Your order is empty, start ordering!")
        return None
    dotline()
    print("Your order:")
    dashline()
    titles = "{:<5}{:^10}{:<22}{:12}{}".format("Index", "Qty", "Flavour", "Price", "SUBTOTAL")
    print(titles)
    for i in range(0, len(co)):
        sub_total = co[i][0] * co[i][1]
        output = "{:2}{:<3}{:^9} {:<21}@ ${:<10.2f} " \
                 "${:3.2f}".format("", i+1, co[i][0], co[i][2], co[i][1], sub_total)
        print(output)
    dashline()
    receipt_calc(co)


def add_to_order(p, co):
    pizza_options(p)
    dotline()
    print("Add to order: ")
    dotline()
    run = False
    while run is False:
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


def change_quantity(co):
    index = get_validated_integer(
        "Please enter the index number of the pizza you would like to change the quantity of: -> ", 1, len(co))
    print("You currently have {} {} pizza/s in your order".format(co[index-1][0], co[index-1][2]))
    new_quan = get_integer_conformation(
        "How many {} pizza's would you like?: -> ".format(co[index-1][2]), 1, 25)
    print("Your order now has {} {} pizza's".format(new_quan, co[index-1][2]))
    co[index - 1][0] = new_quan
    return None


def remove_pizza(co):
    message = "Please enter the index number of the pizza flavour you would like to remove from your order: -> "
    index = get_validated_integer(message, 1, len(co) - 1)
    print("Your currently have {} {} pizza/s in your order".format(co[index - 1][0], co[index - 1][2]))
    message = "Are you sure you would like to remove all {} pizza's from your order? Y/N -> ".format(co[index - 1][2])
    choice = get_validated_string(message, 1, 1).upper()
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


def main_function():
    """Run main menu.

        Set pizza list, set customer order, set menu options, print menu.
        Get user input, if {} letter is chosen, send to {} function.
        Quit option to exit loop.
        returns None
        --------------
        :return: None
        --------------
        L: list of lists, sub-list is [int, int, str]
        --------------
        Two dimensional list:
        the sub-list has two items in it, [integer, string]
        --------------
        """
    starline()
    pizzas = [
        [18.50, "BBQ Chicken", "Description"],
        [18.50, "Hawaiian", "Description"],
        [18.50, "Cheese and Garlic", "Description"],
        [25.50, "Chicken and Brie", "Description"],
        [25.50, "Steak and Kumara", "Description"]
    ]

    customer_order = []
    customer_order_temp = [
        [3, 18.5, "BBQ Chicken"],
        [2, 18.5, "Cheese and Garlic"],
        [1, 18.5, "Steak and Kumara"],
        [2, 25.5, "Hawaiian"],

    ]

    my_menu = [
        ("M", "See Menu"),
        ("A", "Add to order"),
        ("R", "Review Order"),
        ("Q", "Quit"),
        ("T", "Test"),
        ]
    run = True
    while run is True:
        print("Main Menu")
        dotline()
        # print main menu
        for i in range(0, len(my_menu)):
            output = "{}: {}".format(my_menu[i][0], my_menu[i][1])
            print(output)
        # ask for user's choice as input
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
            update_menu(pizzas, customer_order)
            starline()
        elif choice == "T":
            print("test")
            update_menu(pizzas, customer_order_temp)
        else:
            print("Invalid entry, please try again.")


if __name__ == '__main__':
    main_function()
