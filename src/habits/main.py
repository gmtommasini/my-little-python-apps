import requests
from datetime import datetime
import os

TOKEN = os.environ.get("TOKEN")
USERNAME = os.environ.get("USERNAME")

# DOCUMENTATION: https://docs.pixe.la/
base_url = "https://pixe.la"
user_url = base_url+"/v1/users"
graph_url = f"{user_url}/{USERNAME}/graphs"
graph_id = "graph1"
pixel_creation_url = graph_url + '/' + graph_id
graph_headers = {
    "X-USER-TOKEN": TOKEN
}


# User creation
def create_user():
    pix_user_param = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    return requests.post(url=user_url, json=pix_user_param)


# Graph creation
def create_graph():
    graph_body = {
        "id": graph_id,
        "name":"MyFirstGraph",
        "unit":"repetitions",
        "type": "int",
        "color": "momiji"
        # NOTE: colors: shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black) are supported as color kind.
    }
    return requests.post(url=graph_url, json=graph_body, headers=graph_headers)


#### PIXELS ####
date = datetime.now()
date = datetime(year=2023,month=5,day=14)
str_date = date.strftime("%Y%m%d")


# Adding points to the graph
def create_pixel(date : datetime, quantity):
    string_date = date.strftime("%Y%m%d")
    pixel_body = {
        "date": string_date,
        "quantity": quantity
    }
    return requests.post(url=pixel_creation_url, json=pixel_body, headers=graph_headers)


# Updating a pixel)
def update_pixel(dt: datetime, quantity):
    string_date = dt.strftime("%Y%m%d")
    pixel_update_url = f"{pixel_creation_url}/{string_date}"
    pixel_update_body = {
        "quantity": quantity
    }
    return requests.put(url=pixel_update_url, json=pixel_update_body, headers=graph_headers)


# Deleting  a pixel
def delete_pixel(dt:datetime):
    string_date = dt.strftime("%Y%m%d")
    pixel_update_url = f"{pixel_creation_url}/{string_date}"
    return requests.delete(url=pixel_update_url, headers=graph_headers)


response = delete_pixel(date)
print(response.text)