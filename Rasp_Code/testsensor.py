from pymongo import MongoClient
import datetime

#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient("mongodb+srv://root:Qwerty123456@cluster0.1w9ya.mongodb.net/?retryWrites=true&w=majority")
db = client.DummySensors

#Step 2: Create sample data
dummyWL = {
    'type' : "DummyWaterLevelSensor",
    'dateTime' : datetime.datetime.now(),
    'value' : 2356,
    'growbox' : 1
}

#Step 3: Insert business object directly into MongoDB via insert_one
result=db.WaterLevel.insert_one(dummyWL)

#Step 4: Tell us that you are done
print('Finish inserting')