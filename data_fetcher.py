import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name):
    """
    Fetches the animal data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary
    """
    response = requests.get(
        "https://api.api-ninjas.com/v1/animals",
        headers={"X-Api-Key": API_KEY},
        params={"name": animal_name},
    )
    return response.json()
