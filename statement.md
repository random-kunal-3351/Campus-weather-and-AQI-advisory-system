# Problem Statement
On university campuses, sudden spikes in air pollution often go unnoticed until students experience health issues during outdoor sports or physical training. There is a need for a localized system that tracks daily Air Quality Index (AQI) and automatically generates official health advisories. 

# Scope of the Project
This project is a Command Line Interface (CLI) application that allows campus administration to log daily AQI readings. The system categorizes the pollution level using standard CPCB guidelines and issues actionable campus advisories (e.g., suspending sports, mandating masks). It uses native Python file handling to permanently store records for trend tracking.

# Target Users
1. **Campus Administration / Sports Directors:** To log daily readings and decide on canceling outdoor events.
2. **Students / Campus Residents:** To check the daily health advisory before engaging in physical activities.

# High-level Features
* **AQI Logging:** Allows secure entry of daily pollution scores.
* **Automated Advisories:** Categorizes AQI and generates specific campus health rules.
* **Data Persistence:** Saves all historical AQI records locally using text file handling.
* **History Tracking:** Allows users to view past air quality trends.