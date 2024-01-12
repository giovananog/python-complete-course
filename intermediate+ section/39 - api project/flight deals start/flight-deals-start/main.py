#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData


from pprint import pprint


locations = FlightData()
iata_code = locations.get_locations_code()

datamanager = DataManager()
datamanager.sheet_ids()

flight_search = FlightSearch()
flight_search.prices(iata_code)