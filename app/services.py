""" This file contains the functions to save and load data from file. """
import json


def save_data_to_file(petitions_data):
    """ Save the data to file """
    with open("petitions_data.json", "w", encoding="utf-8") as file:
        json.dump(petitions_data, file)
    return petitions_data


def load_data_from_file():
    """ Load the data from file """
    petitions_data = []
    try:
        with open("petitions_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                petitions_data.extend(data)
    except FileNotFoundError:
        pass
    return petitions_data
