# This code convert fahrenheit to celcius
fahrenheit = input('What is the temperature in fahrenheit?')
if fahrenheit.isnumeric():
    celsius = (int(fahrenheit) - 32) * 5/9
    
    print('Temperature in celsius is', int(celsius))
else:
    print('Input is not a number.')
    exit()