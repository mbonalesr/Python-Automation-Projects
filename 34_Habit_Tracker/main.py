import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

PIXELA_USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("TOKEN")

GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
HEADERS = {
    "X-USER-TOKEN": TOKEN,
}

# References
# user_params = {
    # "token": TOKEN,
    # "username": USERNAME,
    # "agreeTermsOfService": "yes",
    # "notMinor": "yes",
# }
# 
# graph_config = {
    # "id": "graph1",
    # "name": "Coding Graph",
    # "unit": "Hr",
    # "type": "float",
    # "color": "sora"
# }


def create_user(token:str, user:str, agree_terms:str, nominor:str) -> str:
    """Creates user account in Pixela"""
    user_params = {
        "token": token,
        "username": user,
        "agreeTermsOfService": agree_terms,
        "notMinor": nominor,
    }

    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    return response.text


def create_graph(id:str, name:str, units:str, type:str, color:str, user:str) -> str:
    """Generates personalised graph on Pixela"""
    graph_config = {
        "id": id,
        "name": name,
        "unit": units,
        "type": type,
        "color": color,
    }
    graph_endpoint = f"{PIXELA_ENDPOINT}/{user}/graphs"

    response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
    return response.text


def add_pixel(user:str, id:str, yr:int, mnth:int, d:int) -> str:
    """Appends a new pixel in our graph"""
    pixel_add_endpoint = f"{PIXELA_ENDPOINT}/{user}/graphs/{id}"

    today = datetime(year=yr, month=mnth, day=d)

    pixel_creation = {
        "date": today.strftime("%Y%m%d"),
        "quantity": input("How many hours did you code today? "),
    }

    response = requests.post(url=pixel_add_endpoint, json=pixel_creation, headers=HEADERS)
    return response.text


def update_pixel(user:str, id:str, yr:int, mnth:int, d:int) -> str:
    """Refreshes a current pixel to a new value"""
    today = datetime(year=yr, month=mnth, day=d)
    update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{user}/graphs/{id}/{today.strftime('%Y%m%d')}"

    pixel_update_data = {
        "quantity": input("How many hours did you code today? "),
    }

    response = requests.put(url=update_pixel_endpoint, json=pixel_update_data, headers=HEADERS)
    return response.text


def delete_pixel(user:str, id:str, yr:int, mnth:int, d:int) -> str:
    """Discards an existing pixel"""
    today = datetime(year=yr, month=mnth, day=d)
    delete_endpoint = f"{PIXELA_ENDPOINT}/{user}/graphs/{id}/{today.strftime('%Y%m%d')}"

    response = requests.delete(url=delete_endpoint, headers=HEADERS)
    return response.text

print(add_pixel(user=PIXELA_USERNAME, id=GRAPH_ID, yr=2026, mnth=7, d=17))
