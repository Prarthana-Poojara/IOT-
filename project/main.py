# import all the necessary libraries 
import network
import urequests
import time
import urandom

# WiFi settings
ssid = 'Wokwi-GUEST'
password = ''  # No password for Wokwi simulated WiFi

# Configuration and creating a link between script and Thinkspeak
writeApiKey = '290NHE90Q02WGCDE'
channel_id = '2486676'
base_url = 'http://api.thingspeak.com/update'

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('Connected to WiFi') # checks if we're connected to the wifi for transfering the data accross successfully 

def sensor_data():
    temperature = urandom.uniform(-50, 50)
    humidity = urandom.uniform(0, 100)
    co2 = urandom.uniform(300, 2000)
    return temperature, humidity, co2 # generates random sensor data and returns 3 values 

def publish_data(temperature, humidity, co2):
    url = f'{base_url}?api_key={writeApiKey}&field1={temperature}&field2={humidity}&field3={co2}'
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            print(f"Data sent successfully: Temperature={temperature}, Humidity={humidity}, CO2={co2}")
        else:
            print(f"Failed to send data: {response.text}")
        response.close()
    except Exception as e:
        print(f"Error occurred: {e}") 

connect_to_wifi(ssid, password)

try:
    while True:
        temperature, humidity, co2 = sensor_data() # the 3 sensor data values are stored in variables 
        publish_data(temperature, humidity, co2) # publishes data to thinkspeak based on our API values and channel ID
        time.sleep(1)  # Publishes every 1 second
except KeyboardInterrupt:
    print('Script stopped') # if user stops 
