#Write a program to read through a mail log, build a his togram using a dictionary to count how many messages
# have come from each email address, and print the dictionary.

# Initialize dictionary
email_counts = dict()

# Prompt for file name
fname = input("Enter file name: ")
try:
    with open(fname, 'r') as fhand:
        for line in fhand:
            if line.startswith("From "):
                words = line.split()
                if len(words) >= 2:
                    email = words[1]  # Second word is the email address
                    email_counts[email] = email_counts.get(email, 0) + 1

    # Print the histogram
    for email, count in email_counts.items():
        print(email, count)

except FileNotFoundError:
    print(f"File '{fname}' not found.")
