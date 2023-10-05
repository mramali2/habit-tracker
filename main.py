import requests
from datetime import datetime
import os

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME="rashad98"
TOKEN= os.environ.get("HABIT_TOKEN")
ID = "graph1"

today = datetime.now()


# Parameters required for Pixela API
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

#Code to create account with piela:

# response = requests.post(url = pixela_endpoint, json= pixela_parameters)
# print(response.text)

# Piexela graph creation endpoint:
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Graph configuration parameters
graph_config={
    "id":"graph1",
    "name":"Reading chart",
    "unit":"pages read",
    "type":"int",
    "color":"ichou"
}

# HTTP header with Token for authentication
headers={
"X-USER-TOKEN":TOKEN
}

# HTTP request to set up graph:
# response=requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Endpoint for creating pixel on graph
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

post_pixel_parameters= {
    # API requires date in format yyyyMMdd, automated to today using datetime module
    "date":today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? "),
}

# Final HTTP post request for adding pixel to graph
response = requests.post(url=pixel_endpoint,json=post_pixel_parameters, headers=headers)
print(response.text)

