"""Pizza Ordering programme."""
from validations import get_validated_integer, \
    get_validated_string, get_integer_conformation, \
    get_address, get_validated_string_y_n, \
    get_validated_phone


def starline():
    """Print starred line.

    Print starred line
    --------------
    :return: None
    --------------
    """
    # print line of 100 stars
    print("*" * 100)


def dashline():
    """Print dashed line.

    Print dashed line
    --------------
    :return: None
    --------------
    """
    # print line of 100 dashes
    print("-" * 100)


def dotline():
    """Print dotted line.

    Print dotted line
    --------------
    :return: None
    --------------
    """
    # print line of 100 dots
    print("." * 100)


def print_menu(m):
    """Print Main Menu.

    Print menu options.

    :param: m (my_menu, a list of letters associated to a menu item)
    :return: None
    """
    # print menu, formatted
    for i in range(0, len(m)):
        output = "{}: {}".format(m[i][0], m[i][1])
        print(output)


def pizza_options(p):
    """Print pizza menu.

    Print titles.
    For the length of the pizza menu,
    print index numbers, name, price and description.

    :param: p (pizza_menu, a multidimensional list of pizza names,
    prices and descriptions)
    :return: None
    """
    # print pizza menu with indexes
    print("PIZZA MENU")
    dotline()
    # print headings above the information to make it easier to understand
    titles = "{:5}   {:22} {:14}  {}".\
        format("Item no.", "Name", "Price", "Description")
    print(titles)
    # print in order: index number +1, space, name, space,
    # description and price
    for i in range(0, len(p)):
        output = "{:3}: {:5} {:20} {} ${}0 {:9} {} "\
            .format(i+1, "", p[i][1], "", p[i][0], "", p[i][2])
        print(output)


def print_order(co):
    """Print customer order.

    Check to see if customer order has anything in it. If not, print message
    If customer order = > 1, print titles.
    For the length of the customer order,
    sub total = the price times the quantity of each pizza flavour
    print pizzas with quantity,
    price and sub total. Set extra to 0.
    Call Receipt calculator.

    :param: co (customer_order, a list of names, prices and
    quantities of pizzas chosen by the customer )
    :return: None
    """
    if len(co) == 0:
        # print message if order is empty
        print("Your order is empty, start ordering!")
        starline()
        return None
    print("YOUR ORDER:")
    dashline()
    # print order headings
    titles = "{:<5}  {:<20}  {:12} {}"\
        .format("QTY", "FLAVOUR", "PRICE", "SUBTOTAL")
    print(titles)
    for i in range(0, len(co)):
        sub_total = co[i][0] * co[i][1]
        # print order
        output = "x{:<5} {:<20} @ ${:<10.2f} ${:3.2f}"\
            .format(co[i][0], co[i][2], co[i][1], sub_total)
        print(output)
    dashline()
    receipt_calc(co, 0)


def print_order_with_indexes(co):
    """Print customer order with indexes.

    Check if length of customer is 0. If so, print message.
    If customer order = > 1, print titles.
    For the length of the customer order,
    sub total = the price times the quantity of each pizza flavour
    print pizzas with index numbers, quantity,
    price and sub total. Set extra to 0.
    Call Receipt calculator.

    :param: co (customer_order, a multidimensional list of names, prices and
    quantities of pizzas chosen by the customer)
    :return: None
    """
    # if order is empty
    if len(co) == 0:
        # print message
        print("Your order is empty, start ordering!")
        starline()
        return False
    # print dotted line
    dotline()
    print("YOUR ORDER:")
    dashline()
    # print order headings
    titles = "{:<5}{:^10}{:<22}{:12}{}"\
        .format("INDEX", "QTY", "FLAVOUR", "PRICE", "SUBTOTAL")
    print(titles)
    for i in range(0, len(co)):
        sub_total = co[i][0] * co[i][1]
        output = "{:2}{:<3}{:^9} {:<21}@ ${:<10.2f} " \
                 "${:3.2f}".format("", i+1, co[i][0],
                                   co[i][2], co[i][1],
                                   sub_total)
        # print order with index numbers
        print(output)
    dashline()
    extra = 0
    receipt_calc(co, extra)


