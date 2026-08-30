#Program to convert Fahrenheit into Celsius and Celsius into Fahrenheit.
temp = float(input('Enter your temperature (C/F): '))
conv = input('Convert into?(Celsius/Fahrenheit): ').lower()
if conv == 'celsius':
    t1 = ((temp-32)*5)/9
    print(t1,'degree Celsius')
elif conv == 'fahrenheit':
    t2 = ((temp*9)+160)/5
    print(t2,'degree Fahrenheit')
else:
    print('Error occured')