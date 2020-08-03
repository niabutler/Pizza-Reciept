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

def get_validated_string(m, min, max):
    """
    to ensure a valid string is returned,
    tests for min and max character len,
    3 arguments: string message, min int, max int
    """
    while True:
        string = input(m)
        #input = input.replace(" ", "")
        if len(string) < min:
            print("You have not entered enough characters")
        elif len(string) > max:
            print("You have entered too many characters")
        else:
            return string






if __name__ =="__main__":
    get_validated_string("Please enter your option: -> ", 1, 5)


