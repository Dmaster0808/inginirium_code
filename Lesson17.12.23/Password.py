def ask_passvord():
    password = input('Введите пароль:')
    if password == 'password':
        print('Пароли совпадают')
    else:
        print('Паралоли не совпадают')

ask_passvord()
