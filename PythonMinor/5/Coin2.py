#-*- coding: cp1251 -*-
import random

CoinNumToStr = { 0:'�����', 1:'����' }
guess = ''
while guess not in CoinNumToStr.values():
    print('�������� ��������� ������������� ������!\n������� ���� ��� �����: ')
    guess = input()
toss = random.randint(0, 1) # 0 - �����
if CoinNumToStr[toss] == guess:
    print('����!')
else:
    print('���! ������ �����!')
    guess = ''
    while guess not in CoinNumToStr.values():
        guess = input()
    toss = random.randint(0, 1)
    if CoinNumToStr[toss] == guess:
        print('����!')
    else:
        print('���. ��� ������������� �� ������� � ���� ����.')