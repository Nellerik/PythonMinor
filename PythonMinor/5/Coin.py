#-*- coding: cp1251 -*-
import random
guess = ''
while guess not in ('����', '�����'):
    print('�������� ��������� ������������� ������!\n������� ���� ��� �����: ')
    guess = input()
toss = random.randint(0, 1) # 0 - �����
if toss == guess:
    print('����!')
else:
    print('���! ������ �����!')
    guess = input()
    if toss == guess:
        print('����!')
    else:
        print('���. ��� ������������� �� ������� � ���� ����.')