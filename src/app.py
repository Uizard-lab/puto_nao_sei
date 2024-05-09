from flask import Flask
from flask import request
from Users import User

app = Flask(__name__)
user = User

@app.route('/drinks', methods=["GET"])
def get_drinks():
    return get_list_of_drinks(50)

@app.route('/drinks/category', methods=["GET"])
def get_drinks_by_category_f():
    category = request.args.get('category')
    return get_drinks_by_category(category)


@app.route('/users', methods=["GET"])
def get_users():
    email = request.args.get('email')
    users.get_user_by_email(email).__dict__
    return get_user_by_email(email)

@app.route('/city', methods = ["GET"])
def city_name():
    return '{"cityName":"Lisbon"}'

@app.route('/plans', methods = ["GET"])
def plans():
    email = request.args.get('email')
    return 'Um plano para ' + email

@app.route('/users', methods=["POST"])
def add_user_post():
    ##data = json.load(Users.User, request.data)
    data = request.get_json()
    print(type(data))

    add_user(email=data["email"],password=data["password"],driver=data["driver"],age=data["age"],weight=data["weight"],
             gender=data["gender"],name=data["name"],emergencyContacts=data["emergencyContacts"],address=data["address"])
    return "success"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

