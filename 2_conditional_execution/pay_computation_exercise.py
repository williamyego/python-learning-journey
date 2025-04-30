#Rewrite your pay program using try and except so that your  program handles non-numeric input gracefully by printing
# a message and exiting the program. Your pay computation should give the employee 1.5
#  times the hourly rate for hours worked above 40 hours.

try:
    stime = input('Enter weekly hours of work: ')
    srate = input('Enter rate of pay: ')
    ftime = float(stime)
    frate = float(srate)

    if ftime <= 0 or frate <= 0:
        print('Invalid working hours or pay rate!')

    elif ftime <= 40:
        pay = ftime * frate
        print('Your pay is:', pay)

    else:
        pay = (40 * frate) + (ftime - 40) * (frate * 1.5)
        print('Your pay is:', pay)

except:
    print('Enter numerical value!')
