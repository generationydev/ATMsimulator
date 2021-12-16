import json


class Database:
    def __init__(self, data):
        self.data = data

    def saveData(self):
        user_data = {
            "name": self.data["name"],
            "password": self.data["password"],
            "isAuth": self.data["isAuth"],
        }

        json_objects = json.dumps(user_data, indent= 4)

        with open(f"user.{self.data['name']}.json", "w") as file:
            file.write(json_objects)
