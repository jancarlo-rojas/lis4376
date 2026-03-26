#!/usr/bin/env python3
import functions as f

def main():
    """Program entry. Calling environment to user-defined functions."""
    # initialize variable(s)
    your_emails = []  # create empty list
    your_phones = []  # create empty list

    # function calls
    f.get_requirements()
    your_emails = f.add_emails()

    # use for testing return values
    # print(len(your_emails), your_emails)
    # exit()

    if len(your_emails) == 0:
        print("No emails!")
    else:
        your_phones = f.get_phones(your_emails)
        # testing returns
        # print(your_phones)
        # exit()

        f.create_contact(your_emails, your_phones)


if __name__ == "__main__":
    main()