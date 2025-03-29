from flight_data_processor import FlightDataProcessor, Status ,InputData
import unittest


class TestFlightDataProcessr(unittest.TestCase):
    def setUp(self):
        self.input_data = InputData
        self.flight_cls = FlightDataProcessor(self.input_data)

    def test_validate_data_function_invalid_input(self):
        wrong_input = [{"flight_number": 256, "departure_time": "2025-02-21 05:30",
                      "arrival_time": "2025-02-22 01:00", "status": "O_TIM"}]
        
        with self.assertRaises(Exception):
            self.flight_cls.validate_data(wrong_input)

    def test_validate_data_function_valid_input(self):
        correct_input = [{"flight_number": "AZ006", "departure_time": "2025-02-21 05:30",
                      "arrival_time": "2025-02-22 01:00", "status": "ON_TIME"}]
        final_output = self.flight_cls.validate_data(correct_input)
        self.assertEqual(len(correct_input), len(final_output))

    def test_add_flight_function_invalid_input_format(self):
        wrong_input = ["flight_number", 256] 
        with self.assertRaises(Exception):
            self.flight_cls.validate_data(wrong_input)

    def test_add_flight_function_with_new_flight_data(self):
        new_flight = {"flight_number": "AZ006", "departure_time": "2025-02-21 05:30",
                      "arrival_time": "2025-02-22 01:00", "status": "ON_TIME"}
        self.flight_cls.add_flight(new_flight)
        self.assertEqual(len(self.flight_cls.flights), 5)

    def test_add_flight_function_with_existing_flight_data(self):
        existing_flight = {"flight_number": "AZ003", "departure_time": "2025-02-21 06:00",
                      "arrival_time": "2025-02-21 12:40", "status": "DELAYED"}
        self.flight_cls.add_flight(existing_flight)
        self.assertEqual(len(self.flight_cls.flights), 4)

    def test_remove_flight_with_invalid_input_format(self):
        Flight_name=234
        with self.assertRaises(Exception):
            self.flight_cls.remove_flight(Flight_name)
        
    def test_remove_flight_with_valid_input(self):
        self.flight_cls.remove_flight("AZ003")
        self.assertEqual(len(self.flight_cls.flights), 3)

    def test_remove_flight_with_invalid_input(self):
        self.flight_cls.remove_flight("AZ008")
        self.assertEqual(len(self.flight_cls.flights), 4)

    def test_flight_by_status_with_invalid_input_format(self):
        with self.assertRaises(Exception):
            self.flight_cls.flights_by_status(0)

    def test_flight_by_status_with_valid_input(self):
         self.assertEqual(len(self.flight_cls.flights_by_status(Status.ON_TIME.value)), 2)

    def test_get_longest_flight(self):
        get_longest_duration = self.flight_cls.get_longest_flight()
        final_output = get_longest_duration.get('flight_number')
        self.assertEqual(final_output, "AZ003")

    def test_update_flight_status_with_invalid_input_format(self):
        new_status=0
        flight_no=23455
        with self.assertRaises(Exception):
            self.flight_cls.update_flight_status(flight_no,new_status)

    def test_update_flight_status_with_valid_input_format(self):
        new_status=Status.CANCELLED.value
        flight_no="AZ002"
        self.flight_cls.update_flight_status(flight_no,new_status)
        final_output=self.flight_cls.flights_by_status(new_status)
        self.assertEqual(len(final_output),1)


if __name__ == "__main__":
    unittest.main()