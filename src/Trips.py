import json
from Users import User

class Trips:
    category = ["Resturant","Market","Stuff"]


    def __init__(self,user,loc,tp,sd,ed):
        self.Currentuser = user
        self.location = loc
        self.Totalprice = tp
        self.startDate = sd
        self.endDate = ed
        print("Trip Created")

    def tripFactory(user,loc,tp,sd,ed):
        trip = Trips(user,loc,tp,sd,ed)
        trip.category = Trips.category
        return trip

    def createtrip(email, loc, tp, sd, ed):
        trip = Trips.tripFactory(email,loc,tp,sd,ed)
        trip.storeTrip()
        return trip

    def getTripbyEmail(email):
        user = User.get_user_by_email(email)
        trip = Trips.loadTrip()

        return Trips(trip["Currentuser"],trip["location"],trip["Totalprice"],trip["startDate"],trip["endDate"])


    def loadTrip():
        with open("repo/trip.json", "r") as file:
            return json.load(file)

    def storeTrip(self):
        with open("repo/trip.json", "w") as file:
            json.dump(self.__dict__, file)



