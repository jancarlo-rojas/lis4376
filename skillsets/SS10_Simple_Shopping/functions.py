"""Skillset 10 Simple shopping cart"""
import random
def get_requirements():
    print("Developer: Jancarlo Rojas")
    print("Simple Shopping Cart!")
    print("\nProgram Requirements:")
    print("1. Capture user-entered shopping items.")
    print("2. Retrieve cost for each item.")
    print("3. Print items, cost, and total of all items.")
    print("4. Must perform data and range validation.")
    print("\n***Extra credit (10 pts):***")
    print("   a. Request tax rate: between 1% and 10%.")
    print("   b. Print pre-tax total, total tax, and total amount with tax.")
    print("   c. Must perform data and range validation.")
    print("\n***Resource(s):***")
    print("Prompt user until valid response: https://www.python-engineer.com/posts/ask-user-for-input/")
    print("Print tabular data:")
    print("   https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data")
    print("   https://www.educba.com/python-print-table/")
    print("\nInput:\n")
def add_items():
    print("Enter -1 to stop program.\n")

    count = 0
    my_items = []

    while True:
        try:
            name = input(f"Enter item {count + 1} name: ").strip()

            # Empty input check
            if name == "":
                raise IndexError

            if name == "-1":
                print("Stopping List.\n")
                break

            my_items.append(name)
            count += 1

        except IndexError:
            print("No item name entered. Try again.\n")

    return my_items

def get_items_cost(items_list):
    my_cost = []

    for item in items_list:
        while True:
            try:
                cost = float(input(f"Enter item {item} cost: $"))

                # Range validation loop
                if cost < 1 or cost > 100:
                    print("Item cost must be between $1 and $100.\n")
                    continue

                my_cost.append(cost)
                break

            except ValueError:
                print("Not a float. Try again.\n")

    return my_cost

def get_cart(items, costs):
    total = 0.0

    print("\n{:<10s} {:>5s}".format("Item", "Cost"))

    for item, cost in zip(items, costs):
        print("{:<10s} ${:.2f}".format(item, cost))
        total += cost

    print("{:<10s} ${:.2f}".format("Total", total))

def pretty_cart(items, costs):
    """Accepts 2 args. Prints shopping cart table and total."""
    get_cart(items, costs)

def get_tax_and_total(costs):
    # Calculate pre-tax total
    subtotal = sum(costs)

    while True:
        try:
            tax_rate = float(input("\n\nEnter tax rate (1% - 10%): "))

            # Range validation
            if tax_rate < 1 or tax_rate > 10:
                print("Tax rate must be between 1% and 10%.\n")
                continue

            break

        except ValueError:
            print("Invalid input. Enter a numeric value.\n")

    # Convert percent to decimal
    tax_decimal = tax_rate / 100

    tax_amount = subtotal * tax_decimal
    total_with_tax = subtotal + tax_amount

    # Output
    print("\n Tax Summary ")
    print("Pre-tax total: ${:.2f}".format(subtotal))
    print("Tax amount:    ${:.2f}".format(tax_amount))
    print("Total w/ tax:  ${:.2f}".format(total_with_tax))