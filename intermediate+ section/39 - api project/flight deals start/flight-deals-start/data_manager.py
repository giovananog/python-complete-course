import requests
URL = "https://api.sheety.co/548b0232936e087fb1affd9b9744628c/flightDeals/prices"

class DataManager:
    def __init__(self):
        pass

    def get_data(self):
        data = requests.get(url=URL)
        return data.json()
    
    def sheet_ids(self):
        data = self.get_data()
        ids = []
        for i in range(len(data["prices"])):
            ids.append(data["prices"][i]["city"])
        return ids
    
    def post_data(self, iata_data):
        sheet_id = self.sheet_ids()
        for i in range(len(sheet_id)):
            body = {
                "price": {
                    "iataCode": iata_data[i]
                }
            }
            r = requests.put(f"{URL}/{i+2}", json=body)
            r.raise_for_status()