def duplicate_check(co, cp):
    """Scan customer list for duplicate values.

    Search for same terms in customer order.
    If same, print message and request customer input.
    If yes, ask to change quantity and replace new
    quantity with old quantity. Returns True.
    If no, returns False

    :param: co, cp (customer_order, a list of names, prices and
    quantities of pizzas chosen by the customer. chosen_pizza,
    a pizza name chosen by the customer)
    :return: bool
    """
    for i in range(0, len(co)):
        if cp is co[i][2]:
            choice = get_validated_string_y_n("You have already "
                                          "ordered this flavour of pizza, "
                                          "would you like to change the "
                                          "quantity? Y or N -> ", 1, 1).\
                upper()
            if choice is "Y":
                updated = get_integer_conformation("How many {} "
                                                   "pizza's would you "
                                                   "like to order? -> "
                                                   .format(co[i][2]), 1, 10)
                co[i][0] = updated
                dashline()
                print("You now have {} {} pizzas".format(updated, cp))
                dashline()
                print_order(co)
                return True
            elif choice is "N":
                return False
    return None


def add_to_order(p, co):
    """Add a new pizza to the customer order.

    Print pizza menu. Request index number to add pizza.
    Run duplicate function. Request quantity of pizzas.
    Create list with pizza and quantity and append to customer_order.
    Ask to add another pizza or not. If yes, continue.
    If no, print order.

    :param: p, co (pizza_menu, a multidimensional list of pizza names,
    prices and descriptions. customer_order, a multidimensional list of
    names, prices and quantities of pizzas chosen by the customer)
    :return: None
    """
    # print pizza options
    pizza_options(p)
    # print dotted line
    dotline()
    print("ADD TO ORDER: ")
    dotline()
    run = False
    while run is False:
        # ask for item number from menu
        input_1 = get_validated_integer("Please enter an item number "
                                        "from the menu above: -> ", 1, len(p))
        input_1 = input_1 - 1
        chosen_pizza = p[input_1][1]
        # ask for quantity of pizzas
        duplicate = duplicate_check(co, chosen_pizza)
        if duplicate is None:
            input_2 = get_integer_conformation("How many {} pizza's "
                                               "would you like? -> "
                                               .format(chosen_pizza), 1, 10)
            # create a temporary list
            temp_list = [input_2, p[input_1][0], chosen_pizza]
            # append temporary list to main order
            co.append(temp_list)
            # ask to repeat the loop and add another pizza
        choice = get_validated_string_y_n("Add another pizza? y/n : ", 1, 1)
        if choice == "Y":
            # if choice is yes, continue the loop and rerun
            continue
        elif choice == "N":
            starline()
            # if choice is no, print order
            print_order(co)
            return None
        else:
            print("Your input is invalid please choose y/n.")


def change_quantity(co):
    """Update/change quantity of pizza in customer order.

    Request index number to change. Print message.
    Request new number of pizzas.
    Replace old number with new number.
    Print conformation. Returns none

    :param: co (customer_order, a multidimensional list of
    names, prices and quantities of pizzas chosen by the customer)
    :return: None
    """
    # get index number of pizza to change
    index = get_validated_integer(
        "Please enter the index number of the pizza you would "
        "like to change the quantity of: -> ", 1, len(co))
    print("You currently have {} {} pizza/s in "
          "your order".format(co[index-1][0], co[index-1][2]))
    new_quan = get_integer_conformation(
        "How many {} pizza's would you like?: -> ".
         format(co[index-1][2]), 1, 25)
    print("Your order now has {} {} pizza's".
          format(new_quan, co[index-1][2]))
    co[index - 1][0] = new_quan
    return None


