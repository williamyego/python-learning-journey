#Write a program to open the file romeo.txt and read it line by line. For
# each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list. If the word
# is not in the list, add it to the list. When the program completes, sort
# and print the resulting words in alphabetical order.

mylist = list()
with open('romeo.txt','r') as rom:
    for line in rom:
        words = line.split()
        for word in words:
            if word not in mylist:
                mylist.append(word)
    mylist.sort(key=str.lower) # Case-insensitive alphabetical sort
    print(mylist)

