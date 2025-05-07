# Python Lists

## Creating a List
- `mylist = [1, 2, 3, 'hello', True]`

## Accessing Elements
- `mylist[0]` → first item
- `mylist[-1]` → last item

## List Functions
- `len(mylist)`
- `max(mylist)` / `min(mylist)` (for numbers or comparable items)
- `sum(mylist)` (for numbers)

## List Methods
- `append(x)` → adds x to the end
- `insert(i, x)` → inserts x at position i
- `remove(x)` → removes first occurrence of x
- `pop(i)` → removes item at index i
- `sort()` → sorts the list
- `reverse()` → reverses the list

## Looping Through a List
```python
for item in mylist:
    print(item)
