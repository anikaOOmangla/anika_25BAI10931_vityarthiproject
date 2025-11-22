# anika_25BAI10931_vityarthiproject
Health Monitoring and Alert System

Overview
This project is a console-based Health Monitoring and Alert System that accepts user inputs for heart rate and body temperature, validates them against predefined healthy thresholds, and generates alerts if readings are out of range. The system logs all inputs and alerts for later review.
The project is structured in a modular design with separate components for input handling, health checking, data logging, reporting, and monitoring control, demonstrating basic principles of object-oriented programming in Python.

Features
Accepts heart rate (bpm) and body temperature (°C) inputs from the user.
Validates health parameters against configurable thresholds.
Generates alerts for abnormal heart rate or temperature values.
Logs each reading along with any alerts.
Displays a detailed report of all logged sessions at program end.
Modular design with 5 separate Python modules/classes for better organization and readability.
Graceful input error handling and user-friendly interface.

Technologies / Tools Used
Python 3 (console/terminal based)
Object-oriented programming with classes and modular files
Basic input/output handling
Conditional checks and list data structure for logging

Installation & Running the Project
Make sure Python 3 is installed on your system. You can download it from python.org
Download or clone this repository containing the following files:
user_input.py
health_check.py
data_logger.py
report.py
monitor.py
vityarthi anika project.py (main runner file)
Open a terminal or command prompt and navigate to the folder containing these files.
Run the main file with the command:
press enter
vityarthi anika project.py
Follow on-screen instructions to input health data or quit the program.

Testing Instructions
Run the program and enter numeric heart rate and temperature values when prompted.
Try entering values below or above normal ranges (Heart Rate: 60-100 bpm, Temperature: 36.1-37.2°C) to test alert generation.
Enter non-numeric values to check error handling.

Exit by typing 'q' to quit and view the full health monitoring log.

Verify the logged data and alerts are correctly displayed at the end.
