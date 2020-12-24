from Recipe import *
from Shopping import *

'''test = Selector(3)
temp_test = GetList(test.recipes)'''
temp_test = ['half cow.txt', 'beef.txt', 'beef - Copy (2).txt','beef no meat.txt']
shopList = GetList(temp_test)
sList = ShoppingList(temp_test, shopList.shopping_list)
ExcelWriter(shopList.shopping_list)

# TODO: Add a main menu to change settings, select create list, etc.