#-*- coding: cp1251 -*-
import random
guess = ''
while guess not in ('орел', 'решка'):
    print('Угадайте результат подбрасывания монеты!\nВведите орел или решка: ')
    guess = input()
toss = random.randint(0, 1) # 0 - решка
if toss == guess:
    print('Есть!')
else:
    print('Увы! Пробуй снова!')
    guess = input()
    if toss == guess:
        print('Есть!')
    else:
        print('Нет. Вам действительно не везезет в этой игре.')