import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").



# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=000'
r = requests.get(url)
data = r.json()

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

yesterday_close = data["Time Series (Daily)"]

list_of_close = [a for (_,a) in yesterday_close.items()]
last_close_yesterday = (list_of_close[0]["4. close"])
print(last_close_yesterday)

#TODO 2. - Get the day before yesterday's closing stock price

day_before_close_price = list_of_close[1]["4. close"]
print(day_before_close_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diffenrence = (abs(float(last_close_yesterday) - float(day_before_close_price)))

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
porcentage_difference = (diffenrence / float(last_close_yesterday) * 100)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if porcentage_difference > 2:
    print('get news')

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

url2 = "https://newsapi.org/v2/everything?qInTitle=Tesla Inc&apiKey=000"
r2 = requests.get(url2)
data2 = r2.json()


# print(articles)
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

three_article = data2["articles"][:3]


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

new_list = [(a["title"], a["description"]) for a in three_article]
print(new_list)

#TODO 9. - Send each article as a separate message via Twilio. 

from twilio.rest import Client

account_sid = "ACdd1ffbfe4797b9c71839b39ad7552302"
auth_token = "a2e7913a451aa8f6d129f1de01f496ca"
client = Client(account_sid, auth_token)

for i in range(len(new_list)):
    message = client.messages.create(
        body = new_list[i],
        from_='+12566671637',
        to='+000'
)



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

