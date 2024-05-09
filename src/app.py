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
    user = User.get_user_by_email(email)
    return user

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
    newtrip = Trips.createtrip(user,data["loc"],data["tp"],data["sd"],data["ed"])
    newtrip = newtrip.__dict__
    return newtrip

@app.route('/signup', methods=["POST"])
def add_user_post():
    ##data = json.load(Users.User, request.data)
    ##O pessoal do Back-End é universalmente gostoso
    data = request.get_json()
    print(type(data))

    User.factoryuser(email=data["email"],password=data["password"],age=data["age"], gender=data["gender"],name=data["name"],address=data["address"])
    return "success"

@app.route('/simulate', methods=["GET"])
def simulate():
    email = request.args.get('email')
    days = request.args.get("days")
    return [1920,2000,3000,1]


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

