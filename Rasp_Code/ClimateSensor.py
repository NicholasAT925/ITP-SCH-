from pymongo import MongoClient

# Temperature and Humidity class
class TempAndHumidity:
    def __init__(self, GrowBox, Type):
        self.GrowBox = GrowBox
        self.Type = Type

    def set_GrowBox(self, GrowBox):
        self.GrowBox = GrowBox

    def set_Type(self, Type):
        self.Type = Type
    
    def send_To_DB(self, Temp, Humidity, time, Mongo_client):
        client = MongoClient(Mongo_client)  # Link to MongoDB
        db = client.DummySensors  # Collection: DummySensors
        Data = {
            'Type': self.Type,
            'dateTime': time,
            'Temperature': Temp,
            'Humidity': Humidity,
            'Growbox': self.GrowBox
        }
        db.TempAndHumidity.insert_one(Data)
        print('Finish inserting')
