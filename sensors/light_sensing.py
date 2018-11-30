#!/user/bin/env python3
import RPi.GPIO as GPIO
import time
import datetime
import os
from alert import send_pic_gmail_alert

light_sensor = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(light_sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(light_sensor)

    if not input_state:
        print("taking a pic")
        time.sleep(3)

        current_time = datetime.datetime.now()
        image_jpb = time.strftime('%m_%d_%Y_%H_%m_%s') + "_image.jpb"
        os.system("raspistill -o " + image_jpb)
        print("pic taken")

        image_data = open(image_jpb, 'rb').read()
        send_pic_gmail_alert(image_data, image_jpb, current_time)
    else:
        print("nothing")
