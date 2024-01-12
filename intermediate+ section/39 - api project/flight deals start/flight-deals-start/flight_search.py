import requests
import datetime
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
API_KEY = "zmq6aw7_6EJvSyygw_mSj5r_j0EaDCNb"
FLY_FROM = "LON"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def prices(self, fly_to_list):
        date = datetime.datetime.now()
        a = date.strftime("%m")
        b = 12 - int(a)
        header = {
            "apikey": API_KEY,
        }
        
        for i in fly_to_list:
            body = {
                "fly_to": i,
                "fly_from": FLY_FROM,
                "date_from": date.strftime("%d/%m/20%y"),
                "date_to": date.strftime(f"%d/{b}/20%y")
            }
            response = requests.get(url=TEQUILA_ENDPOINT, params=body, headers=header)
            print(response.text)