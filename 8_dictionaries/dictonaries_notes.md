# Dictionaries in python

Dictionaries store data in **key-value pairs**. They are **unordered**, **changeable**, and **do not allow duplicate keys**.

## Creating a Dictionary

````
person = {
    "name": "Yego",
    "age": 26
}
print(person["name"])  # Output: Yego
````
## Adding or Updating Entries
person["location"] = "Nairobi"

## Looping Through a Dictionary
````
for key in person:
    print(key, person[key])  # Prints key and value
````

## Using *.get()* to avoid errors
````
salary = person.get("salary", 0)  # Returns 0 if "salary" doesn't exist
print(salary)  # Output: 0
````





