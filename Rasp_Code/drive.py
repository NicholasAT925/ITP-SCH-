import RPi.GPIO as GPIO 
import time
import Adafruit_DHT
import datetime
import pymongo
from pymongo import MongoClient
from LightSensor import *
from NutrientSensor import *
from ClimateSensor import *

# MongoDB Connection
## Connection to MongoDB - Note: Change connection string as needed
# client = MongoClient("mongodb+srv://root:Qwerty123456@cluster0.1w9ya.mongodb.net/?retryWrites=true&w=majority") # Link to MongoDB 
clientAddress = "mongodb+srv://root:Qwerty123456@cluster0.1w9ya.mongodb.net/?retryWrites=true&w=majority"
## Specifying the Collection being used in the DB
# db = client.DummySensors # Collection: DummySensors
# collection = client.DummySensors
# Date and Time
dateTime = datetime.datetime.now()

# Seting GPIO MODE
GPIO.setmode(GPIO.BOARD)

# SENSORS
## Light

## CLIMATE
### Temp & Humi Sensor
SensorType = "Temperature and Humidity"
TempHumiSensor_1_Input_Pin = 4 # Input pin for the first Humi&Temp Sensor.
DHT_SENSOR = Adafruit_DHT.DHT11 # Usinf Adafruit Library to identify the Type of Sensor being used.

## Nutrient

Sensor1 = TempAndHumidity(1, SensorType)
# Driver Code
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, TempHumiSensor_1_Input_Pin)
    if humidity is not None and temperature is not None:
        Sensor1.send_To_DB(temperature, humidity, dateTime, clientAddress)
    else:
        print("Sensor failure. Check wiring.")
    time.sleep(5)


# while True:
#     humidity, temperature = Adafruit_DHT.read(
#         DHT_SENSOR, TempHumiSensor_1_Input_Pin)
#     if humidity is not None and temperature is not None:
#         print(f"Temp = {temperature:0.1f} C  Humidity ={humidity:0.1f}%")
#         Data = {
#             'Type': SensorType,
#             'dateTime': datetime.datetime.now(),
#             'Temperature': temperature,
#             'Humidity': humidity,
#             'Growbox': 1
#         }
#         result = db.TempAndHumidity.insert_one(Data)
#         print('Finish inserting')
#     else:
#         print("Sensor failure. Check wiring.")
#     time.sleep(5)
