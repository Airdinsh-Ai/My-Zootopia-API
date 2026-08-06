import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def load_data_from_api(animal_name):
    """Fetches animal data from the API Ninjas Animals API"""
    response = requests.get(
        "https://api.api-ninjas.com/v1/animals",
        headers={"X-Api-Key": API_KEY},
        params={"name": animal_name},
    )
    return response.json()


def read_template(file_path):
    """Reads the HTML template file and returns its content as string"""
    with open(file_path, "r") as handle:
        return handle.read()


def serialize_animal(animal_obj):
    """Converts a single animal object into an HTML card string"""
    output = ""
    output += '<li class="cards__item">\n'

    if "name" in animal_obj:
        output += f'<div class="card__title">{animal_obj["name"]}</div>\n'

    output += '<div class="card__text">\n'
    output += '<ul class="card__list">\n'

    if "diet" in animal_obj["characteristics"]:
        output += (
            f"<li><strong>Diet:</strong> {animal_obj['characteristics']['diet']}</li>\n"
        )

    if "locations" in animal_obj:
        output += f"<li><strong>Location:</strong> {animal_obj['locations'][0]}</li>\n"

    if "type" in animal_obj["characteristics"]:
        output += (
            f"<li><strong>Type:</strong> {animal_obj['characteristics']['type']}</li>\n"
        )

    if "lifespan" in animal_obj["characteristics"]:
        output += f"<li><strong>Lifespan:</strong> {animal_obj['characteristics']['lifespan']}</li>\n"

    if "weight" in animal_obj["characteristics"]:
        output += f"<li><strong>Weight:</strong> {animal_obj['characteristics']['weight']}</li>\n"

    output += "</ul>\n"
    output += "</div>\n"
    output += "</li>\n"
    return output


def get_skin_type(animal_obj):
    """Returns the animal's skin_type, or 'Unknown' if the field is missing"""
    return animal_obj["characteristics"].get("skin_type", "Unknown")


animal_name = input("Enter a name of an animal: ")
animals_data = load_data_from_api(animal_name)
html_template = read_template("animals_template.html")

animals_info = ""

if animals_data:
    for animal in animals_data:
        animals_info += serialize_animal(animal)
else:
    animals_info = f'<h2>The Animal "{animal_name}" doesnt exist.</h2>'

html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

with open("animals.html", "w") as file:
    file.write(html_output)

print("Website was successfully generated to the file animals.html.")
