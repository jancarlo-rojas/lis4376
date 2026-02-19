"""module docstring goes here"""

def get_requirements():
    """function prints program requirements"""

    print("\nPython Dictionaries")
    print("\nProgram Requirements:\n"
          + "Developer: Jancarlo Rojas\n"
          + "1. Dictionaries (Python data structure): unordered key:value pairs.\n"
          + "2. Dictionary: an associative array (also known as hashes).\n"
          + "3. Any key in a dictionary is associated (or mapped) to a value (i.e., any Python data type).\n"
          + "4. Keys: must be of immutable type (string, number or tuple with immutable elements) and must be unique.\n"
          + "5. Values: can be any data type and can repeat.\n"
          + "6. Dictionaries have key-value pairs instead of single values; differentiating a dictionary from a set.\n"
          + "7. Two methods to create dictionaries:\n"
          + "\ta. Initialize dictionary with key/value pairs.\n"
          + "\tb. Create empty dictionary, using curly braces {}: my_dictionary = {}\n"
          + "\t   Then, assign values to keys: my_dictionary['key1'] = \"some value\"\n"
          + "8. Backward-engineer the following program.\n")


def get_dictionary():
    """function to create and return dictionary"""
    state_capitals = {
        "Alaska": "Juneau",
        "Texas": "Austin",
        "California": "Sacramento",
        "Montana": "Helena",
        "New Mexico": "Santa Fe"
    }
    return state_capitals


def parse_dictionary(my_dictionary):
    """print dictionary contents in multiple ways"""

    print("\nReturn Dictionary's key value pairs, built-in function")
    for k, v in my_dictionary.items():
        print(f"{k} : Value = {v}")

    print("\nDisplay all keys, built in function")
    print(list(my_dictionary.keys()))

    print("\nDisplay all values in dictionary")
    print(list(my_dictionary.values()))

    print("\nDisplay specific key value pair Alaska")
    print(my_dictionary.get("Alaska", "Alaska not found"))


def count_dictionary(my_dictionary):
    print("\nCount number of items")
    print(len(my_dictionary))


def add_elements(my_dictionary):
    my_dictionary["Arizona"] = "Scottsdale"
    print("\nPrint dictionary with added element: ")
    print(my_dictionary)


def update_elements(my_dictionary):
    my_dictionary["Arizona"] = "Phoenix"
    print("\nPrint dictionary after updated element: ")
    print(my_dictionary)


def delete_elements(my_dictionary):
    print("\nDelete element \"Arizona\" from dictionary")

    # safe delete: removes Arizona if it exists, does nothing if it doesn't
    my_dictionary.pop("Arizona", None)

    print("\nPrint dictionary after deleting element: ")
    print(my_dictionary)


def delete_dictionary(my_dictionary):
    print("\nDelete entire dictionary")
    my_dictionary.clear()

    print("\nPrint dictionary after deleting entire dictionary: ")
    print(my_dictionary)
