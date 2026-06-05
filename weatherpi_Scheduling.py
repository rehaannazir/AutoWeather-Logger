import requests as req
import pandas as pd
import time 
import tenacity
import logging
import schedule
from tenacity import retry
from datetime import datetime

# Mannual exception handling using source codes

def retryableAPICall(Exception):
    pass

def nonRetryableAPICall(Exception):
    pass

def check_status(response):

    if response.status_code in [500, 502, 503, 504, 429]:
        raise retryableAPICall(f"Retryable API Call Error. Status Code: {response.status_code}")
    
    if 400 < response.status_code < 500:
        raise nonRetryableAPICall(f"Non Retryable API Call Error. Status Code: {response.status_code}")
    
# Setting logging Environment

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

url = "https://api.open-meteo.com/v1/forecast"  # Weather API 

"""
Parameters:
1. Latitude
2. Longitude
3. current_weather
"""


params = {
    "latitude": 31.5204,      # Lahore
    "longitude": 74.3587,
    "current_weather" : True
}

# Decorator for Retries if API call failed

@retry(
        retry = tenacity.retry_if_exception_type((
            req.exceptions.ConnectionError,
            req.exceptions.ConnectTimeout,
            retryableAPICall
        )),
        stop = tenacity.stop_before_delay(15),
        wait = tenacity.wait_exponential(multiplier = 1, min = 2, max = 20),
        before_sleep = tenacity.before_sleep_log(logger, logging.WARNING),
        reraise = True
        
)


#Fetching weather safely from API

def fetch_weather():

    response = req.get(url, params = params, timeout = 10)

    check_status(response)
    response.raise_for_status()


    try:
        data = response.json()["current_weather"]


        
        row = {
            "Current Time" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Temperature" : data["temperature"],
            "Windspeed" : data["windspeed"],
            "Wind Direction" : data["winddirection"],
            "Weather Code" : data["weathercode"]
        }

        new_data = pd.DataFrame([row])

        new_data.to_excel(
            "weather_data.xlsx",
            index = False,
            header=not pd.io.common.file_exists("weather_data.xlsx")
        )

        print(f"Data Saved! {row}")

    except retryableAPICall as r:
        print("Retryable API Call error occured")

    except nonRetryableAPICall as r:
        print("Non  Retryable API Call error occured")

    except req.exceptions.JSONDecodeError as j:
        print("JSON Decode Error Occured. No JSON file available")

    except req.exceptions.RequestException as q:
        print("Request Exception error occured")
    
    except req.exceptions.Timeout as q:
        print("Timeout error occured")
    
    except req.exceptions.ConnectTimeout as q:
        print("Timeout error occured")



schedule.every(10).seconds.do(fetch_weather)

print("Scheduler Started...")

while True:

    schedule.run_pending()

    time.sleep(2)