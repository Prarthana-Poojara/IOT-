# IOT-

The Internet of Things (IoT) system developed in this project aims to collect environmental data from virtual sensors, store the data in a cloud-based platform (ThingSpeak), and provide real-time and historical data visualization using MATLAB. The system simulates an environmental station with sensors measuring temperature, humidity, and CO2 levels. This report outlines the steps taken to develop this IoT system.

The IoT system consists of the following components:

•	Virtual Environmental Station: A simulated station generating random sensor data.
•	ThingSpeak: A cloud-based IoT platform used to store and analyze sensor data.
•	MATLAB Analysis App: A tool to visualize and analyze data from ThingSpeak.
Virtual Environmental Station
•	Programming Language: Python
•	Libraries Used: network, urequests, time, urandom
Functions:
•	connect_to_wifi: Connects to a WiFi network.
•	sensor_data: Generates random sensor data for temperature, humidity, and CO2.
•	publish_data: Sends sensor data to ThingSpeak using HTTP requests.
 
Workflow:
•	Connect to WiFi.
•	Generate random sensor data.
•	Send data to ThingSpeak every 1 second.

 

ThingSpeak Configuration
Channel Settings:
Channel ID: 2486676
Write API Key: 290NHE90Q02WGCDE
Fields:
Field1: Temperature
Field2: Humidity
Field3: CO2

MATLAB Analysis App Configuration
Visualization Templates: Used built-in MATLAB Visualization templates provided by ThingSpeak.
 

Conclusion
The IoT system successfully collects, stores, and visualizes environmental data using a virtual environmental station, ThingSpeak, and MATLAB. The system provides real-time monitoring of environmental conditions and historical data analysis, which can be valuable for various applications such as smart agriculture, home automation, and industrial monitoring.
