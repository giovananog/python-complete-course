import requests
from twilio.rest import Client

parameters = {
    "lat": "-21.426164",
    "lon": "-45.947988",
    "appid": "000",
    "exclude": "current,minutely,daily",
}

response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()

data = response.json()

will_rain = ["Bring an umbrella" for i in range(12) if int(data["hourly"][i]["weather"][0]["id"]) > 700]



if "Bring an umbrella" in will_rain:
    account_sid = '0'
    auth_token = '0'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="vai chover...",
    from_='+12566671637',
    to='+0000'
)