#Write a program to prompt for a file name, and then read
#through the file and look for lines of the form: X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print out the average spam confidence.

fname = input('Enter file name: ')
try:
    with open(fname, 'r') as file:
        count = 0
        total = 0.0
        for line in file:
            line = line.strip()
            if not line.startswith('X-DSPAM-Confidence:'):
                continue
            count += 1
            value = float(line.split(':')[1].strip())
            total += value
        average = total / count
        print(f'Total: {total}')
        print(f'Count: {count}')
        print(f'Average: {average}')
except FileNotFoundError:
    print('File not found.')

