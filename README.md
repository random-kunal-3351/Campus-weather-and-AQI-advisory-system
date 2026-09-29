# Campus Weather and AQI Advisory System

## Overview
This project is a Command Line Interface (CLI) application built in Python to help university campuses monitor daily air pollution levels. It takes the daily Air Quality Index (AQI) as input and automatically generates official health advisories (like mandating masks or suspending outdoor sports) based on Central Pollution Control Board (CPCB) standards. The system uses native Python file handling to permanently save daily records without needing a complex database.

## Features
* **Log AQI:** Safely input and record the daily air quality score.
* **Automated Advisories:** Instantly categorizes the AQI (Good to Severe) and provides actionable campus health guidelines.
* **Data Persistence:** Automatically saves all records to a local `campus_aqi.txt` file so no data is lost when the program closes.
* **AQI History:** View all past logs to track seasonal pollution trends on campus.
* **Input Validation:** Prevents program crashes by catching invalid user inputs (like typing letters instead of numbers).

## Technologies & Tools Used
* **Language:** Python 3
* **IDE / Code Editor:** Visual Studio Code (VS Code)
* **Storage:** Local text file handling (`.txt`)
* **Built-in Modules:** `os`, `datetime`

## Steps to Install & Run
1. Clone this repository to your local machine using your terminal or command prompt:
   ```bash
   git clone [https://github.com/random-kunal-3351/Campus-weather-and-AQI-advisory-system.git](https://github.com/random-kunal-3351/Campus-weather-and-AQI-advisory-system.git)
