#-*- coding: cp1251 -*-
import re
from tkinter import TRUE

#������� 8 ��������
#������� + ������ �������
#������� 1 �����

while TRUE:
    passwordRe = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}')
    userPassword = input("password: ")

    if passwordRe.search(userPassword):
        print("������� ������")
    else:
        print("������ ������")