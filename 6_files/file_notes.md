# Working with Files in Python

## Opening Files
- `open(filename, mode)`
- Modes: `'r'` (read), `'w'` (write), `'a'` (append), `'rb'` (binary)

## Reading Files
- `.read()` – reads entire file
- `.readline()` – reads one line
- `.readlines()` – reads all lines into a list
- Looping: `for line in file:`

## Writing Files
- `.write()` – writes to the file (must be in write/append mode)
- Remember to close files or use `with open(...) as f`

## Best Practice
- Use `with` statement to handle files safely (auto-close)
