from Drinks import Drinks
from Users import Users
from DrinkLogs import DrinkLogs

drinks = Drinks()
drink_log = DrinkLogs()
users = Users(drink_log)

def get_user_by_email(email: str):
    return 

def add_user(name: str, gender: str, weight: float, age: int, driver: bool, email: str, password: str,emergencyContacts,address):
    users.add_user(name=name, gender=gender, weight=weight, age=age, driver=driver, email=email,
                   password=password,emergencyContacts=emergencyContacts,address=address)

def get_bac_by_user_id(user_id: int):
    return users.get_bac_by_user_id(user_id)

def get_drinks_by_category(category):
    return [i.__dict__ for i in drinks.get_drinks_by_category(category)]

def get_list_of_drinks(n_drinks: int):
    return [i.__dict__ for i in drinks.get_list_of_drinks(n_drinks)]

def get_drinks_by_name(drink_name: str):
    return [i.__dict__ for i in drinks.get_drinks_by_name(drink_name)]
