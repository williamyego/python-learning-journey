#Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print out the contents of your
# dictionary (order does not matter).

# Initialize dictionary
day_counts = dict()

# Prompt for file name
fname = input("Enter file name: ")
try:
    with open(fname, 'r') as fhand:
        for line in fhand:
            if line.startswith("From "):
                words = line.split()
                if len(words) >= 3:
                    day = words[2]  # The third word is the day of the week
                    day_counts[day] = day_counts.get(day, 0) + 1

    # Print results
    for day, count in day_counts.items():
        print(day, count)

except FileNotFoundError:
    print(f"File '{fname}' not found.")
