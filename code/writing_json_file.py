import json

data = {
  "name": "Pepe",
  "last_name": "García"
}

with open("data.json", "w") as file:
    json.dump(data, file)
