import csv
import os

# TODO: parse in such a way:
# 0. Add another column that holds the price of the unit (as a whole) in itemSKUs.csv - Done
# 1. dict: non vegan option maps to a vegan option, but with 1 key, multiple values
# 2. dict: create another dictionary that reads in vegan options as keys, and values are price.


def open_read_csv_file(file_to_read_in):
    # This function opens a file that is passed in determines the dialect (what format CSV file it is)
    # Then opens the file, and resets the carriage return to top of file.
    # Then returns the file
    file_obj = open(file_to_read_in, 'r', newline='')
    dialect = csv.Sniffer().sniff(file_obj.read())
    file_obj.seek(0)
    print(dialect)
    return csv.reader(file_obj, dialect)


if __name__ == "__main__":
    location_of_skus = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/itemSKUs.csv'
    location_of_Menu_Alternatives = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/MenuItemAlternatives.csv'
    location_of_Menu_Item_Ingrediants = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/menuItemIngrediants.csv'
    
    Skus_Csv = open_read_csv_file(location_of_skus)
    Alternatives_Csv = open_read_csv_file(location_of_Menu_Alternatives)
    Menu_Ingrediants = open_read_csv_file(location_of_Menu_Item_Ingrediants)

    print(f'\n\nSKU CSV File:\n{list(Skus_Csv)}\nIngredients CSV File:\n\n{list(Alternatives_Csv)}\nMenu Ingrediants CSV File:\n\n{list(Menu_Ingrediants)}\n')