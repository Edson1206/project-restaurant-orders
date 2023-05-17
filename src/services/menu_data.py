from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.path = source_path
        self.load_data()

    def load_data(self):
        with open(self.path) as file:
            data = csv.DictReader(file)
            orders = list(data)

        for order in orders:
            name = order["dish"]
            price = float(order["price"])
            ingredient = Ingredient(order["ingredient"])
            amount = int(order["recipe_amount"])

            self.add_dish(name, price)
            self.add_ingredient_dependency(name, ingredient, amount)

    def add_dish(self, name: str, price: float):
        self.dishes.add(Dish(name, price))

    def add_ingredient_dependency(
            self, dish_name: str, ingredient: Ingredient, amount: int):
        for dish in self.dishes:
            if dish.name == dish_name:
                dish.add_ingredient_dependency(ingredient, amount)
