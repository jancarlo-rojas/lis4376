#!/usr/bin/env python3
"""
module docstring goes here
"""

import functions as f


def main():
    f.get_requirements()

    your_dictionary = f.get_dictionary()

    f.parse_dictionary(your_dictionary)
    f.count_dictionary(your_dictionary)
    f.add_elements(your_dictionary)
    f.update_elements(your_dictionary)
    f.delete_elements(your_dictionary)
    f.delete_dictionary(your_dictionary)


if __name__ == "__main__":
    main()
