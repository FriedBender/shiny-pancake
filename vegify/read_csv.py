import csv
import os

# TODO: parse in such a way:
# 0. Add another column that holds the price of the unit (as a whole) in itemSKUs.csv - Done
# 1. dict: non vegan option maps to a vegan option, but with 1 key, multiple values
# 2. dict: create another dictionary that reads in vegan options as keys, and values are price.


def open_read_as_dict_csv_file(file_to_read_in):
    # This function opens a file that is passed in determines the dialect (what format CSV file it is)
    # Then opens the file, and resets the carriage return to top of file.
    # Then returns the file
    file_obj = open(file_to_read_in, 'r', newline='')
    dialect = csv.Sniffer().sniff(file_obj.read())
    file_obj.seek(0)
    return csv.reader(file_obj, dialect=dialect)

def print_dict(dictionary_object: dict):
    print("\n")
    for key, value in dictionary_object.items:
        print(f'Key:{key} -> Value: {value}')
    print("\n")



if __name__ == "__main__":
    location_of_skus = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/itemSKUs.csv'
    location_of_Menu_Alternatives = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/MenuItemAlternatives.csv'
    location_of_Menu_Item_Ingrediants = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/menuItemIngrediants.csv'
    
    Skus_csv = open_read_as_dict_csv_file(location_of_skus)
    Alternatives_csv = open_read_as_dict_csv_file(location_of_Menu_Alternatives)
    Menu_Ingrediants_csv = open_read_as_dict_csv_file(location_of_Menu_Item_Ingrediants)

    print_dict(Skus_dict)