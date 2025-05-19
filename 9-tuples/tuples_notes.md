# Tuples

## What is a Tuple?
A **tuple** is a collection of items that is:
- **Ordered**
- **Immutable** (cannot be changed after creation)
- Can contain **mixed data types**

### Example:
```python
t = ('apple', 5, True)
print(t[0])     # Output: apple
```
## Differences from Lists
- Tuples use ()` instead of []
- Tuples cannot be modified: no .append(), .remove(), or item assignment.

## Tuple Assignment
Tuples allow multiple variables to be assigned at once.
````
(x, y) = (4, 'fred')
print(x)  # 4
print(y)  # fred
````
