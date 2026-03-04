#!/usr/bin/env python3
import functions as f

def main():

    size = 0
    your_list = []

    f.get_requirements()
    size = f.get_list_size()

    your_list = f.create_list(size)

    f.sort_list(your_list)


if __name__ == "__main__":
    main()