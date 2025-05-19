# Write a program to look for lines of the form:
#  New Revision: 39772
#  Extract the number from each of the lines using a regular expression
#  and the findall() method. Compute the average of the numbers and
#  print out the average as an integer.
import re

inp = input('Enter a file name: ')
try:
    with open(inp, 'r') as fr:
        count = 0
        total = 0
        for line in fr:
            line = line.rstrip()
            x = re.findall(r'New Revision: ([0-9]+)', line)
            if x:
                num = int(x[0])  # x is a list with one item
                total += num
                count += 1
        if count > 0:
            average = total / count
            print(f'Average: {int(average)}')
        else:
            print('No matching lines found.')
except FileNotFoundError:
    print('File does not exist!')

