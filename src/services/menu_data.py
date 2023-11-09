import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self._load_menu_data(source_path)

    def _load_menu_data(self, source_path):
        dish_data = self._read_csv_data(source_path)
        self._create_dishes(dish_data)

    def _read_csv_data(self, source_path):
        dish_data = {}
        with open(source_path, newline="", encoding="utf-8") as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader, None)

            for dish_name, price, ingredient_name, quantity in csv_reader:
                dish_data.setdefault(
                    dish_name, {"price": float(price), "ingredients": set()}
                )
                dish_data[dish_name]["ingredients"].add(
                    (Ingredient(ingredient_name), int(quantity))
                )
        return dish_data

    def _create_dishes(self, dish_data):
        for dish_name, data in dish_data.items():
            dish = Dish(dish_name, data["price"])
            for ingredient, quantity in data["ingredients"]:
                dish.add_ingredient_dependency(ingredient, quantity)
            self.dishes.add(dish)
