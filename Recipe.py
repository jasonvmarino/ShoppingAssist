from os import getcwd,chdir,listdir

class Selector:
    def __init__(self, days):
        self.days = int(days)
        self.recipes = []
        self.types = []
        self.keyword()

    def selection(self):  # Allows you to input how many you would like to select. Calls function to select.
        select_num = int(input('How many would you like to select?'))
        while select_num == 0 or select_num > self.days:
            select_num = input('Exceeds number of days. How many would you like to select?')
        self.days -= select_num
        while select_num > 0:
            # Insert search recipe function here
            select_num -= 1

    def keyword(self, rand = ''):  # Used to check recipes for keywords
        def_dir = getcwd()
        recipe_list = []
        lor = []
        path = getcwd() + chr(92) + 'recipes' + chr(92)
        keyword = input('What is a keyword in the recipe?')
        chdir(path)  # Changing directory to look at recipe list
        recipe_list = listdir()
        for item in recipe_list:
            with open(item) as file:  # Checking keywords in files
                r_keywords = []
                print(item)  # Used to print out recipe names first. DEBUG ITEM
                text = file.readlines()
                for line in text:
                    if line == 'keywords:\n':
                        pass
                    elif line == '\n':
                        break
                    else:
                        r_keywords.append(line[:-1])
                print(r_keywords)  # Used to print out keywords for recipes. DEBUG ITEM





        #if rand == '':
