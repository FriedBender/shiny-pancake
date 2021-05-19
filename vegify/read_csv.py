import csv
import os

# TODO: parse in such a way:
# 0. Add another column that holds the price of the unit (as a whole) in itemSKUs.csv - Done
# 1. dict: non vegan option maps to a vegan option, but with 1 key, multiple values (menuItemIngrediants.csv) - Done
# 2. dict: create another dictionary that reads in vegan options as keys, and values are price.


def open_read_csv_file(file_to_read_in):
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
            # I will make duplicate rows append to the existing key
            pass
        dictionary_object[key] = row[1:]
    return dictionary_object


def return_value_from_key(dictionary_object: dict, key: str, column: int) -> str:
    # This will take in a dictionary from which you want to search the key
    # A key, for which you want to search
    # and which value you want to return
    # Note: If needed, this can be modified to take in a variable amount of arguments
    #   https://stackoverflow.com/questions/919680/can-a-variable-number-of-arguments-be-passed-to-a-function
    return dictionary_object.get(key)[column]

def print_dict(header, dictionary_object: dict) -> None:
    # Theoretically, this function is going to print out a pretty version of the
    # dicationary object, which will be formatted in some way....... hopefully.
    print("\n")
    print(f'{header}')
    for key, value in dictionary_object.items():
        print(f'Key: {key} ---> Value: {value}')
    print("\n")





if __name__ == "__main__":
    # Max's computer locations
    location_of_skus = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/itemSKUs.csv'
    location_of_Menu_Alternatives = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/MenuItemAlternatives.csv'
    location_of_Menu_Item_Ingrediants = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/menuItemIngrediants.csv'
    
    # Macbook locations
    mac_location_of_skus = '/Users/max/Desktop/shiny-pancake/itemSKUs.csv'
    mac_location_of_Menu_Alternatives = '/Users/max/Desktop/shiny-pancake/MenuItemAlternatives.csv'
    mac_location_of_Menu_Item_Ingrediants = '/Users/max/Desktop/shiny-pancake/menuItemIngrediants.csv'

    # Create the csv objects
    # I should make this into a function with varying amount of arguments passed in.
    skus_header, skus_csv = open_read_csv_file(location_of_skus)
    vegan_alternatives_header, vegan_alternatives_csv = open_read_csv_file(location_of_Menu_Alternatives)
    menu_Ingrediants_header, menu_Ingrediants_csv = open_read_csv_file(location_of_Menu_Item_Ingrediants)

    # create dictionary values
    # I should make this into a function with varying amount of arguments passed in.
    skus_dictionary_structure = create_dictionary_object(skus_csv)
    vegan_alternatives_dictionary_structure = create_dictionary_object(vegan_alternatives_csv)
    menu_Ingrediants_dictionary_structure = create_dictionary_object(menu_Ingrediants_csv)

