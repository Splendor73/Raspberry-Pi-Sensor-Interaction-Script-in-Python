## Raspberry Pi Sensor Interaction Script in Python

### Overview
This repository contains a Python script designed for Raspberry Pi to interact with various hardware components, such as temperature sensors, ultrasonic sensors, a buzzer, and a vibration motor. This script perpetually monitors the ambient temperature and the distance from an object and triggers the buzzer or vibration motor based on predefined conditions to provide alerts or feedback.

### How the Script Works
1. **Initialization:**
   - The script initializes and configures the GPIO pins on the Raspberry Pi to interact with the connected hardware components.
   
2. **Reading Sensors:**
   - The script continually monitors and retrieves data from the temperature and ultrasonic sensors.
   
3. **Response Mechanism:**
   - Depending on the sensor readings, it activates the buzzer or the vibration motor.

### Code Structure
- **Library Imports:**
   ```python
   import os
   import RPi.GPIO as GPIO
   import time
   from gpiozero import PWMOutputDevice
   ```
   
- **Global Variables:**
   - TRIG, ECHO, BuzzerPin, motorLeft, buzzDuration, and vibrateDuration are assigned here.
   ```python
   TRIG = 17
   ECHO = 18
   BuzzerPin = 13
   motorLeft = PWMOutputDevice(19)
   buzzDuration = 0.5
   vibrateDuration = 1
   ```
   
- **Functions:**
   - **`setup()`:** Initializes the sensors and output devices.
   - **`get_temperature()`:** Reads data from the temperature sensor.
   - **`get_distance()`:** Retrieves data from the ultrasonic sensor.
   - **`vibrate(duration)`:** Activates the vibration motor.
   - **`buzz(duration)`:** Triggers the buzzer.
   - **`loop()`:** Main loop that reads from sensors and calls response functions based on conditions.
   - **`destroy()`:** Cleans up the GPIO setup before exiting.

- **Main Execution:**
   ```python
   if __name__ == '__main__':
       try:
           setup()
           loop()
       except KeyboardInterrupt:
           destroy()
   ```

### Important Notes
- The script utilizes libraries like `os`, `RPi.GPIO`, `time`, and `gpiozero`. Make sure they are installed on your Raspberry Pi.
- Ensure that all the hardware components are correctly connected for the accurate functioning of the script.

### Running the Script
To run the script, ensure all hardware components are properly connected, and the required libraries are installed on your Raspberry Pi. Navigate to the directory containing the script and execute it using the following command:
```sh
python3 script_name.py
```
(Replace `script_name.py` with the actual name of your script.)

### Contribution
Fork this project, make enhancements, or fix any bugs and create a pull request. Please keep the `README.md` updated, clear, and concise when you make changes or enhancements.

### Example
```python
def setup():
   #... setting up GPIO Pins and sensors...
```

### Final Thoughts
Review the script thoroughly to understand the interactions between the Raspberry Pi and the connected hardware components before executing or modifying it. If you encounter any issues or have suggestions for improvement, feel free to contribute.
```
