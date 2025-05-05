#Write a while loop that starts at the last character in the string and works its way backwards
# to the first character in the string, printing each letter on a separate line, except backwards.

index = -1
word = input('Enter a word:')
while index >= -(len(word)):
    print(word[index])
    index += -1

