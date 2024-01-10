import requests
from data_manager import DataManager
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
API_KEY = "zmq6aw7_6EJvSyygw_mSj5r_j0EaDCNb"

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.flight_data = {}

    def get_locations_code(self):
        datamanager = DataManager()
        ids = datamanager.sheet_ids()

        header = {
            "apikey": API_KEY,
        }

        for i in range(len(ids)):
            term = ids[i]
            body = {
            "location_types": "city",
            "term": term,
            }
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=header, params=body)
            response.raise_for_status()
            self.flight_data[i] = response.json()["locations"][0]["code"]
        return self.flight_data