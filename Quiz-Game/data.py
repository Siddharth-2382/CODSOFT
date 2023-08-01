import requests

# Create params for OpenTriviaDB API url
parameters = {
    "amount": 10,
    "type": "multiple",
}

# Get the response from OpenTriviaDB api
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

# Convert the response to json
data = response.json()

# Store results from the raw data in a list
question_data = data["results"]
