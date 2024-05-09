import json
from flask import Flask
from flask import request
from Users import User
from Trips import Trips

app = Flask(__name__)
user = User
User.loaduserstatic()


@app.route('/users', methods=["GET"])
def get_users():
    email = request.args.get('email')
    users.get_user_by_email(email).__dict__
    return get_user_by_email(email)

@app.route('/city', methods = ["GET"])
def city_name():
    return '{"cityName":"Lisbon"}'

@app.route('/trips', methods = ["GET"])
def plans():
    email = request.args.get('email')
    trip = Trips.getTripbyEmail(email=email)
    return trip

@app.route('/trips', methods = ["POST"])
def create():
    email = request.args.get('email')
    user = User.get_user_by_email(email)
    data = request.get_json()
    newtrip = Trips.tripFactory(user,data["loc"],data["tp"],data["sd"],data["ed"])
    newtrip = newtrip.__dict__
    return json.dumps(newtrip)
@app.route('/users', methods=["POST"])
def add_user_post():
    ##data = json.load(Users.User, request.data)
    ##O pessoal do Back-End é universalmente gostoso
    data = request.get_json()
    print(type(data))

    User.factoryuser(email=data["email"],password=data["password"],age=data["age"], gender=data["gender"],name=data["name"],address=data["address"])
    return "success"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

