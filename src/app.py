from flask import Flask, request, jsonify, make_response
from Users import User
from Trips import Trips
import json

app = Flask(__name__)
categorygeneral = {"Restaurants":28.275,"Transportation":10.52,"Habitation":84.82,"Opythers":158}

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
    password = request.args.get('password')
    user = User.get_user_by_email(email)
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400
    if user["password"] != password:
        return jsonify({"error": "Wrong password! Please try again"})
    return jsonify(user)

@app.route('/city', methods=["GET"])
def city_name():
    return jsonify({"cityName": "Lisbon"})

@app.route('/trips', methods=["GET", "POST","PATCH"])
def trips():
    if request.method == "GET":
        email = request.args.get('email')
        trip = Trips.getTripbyEmail(email=email)
        return json.dumps(trip.__dict__)
    elif request.method == "POST":
        email = request.args.get('email')
        user = User.get_user_by_email(email)
        data = request.get_json()
        newtrip = Trips.createtrip(user, data["loc"], data["tp"], data["sd"], data["ed"])
        return json.dumps(newtrip.__dict__)

@app.route('/signup', methods=["POST"])
def add_user_post():
    data = request.get_json()
    User.factoryuser(email=data["email"], password=data["password"], age=data["age"], gender=data["gender"], name=data["name"], address=data["address"])
    return "success"

@app.route('/simulate', methods=["GET"])
def simulate():
    email = request.args.get('email')
    days = request.args.get("days")
    trip = Trips.getTripbyEmail(email)
    totalprice = trip.Totalprice
    listofpercentage = []
    for cat in categorygeneral:
        percentage = categorygeneral[cat] / sum(categorygeneral.values())
        print(percentage * 100)
        listofpercentage.append(percentage * 100)

    return listofpercentage

@app.route('/pricepercategory', methods=["POST"])
def pricepercategory():
    category = {"Restaurants":28.275,"Transportation":10.52,"Habitation":84.82,"Others":158}
    data = request.get_json()
    print(category["Resturant"] * 1.5 )

    if category["Restaurants"] * 1.5 < data["Restaurants"]:
        message = f"Restaurants is over budget by 50% (Max is: {category['Restaurants'] * 1.5})"
        messagejson = json.dumps({"msg": message})
        return messagejson
    elif category["Habitation"] * 1.5 < data["Habitation"]:
        message = f"Habitation is over budget by 50% (Max is: {category['Habitation'] * 1.5})"
        messagejson = json.dumps({"msg": message})
        return messagejson
    elif category["Transportation"] * 1.5 < data["Transportation"]:
        message = f"Transportation is over budget by 50% (Max is: {category['Transportation'] * 1.5})"
        messagejson = json.dumps({"msg": message})
        return messagejson
    elif category["Others"] * 1.5 < data["Others"]:
        message = f"Others is over budget by 50% (Max is: {category['Others'] * 1.5})"
        messagejson = json.dumps({"msg": message})
        return messagejson
    else:
        category["Habitation"] = data["Habitation"]
        category["Resturant"] = data["Resturant"]
        category["Transportation"] = data["Transportation"]
        category["Others"] = data["Others"]
        categorygeneral["Habitation"] = data["Habitation"]
        categorygeneral["Restaurants"] = data["Restaurants"]
        categorygeneral["Transportation"] = data["Transportation"]
        categorygeneral["Others"] = data["Others"]

    return json.dumps(category)



@app.route('/simulateDays', methods=["GET"])
def simulateDays():
    email = request.args.get('email')
    days = request.args.get("days")
    trip = Trips.getTripbyEmail(email)
    daysPrice = trip.Totalprice / int(days)
    return daysPrice

@app.route('/simulateDays', methods=["PATCH"])
def simulateDaysPatch():
    email = request.args.get('email')
    price = request.args.get("price")
    days = request.args.get("days")
    trip = Trips.getTripbyEmail(email)
    trip.Totalprice = trip.Totalprice - int(price)
    Trips.tripsStore.append(trip)
    Trips.storeTrip()

    return json.dumps(trip.__dict__)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
