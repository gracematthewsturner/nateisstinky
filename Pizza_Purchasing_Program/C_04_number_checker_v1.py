# functions go here
def num_check(question, num_type, exit_code=None):
    """checks that users enter an integer / float that is more than 0.
"""

    if num_type == "integer":
        error = "Oops - please enter an integer more than 0."
        change_to = int
    else:
        error = "Oops - please enter a number more than 0."
        change_to = float

    while True:
        response = input(question).lower()

        # check for exit code
        if response == exit_code:
            return response

        try:
            # change response to an integer to check its more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine

# loop for testing purposes...
while True:
    print()

    my_float = num_check("Please enter a number more than 0", "float", "")
    print(f"Thanks. You chose {my_float}")
    print()
    my_int = num_check("Please enter an integer more than 0", "integer", "")

    if my_int == "":
        print("You have chosen infinite mode.")
    else:
        print(f"Thanks. You chose {my_int}")
