import serial
import time

ArduinoConnection = serial.Serial("com5", 9600)
time.sleep(2)

print (ArduinoConnection.readline())

while 1:

    indicator = (input("Enter the option: \n"))

    if indicator == "1":

        ArduinoConnection.write(indicator.encode())
        print("LED should turn on.")
        time.sleep(1)

    if indicator == "0":
        ArduinoConnection.write(indicator.encode())
        print("LED should trun off.")
        time.sleep(1)

