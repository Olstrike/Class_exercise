#oliver stafferöd
#TEINF-20



from pickle import APPEND
from random import randint


class resturant:
    def __init__(self, name, menu: list, ingredients, food, guests, money) -> None:
        self.name = name
        self.menu = menu
        self.ingredients = ingredients
        self.food = food
        self.guests = guests
        self.money = money
    
    def make_food(self):
        return self.food +1, self.ingredients -1
    
    def make_menu(self):
        return self.menu.append("What's on the menue?: ")

    def want_food(self):
        randint(1, )
        return print()


