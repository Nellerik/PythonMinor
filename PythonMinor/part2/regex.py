#-*- coding: cp1251 -*-
import re

#������� 8 ��������
#������� + ������ �������
#������� 1 �����

passwordRe = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$')
userPassword = input("password: ")

if passwordRe.search(userPassword):
    print("������� ������")
else:
    print("������ ������")