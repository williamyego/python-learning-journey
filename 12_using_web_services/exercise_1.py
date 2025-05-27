#Write a program that Prompts the user for a URL that returns JSON data,Reads the data and parses it.
#The program should Extract the count values from all comments,Compute the sum of these counts,
# Print the total count and the number of items.
import urllib.request
import json

# Prompt the user for the URL
url = input("Enter URL: ")

print(f"Retrieving {url}")
# Open the URL and read the data
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print(f"Retrieved {len(data)} characters")

# Load the JSON data
try:
    info = json.loads(data)
except json.JSONDecodeError:
    print("Error: Could not parse JSON")
    exit()

# Extract the counts
count = 0
total = 0

for item in info['comments']:
    count += 1
    total += int(item['count'])

print(f"Count: {count}")
print(f"Sum: {total}")

