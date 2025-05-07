#Write a program to read through the mail box data and when you find line that starts with “From”,
# you will split the line into words using the split function. We are interested in who sent the
# message, which is the second word on the From line.
#You will parse the From line and print out the second word for each From line, then you will also count the number
# of From (not From:) lines and print out a count at the end.

fname = input('Enter file name:')
count = 0
with open(fname,'r') as fread:
    for line in fread:
        line = line.strip()
        if not line.startswith('From'):continue
        words = line.split()
        print(words[1])
        count += 1
    print(f"There were {count} lines in the file with 'From' as the first word")

