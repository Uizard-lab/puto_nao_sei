import json
from threading import Lock



class Drinks:
    _DRINKS_LOCK = Lock()

    class Drink:
        def __init__(self, id: int, drink_name: str, alcohol: str, category: str, bac: float):
            self.id = id
            self.drink_name = drink_name
            self.alcohol = alcohol
            self.category = category
            self.bac = bac

    def __init__(self):
        self._drinks = []
        try:
            self.load_drinks()
        except Exception:
            pass

    def load_drinks(self):
        with Drinks._DRINKS_LOCK:
            with open("../repo/drinks.json", "r") as file:
                self._drinks = json.load(file, object_hook=lambda x: Drinks.Drink(**x))

    def store_drinks(self):
        with Drinks._DRINKS_LOCK:
            with open("../repo/drinks.json", "w") as file:
                json.dump(self._drinks, file, default=lambda x: x.__dict__, indent=4)

    def get_drinks_by_name(self, drink_name: str) -> list[Drink]:
        drinks = []
        for drink in self._drinks:
            if drink.drink_name.startswith(drink_name):
                drinks.append(drink)
        return drinks


    def get_drinks_by_id(self, id):
        for drink in self._drinks:
            if drink.id == id:
                return drink
        return None

    def get_drinks_by_category(self, category):
        drinks = []

        for drink in self._drinks:
            if drink.category == category:
                drinks.append(drink)
        return drinks

    def get_list_of_drinks(self, n_drinks=-1):
        if n_drinks == -1:
            return self._drinks
        return self._drinks[:n_drinks]

