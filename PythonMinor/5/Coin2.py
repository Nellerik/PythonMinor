#-*- coding: cp1251 -*-
import random

CoinNumToStr = { 0:'решка', 1:'орел' }
guess = ''
while guess not in CoinNumToStr.values():
    print('Угадайте результат подбрасывания монеты!\nВведите орел или решка: ')
    guess = input()
toss = random.randint(0, 1) # 0 - решка
if CoinNumToStr[toss] == guess:
    print('Есть!')
else:
    print('Увы! Пробуй снова!')
    guess = ''
    while guess not in CoinNumToStr.values():
        guess = input()
    toss = random.randint(0, 1)
    if CoinNumToStr[toss] == guess:
        print('Есть!')
    else:
        print('Нет. Вам действительно не везезет в этой игре.')