#Write a program which repeatedly reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except
# and print an error message and skip to the next number.

total = 0
count = 0
while True:
     try:
         inp = input('Enter a number:')
         if inp == 'done':
             break
         num = float(inp)
         count += 1
         total = total + num
         average = total/count

     except:
         print('Bad input!')

print(f'Count: {count}\nTotal: {total}\nAverage: {average}')



