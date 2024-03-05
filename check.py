import json

# open the users.json file and load the data
with open('users.json') as f:
    data = json.load(f)

# see the number of users fetched
print(len(data))