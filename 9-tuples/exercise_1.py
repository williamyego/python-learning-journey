# Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lowercase and only count the letters a-z.
# Your program should not count spaces,digits,punctuation,or anything other than the letters a-z.

import string

i = input('Enter file name: ')
d = dict()

try:
    with open(i, 'r') as fread:
        for line in fread:
            line = line.translate(str.maketrans('', '', string.punctuation))
            line = line.strip().lower()

            for char in line:
                if char.isalpha():
                    d[char] = d.get(char, 0) + 1

    lst = [(val, key) for key, val in d.items()]
    lst.sort(reverse=True)

    for val, key in lst:
        print(key, val)

except FileNotFoundError:
    print('File does not exist!')



