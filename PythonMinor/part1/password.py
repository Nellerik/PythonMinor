#! python3
#-*- coding: cp1251 -*-
PASSWORD = {'email': 'QsadwWqWASDs'}
import sys, pyperclip
if len(sys.argv) < 2:
    print('Использование: python password.py [имя учетной записи] - копирование пароля учетной записи')
    sys.exit()
    
account = sys.argv[1]
if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('Пароль для ' + account + ' Скопирован в буфер.')
else:
    print('Учетная запись ' + account + ' отсутсвет в списке')