import requests
from bs4 import BeautifulSoup
from lxml import etree
import smtplib

header = {
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(url=url, headers=header)

# print(response.text.encode('utf-8'))


soup = BeautifulSoup(response.text, "lxml")

price = float((soup.find(class_="a-offscreen")).getText().split("$")[1])
print(price)

normal_price = 100

if price < normal_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="123@gmail.com", password="12345")
        connection.sendmail(to_addrs="ex@gmail.com", from_addr="123@gmail.com", msg=f"The product is below the price!!! Get it now for {price}")
