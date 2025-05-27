# Using Web Services
##  What is a Web Service?

A web service is a way for applications to communicate over the web using standardized formats like JSON or XML.
##  Common Data Formats

- `JSON` (JavaScript Object Notation): Lightweight and easy to use with Python.

- `XML` (Extensible Markup Language): Older format, still used in many systems.
## Using urllib to Access a JSON API
````
import urllib.request
import json

url = 'https://api.agify.io/?name=michael'  # Public API to predict age based on name
print(f'Retrieving {url}...')
response = urllib.request.urlopen(url)
data = response.read().decode()

print('Retrieved', len(data), 'characters')
info = json.loads(data)
print(json.dumps(info, indent=4))  # Pretty print the JSON

print(f"Name: {info['name']}, Predicted Age: {info['age']}")
````
## Using requests for cleaner syntax
````
import requests

url = 'https://api.genderize.io?name=sarah'
response = requests.get(url)
data = response.json()

print(f"Name: {data['name']}, Gender: {data['gender']}, Probability: {data['probability']}")
````
