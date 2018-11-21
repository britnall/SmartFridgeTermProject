from DHT11 import dht11
import RPi.GPIO as GPIO
import time
import datetime
from alert import send_gmail_alert

data_pin=14


def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # read data using pin 14
    instance = dht11.DHT11(pin=data_pin)

    last_email_time = datetime.datetime.now()
    first_update = True

    while True:
        result = instance.read()

        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)

        if result.is_valid():
            current_time = datetime.datetime.now()
            print("Last valid input: " + str(current_time))

            temp_fehrenheit = (float(result.temperature) * (9.0/5.0)) + 32.0
            # FDA regulation at or below 40 degrees is unsafe for refrigeration
            if not (temp_fehrenheit <= 40.0 and temp_fehrenheit > 0.0):

                # Only send email alert once every hour
                elapsed_time = current_time - last_email_time
                if elapsed_time > datetime.timedelta(hours=1) or first_update:
                    print("GMAIL ALERT SENT")
                    send_gmail_alert(temp_fehrenheit, current_time)
                    first_update = False
                    last_email_time = current_time

            # check temperature every minute if last value was valid
            time.sleep(60)
        else:
            time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Program Killed.")
