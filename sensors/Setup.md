For the temperature sensor, the python code used to read the data from the DHT11 is from here:
https://github.com/szazo/DHT11_Python

To use that code, the pin number is set to 14 to where the data is read from.
If the pin number is not 14, then you will need to change that in temp_sensing_py line#14 in order for it to work.

If the temperature gets too high, an gmail email alert is sent. This is done in alert.py. I created an email address to send the emails
specifally for this project. This should work since we enabled WiFi on the device already.
The email address is: "refridgeratorsensor@gmail.com" with the password "cs370termproject"

Python will need to be installed on the Raspberry Pi. From my understanding, the RPi library used for the sensor should be installed
along with python when its installed on the device.
To install
```sudo apt-get install python3```