def remove_pizza(co):
    """Remove a pizza from the customer order.

    Ask for index number of pizza to remove.
    Print message. Ask for user conformation.
    if yes, remove row from customer order. Print order.
    If no, returns none.

    :param: co (customer_order, a multidimensional list of
    names, prices and quantities of pizzas chosen by the customer)
    :return: None
    """
    # set message
    message = "Please enter the index number of the pizza flavour " \
              "you would like to remove from your order: -> "
    index = get_validated_integer(message, 1, len(co))
    print("Your currently have {} {} pizza/s in "
          "your order".format(co[index - 1][0], co[index - 1][2]))
    # get customer conformation... are you sure?
    message = "Are you sure you would like to remove all {} " \
              "pizza's from your order? Y/N -> ".format(co[index - 1][2])
    choice = get_validated_string_y_n(message, 1, 1).upper()
    if choice == "Y":
        # if choice is 'Y' yes, remove pizza with {} index number from order
        co.pop(index - 1)
        print_order(co)
    elif choice == "N":
        # if choice is 'N' no, return None
        return None
    else:
        print("Please enter 'Y' yes or 'N' no: -> ")


def print_final_receipt(co, cd):
    """Print final receipt (with delivery charges).

    Look for "delivery" in customer details list.
    If there, print relevant customer details incl address,
    set extra charges to $3.50,
    print the order with delivery charges added, final cost and GST.
    If not there, print relevant customer details,
    print order with final cost and GST

    :param: co, cd (customer_order, a multidimensional list of
    names, prices and quantities of pizzas chosen by the customer.
    customer_details, a multidimensional list of customers name, and relevant details)
    :return: None
    """
    if len(co) == 0:
        # print if order is empty
        print("Your order is empty, start ordering!")
        return None
    elif "delivery" in cd:
        # set extra charges to $3.50
        extra = 3.5
        starline()
        print("YOUR ORDER:")
        dashline()
        # print customer details for delivery
        # (name, address, postcode, phone number)
        print("{}".format(cd[0]))
        print("{} {}, {}".format(cd[2], cd[3], cd[4]))
        print("{}".format(cd[5]))
        print("{}".format(cd[1]))
        dashline()
        # print titles
        titles = "{:^10}{:<22}{:12}{}"\
            .format("QTY", "FLAVOUR", "PRICE", "SUBTOTAL")
        print(titles)
        for i in range(0, len(co)):
            # print calculated sub totals
            sub_total = co[i][0] * co[i][1]
            output = "{}{:^9} {:<21}@ ${:<10.2f} " \
                     "${:3.2f}".format("", co[i][0],
                                       co[i][2], co[i][1],
                                       sub_total)
            # print order with index numbers
            print(output)
        dashline()
        # calculate values
        receipt_calc(co, extra)
    else:
        starline()
        print("YOUR ORDER:")
        dashline()
        # print customer details for pick up (name, phone number)
        print("{}".format(cd[0]))
        print("{}".format(cd[1]))
        dashline()
        # print titles
        titles = "{:^10}{:<22}{:12}{}"\
            .format("QTY", "FLAVOUR", "PRICE", "SUBTOTAL")
        print(titles)
        for i in range(0, len(co)):
            # print calculated sub totals
            sub_total = co[i][0] * co[i][1]
            output = "{}{:^9} {:<21}@ ${:<10.2f} " \
                     "${:3.2f}".format("", co[i][0],
                                       co[i][2], co[i][1],
                                       sub_total)
            # print order with index numbers
            print(output)
        dashline()
        receipt_calc(co, 0)


def receipt_calc(co, extra):
    """Calculate final cost, GST and extra charges.

    Total cost is set to 0. For the length of the list,
    the total cost is += to the quantity of
    pizzas times the price for each flavour plus
    extra charges for delivery.
    GST is calculated using 3/23.

    :param: co, extra (customer_order, a multidimensional list of
    names, prices and quantities of pizzas chosen by the customer.
    extra, delivery charge)
    :return: None
    """
    # set total cost to 0
    total_cost = 0
    for i in range(0, len(co)):
        # the total for each row is the price times the quantity
        total_cost += co[i][0] * co[i][1] + extra
        # print total cost, GST and extra charges
    print("{:26}Extra Charges: ${:5.2f} ".format("", extra))
    print("{:36}GST: ${:5.2f} ".format("", total_cost * (3 / 23)))
    print("{:29}Total Cost: ${:5.2f} ".format("", total_cost))
    dashline()


