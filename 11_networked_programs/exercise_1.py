#Write a program to retrieve a web page and count the number of occurrences of a specific word.
import urllib.request
import string

url = input('Enter URL: ')
target_word = input('Enter the word to count: ').lower()

try:
    fhand = urllib.request.urlopen(url)
    counts = dict()

    for line in fhand:
        line = line.decode().strip().lower()
        line = line.translate(str.maketrans('', '', string.punctuation))
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    if target_word in counts:
        print(f"The word '{target_word}' occurs {counts[target_word]} times.")
    else:
        print(f"The word '{target_word}' was not found in the page.")

except Exception as e:
    print("Error retrieving or processing the URL:", e)
