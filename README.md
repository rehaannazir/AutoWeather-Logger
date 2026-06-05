# AutoWeather Logger

AutoWeather Logger is a Python automation project that fetches real-time weather data from the Open-Meteo API at scheduled intervals and stores the cleaned data into an Excel file using Pandas.

This project demonstrates API fetching, scheduling, retry handling, error handling, logging, and data export automation.

---

## Features

- Fetches current weather data from Open-Meteo API
- Runs automatically after a fixed time interval using `schedule`
- Handles retryable API errors using `tenacity`
- Handles API status codes manually
- Saves clean structured data into an Excel file
- Uses Pandas for data formatting
- Uses logging to track retry attempts
- Includes timeout and request exception handling

---

## Tech Stack

- Python
- Requests
- Pandas
- Schedule
- Tenacity
- Logging
- Open-Meteo API

---

## API Used

This project uses the Open-Meteo Weather API.

### API Endpoint

```python
https://api.open-meteo.com/v1/forecast
```

### Parameters

```python
latitude = 31.5204
longitude = 74.3587
current_weather = True
```

Location Used: **Lahore, Pakistan**

---

## How It Works

```text
Start Scheduler
      ↓
Run API call every 10 seconds
      ↓
Fetch weather data
      ↓
Check API status code
      ↓
Retry if the error is retryable
      ↓
Convert response into clean Pandas DataFrame
      ↓
Save data into Excel file
```

---

## Data Saved

| Column | Description |
|----------|-------------|
| Current Time | Time when the data was fetched |
| Temperature | Current temperature |
| Windspeed | Current wind speed |
| Wind Direction | Wind direction |
| Weather Code | Weather condition code |

---

## Installation

Install the required libraries:

```bash
pip install requests pandas schedule tenacity openpyxl
```

---

## How to Run

Run the Python file:

```bash
python weather_logger.py
```

After running, the scheduler will start and fetch weather data every 10 seconds.

### Example Output

```text
Scheduler Started...

Data Saved! {
    'Current Time': '2026-06-05 19:30:10',
    'Temperature': 33.5,
    'Windspeed': 9.2,
    'Wind Direction': 180,
    'Weather Code': 1
}
```

---

## Output File

```text
weather_data.xlsx
```

---

## Error Handling

The project handles:

- Connection Errors
- Timeout Errors
- Retryable API Errors
- Non-Retryable API Errors
- JSON Decode Errors
- HTTP Status Code Errors

### Retryable Status Codes

```text
500
502
503
504
429
```

### Non-Retryable Status Codes

```text
401
403
404
```

---

## Concepts Demonstrated

- API Integration
- API Response Validation
- Retry Logic
- Exponential Backoff Strategy
- Logging
- Scheduling
- Data Processing
- Data Export Automation
- Exception Handling
- Excel Automation

---

## Future Improvements

- Append records to Excel without overwriting existing data
- Add support for multiple cities
- Store data in SQLite or PostgreSQL
- Send email alerts
- Send Telegram notifications
- Build a Streamlit dashboard
- Create a FastAPI backend service
- Deploy on a cloud server
- Add weather trend analysis

---

## Project Structure

```text
AutoWeatherLogger/
│
├── weather_logger.py
├── weather_data.xlsx
├── requirements.txt
└── README.md
```