def checkout(co):
    """Finalise order and checkout.

    set menu options, either pickup or delivery.
    Ask user for input.
    If P, ask for limited details.
    Create list and add to customer details (cd). Print final receipt.
    If D, ask for appropriate details.
    Create list and add to customer details (cd). Print final receipt.

    :param: co (customer_order, a multidimensional list of
    names, prices and quantities of pizzas chosen by the customer)
    :return: bool
    """
    if len(co) == 0:
        # no pizza's in list
        print("Your order is empty, start ordering!")
        return None
    my_menu = [
        ("P", "Pick up"),
        ("D", "Delivery")
        ]
    run = True
    while run is True:
        for i in range(0, len(my_menu)):
            # print menu
            output = "{}: {}".format(my_menu[i][0], my_menu[i][1])
            print(output)
            # ask for user input
        choice = get_validated_string("Please choose an option: -> ",
                                      1, 1).upper()
        if choice == "P":
            print("Payment can be made on pickup.")
            dashline()
            # get relevant customer details for pick up
            name = get_validated_string("Please enter your name: -> ",
                                        1, 15).upper()
            number = get_validated_phone("Please enter a contact number "
                                         "(mobile): -> ", 9, 12)
            # create list with customer details
            cd = [name, number, "pickup", "", "", "", ""]
            # print receipt
            print_final_receipt(co, cd)
            print("Thank you for stopping by Pete's Pizza's, your food will "
                  "be ready shortly!")
            starline()
            return True
        elif choice == "D":
            print("Payment can be made on delivery.")
            dashline()
            # get relevant customer details for delivery
            name = get_validated_string("Please enter your name: -> ", 1, 15).\
                upper()
            # get validated phone number
            mobile = get_validated_phone("Please enter a contact number "
                                         "(mobile): -> ", 9, 12)
            number = get_validated_string("Please enter your street "
                                          "number: ", 1, 3)
            street = get_address("Please enter your street name: ", 3, 15)
            suburb = get_validated_string("Please enter your suburb: ", 3, 15)
            postcode = get_validated_string("Please enter your "
                                            "postcode: ", 4, 4)
            # create list with customer details
            cd = [name, mobile, number, street, suburb, postcode, "delivery"]
            # print receipt
            print_final_receipt(co, cd)
            print("Thank you for stopping by Pete's Pizza's, "
                  "your food will be with you shortly!")
            starline()
            return True
        else:
            print("Please enter 'P' or 'D'")


def update_menu(p, co, cd):
    """Run update menu.

    Set menu options, print menu.
    Get user input, if {} letter is chosen, send to {} function.
    Quit option to exit loop.
    returns None
    User is able to update their order by adding,
    removing and changing quantities of pizza's

    :param: p, co, cd (pizza_menu, a multidimensional list of pizza names,
    prices and descriptions. customer_order, a multidimensional list of
    names, prices and quantities of pizzas chosen by the customer.
    customer_details, a multidimensional list of customers name, and relevant details)
    :return: None, bool
    """
    my_menu = [
        ("C", "Change a quantity"),
        ("R", "Remove a Pizza"),
        ("A", "Add a pizza"),
        ("Q", "Main Menu")
    ]
    run = True
    while run is True:
        print("REVIEW ORDER")
        if len(co) == 0:
            print("Your order is empty, please start ordering!")
            return False
        else:
            run = print_order_with_indexes(co)
            # print main menu
            for i in range(0, len(my_menu)):
                output = "{}: {}".format(my_menu[i][0], my_menu[i][1])
                print(output)
            # ask for user's choice as input
            choice = get_validated_string("Please choose an option: -> ",
                                          1, 1).upper()
            if choice == "C":
                starline()
                change_quantity(co)
                starline()
            elif choice == "R":
                starline()
                remove_pizza(co)
            elif choice == "A":
                starline()
                add_to_order(p, co, cd)
            elif choice == "Q":
                return None
            else:
                return None


