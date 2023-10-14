import time
import serial
import string
import pynmea2
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
port = "/dev/ttyAMA0" # the serial port to which the pi is connected.
 
#create a serial object
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
while True:
    try:
        data = ser.readline()
    except Exception as e:
        print("Error:", str(e))
        continue

    # Wait for the serial port to receive data
    if data.startswith(b'$GPGGA'):  
        msg = pynmea2.parse(data.decode())
        print(msg)
    
    time.sleep(2)  # Sleep for 2 seconds before reading the next data
