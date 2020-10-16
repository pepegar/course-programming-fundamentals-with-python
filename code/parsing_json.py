import json

with open("data.json") as file:

    json_data = json.load(file)

    print(json_data)
