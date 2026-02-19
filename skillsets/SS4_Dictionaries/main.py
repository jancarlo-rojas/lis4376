#!/usr/bin/env python3
"""
module docstring goes here
"""

import functions as f


def main():
    f.get_requirements()

    mydictionary = f.get_dictionary()

    f.parse_dictionary(mydictionary)
    f.count_dictionary(mydictionary)
    f.add_elements(mydictionary)
    f.update_elements(mydictionary)
    f.delete_elements(mydictionary)
    f.delete_dictionary(mydictionary)


if __name__ == "__main__":
    main()
