# Regular Expressions in Python
## What is a Regular Expression?
- A regular expression (regex) is a sequence of characters that forms a search pattern, mainly used for string searching and manipulation.
## Importing the re Module
````
import re
````
## Basic Functions in re
- `re.search()`: Searches a string for a match and returns a match object.
````
import re
text = "My number is 07239112534"
match = re.search(r'\d+', text)
if match:
    print(match.group())  # 07239112534
````
- `re.findall()`: Returns a list of all matches.
````
text = "My numbers are 07239112534 and 070031356352"
numbers = re.findall(r'\d+', text)
print(numbers)  # ['07239112534', '070031356352']
````
- `re.match()`: Checks for a match only at the beginning of the string.
## Special Characters and Patterns
| Pattern | Description                  |
| ------- | ---------------------------- |
| `.`     | Any character except newline |
| `^`     | Beginning of line            |
| `$`     | End of line                  |
| `*`     | Zero or more occurrences     |
| `+`     | One or more occurrences      |
| `\d`    | Digit (0–9)                  |
| `\D`    | Non-digit                    |
| `\w`    | Word character               |
| `\W`    | Non-word character           |
| `\s`    | Whitespace                   |
| `\S`    | Non-whitespace               |


