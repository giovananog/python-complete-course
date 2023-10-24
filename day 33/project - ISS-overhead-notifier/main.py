import requests
from datetime import datetime
import smtplib

MY_LAT = -17.745680
MY_LONG = -48.625790

def send_email():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT +5 and  MY_LONG - 5 <= iss_longitude <= MY_LONG +5 and (time_now.hour >= sunset or time_now.hour <= sunrise):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="ex@gmail.com", password="12345")
            connection.sendmail(to_addrs="aa@gmail.com", msg="LOOK AT THE SKY, THE ISS IS CLOSE TO YOU RIGHT NOW!!")



response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
data = iss_response.json()

iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])



send_email()