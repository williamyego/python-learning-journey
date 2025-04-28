#A program that prompts the user for hours and rate per hour to compute gross pay.
hour = input('Enter hours worked:')
rate = input('Enter rate per hour:')
hr = float(hour) #converts to a str to float
rt = float(rate)
pay = hr * rt #computes the pay
print('Your pay is',pay)