# print(type('7'))
# print(type(7))
# print(type(7.1))

'''print(isinstance('7', str))
print(isinstance(7, int))
print(isinstance(7.1, float))

print(isinstance(7, str))
print(isinstance('7', int))
print(isinstance('7.1', float))

numeric_value = '7'
print(numeric_value.isnumeric())

string_value = 'Bob'
print(string_value.isnumeric())'''

first_value = input('First Number: ')

if first_value.isnumeric() == False:
    print('Value is not a number.')
    exit()

second_value = input('Second Number: ')

if second_value.isnumeric() == False:
    print('Value is not a number.')
    exit()

first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print('Sum: ' + str(sum))