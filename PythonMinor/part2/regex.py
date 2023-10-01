#-*- coding: cp1251 -*-
import re

#Минимум 8 символов
#Верхний + нижний регистр
#Минимум 1 цифра

passwordRe = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$')
userPassword = input("password: ")

if passwordRe.search(userPassword):
    print("Сильный пароль")
else:
    print("Слабый пароль")