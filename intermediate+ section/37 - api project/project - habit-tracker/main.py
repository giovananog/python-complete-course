import requests
import datetime

USERNAME = "giovana"
TOKEN = "000"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "NotMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# o headers nao aparece explicitamente na url
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# post value on the graph

post_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
post_graph_congif = {
    "date": "20230921",
    "quantity": "10.4"
}

# i also added a quantity of 5 on the day of 20230922

# response = requests.post(url=post_graph_endpoint, json=post_graph_congif, headers=headers)
# print(response.text)

# now using the datetime module 

today = datetime.datetime.now()

post_graph_congif = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.4"
}


# using put method, so i can update an existing quantity on a existing day

put_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

put_graph_congif = {
    "quantity": "45"
}

# response = requests.put(url=put_graph_endpoint, json=put_graph_congif, headers=headers)



# using delete metod to delete a pixel

delete_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_graph_endpoint, headers=headers)
# print(response.text)

# :)
