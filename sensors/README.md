## Refrigerator System
To run both sensor modules at the same time, run refrigerator_system.py

## Temperature Sensor
For the temperature sensor, the python code used to read the data from the DHT11 is from here:
https://github.com/szazo/DHT11_Python

To use that code, the pin number is set to 14 to where the data is read from.
If the pin number is not 14, then you will need to change that in temp_sensing.py line#7 in order for it to work.

## Light Sensor and Camera
To use that code, the pin number is set to 26 to where the data is read from.
If the pin number is not 26, then you will need to change that in light_sensing.py line#8 in order for it to work.

## Email Alerts
If the light is on, a gmail email alert is sent with a picture of the inside of the refrigerator. 
If the temperature gets too high, a gmail email alert is sent with the time and temperature. 
This is done in alert.py. 
A project email address was created to send the emails specifically for this project. 
With WiFi enabled on the device, the emails should be sent.
The email address is: "refridgeratorsensor@gmail.com" with the password "cs370termproject"

## Python Modules
Python will need to be installed on the Raspberry Pi to run the programs. 
To install
```sudo apt-get install python3```

From my understanding, the RPi.GPIO library used for the sensors should be installed
along with python when its installed on the device.
If not, install using
```sudo apt-get install python-dev python-rpi.gpio```
