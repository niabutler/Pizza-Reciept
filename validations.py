def get_validated_integer(m, min, max):
    """
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

def get_string(m):
    while True:
        string = input(m)
        return string


def get_validated_string(m, min, max):
    """
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


def get_validated_string_Y_N(m, min, max):
    """
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
            print("You have entered too many characters, please enter 1.".format(max))
        elif choice in ["Y", "N"]:
            return choice
        else:
            print("Your input is invalid please choose y/n.")




#currently not being used - delete later
def single_entry_integer(m, min, max):
    while True:
        try:
            number = int(input(m))
            number = number.replace(" ", "")
        except ValueError:
            print("Please enter a number.")
            continue
        if number < min:
            print("Your entry is too small")
            return None
        elif number > max:
            print("You can only up to 5 of one pizza")
        else:
            return number


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


def get_address(m, min, max):
    """
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
    """
        to ensure only a valid string of numbers
        is returned.
        tests for min and max character len,
        3 arguments: string message, min int, max int
        """
    while True:
        choice = input(m)
        choice = choice.replace(" ", "")
        if len(choice) < min:
            print("You have not entered enough characters")
            continue
        elif len(choice) > max:
            print("You can only enter {} character/s".format(max))
            continue
        not_numbers = False
        for i in range(0, len(choice)):
            if choice[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "+"]:
                not_numbers = True
        if not_numbers == True:
            print("You should not have any letters in your phone number.")
            continue






if __name__ =="__main__":
    # get_integer_conformation("Please enter your number of pizzas : -> ", 1, 9)
    # get_validated_string_Y_N("Enter y, n", 1, 1)
    get_validated_phone("Phone number -> ", 1, 12)


