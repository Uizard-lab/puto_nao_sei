from flask import Flask, request, jsonify, make_response
from Users import User
from Trips import Trips

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

user = User
User.loaduserstatic()

@app.route('/users', methods=["GET"])
def get_users():
    email = request.args.get('email')
    user = User.get_user_by_email(email)
    return jsonify(user.__dict__)

@app.route('/city', methods=["GET"])
def city_name():
    return jsonify({"cityName": "Lisbon"})

@app.route('/trips', methods=["GET", "POST"])
def trips():
    if request.method == "GET":
        email = request.args.get('email')
        trip = Trips.getTripbyEmail(email=email)
        return jsonify(trip.__dict__)
    elif request.method == "POST":
        email = request.args.get('email')
        user = User.get_user_by_email(email)
        data = request.get_json()
        newtrip = Trips.createtrip(user, data["loc"], data["tp"], data["sd"], data["ed"])
        return jsonify(newtrip.__dict__)

@app.route('/signup', methods=["POST"])
def add_user_post():
    data = request.get_json()
    User.factoryuser(email=data["email"], password=data["password"], age=data["age"], gender=data["gender"], name=data["name"], address=data["address"])
    return "success"

@app.route('/simulate', methods=["GET"])
def simulate():
    email = request.args.get('email')
    days = request.args.get("days")
    return jsonify([1920, 2000, 3000, 1])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
