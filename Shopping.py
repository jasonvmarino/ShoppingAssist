from os import getcwd,chdir

class ShoppingList():
    def __init__(self, recipes):
        self.recipes = recipes
        print(self.recipes)
        self.get_ingredients()

    def get_ingredients(self):
        def_dir = getcwd()
        chdir(getcwd() + chr(92) + 'recipes' + chr(92))
        for item in self.recipes:
            with open(item) as file:
                text = file.read().splitlines()
                for item in text:
                    print(item)