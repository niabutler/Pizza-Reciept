"""This document consists of validation functions reqired in 'main_file'."""


def get_validated_integer(m, min, max):
    """Get validated integer.

    to ensure a valid integer is returned,
    tests the input for including the minimum
    and maximum lengths and a string message,
    3 arguments: string message, min int, max int
    """
    while True:
        try:
            number = int(input(m))
        except ValueError:
            print("This is not a valid entry.")
            continue
        if number < min:
            print("Your entry is too small")
            continue
        elif number > max:
            print("Your entry is too big")
        else:
            return number


def get_validated_string(m, min, max):
    """Get validated string.

    to ensure a valid string is returned,
    tests for min and max character len,
    3 arguments: string message, min int, max int
    """
    while True:
        string = input(m)
        string = string.replace(" ", "")
        if len(string) < min:
            print("You have not entered enough characters")
        elif len(string) > max:
            print("You can only enter {} character/s".format(max))
        else:
            return string


def get_validated_string_y_n(m, min, max):
    """Get validated string (Y, N).

    to ensure a valid string is returned of a
    single letter in the list, Y or N.
    tests for min and max character len,
    3 arguments: string message, min int, max int
    """
    while True:
        choice = input(m).upper()
        choice = choice.replace(" ", "")
        if len(choice) < min:
            print("You have not entered enough characters, please enter 1.")
        elif len(choice) > max:
            print("You have entered too many characters, "
                  "please enter 1.".format(max))
        elif choice in ["Y", "N"]:
            return choice
        else:
            print("Your input is invalid please choose y/n.")


def get_integer_conformation(m, min, max):
    """Get integer with conformation.

    to ensure a valid integer is returned,
    tests for minimum and maximum lengths
    and a string message, requests customer
    conformation if input is greater than the max.
    3 arguments: string message, min int, max int
    """
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
            choice = get_validated_string("Press <enter> to confirm or "
                                          "any other key to re-enter -> ",
                                          0, 1).upper()
            if choice == "":
                return number
        else:
            return number


def get_address(m, min, max):
    """Get address.

    to ensure a valid street address is returned,
    tests for min and max character len,
    3 arguments: string message, min int, max int
    """
    while True:
        string = input(m)
        if len(string) < min:
            print("You have not entered enough characters")
        elif len(string) > max:
            print("You can only enter {} character/s".format(max))
        else:
            return string


def get_validated_phone(m, min, max):
    """Get validated phone number.

    to ensure only a valid string of numbers
    is returned.
    tests for min and max character len,
    3 arguments: string message, min int, max int
    """
    while True:
        choice = input(m)
        choice = choice.replace(" ", "")
        if len(choice) < min:
            print("You have not entered enough characters, "
                  "the minimum is 9 characters")
            continue
        elif len(choice) > max:
            print("You can only enter {} character/s".format(max))
            continue
        not_numbers = False
        for i in range(0, len(choice)):
            if choice[i] not in ["0", "1", "2", "3", "4", "5",
                                 "6", "7", "8", "9", "-", "+"]:
                not_numbers = True
        if not_numbers is True:
            print("You should not have any letters in your phone number.")
            continue
        else:
            return choice


if __name__ == "__main__":
    get_validated_string("Please enter 'Y' yes or 'N' no -> ", 1, 1)


