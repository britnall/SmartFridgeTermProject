import RPi.GPIO as GPIO
from DHT11 import dht11
import time
import datetime
from alert import send_gmail_alert

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=14)

# Only send email alert once every hour
last_email_time = datetime.datetime.now()

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)

        temp_fehrenheit = (float(result.temperature) * (9.0/5.0)) + 32.0
        current_time = datetime.datetime.now()

        # FDA regulation at or below 40 degrees is unsafe for refrigeration
        if not temp_fehrenheit <= 40.0 and not temp_fehrenheit > 0.0:
            if last_email_time.hour - current_time.hour >= 1:
                send_gmail_alert(temp_fehrenheit, current_time)
                last_email_time = current_time

        # check temperature every 5 minutes if last value was valid
        time.sleep(60*5)
