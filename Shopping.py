from os import getcwd,chdir
from collections import defaultdict

class GetList:
    def __init__(self, recipes):
        self.recipes = recipes
        self.ingredient_list = []
        self.shopping_list_dd = defaultdict(float)
        self.shopping_list = {}
        self.execute()

    def execute(self):
        self.get_ingredients()
        self.add_to_list()
        self.shopping_list = dict(self.shopping_list_dd)

    def get_ingredients(self):
        def_dir = getcwd()
        chdir(getcwd() + chr(92) + 'recipes' + chr(92))
        for item in self.recipes:
            with open(item) as file:
                text = file.read().splitlines()
                begin = text.index('shopping list:',0)
                end = text.index('',begin)
                for items in text[begin+1:end]:
                    self.ingredient_list.append(items)
        chdir(def_dir)

    def add_to_list(self):
        for item in self.ingredient_list:
            split = item.index(' ')
            value = float(item[:split])
            key = item[split+1:]
            self.shopping_list_dd[key] += value



class ShoppingList:
    def __init__(self, recipes, ingredients, staples=''):
        self.ingredients = ingredients
        self.recipes = recipes
        self.staples = staples
        print(self.recipes)
        print(self.ingredients)