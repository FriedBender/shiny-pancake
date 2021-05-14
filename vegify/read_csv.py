# File to read in CSV

import csv
import os


def open_read_csv_file(file_to_read_in):
    file_obj = open(file_to_read_in, 'r', newline='')
    return csv.reader(file_obj)


if __name__ == "__main__":
    location_of_skus = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/itemSKUs.csv'
    location_of_Menu_Alternatives = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/MenuItemAlternatives.csv'
    location_of_Menu_Item_Ingrediants = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/menuItemIngrediants.csv'
    
    Skus_Csv = open_read_csv_file(location_of_skus)
    Alternatives_Csv = open_read_csv_file(location_of_Menu_Alternatives)
    Menu_Ingrediants = open_read_csv_file(location_of_Menu_Item_Ingrediants)

    print(f'\nSku CSV File:\n{Skus_Csv}\nIngredients CSV File:\n{Alternatives_Csv}\nMenu Ingrediants CSV File:\n{Menu_Ingrediants}\n')

    for line in Skus_Csv:
        print(line)