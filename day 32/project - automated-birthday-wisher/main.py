from random import*
from pandas import*
import smtplib
import datetime as dt

now = dt.datetime.now()
month = now.month
day = now.day
data = (read_csv("birthdays.csv"))

for i in range(len(data)):
    if data.to_dict()['month'][i] == month and data.to_dict()['day'][i] == day:
        birth_person = data.to_dict()['name'][i]
        birth_email = data.to_dict()['email'][i]

with open(f"letter_templates/letter_{randint(1,3)}.txt", "r") as letter:
    content = letter.read()

new_content = content.replace("[NAME]", birth_person)
print(new_content)

if "gmail" in birth_email:
    type_email = "smtp.gmail.com"
elif "yahoo" in birth_email:
    type_email = "smtp.mail.yahoo.com"
elif "hotmail" in birth_email:
    type_email = "smtp.live.com"
elif "outlook" in birth_email:
    type_email = "smtp-mail.outlook.com"


with smtplib.SMTP(type_email) as connection:
    connection.starttls()
    connection.login(user="sla@gmail.com", password="123")
    connection.sendmail(from_addr="sla@gmail.com", to_addrs=birth_email)




