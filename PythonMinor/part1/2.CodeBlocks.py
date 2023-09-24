name = input('Name: ')
password = input('Password: ')

if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted')
    else:
        print('Wrong password')
else:
    print('User  not registered')