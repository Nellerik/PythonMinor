#! python3
#-*- coding: cp1251 -*-
PASSWORD = {'email': 'QsadwWqWASDs'}
import sys, pyperclip
if len(sys.argv) < 2:
    print('�������������: python password.py [��� ������� ������] - ����������� ������ ������� ������')
    sys.exit()
    
account = sys.argv[1]
if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('������ ��� ' + account + ' ���������� � �����.')
else:
    print('������� ������ ' + account + ' ��������� � ������')