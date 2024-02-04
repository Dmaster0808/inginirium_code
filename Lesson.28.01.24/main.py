num1 = int(input("Введите пепвое число"))
num2 = int(input("Введите второе число"))
sign = input("Введите операцию, которую хотите выполнить (+,-,*,/): ")

if sign == '+':
    print(num1 + num2)
elif sign == "-":
    print(num1 - num2)
elif sign == "*":
    print(num1 * num2)
elif sign == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print('separation на 0')


