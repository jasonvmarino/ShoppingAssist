from Recipe import *
from Shopping import *

#test = Selector(3)
#GetList(temp_test.recipes)
temp_test = ['beef.txt', 'half cow.txt', 'beef - Copy (2).txt']
shopList = GetList(temp_test)
ShoppingList(temp_test, shopList.shopping_list)