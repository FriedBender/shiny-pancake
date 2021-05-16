import csv
import os

# TODO: parse in such a way:
# 0. Add another column that holds the price of the unit (as a whole) in itemSKUs.csv - Done
# 1. dict: non vegan option maps to a vegan option, but with 1 key, multiple values (menuItemIngrediants.csv)
# 2. dict: create another dictionary that reads in vegan options as keys, and values are price.


def open_read_as_dict_csv_file(file_to_read_in):
    # This function opens a file that is passed in determines the dialect (what format CSV file it is)
    # Then opens the file, and resets the carriage return to top of file.
    # Then returns the file
    file_obj = open(file_to_read_in, 'r', newline='')
    dialect = csv.Sniffer().sniff(file_obj.read())
    file_obj.seek(0)
    csv_object = csv.reader(file_obj, dialect=dialect)
    csv_object_header = next(csv_object)
    return csv_object_header, csv_object


def create_dictionary_object(csv_object) -> dict:
    dictionary_object = {}
    for row in csv_object:
        key = row[0]
        if key in dictionary_object:
            # Need to figure out duplicate row handling here.
            pass
        dictionary_object[key] = row[1:]
    return dictionary_object

def print_dict(header, dictionary_object: dict):
    # Theoretically, this function is going to print out a pretty version of the
    # dicationary object, which will be formatted in some way....... hopefully.
    print("\n")
    print(f'{header}\n')
    print(dictionary_object)
    print("\n")



if __name__ == "__main__":
    location_of_skus = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/itemSKUs.csv'
    location_of_Menu_Alternatives = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/MenuItemAlternatives.csv'
    location_of_Menu_Item_Ingrediants = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/menuItemIngrediants.csv'
    
    mac_location_of_skus = '/Users/max/Desktop/shiny-pancake/itemSKUs.csv'
    mac_location_of_Menu_Alternatives = '/Users/max/Desktop/shiny-pancake/MenuItemAlternatives.csv'
    mac_location_of_Menu_Item_Ingrediants = '/Users/max/Desktop/shiny-pancake/menuItemIngrediants.csv'


    Skus_csv = open_read_as_dict_csv_file(mac_location_of_skus)
    Alternatives_csv = open_read_as_dict_csv_file(mac_location_of_Menu_Alternatives)
    csv_menu_Ingrediants_header, Menu_Ingrediants_csv = open_read_as_dict_csv_file(mac_location_of_Menu_Item_Ingrediants)

    #   print_dict(csv_menu_Ingrediants_header, Menu_Ingrediants_csv)
    Menu_Ingrediants_dictionary = create_dictionary_object(Menu_Ingrediants_csv)
    print(Menu_Ingrediants_dictionary)