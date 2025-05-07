#Write a program to read through a file and print the contents of the file (line by line) all in upper case.

with open('mbox-short.txt', 'r') as filerd:  #opening by with statement autocloses the file
    for line in filerd:
        print(line.rstrip().upper())  #rstrip clears whitespaces #upper converts to uppercase
