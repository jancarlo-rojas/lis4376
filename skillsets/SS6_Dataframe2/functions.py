"""
function library for pandas DataFrames/Series
"""

import pandas as pd

# read data into pandas "global" DataFrame (for access in functions below)
df = pd.read_csv("titanic.csv")


def get_requirements():
    """function prints program requirements"""

    print("\nPandas DataFrames and Series Data Structures")
    print("\nProgram Requirements:\n"
          + "Developer: Jancarlo Rojas\n"
          + "1. Working with pandas DataFrames and Series data structures, for tabular data handling.\n"
          + "2. DataFrame: Two-dimensional labeled data structure (i.e., rows/cols).\n"
          + "3. DataFrame: Series collection. Each column is Series sharing same index.\n"
          + "4. Using multiple conditions: not, and, or.\n"
          + "5. Logical operators, numeric comparisons, counting/comparing NaN/non-NaN values.\n\n"
          + "Note: not, and, or statements require truth-values.\n"
          + "Pandas requires \"bitwise\" (overloaded operators): not (~), and (&), or (|).\n"
          + "Print pandas version:\n"
          )
    print(pd.__version__)


def get_data():
     

    print("\nDisplay data:")
    print(df)

    print("\nDisplay type:")
    print(type(df))


def count_passengers():
    

    total_passengers = len(df)
    print("\nTotal number of passengers:", total_passengers)
    return total_passengers


def count_perished():
     

    total_perished = (df["survived"] == "no").sum()
    print("\nTotal number perished:", total_perished)
    return total_perished


def count_males_perished():
     
    males_perished = ((df["survived"] == "no") & (df["gender"] == "male")).sum()
    print("\nTotal males perished:", males_perished)
    return males_perished


def percent_males_who_died():
     

    total_perished = (df["survived"] == "no").sum()
    males_perished = ((df["survived"] == "no") & (df["gender"] == "male")).sum()

    pct = (males_perished / total_perished * 100) if total_perished else 0
    print(f"\nPercentage of males who died from total perished: {pct:.2f}%")
    return pct


def count_age_extremes():
     

    # comparisons with NaN evaluate False automatically
    extreme_age = (df["age"] > 70) | (df["age"] < 5)
    total_extreme_age = extreme_age.sum()

    print("\nTotal number of passengers older than 70 OR younger than 5:", total_extreme_age)
    return total_extreme_age


def count_unique_home_countries():
    

    unique_countries = df["country"].nunique(dropna=True)
    print("\nTotal number of unique home countries:", unique_countries)
    return unique_countries


def count_unique_home_countries_excluding_england_france():
     

    filtered = df.loc[~df["country"].isin(["England", "France"]), "country"]
    unique_excluding = filtered.nunique(dropna=True)

    print("\nTotal number of unique home countries, not including England or France:", unique_excluding)
    return unique_excluding
