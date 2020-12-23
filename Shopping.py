from os import getcwd,chdir,listdir
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
    def __init__(self, recipes, ingredients):
        self.ingredients = ingredients
        self.recipes = recipes
        self.staples = []
        self.shopping_list = {}
        self.categories = []
        self.execute()

    def execute(self):
        self.getStaples()
        self.checkStaples()
        self.remove_duplicates()
        self.load_categories()

    def getStaples(self):
        def_dir = getcwd()
        chdir(getcwd() + chr(92) + 'misc' + chr(92))
        with open('staples.txt') as file:
            self.staples = file.read().splitlines()
        chdir((def_dir))

    def checkStaples(self):
        func = True
        while func:
            print('Would you like the remove any of the items?')
            counter = 1
            print('0) Keep all items')
            for items in self.staples:
                print(str(counter) + ') ' + str(items).title())
                counter += 1
            check = int(input('> '))
            if check != 0:
                self.staples.remove(self.staples[check - 1])
            if check == 0:
                func = False

    def remove_duplicates(self):
        for key,values in self.ingredients.items():
            if key not in self.staples:
                self.shopping_list[key.lower()] = values
        for item in self.staples:
            self.shopping_list[item] = ''
        print(self.shopping_list)

    def load_categories(self):
        def_dir = getcwd()
        chdir(getcwd() + chr(92) + 'misc' + chr(92))
        with open('settings.txt') as file:
            raw_text = file.read().splitlines()
            categories = [raw_text.index(i) for i in raw_text if 'categories =' in i]
            for item in categories:
                value = int(item)
            get_setting = raw_text[value]
            start_read = get_setting.index('=') + 3
            setting = get_setting[start_read:-1]
        chdir(def_dir)
        chdir(getcwd() + chr(92) + 'categories' + chr(92))
        with open(setting) as file:
            raw_text = file.read().splitlines()
            for item in raw_text:
                self.categories.append(item.lower())

    # TODO: create embeded dictionaries with categories, items, and amounts
    # TODO: write items from dictionaries to excel file