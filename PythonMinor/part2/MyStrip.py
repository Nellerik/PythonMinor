#-*- coding: cp1251 -*-
import re

def MyStrip(str1, substr = ""):
    if substr == "":
        return re.sub(r'^\s+|\s+$', '', str1)
    return re.sub(substr, '', str1)

str1 = input("������: ")
str2 = input("������ �� ������: ")
print(MyStrip(str1, str2))