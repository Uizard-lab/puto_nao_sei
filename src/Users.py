
import json
class User:
    id = 0
    name = ""
    gender = ""
    address = ""
    age = 0
    email = ""
    password = ""
    currentUsers = []
    def loaduserstatic():
            User.currentUsers = User.load_users()

    def factoryuser( name: str, gender: str, 
                    age: int,  email: str, address: str, password: str):
        newuser = User()
        newuser.name = name
        newuser.gender = gender
        newuser.age = age
        newuser.email = email
        newuser.password = password
        newuser.address = address
        User.loaduserstatic()
        User.currentUsers.append(newuser)        
        newuser.store_users()
        return newuser

    def load_users():

        with open("repo/users.json", "r") as file:
            return json.load(file)

    def store_users(self):
        with open("repo/users.json", "w") as file:
            json.dump(self.currentUsers, file, default=lambda x: x.__dict__, indent=4)

    def get_user_by_email(email: str):
        for user in User.currentUsers:
            print(type(user))
            if user["email"] == email:
                return user
        return None

    def get_user_by_id(self, user_id: int) :
        for user in self._users:
            if user.id == user_id:
                return user
        return None

    def get_next_id(self) -> int:
        if not self._users:
            return 1
        return self._users[-1].id + 1

