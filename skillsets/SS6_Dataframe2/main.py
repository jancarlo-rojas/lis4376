#!/usr/bin/env python3
"""
module docstring goes here
"""

import functions as f


def main():
    """program entry"""
    f.get_requirements()
    f.get_data()
    f.count_passengers()
    f.count_perished()
    f.count_males_perished()
    f.percent_males_who_died()
    f.count_age_extremes()
    f.count_unique_home_countries()
    f.count_unique_home_countries_excluding_england_france()


if __name__ == "__main__":
    main()
