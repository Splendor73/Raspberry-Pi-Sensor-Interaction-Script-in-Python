import os
import RPi.GPIO as GPIO
import time
from gpiozero import PWMOutputDevice

#Set up  GPIO pins for sensors and outputs
TRIG = 17
ECHO = 18
BuzzerPin = 13
motorLeft = PWMOutputDevice(19)

buzzDuration = 0.5
vibrateDuration = 1


#Set up sensors and outputs
def setup():
    global tempSens, BuzzerPin
    # Set up the temperature sensor
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
			      tempSens = i
    # Set up the ultrasonic sensor
    # GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    # Set up the buzzer
    GPIO.setup(BuzzerPin, GPIO.OUT)
    GPIO.output(BuzzerPin, GPIO.HIGH)
    # Set up the vibration motor
    motorLeft.value = 0


#Read the temperature from the temp sensor
def get_temperature():
    location = '/sys/bus/w1/devices/' + tempSens + '/w1_slave'
    tFile = open(location)
    text = tFile.read()
    tFile.close()
    secondline = text.split("\n")[1]
    tempData = secondline.split(" ")[9]
    temperature = float(tempData[2:])
    temperature = temperature / 1000
    return temperature

def get_distance():
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)

    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        a = 0
    time1 = time.time()
    while GPIO.input(ECHO) == 1:
        a = 1
    time2 = time.time()

    during = time2 - time1
    return during * 340 / 2 * 100


# Vibrate the motor
def vibrate(duration):
    motorLeft.value = 1
    time.sleep(duration)
    motorLeft.value = 0


# Activate the buzzer
def buzz(duration):
    GPIO.output(BuzzerPin, GPIO.LOW)
    time.sleep(duration)
    GPIO.output(BuzzerPin, GPIO.HIGH)

def loop():
   while True:
       # Read temp and distance
       temperature = get_temperature()
       distance = get_distance()

       # Print temperature and distance readings
       print("Temperature: %.1f C, Distance: %.1f cm" % (temperature, distance))
       time.sleep(0.1)

       # Execute conditions based on temperature and distance readings
       if 10 > distance >= 5.5:
           vibrate(2)
           time.sleep(3)

       elif distance < 5.5:
           vibrate(2)

       if temperature < 20:
           buzz(2)
           time.sleep(5)

       elif temperature >= 20:
           buzz(5)
           vibrate(5)
           time.sleep(5)

       time.sleep(0.1)

def destroy():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()
    motorLeft.value = 0
    GPIO.output(BuzzerPin, GPIO.HIGH) # Stop the buzzer

#Run the program
if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()