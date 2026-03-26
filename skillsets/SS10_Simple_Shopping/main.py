"""Skillset 10 Shopping cart"""

import functions as f

def main():
    f.get_requirements()

    your_items = []
    your_costs = []

    your_items = f.add_items()

    if len(your_items) == 0:
        print("No shopping cart items.")
    else:
        your_costs = f.get_items_cost(your_items)
        #f.get_cart(your_items, your_costs)
        f.pretty_cart(your_items, your_costs)

if __name__ == "__main__":
    main()