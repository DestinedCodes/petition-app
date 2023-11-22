import json


# Function to save data to file
def save_data_to_file(petitions_data):
    with open("petitions_data.json", "w") as file:
        json.dump(petitions_data, file)


# # Function to load data from file
def load_data_from_file():
    petitions_data = []
    try:
        with open("petitions_data.json", "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                petitions_data.extend(data)
    except FileNotFoundError:
        pass
    return petitions_data