def cancel_order():
    """Cancel order.

    Ask for user conformation,
    if user chooses to continue,
    returns True
    if not,
    returns False

    :return: bool
    """
    message = "Are you sure you want to cancel your order? Y/N -> "
    choice = get_validated_string_y_n(message, 1, 1).upper()
    if choice == "Y":
        dashline()
        print("Your order has been cancelled.")
        print("Thank you for stopping by Pete's Pizza's! See you next time!")
        return True
    elif choice == "N":
        return False
    else:
        print("Please enter 'Y' yes or 'N' no: -> ")


def main_function():
    """Run main menu.

    Set pizza list, set customer order, set menu options, print menu.
    Get user input, if {} letter is chosen, send to {} function.
    Quit option to exit loop.
    returns None

    :return: None
    """
    starline()
    pizzas = [
        [18.50, "BBQ runaway", "BBQ base with chicken, "
                               "stringy mozzarella cheese and smoky bacon."],
        [18.50, "Pina Colada", "The basic ham, stringy mozzarella cheese "
                               "and pineapple."],
        [18.50, "Sally", "Modern margherita. Triple cheese, "
                         "tomato base with a sprinkle of herbs."],
        [18.50, "Cheese and Garlic", "Stringy mozzarella cheese, "
                                     "white sauce base and a hint of garlic."],
        [18.50, "Vego", "Vegetarian pizza with capsicum, spinach, "
                        "mushrooms, tomato and stringy mozzerella cheese."],
        [25.50, "Chicken and Brie", "Freshly roasted chicken with melted brie "
                                    "and a cranberry sauce."],
        [25.50, "Steak and Kumara", "Freshly braised steak, kumara pieces "
                                    "and a mint sauce."],
        [25.50, "Shrimp Scampi", "White sauce base with garlic shrimp, "
                                 "stringy mozzarella cheese and fresh herbs."],
        [25.50, "Meaty Goodness", "BBQ base with chicken, bacon, sausage, "
                                  "steak and smoky mozzarella."],
        [25.50, "Surprise", "A pizza of the day, you don't find out "
                            "until you get it!"],
        [25.50, "Roll up", "For you and your besties to share! Tomato base, "
                           "mozzarella cheese, ham, chicken."],
    ]

    my_menu = [
        ("M", "See Menu"),
        ("A", "Add to Order"),
        ("R", "Review Order"),
        ("C", "Cancel Order"),
        ("F", "Finalise Order"),
        ("Q", "Quit"),
        ("T", "Test"),
        ]

    start_order = True
    print("Welcome to Pete's Pizzas, please start your order!")
    run = True
    while run is True:
        while start_order is True:
            # when start_order = True,
            # clear customer details by setting it to []
            # clear customer order by setting it to []
            customer_order = []
            customer_details = []
            # set start_order to false
            start_order = False
        print("Main Menu")
        dotline()
        # print main menu
        for i in range(0, len(my_menu)):
            output = "{}: {}".format(my_menu[i][0], my_menu[i][1])
            print(output)
        # ask for user's choice as input
        choice = get_validated_string("Please choose an "
                                      "option: -> ", 1, 1).upper()
        if choice == "M":
            starline()
            # if choice is M
            # print pizza menu
            pizza_options(pizzas)
            starline()
        elif choice == "Q":
            # if choice is Q
            # set start_order to True
            print("Thank you for choosing Pete's Pizza's! "
                  "Have a nice evening :)")
            start_order is False
        elif choice == "A":
            # if choice is A
            # run add_to_order function
            starline()
            add_to_order(pizzas, customer_order)
            starline()
        elif choice == "R":
            # if choice is R
            # run update_menu
            starline()
            update_menu(pizzas, customer_order, customer_details)
            starline()
        elif choice == "C":
            # if choice is C
            # set start_order to outcome
            # of cancel_order function
            starline()
            start_order = cancel_order()
            starline()
        elif choice == "F":
            # if choice is F
            # set start_order to outcome
            # of checkout function
            starline()
            start_order = checkout(customer_order)
            starline()
        elif choice == "T":
            print("test")
            # print_order_with_indexes(customer_order_temp)
        else:
            print("Invalid entry, please try again.")



if __name__ == '__main__':
    main_function()
