#! python3
#-*- coding: cp1251 -*-
import re, os
directory = "txtFiles"

print('Введите regex выражение: ')
userRegex = re.compile(input())
for fileName in os.listdir(directory):
    if fileName.endswith(".txt"):
        file = open(directory + '\\' + fileName, "r")
        for line in file.readlines():
            if len(re.findall(userRegex, line)) > 0:
                print(line.replace('\n', ''))
        file.close()