# Open the file
fname = "words.txt"
words_dict = dict()

try:
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                words_dict[word] = True  # Value doesn't matter, using True as a placeholder

    # Test if a word is in the dictionary
    test_word = input("Enter a word to check: ")
    if test_word in words_dict:
        print(f"'{test_word}' is in the dictionary.")
    else:
        print(f"'{test_word}' is NOT in the dictionary.")

except FileNotFoundError:
    print(f"File '{fname}' not found.")
