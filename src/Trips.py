import json
from Users import User

class Trips:
    Currentuser = ""
    location = ""
    Totalprice = ""
    startDate = 0
    endDate = 0
    category = ["Resturant","Market","Stuff"]
    tripsStore = [] 


    def tripFactory(user,loc,tp,sd,ed):
        trip = Trips()
        trip.Currentuser = user
        trip.location = loc
        trip.Totalprice = tp
        trip.startDate = sd
        trip.endDate = ed
        trip.category = Trips.category
        return trip

    def createtrip(email, loc, tp, sd, ed):
        user = User.get_user_by_email(email)
        trip = Trips.tripFactory(user,loc,tp,sd,ed)
        Trips.tripsStore.append(trip)
        Trips.storeTrip()
        return trip

    def getTripbyEmail(email):
        user = User.get_user_by_email(email)
        for trip in Trips.tripsStore:
            if user == trip.Currentser:
                print("One func")


    def tripbyuser(email):
        user = User.get_user_by_email(email)

    def loadTrip():
        with open("../repo/trip.json", "r") as file:
            return json.load(file)

    def storeTrip():
        with open("../repo/trip.json", "w") as file:
            json.dump(Trips.storeTrip, file)

