import pytest
from . import read_csv
import csv
import pandas

# These are local to FriedBenders file structure, modify them as needed
location_of_skus = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/itemSKUs.csv'
location_of_Menu_Alternatives = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/MenuItemAlternatives.csv'
location_of_Menu_Item_Ingrediants = '/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/menuItemIngrediants.csv'

class TestRead_Csv(unittest.TestCase):

    def test_open_read_csv_file() -> None:
        print("testing")
        assert 1==0 # Let this fail