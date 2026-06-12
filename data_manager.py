import json

def load_data():
    with open("data/data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def get_events():
    data = load_data()
    return data["events"]

def get_tourism():
    data = load_data()
    return data["tourism"]

def get_restaurants():
    data = load_data()
    return data["restaurants"]

def get_emergency():
    data = load_data()
    return data["emergency"]

def get_embassies():
    data = load_data()
    return data["embassies"]