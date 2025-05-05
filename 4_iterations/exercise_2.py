#Write another program that prompts for a list of numbers as above and at the end prints out
# both the maximum and minimum of the numbers instead of the average.

largest = None
smallest = None
lst = list()
while True:
    try:
        inp = input('Enter a number:')
        if inp == 'done':
            break
        num = float(inp)
        lst.append(num)
    except:
        print('Bad input!')
for values in lst:
    if largest is None or values > largest:
        largest = values
    if smallest is None or values < smallest:
        smallest = values

print(f'Largest: {largest}\nSmallest: {smallest}')
