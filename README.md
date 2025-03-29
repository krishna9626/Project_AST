# Project_AST
# Flight Data Processor


## Objective
 Implement a robust Python class that processes flight data and demonstrates clean coding practices while incorporating unit testing.

## Task Description
You are given a list of flight data in JSON format. Each flight entry consists of several details. Your goal is to implement a FlightDataProcessor class with advanced features that include handling data transformations and deriving insights from the data.
# 1.Attributes:
oflights: A list of dictionaries, where each dictionary represents a flight with the following keys: 
flight_number (string)
departure_time (string in "YYYY-MM-DD HH:MM" format)
arrival_time (string in "YYYY-MM-DD HH:MM" format)
duration_minutes (integer)
status (enum, e.g. "ON_TIME", "DELAYED", "CANCELLED")
# 2.Methods:
oadd_flight(data: dict) -> None: Adds a new flight to the list, ensuring no duplicates (by flight number).
oremove_flight(flight_number: str) -> None: Removes a flight based on the flight number.
oflights_by_status(status: str) -> List[dict]: Returns all flights with a given status.
oget_longest_flight() -> dict: Returns the flight with the longest duration in minutes.

## Requirements

- python 3 or higher

## Example Data
flight_data = [
    {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30", "arrival_time": "2025-02-20 03:45", "status": "ON_TIME"},
    {"flight_number": "AZ002", "departure_time": "2025-02-21 11:00", "arrival_time": "2025-02-21 16:00", "status": "DELAYED"},
]


## Running script

```sh
python flight_data_processor.py
```

## Running Unit Tests

To ensure correctness, run the unit tests using the following command:

```sh
python -m unittest test_flight_data_processor.py
```
