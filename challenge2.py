# little calculator

first_num = input('First number?')
operation = input('Operation?')
second_num = input('Second number?')

if first_num.isnumeric() and second_num.isnumeric():
    if operation == '+':
        summ = int(first_num) + int(second_num)
        print('sum of', first_num, '+', second_num,'equals', summ)
    elif operation == '-':
        dif = int(first_num) - int(second_num)
        print('difference of', first_num, '-', second_num,'equals', dif)
    elif operation =='*':
        prod = int(first_num) * int(second_num)
        print('product of', first_num, '*', second_num,'equals', prod)
    elif operation == '/':
        quot = int(first_num) / int(second_num)
        print('quotient of', first_num, '/', second_num,'equals', quot)
    elif operation == '%':
        mod = int(first_num) % int(second_num)
        print('modulus of', first_num, '%', second_num,'equals',mod)
    elif operation == '**':
        exp = int(first_num) ** int(second_num)
        print('exponent of', first_num, '**', second_num,'equals', exp)
    else:
        print('Operation not recognized.')
else:
    print('Please input a number.')

