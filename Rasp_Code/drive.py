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
client = MongoClient("mongodb+srv://root:Qwerty123456@cluster0.1w9ya.mongodb.net/?retryWrites=true&w=majority") # Link to MongoDB 
## Specifying the Table being used in the DB
db = client.DummySensors # Table: DummySensors

# Seting GPIO MODE
GPIO.setmode(GPIO.BOARD)

# SENSORS
## Light
## CLIMATE
### Temp & Humi Sensor
TempHumiSensor_1_Input_Pin = 4 # Input pin for the first Humi&Temp Sensor.
DHT_SENSOR = Adafruit_DHT.DHT11 # Usinf Adafruit Library to identify the Type of Sensor being used.
## Nutrient


# Driver Code
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, TempHumi_Input_Pin)
    if humidity is not None and temperature is not None:
        print(f"Temp = {temperature:0.1f} C  Humidity ={humidity:0.1f}%")
    else:
        print("Sensor failure. Chenck wiring.")
    time.sleep(5)
