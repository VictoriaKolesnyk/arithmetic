def arithmetic(arg1, arg2, arg3):
    if arg3 == '+':
        return print(arg1 + arg2)
    elif arg3 == '-':
        return print(arg1 - arg2)
    elif arg3 == '*':
        return print (arg1 * arg2)
    elif arg3 == '/':
        return print(arg1 / arg2)
    else:
        return print( "Неизвестная операция")
arg1 = int(input('введите первое число:  '))
arg2 = int(input('введите второе число:  '))
arg3 = input('желаемая операция: ')
arithmetic(arg1, arg2, arg3)
