from datetime import datetime
from enum import Enum


InputData = [
    {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30", "arrival_time": "2025-02-20 03:45",
     "status": "ON_TIME"},
    {"flight_number": "AZ002", "departure_time": "2025-02-21 11:00", "arrival_time": "2025-02-21 16:00",
     "status": "DELAYED"},
     {"flight_number": "AZ003", "departure_time": "2025-02-20 06:00", "arrival_time": "2025-02-21 12:30",
     "status": "DELAYED"},
     {"flight_number": "AZ004", "departure_time": "2025-02-20 01:50", "arrival_time": "2025-02-20 03:45",
     "status": "ON_TIME"},
]

class Status(Enum):
    ON_TIME = "ON_TIME"
    DELAYED = "DELAYED"
    CANCELLED = "CANCELLED"


class FlightDataProcessor:
    def __init__(self, flights: list) -> None:
        """
        Initializes an Flight Data object

        Args:
            flights (list): Input data.
            
        """
        updated_data = self.validate_data(flights)
        self.flights = updated_data

    def validate_data(self, flights: list) -> list:
        """
        Validates the Flight Data in specified format.

        Args:
            flights (list): Input data.

        Returns:
            flights (list): After sucessfull validation, it returns a list.
            
        """
        updated_data = []
        for x in flights:
            if not isinstance(x["flight_number"], str):
                raise TypeError("flight_number should be string")
            if not isinstance(x['departure_time'], str):
                raise TypeError("departure_time  should be string") 
            if x['departure_time'] != (datetime.strptime(x['departure_time'],"%Y-%m-%d %H:%M").strftime("%Y-%m-%d %H:%M")):
                raise ValueError("departure_time date format is not specified format")
            if not isinstance(x['arrival_time'], str):
                raise TypeError("arrival_time  should be string") 
            if x['arrival_time'] != (datetime.strptime(x['arrival_time'],"%Y-%m-%d %H:%M").strftime("%Y-%m-%d %H:%M")):
                raise ValueError("arrival_time date format is not specified format")
            if x['status'] != Status(x["status"]).value:
                raise ValueError("Invalid Status")         
            duration_minutes = ((datetime.strptime(x["arrival_time"], "%Y-%m-%d %H:%M") -  datetime.strptime(x["departure_time"], "%Y-%m-%d %H:%M")).total_seconds())/(60)
            x['duration_minutes']=int(duration_minutes)
            updated_data.append(x)

        return updated_data
    
    def add_flight(self, data: dict) -> None:
        """
        Add new flight details in existing flight data.

        Args:
            data (dict): Input data.

        Returns:
            None : After adding new data, it returns a None otherwise it throws error.
            
        """
        if isinstance(data, dict) :
            updated_data = self.validate_data([data])
            flight_num = tuple(x.get("flight_number")  for x in self.flights)
            if data['flight_number'] not in flight_num:
                self.flights.extend(updated_data)
            return
        else:
            raise TypeError("Data should be in dictionary format")


    def remove_flight(self, flight_number : str) -> None:
        """
        Remove flight details in existing flight data based on given input.

        Args:
            flight_number (str): Input data.

        Returns:
            None : After removing given data, it returns a None otherwise it throws error.
            
        """
        if isinstance(flight_number, str) :
            self.flights = [x for x in self.flights if x.get('flight_number') != flight_number]
            return
        else:
            raise TypeError("flight_number should be string")


    def flights_by_status(self, status : str) -> list[dict]:
        """
        This funtion gives the flight details based on given status.

        Args:
            status (str): Input data.

        Returns:
            List[dict] :  It returns a list of dictionaries when it sucessfully executed otherwise it throws error.
            
        """
        if isinstance(status, str) :
            return [x for x in self.flights if x.get('status') == status]
        else:
            raise TypeError("flight_number should be string")

    def get_longest_flight(self) -> dict:
        """
        This funtion gives longest time travelling distance taken by the Flight.

        Returns:
            dict :  It returns a dictionary r.
            
        """
        return max(self.flights, key=lambda x: x['duration_minutes'])
    
    def display_flight(self) -> list[dict]:
        """
        This funtion prints the flight details.

        Returns:
            list[dict] :  It returns a list of dictionaries.
            
        """
        print(f"Flight Data :  {self.flights}")

    def update_flight_status(self, flight_number:str, new_status:str) -> None:
        """
        Update the flight status based on given flight number and status.

        Args:
            flight_number (str): first Input arg (flight_number).
            status (str): Second Input arg (status).

        Returns:
            None : After updating given flight number and status, it returns a None otherwise it throws error.
            
        """
        if isinstance(flight_number,str) and isinstance(new_status,str):
            for flight in self.flights:
                if flight.get('flight_number') == flight_number:
                    flight['status'] = Status(new_status).value
                    return
        else:
            raise TypeError("flight_number and status should be string")

   

# FDP = FlightDataProcessor(InputData)

# new_flight_data = {"flight_number": "AZ005", "departure_time": "2025-02-22 18:30", "arrival_time": "2025-02-23 01:40",
#      "status": "ON_TIME"}
# FDP.add_flight(new_flight_data)
# FDP.display_flight()
# FDP.remove_flight("AZ005")


# get_flight_status = FDP.flights_by_status("ON_TIME")
# print("Flight status ",get_flight_status)

# get_longest_flight_by_duration = FDP.get_longest_flight()
# print("Longest travel duration",get_longest_flight_by_duration)

# FDP.update_flight_status("AZ003","CANCELLED")
# FDP.display_flight()

