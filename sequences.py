def generate_arithmetic_sequence() -> list:

    """- Uses user inputs to generate an arithmetic sequence.\n- Function reads in three integers, the first term, the common difference\nand the number of desrired terms."""

    try:
        start_value = int(input("Enter the first term in the sequence: "))
        common_difference = int(input("Enter the common difference of the sequence: "))
        number_of_terms = int(input("Enter how many terms you would like included: "))

        #Create an empty list to store the sequence
        sequence = []

        for i in range(0, number_of_terms): sequence.append(start_value + (i * common_difference))

        return sequence

    except ValueError:
        print("You have entered invalid information\nPlease enter 3 integer values")
        return generate_arithmetic_sequence()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting Program.")
        raise
    except Exception as e:
        print(f"\nUnexpected error occured: {e}")
        return unknown_error_handler(e)

def generate_geometric_sequence() -> list:
    """- Uses user inputs to generate a geometric sequence.\n- Function reads in three integers, the first term, the common ratio\nand the number of desrired terms."""

    try:
        start_value = int(input("Enter the first term in the sequence: "))
        common_ratio = int(input("Enter the common ratio of the sequence: "))
        number_of_terms = int(input("Enter how many terms you would like included: "))

        #Create an empty list to store the sequence
        sequence = []

        for i in range(0, number_of_terms): sequence.append(start_value * common_ratio**i)

        return sequence

    except ValueError:
        print("You have entered invalid information\nPlease enter 3 integer values")
        return generate_geometric_sequence()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exciting Program.")
        raise
    except Exception as e:
        print(f"\nUnexpected error occured: {e}")
        return unknown_error_handler(e)

def unknown_error_handler(error: Exception) -> None:

    """If an unexpected error occurs, will ask the user if they wish to start again or quit."""

    #Ask the user if they want to restart
    restart = str(input("\nWould you like to try again (Y/N)? ")).upper()
    if restart == "Y":
        return generate_arithmetic_sequence()
    elif restart == "N":
        raise
    else:
        print("Invalid input")
        return unknown_error_handler()