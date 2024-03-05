import json
import os
import requests
import time
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv('API_KEY')

# url for zendesk api request endpoint
url = 'https://myworkspace.zendesk.com/api/v2/organizations.json'

# Define the headers
headers = {
    'Authorization': api_key,  # Replace 'your_api_key' with your actual API key
}

# This is just to keep track of the number of requests made
request_count = 1

# This is to store the organizations data
organizations = []

# clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

while url:
    print(f'Fetching organizations data with count: {request_count}...')
    response = requests.get(url, headers=headers)
    data = response.json()
    res_org_data = data['organizations']
    organizations = organizations + res_org_data

    # Check if 'next_page' is in the response
    if 'next_page' in data and data['next_page'] is not None:
        print('Next page found...')
        url = data['next_page']
        request_count += 1
    else:
        print('No next page found...')
        url = None

    # pause for 50 ms to avoid hitting the rate limit
    time.sleep(0.05)

# see the number of users fetched
print(len(organizations))

# Write the users into a JSON file
with open('orgs.json', 'w') as f:
    json.dump(organizations, f)

# write the users into csv file
with open('orgs.csv', 'w') as f:
    f.write('id,name,tags,notes,created_at\n')
    for org in organizations:
        f.write(f"{org['id']},{org['name']},{org['tags']},{org['notes']},{org['created_at']}\n")




