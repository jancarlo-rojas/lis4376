import random

def get_requirements():

    print("Developer: Jancarlo Rojas")
    print("Pseudo-Random Number Lists")

    print("\nProgram Requirements:\n"
          + "1. Create pseudo-random list of numbers.\n"
          + "2. Sort pseudo-random list of numbers.\n"
          + "3. Must perform data and range validation.\n")

    print("Input:")


def get_list_size():

    while True:
        try:

            size = 0

            size = int(input("Enter list size: "))

            is_within_range = False

            while not is_within_range:

                if size >= 1 and size <= 10:
                    is_within_range = True
                else:
                    print("List size must be between 1 and 10.\n")
                    size = int(input("Enter list size: "))

        except ValueError:
            print("Not an int! Try again.\n")
            continue
        else:
            return size


def create_list(size):

    my_list = []

    for my_iterator in range(size):

        while True:

            number = random.randint(1, size)

            if not number in my_list:

                my_list.append(number)
                break

    return my_list


def sort_list(test_list):

    print("\nOriginal pseudo-random number list: ", test_list)

    test_list.sort()
    print("Sorted list (ascending):", test_list)

    test_list.sort(reverse=True)
    print("Sorted list (descending):", test_list)