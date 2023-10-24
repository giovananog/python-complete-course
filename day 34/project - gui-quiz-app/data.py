import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

content = requests.get(url="https://opentdb.com/api.php", params=parameters)
content.raise_for_status()
json_data = content.json()
question_data = json_data["results"]