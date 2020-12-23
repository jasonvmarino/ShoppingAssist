from os import getcwd,chdir,listdir
from random import randint

class Selector:
    def __init__(self, days):
        self.days = int(days)
        self.recipes = []
        self.types = []
        self.selection()
        self.final_check()

    def selection(self):  # Allows you to input how many you would like to select. Calls function to select.
        select_num = int(input('How many would you like to select?\n> '))
        while select_num > self.days:
            select_num = int(input('Exceeds number of days. How many would you like to select?\n> '))
        self.days -= select_num
        while select_num > 0:
            self.get_recipe()
            select_num -= 1
        print('Done with selected')
        while self.days > 0:
            self.get_recipe(rand=1)
            self.days -= 1

    def get_recipe(self, rand=0):  # Used to check recipes for keywords, return recipe
        def_dir = getcwd()
        lor = []
        path = getcwd() + chr(92) + 'recipes' + chr(92)
        while len(lor) == 0:
            keyword = input('What is a keyword in the recipe?\n> ').lower()
            chdir(path)  # Changing directory to look at recipe list
            recipe_list = listdir()
            if keyword == 'all':
                lor = recipe_list[:]
            else:
                for item in recipe_list:
                    with open(item) as file:
                        raw_text = file.read().splitlines()
                        for lines in raw_text:
                            if lines.lower() == keyword.lower():
                                lor.append(item)
                for item in lor:
                    if item in self.recipes:
                        lor.remove(item)
        if rand == 0:
            value = 1
            print('Which recipe would you like to use?')
            for item in lor:
                print(str(value) + ') ' + item[:-4].title())
                value += 1
            selected = int(input('> ')) - 1
            self.recipes.append(lor[selected])
        if rand == 1:
            value = randint(0,len(lor) - 1)
            self.recipes.append(lor[value])
        chdir(def_dir)

    def final_check(self):
        print('Would you like the replace any of the recipes?')
        counter = 1
        print('0) Keep all recipes')
        for items in self.recipes:
            print(str(counter) + ') ' + str(items[:-4]).title())
            counter += 1
        check = int(input('> '))
        if check != 0:
            self.recipes.remove(self.recipes[check - 1])
            type = input('Would you like to select a recipe? (y/n)\n> ').lower()
            if type == 'y':
                self.get_recipe()
            else:
                self.get_recipe(rand=1)
            self.final_check()