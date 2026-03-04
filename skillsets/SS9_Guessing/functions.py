import random

def get_requirements():

    print("Developer: Jancarlo Rojas")
    print("Guessing Game")

    print("\nProgram Requirements:\n"
          + "1. Create guessing game based upon pseudo-random numbers.\n"
          + "2. Must perform data and range validation.\n")


    print("Input:")


def get_lower():

    while True:
        try:
            lower = 0
            lower = int(input("Enter lower number: "))

            is_within_range = False

            while not is_within_range:

                if lower >= -1000 and lower <= 1000:
                    is_within_range = True
                else:
                    print("Lower must be between -1000 and 1000.\n")
                    lower = int(input("Enter lower: "))

        except ValueError:
            print("Not an int! Try again.\n")
            continue
        else:
            return lower


def get_upper():

    while True:
        try:
            upper = 0
            upper = int(input("Enter upper number: "))

            is_within_range = False

            while not is_within_range:

                if upper >= -1000 and upper <= 1000:
                    is_within_range = True
                else:
                    print("Upper must be between -1000 and 1000.\n")
                    upper = int(input("Enter upper: "))

        except ValueError:
            print("Not an int! Try again.\n")
            continue
        else:
            return upper


def play_game(lower, upper):

    count = 0
    rand_int = random.randint(lower, upper)

    while True:

        count += 1
        guess = int(input("\nEnter guess: "))

        if guess < rand_int:
            print("Too low!")

        elif guess > rand_int:
            print("Too high!")

        else:
            print("Bingo! Number of tries:", count)
            break